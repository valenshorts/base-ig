"""Saca CATALOG y COMBOS de public/index.html y los guarda en netlify/functions/catalogo.json.

Corre en cada deploy de Netlify (ver netlify.toml), así los precios que cobra Mercado Pago
son siempre los mismos que muestra la web. El navegador nunca manda precios: solo ids.
"""
import json
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(AQUI, '..', 'public', 'index.html'), encoding='utf-8').read()


def bloque(nombre):
    m = re.search(r'const ' + nombre + r' = (\[.*?\n?\]);', html, re.S)
    if not m:
        raise SystemExit(f'No encontré {nombre} en index.html')
    return json.loads(m.group(1))


catalogo = {
    'productos': {str(p['id']): {
        'titulo': f"{p['marca']} {p.get('nombre') or p['producto']} {p.get('presentacion') or p['formato']}",
        'precio': int(p['precio_transferencia']),
        'sabores': p.get('sabores') or [],
    } for p in bloque('CATALOG')},
    'combos': {c['id']: {
        'titulo': c['nombre'] + ' (' + ' + '.join(f"{i['producto']} {i['formato']}" for i in c['items']) + ')',
        'precio': int(c['precio_combo']),
    } for c in bloque('COMBOS')},
}
dest = os.path.join(AQUI, '..', 'netlify', 'functions', 'catalogo.json')
json.dump(catalogo, open(dest, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"catalogo.json: {len(catalogo['productos'])} productos, {len(catalogo['combos'])} combos")
