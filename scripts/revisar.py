"""Revisión automática de un día de la cola (queue/AAAA-MM-DD).

Uso: python scripts/revisar.py queue/2026-11-14 [--reporte reporte.md]
Sale con código 1 si encuentra algún ERROR (no se debe aprobar el PR).

Soporta dos formatos:
- plan.json con varios contenidos (posts, historias y reels con horario)
- formato viejo: post_N.jpg + historia.jpg + texto.txt
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile, unicodedata
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(RAIZ, 'kit')
LEGAL = 'SUPLEMENTA DIETAS INSUFICIENTES. CONSULTE A SU MÉDICO Y/O FARMACÉUTICO.'
WA = '11 2178-9431'
PROHIBIDAS = ['nutristock', 'one fit', 'onefit', 'más vendido', 'en stock', 'cura ', 'curar',
              'garantiza', 'garantizado', 'adelgaz', 'quema grasa', 'quemador de grasa', 'milagro', 'sin efectos secundarios']


def sin_acentos(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c) != 'Mn')


PROHIBIDAS_N = sorted({sin_acentos(p) for p in PROHIBIDAS})


def precios_validos():
    txt = open(os.path.join(KIT, 'README.md'), encoding='utf-8').read()
    return set(re.findall(r'\$\s?[\d.]+\d', txt))


def emoji_cmap():
    try:
        from fontTools.ttLib import TTFont
        f = subprocess.run(['fc-match', 'Noto Color Emoji', '--format=%{file}'], capture_output=True, text=True).stdout.strip()
        return set(TTFont(f, lazy=True).getBestCmap().keys()) if f else None
    except Exception:
        return None


def ffmpeg_bin():
    f = shutil.which('ffmpeg')
    if f:
        return f
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


class Rev:
    def __init__(self, carpeta):
        self.c = carpeta
        self.err, self.av = [], []
        self.precios = precios_validos()

    def imagen(self, nom, tipo):
        ruta = os.path.join(self.c, nom)
        if not os.path.exists(ruta):
            self.err.append(f'Falta el archivo {nom}.')
            return
        im = Image.open(ruta)
        ok = {(1080, 1920)} if tipo == 'historia' else {(1080, 1350), (1080, 1080)}
        if im.format != 'JPEG':
            self.err.append(f'{nom}: tiene que ser JPG (la API de Instagram solo acepta JPEG).')
        if im.size not in ok:
            self.err.append(f'{nom}: mide {im.size[0]}×{im.size[1]}, se esperaba {" o ".join(f"{w}×{h}" for w, h in ok)}.')
        if os.path.getsize(ruta) > 8 * 1024 * 1024:
            self.err.append(f'{nom}: pesa más de 8 MB.')

    def video(self, nom):
        ruta = os.path.join(self.c, nom)
        if not os.path.exists(ruta):
            self.err.append(f'Falta el archivo {nom}.')
            return
        if os.path.getsize(ruta) > 300 * 1024 * 1024:
            self.err.append(f'{nom}: pesa más de 300 MB.')
        ff = ffmpeg_bin()
        if not ff:
            self.av.append(f'{nom}: no hay ffmpeg para revisar el video.')
            return
        info = subprocess.run([ff, '-hide_banner', '-i', ruta], capture_output=True, text=True).stderr
        m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', info)
        dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0
        if not 3 <= dur <= 90:
            self.err.append(f'{nom}: dura {dur:.1f} s; un reel tiene que durar entre 3 y 90 segundos.')
        v = re.search(r'Video: (\w+).*?, (\d{2,5})x(\d{2,5})', info)
        if not v:
            self.err.append(f'{nom}: no se pudo leer la pista de video.')
        else:
            if v.group(1) != 'h264':
                self.err.append(f'{nom}: el video tiene que ser H.264 (es {v.group(1)}).')
            if (int(v.group(2)), int(v.group(3))) != (1080, 1920):
                self.err.append(f'{nom}: mide {v.group(2)}×{v.group(3)}, un reel tiene que ser 1080×1920.')
        if 'Audio: aac' not in info:
            self.av.append(f'{nom}: no tiene pista de audio AAC (Instagram a veces lo rechaza).')

    def texto(self, nom):
        ruta = os.path.join(self.c, nom)
        if not os.path.exists(ruta):
            self.err.append(f'Falta {nom} (el texto de la publicación).')
            return
        cap = open(ruta, encoding='utf-8').read().strip()
        low = sin_acentos(cap.lower())
        if len(cap) > 2200:
            self.err.append(f'{nom}: tiene {len(cap)} caracteres; Instagram permite 2200.')
        if len(re.findall(r'#\w+', cap)) > 30:
            self.err.append(f'{nom}: tiene más de 30 hashtags.')
        if 'link en la bio' not in low:
            self.err.append(f'{nom}: no dice «link en la bio» (catálogo en la web).')
        if WA not in cap:
            self.err.append(f'{nom}: no tiene el WhatsApp {WA}.')
        if 'mensaje' not in low:
            self.err.append(f'{nom}: no aclara que el WhatsApp es solo por mensaje.')
        if LEGAL not in cap.upper():
            self.err.append(f'{nom}: no tiene la leyenda legal.')
        if '?' not in cap.split('#')[0][-400:]:
            self.err.append(f'{nom}: no termina con una pregunta.')
        for p in PROHIBIDAS_N:
            if p in low:
                self.err.append(f'{nom}: palabra o frase no permitida «{p.strip()}».')
        for pr in re.findall(r'\$\s?[\d.]+\d', cap):
            if pr not in self.precios:
                self.err.append(f'{nom}: el precio {pr} no figura en el README del kit.')

    def diseno(self):
        """Vuelve a renderizar con los scripts guardados y aplica los chequeos de diseño."""
        scripts = [a for a in os.listdir(self.c) if a.endswith('.py')]
        if not scripts:
            self.err.append('No están los scripts .py que generaron las imágenes; no se puede revisar el diseño.')
            return 0
        cmap = emoji_cmap()
        with tempfile.TemporaryDirectory() as tmp:
            rep = os.path.join(tmp, 'check.json')
            for sc in scripts:
                env = dict(os.environ, BASE_CHECK=rep, PYTHONPATH=KIT)
                r = subprocess.run([sys.executable, os.path.abspath(os.path.join(self.c, sc)), tmp], env=env,
                                   capture_output=True, text=True, cwd=tmp)
                if r.returncode:
                    self.err.append(f'El script {sc} falló al renderizar:\n```\n{r.stderr[-1500:]}\n```')
            reps = json.load(open(rep, encoding='utf-8')) if os.path.exists(rep) else []
        for r in reps:
            nom, texto = r['png'], r['text']
            self.err += [f'{nom}: {i}' for i in r['issues']]
            low = sin_acentos(texto.lower())
            for p in PROHIBIDAS_N:
                if p in low:
                    self.err.append(f'{nom}: palabra o frase no permitida «{p.strip()}».')
            for pr in re.findall(r'\$\s?[\d.]+\d', texto):
                if pr not in self.precios:
                    self.err.append(f'{nom}: el precio {pr} no figura en el README del kit.')
            if LEGAL not in texto.upper():
                self.err.append(f'{nom}: falta la leyenda legal.')
            for tel in re.findall(r'\b11[\s-]?\d{4}[\s-]?\d{4}\b', texto):
                if tel != WA:
                    self.err.append(f'{nom}: el WhatsApp «{tel}» no coincide con {WA}.')
            if cmap is not None:
                for em in r['emojis']:
                    if any(ord(ch) not in (0xFE0F, 0x200D) and not 0x1F3FB <= ord(ch) <= 0x1F3FF and ord(ch) not in cmap for ch in em):
                        self.err.append(f'{nom}: el emoji «{em}» no existe en la fuente y se vería como un cuadradito.')
            if '📅' in ''.join(r['emojis']):
                self.av.append(f'{nom}: 📅 se ve como un calendario con fecha («July 17»); conviene cambiarlo.')
        return len(reps)


def revisar(carpeta):
    rv = Rev(carpeta)
    resumen = []
    ruta_plan = os.path.join(carpeta, 'plan.json')
    if os.path.exists(ruta_plan):
        plan = json.load(open(ruta_plan, encoding='utf-8'))
        items = plan.get('items', [])
        if not items:
            rv.err.append('plan.json no tiene contenidos.')
        horas = {}
        for it in items:
            iid, tipo, hora = it.get('id', '?'), it.get('tipo'), it.get('hora', '')
            if not re.fullmatch(r'([01]\d|2[0-3]):[0-5]\d', hora):
                rv.err.append(f'{iid}: hora inválida «{hora}».')
            horas.setdefault(hora, []).append(iid)
            if tipo == 'post':
                imgs = it.get('imagenes', [])
                if not 1 <= len(imgs) <= 10:
                    rv.err.append(f'{iid}: un post lleva de 1 a 10 imágenes (tiene {len(imgs)}).')
                for n in imgs:
                    rv.imagen(n, 'post')
                rv.texto(it.get('texto', f'{iid}.txt'))
                resumen.append(f'{hora} · post «{iid}» ({len(imgs)} imagen/es)')
            elif tipo == 'historia':
                rv.imagen(it.get('imagen', ''), 'historia')
                resumen.append(f'{hora} · historia «{iid}»')
            elif tipo == 'reel':
                rv.video(it.get('video', ''))
                rv.texto(it.get('texto', f'{iid}.txt'))
                resumen.append(f'{hora} · reel «{iid}»')
            else:
                rv.err.append(f'{iid}: tipo desconocido «{tipo}».')
        for h, ids in horas.items():
            if len(ids) > 1:
                rv.av.append(f'Varios contenidos a la misma hora ({h}): {", ".join(ids)}.')
        rv.diseno()
    else:
        archivos = sorted(os.listdir(carpeta))
        posts = sorted([a for a in archivos if re.fullmatch(r'post_\d+\.jpg', a)], key=lambda a: int(re.findall(r'\d+', a)[0]))
        if not posts:
            rv.err.append('No hay plan.json ni imágenes del post.')
        for p in posts:
            rv.imagen(p, 'post')
        if 'historia.jpg' in archivos:
            rv.imagen('historia.jpg', 'historia')
        rv.texto('texto.txt')
        rv.diseno()
        resumen.append(f'19:30 · post ({len(posts)} imagen/es)' + (' + historia' if 'historia.jpg' in archivos else ''))
    return rv.err, rv.av, resumen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('carpetas', nargs='+')
    ap.add_argument('--reporte')
    a = ap.parse_args()
    md, total = [], 0
    for c in a.carpetas:
        e, w, res = revisar(c)
        total += len(e)
        md.append(f'## {"✅" if not e else "❌"} {os.path.basename(c.rstrip("/"))}')
        md += [f'- {r}' for r in res]
        if e:
            md.append('\n**Errores (corregir antes de aprobar):**')
            md += [f'- {x}' for x in e]
        if w:
            md.append('\n**Avisos:**')
            md += [f'- {x}' for x in w]
        if not e and not w:
            md.append('\nTodo en orden: medidas, videos, textos, precios, leyenda legal, emojis y textos de las publicaciones.')
        md.append('')
    out = '\n'.join(md)
    print(out)
    if a.reporte:
        open(a.reporte, 'w', encoding='utf-8').write(out)
    sys.exit(1 if total else 0)


if __name__ == '__main__':
    main()
