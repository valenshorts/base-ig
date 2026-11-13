"""Arma la carpeta de un día en la cola: queue/AAAA-MM-DD/ con plan.json.

Uso (recomendado, varios contenidos por día):
  python scripts/armar.py --plan out/plan_fuente.json

plan_fuente.json:
{
  "fecha": "2026-11-14",
  "scripts": ["kit/2026-11-14_post1.py", "kit/2026-11-14_historias.py", ...],
  "items": [
    {"id": "historia1", "tipo": "historia", "hora": "11:00", "imagen": "out/h1.png"},
    {"id": "post1", "tipo": "post", "hora": "13:00", "imagenes": ["out/p1_1.png", "out/p1_2.png"], "texto": "out/post1.txt"},
    {"id": "reel", "tipo": "reel", "hora": "20:30", "video": "out/reel.mp4", "texto": "out/reel.txt"},
    ...
  ]
}

Convierte los PNG a JPG (la API de Instagram solo acepta JPEG), copia videos, textos y scripts
y escribe queue/AAAA-MM-DD/plan.json con los nombres finales.

Modo viejo (un post + una historia): --fecha --post ... --historia ... --texto ... --scripts ...
"""
import argparse, json, os, re, shutil
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TIPOS = {'post', 'historia', 'reel'}


def a_jpg(src, dst):
    Image.open(src).convert('RGB').save(dst, 'JPEG', quality=95, subsampling=0, optimize=True)


def armar_plan(ruta):
    src = json.load(open(ruta, encoding='utf-8'))
    fecha = src['fecha']
    out = os.path.join(RAIZ, 'queue', fecha)
    os.makedirs(out, exist_ok=True)
    plan = {'fecha': fecha, 'items': []}
    ids = set()
    for it in src['items']:
        iid, tipo, hora = it['id'], it['tipo'], it['hora']
        if tipo not in TIPOS:
            raise SystemExit(f'Tipo desconocido: {tipo}')
        if not re.fullmatch(r'[a-z0-9_]+', iid) or iid in ids:
            raise SystemExit(f'id inválido o repetido: {iid}')
        if not re.fullmatch(r'([01]\d|2[0-3]):[0-5]\d', hora):
            raise SystemExit(f'Hora inválida en {iid}: {hora}')
        ids.add(iid)
        e = {'id': iid, 'tipo': tipo, 'hora': hora}
        if tipo == 'post':
            e['imagenes'] = []
            for i, p in enumerate(it['imagenes'], 1):
                nom = f'{iid}_{i}.jpg'
                a_jpg(p, os.path.join(out, nom))
                e['imagenes'].append(nom)
        elif tipo == 'historia':
            nom = f'{iid}.jpg'
            a_jpg(it['imagen'], os.path.join(out, nom))
            e['imagen'] = nom
        else:
            nom = f'{iid}.mp4'
            shutil.copy(it['video'], os.path.join(out, nom))
            e['video'] = nom
        if tipo in ('post', 'reel'):
            nom = f'{iid}.txt'
            shutil.copy(it['texto'], os.path.join(out, nom))
            e['texto'] = nom
        plan['items'].append(e)
    plan['items'].sort(key=lambda x: x['hora'])
    for s in src.get('scripts', []):
        shutil.copy(s, os.path.join(out, os.path.basename(s)))
    json.dump(plan, open(os.path.join(out, 'plan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('Listo:', out)
    for e in plan['items']:
        print(f"  {e['hora']}  {e['tipo']:8} {e['id']}")


def armar_simple(a):
    out = os.path.join(RAIZ, 'queue', a.fecha)
    os.makedirs(out, exist_ok=True)
    for i, p in enumerate(a.post, 1):
        a_jpg(p, os.path.join(out, f'post_{i}.jpg'))
    if a.historia:
        a_jpg(a.historia, os.path.join(out, 'historia.jpg'))
    shutil.copy(a.texto, os.path.join(out, 'texto.txt'))
    for s in a.scripts:
        shutil.copy(s, os.path.join(out, os.path.basename(s)))
    print('Listo:', out, sorted(os.listdir(out)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--plan')
    ap.add_argument('--fecha')
    ap.add_argument('--post', nargs='+')
    ap.add_argument('--historia')
    ap.add_argument('--texto')
    ap.add_argument('--scripts', nargs='+', default=[])
    a = ap.parse_args()
    if a.plan:
        armar_plan(a.plan)
    elif a.fecha and a.post and a.texto:
        armar_simple(a)
    else:
        ap.error('Usá --plan plan_fuente.json (o el modo viejo con --fecha --post --texto --scripts)')


if __name__ == '__main__':
    main()
