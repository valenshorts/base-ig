"""Saca CATALOG y COMBOS de public/index.html y los guarda en netlify/functions/catalogo.json.

Corre en cada deploy de Netlify (ver netlify.toml), así los precios que cobra Mercado Pago
son siempre los precios de lista (sin el 10% OFF de transferencia) que muestra la web. El navegador nunca manda precios: solo ids.
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


def precio_lista_combo(transferencia):
    # Mercado Pago cobra precio de lista: el combo sin el 10% OFF, redondeado hacia arriba a $...900
    base = transferencia / 0.9
    return int(-(-(base - 900) // 1000) * 1000 + 900)


catalogo = {
    'productos': {str(p['id']): {
        'titulo': f"{p['marca']} {p.get('nombre') or p['producto']} {p.get('presentacion') or p['formato']}",
        'precio': int(p['precio_normal']),
        'sabores': p.get('sabores') or [],
    } for p in bloque('CATALOG')},
    'combos': {c['id']: {
        'titulo': c['nombre'] + ' (' + ' + '.join(f"{i['producto']} {i['formato']}" for i in c['items']) + ')',
        'precio': precio_lista_combo(c['precio_combo']),
    } for c in bloque('COMBOS')},
}
dest = os.path.join(AQUI, '..', 'netlify', 'functions', 'catalogo.json')
json.dump(catalogo, open(dest, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"catalogo.json: {len(catalogo['productos'])} productos, {len(catalogo['combos'])} combos")
