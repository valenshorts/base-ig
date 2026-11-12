"""Arma la carpeta de una publicación en la cola: queue/AAAA-MM-DD/

Uso:
  python scripts/armar.py --fecha 2026-11-13 \
      --post out/flyer_1.png out/flyer_2.png --historia out/historia.png \
      --texto texto.txt --scripts kit/flyer.py kit/historia.py

Convierte los PNG a JPG (la API de Instagram solo acepta JPEG), los renombra
post_1.jpg… / historia.jpg y copia el texto y los scripts que generaron las imágenes
(se usan para volver a revisar el diseño en GitHub).
"""
import argparse, os, shutil
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def a_jpg(src, dst):
    im = Image.open(src).convert('RGB')
    im.save(dst, 'JPEG', quality=95, subsampling=0, optimize=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fecha', required=True)
    ap.add_argument('--post', nargs='+', required=True)
    ap.add_argument('--historia')
    ap.add_argument('--texto', required=True)
    ap.add_argument('--scripts', nargs='+', required=True)
    a = ap.parse_args()
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


if __name__ == '__main__':
    main()
