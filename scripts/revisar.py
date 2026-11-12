"""Revisión automática de una publicación de la cola (queue/AAAA-MM-DD).

Uso: python scripts/revisar.py queue/2026-11-13 [--reporte reporte.md]
Sale con código 1 si encuentra algún ERROR (no se debe aprobar el PR).
"""
import argparse, json, os, re, subprocess, sys, tempfile, unicodedata
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(RAIZ, 'kit')
LEGAL = 'SUPLEMENTA DIETAS INSUFICIENTES. CONSULTE A SU MÉDICO Y/O FARMACÉUTICO.'
WA = '11 2178-9431'
PROHIBIDAS = ['nutristock', 'one fit', 'onefit', 'más vendido', 'mas vendido', 'en stock', 'cura ', 'curar',
              'garantiza', 'garantizado', 'adelgaz', 'quema grasa', 'quemador de grasa', 'milagro', 'sin efectos secundarios']


def sin_acentos(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c) != 'Mn')


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


def revisar(carpeta):
    errores, avisos = [], []
    archivos = sorted(os.listdir(carpeta))
    posts = sorted([a for a in archivos if re.fullmatch(r'post_\d+\.jpg', a)], key=lambda a: int(re.findall(r'\d+', a)[0]))
    historia = 'historia.jpg' in archivos

    # 1 · Archivos e imágenes
    if not posts:
        errores.append('No hay imágenes del post (post_1.jpg, post_2.jpg, …).')
    if len(posts) > 10:
        errores.append(f'El carrusel tiene {len(posts)} imágenes; Instagram permite hasta 10.')
    esperado = [f'post_{i}.jpg' for i in range(1, len(posts) + 1)]
    if posts != esperado:
        errores.append(f'Numeración del carrusel incorrecta: {posts}')
    for a in posts + (['historia.jpg'] if historia else []):
        im = Image.open(os.path.join(carpeta, a))
        tam = os.path.getsize(os.path.join(carpeta, a))
        ok = {(1080, 1920)} if a == 'historia.jpg' else {(1080, 1350), (1080, 1080)}
        if im.format != 'JPEG':
            errores.append(f'{a}: tiene que ser JPG (la API de Instagram solo acepta JPEG).')
        if im.size not in ok:
            errores.append(f'{a}: mide {im.size[0]}×{im.size[1]}, se esperaba {" o ".join(f"{w}×{h}" for w, h in ok)}.')
        if tam > 8 * 1024 * 1024:
            errores.append(f'{a}: pesa más de 8 MB.')
    if not historia:
        avisos.append('No hay historia (historia.jpg). Se publica solo el post.')

    # 2 · Chequeos de diseño (se vuelve a renderizar con los scripts guardados)
    scripts = [a for a in archivos if a.endswith('.py')]
    reportes = []
    if not scripts:
        errores.append('No están los scripts .py que generaron las imágenes; no se puede revisar el diseño.')
    with tempfile.TemporaryDirectory() as tmp:
        rep = os.path.join(tmp, 'check.json')
        for sc in scripts:
            env = dict(os.environ, BASE_CHECK=rep, PYTHONPATH=KIT)
            r = subprocess.run([sys.executable, os.path.abspath(os.path.join(carpeta, sc)), tmp], env=env,
                               capture_output=True, text=True, cwd=tmp)
            if r.returncode:
                errores.append(f'El script {sc} falló al renderizar:\n```\n{r.stderr[-1500:]}\n```')
        if os.path.exists(rep):
            reportes = json.load(open(rep, encoding='utf-8'))
    precios = precios_validos()
    cmap = emoji_cmap()
    for r in reportes:
        nom = r['png']
        for i in r['issues']:
            errores.append(f'{nom}: {i}')
        texto = r['text']
        low = sin_acentos(texto.lower())
        for p in sorted({sin_acentos(x) for x in PROHIBIDAS}):
            if p in low:
                errores.append(f'{nom}: palabra o frase no permitida «{p.strip()}».')
        for pr in re.findall(r'\$\s?[\d.]+\d', texto):
            if pr not in precios:
                errores.append(f'{nom}: el precio {pr} no figura en el README del kit.')
        if LEGAL not in texto.upper():
            errores.append(f'{nom}: falta la leyenda legal.')
        for tel in re.findall(r'\b11[\s-]?\d{4}[\s-]?\d{4}\b', texto):
            if tel != WA:
                errores.append(f'{nom}: el WhatsApp «{tel}» no coincide con {WA}.')
        if cmap is not None:
            for em in r['emojis']:
                faltan = [c for c in em if ord(c) not in (0xFE0F, 0x200D) and not (0x1F3FB <= ord(c) <= 0x1F3FF) and ord(c) not in cmap]
                if faltan:
                    errores.append(f'{nom}: el emoji «{em}» no existe en la fuente y se vería como un cuadradito.')
        if '📅' in ''.join(r['emojis']):
            avisos.append(f'{nom}: 📅 se ve como un calendario con fecha («July 17»); conviene cambiarlo.')
    if scripts and reportes:
        n_post = sum(1 for r in reportes if r['size'] == [1080, 1350] or r['size'] == [1080, 1080])
        if n_post != len(posts):
            avisos.append(f'Los scripts generan {n_post} slides de post pero hay {len(posts)} JPG en la carpeta.')

    # 3 · Texto del post
    ruta_txt = os.path.join(carpeta, 'texto.txt')
    if not os.path.exists(ruta_txt):
        errores.append('Falta texto.txt (el texto del post).')
    else:
        cap = open(ruta_txt, encoding='utf-8').read().strip()
        low = sin_acentos(cap.lower())
        if len(cap) > 2200:
            errores.append(f'El texto tiene {len(cap)} caracteres; Instagram permite 2200.')
        tags = re.findall(r'#\w+', cap)
        if len(tags) > 30:
            errores.append(f'El texto tiene {len(tags)} hashtags; Instagram permite 30.')
        if 'link en la bio' not in low:
            errores.append('El texto no dice «link en la bio» (catálogo en la web).')
        if WA not in cap:
            errores.append(f'El texto no tiene el WhatsApp {WA}.')
        if 'mensaje' not in low:
            errores.append('El texto no aclara que el WhatsApp es solo por mensaje.')
        if LEGAL not in cap.upper():
            errores.append('El texto no tiene la leyenda legal.')
        if '?' not in cap.split('#')[0][-400:]:
            errores.append('El texto no termina con una pregunta.')
        for p in sorted({sin_acentos(x) for x in PROHIBIDAS}):
            if p in low:
                errores.append(f'Texto del post: palabra o frase no permitida «{p.strip()}».')
        for pr in re.findall(r'\$\s?[\d.]+\d', cap):
            if pr not in precios:
                errores.append(f'Texto del post: el precio {pr} no figura en el README del kit.')
    return errores, avisos, posts, historia


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('carpetas', nargs='+')
    ap.add_argument('--reporte')
    a = ap.parse_args()
    md, total = [], 0
    for c in a.carpetas:
        e, w, posts, hist = revisar(c)
        total += len(e)
        md.append(f'## {"✅" if not e else "❌"} {os.path.basename(c.rstrip("/"))}')
        md.append(f'{len(posts)} imagen(es) de post · historia: {"sí" if hist else "no"}')
        if e:
            md.append('\n**Errores (corregir antes de aprobar):**')
            md += [f'- {x}' for x in e]
        if w:
            md.append('\n**Avisos:**')
            md += [f'- {x}' for x in w]
        if not e and not w:
            md.append('\nTodo en orden: medidas, textos, precios, leyenda legal, emojis y texto del post.')
        md.append('')
    out = '\n'.join(md)
    print(out)
    if a.reporte:
        open(a.reporte, 'w', encoding='utf-8').write(out)
    sys.exit(1 if total else 0)


if __name__ == '__main__':
    main()
