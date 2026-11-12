"""Kit de diseño BASE Suplementos: helpers para flyers de Instagram (1080x1350) e historias (1080x1920)."""
import asyncio, os
D = os.path.dirname(os.path.abspath(__file__))

# Marca: cuadrado lima con barra negra abajo (igual que la web)
MARK = '<svg viewBox="0 0 36 36" width="{s}" height="{s}"><rect width="36" height="36" fill="#C6F432"/><rect x="10" y="25" width="16" height="4" fill="#0B0B0C"/></svg>'
ARROW = '<svg viewBox="0 0 40 24" width="44" height="24"><path d="M2 12h34M26 3l10 9-10 9" fill="none" stroke="#0B0B0C" stroke-width="3.6" stroke-linecap="square"/></svg>'
OK = '<b class="ic">✓</b>'
X = '<b class="ic">✕</b>'
LEGAL_TXT = 'SUPLEMENTA DIETAS INSUFICIENTES. CONSULTE A SU MÉDICO Y/O FARMACÉUTICO.'
WA = '11 2178-9431'
IG = '@basesuplementos.ar'

CSS = """
@font-face{font-family:Archivo Black;src:url(fonts/archivo-black-latin-400-normal.woff2)}
@font-face{font-family:Montserrat;font-weight:500;src:url(fonts/montserrat-latin-500-normal.woff2)}
@font-face{font-family:Montserrat;font-weight:600;src:url(fonts/montserrat-latin-600-normal.woff2)}
@font-face{font-family:Montserrat;font-weight:700;src:url(fonts/montserrat-latin-700-normal.woff2)}
@font-face{font-family:Montserrat;font-weight:800;src:url(fonts/montserrat-latin-800-normal.woff2)}
@font-face{font-family:Montserrat;font-weight:900;src:url(fonts/montserrat-latin-900-normal.woff2)}
:root{--bk:#0B0B0C;--panel:#111112;--panel2:#19191b;--line:#2a2a2d;--l:#C6F432;--ld:#8FB31E;--w:#fff;--off:#F3F2ED;--gr:#8b8b8f}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;background:var(--bk)}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;color:var(--w);font-family:Montserrat;background:var(--bk);
   background-image:radial-gradient(ellipse 900px 520px at 88% 4%,rgba(198,244,50,.11),transparent 62%)}
.s.story{height:1920px}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);background-size:90px 90px;pointer-events:none}
.hd{position:absolute;left:80px;right:80px;top:64px;display:flex;align-items:center;justify-content:space-between}
.br{display:flex;align-items:center;gap:16px}
.br span{font-family:'Archivo Black';font-size:40px;line-height:.9;letter-spacing:-.5px;display:flex;flex-direction:column}
.br small{font-family:Montserrat;font-weight:700;font-size:12.5px;letter-spacing:5.2px;color:var(--l);margin-top:6px}
.cnt{font-size:26px;font-weight:700;color:var(--gr);letter-spacing:3px} .cnt b{color:var(--l)}
.eb{position:absolute;left:80px;display:flex;align-items:center;gap:16px;color:var(--l);font-weight:700;font-size:26px;letter-spacing:5px;text-transform:uppercase}
.eb:before{content:"";width:40px;height:4px;background:var(--l)}
.t{position:absolute;left:80px;right:70px;font-family:Montserrat;font-weight:900;text-transform:uppercase;line-height:1.0;letter-spacing:-1.5px}
.t .hl{color:var(--l)}
.t .box{display:inline-block;background:var(--l);color:var(--bk);padding:6px 22px 10px;margin-top:10px;letter-spacing:-1px}
.txt{position:absolute;left:80px;right:80px;font-size:32px;font-weight:500;line-height:1.38;color:#d6d6d8} .txt b{color:#fff;font-weight:800} .txt em{font-style:normal;color:var(--l);font-weight:700}
.panel{position:absolute;background:var(--panel);border:2px solid var(--line)}
.panel.on{border-color:var(--l);background:linear-gradient(160deg,rgba(198,244,50,.13),var(--panel) 70%)}
.btn{position:absolute;display:flex;align-items:center;gap:14px;background:var(--l);color:var(--bk);font-weight:800;font-size:30px;letter-spacing:1.5px;text-transform:uppercase;padding:18px 30px}
.btn.ghost{background:transparent;color:var(--w);border:2px solid #3a3a3d}
.legal{position:absolute;left:80px;right:80px;bottom:30px;font-size:18px;font-weight:600;letter-spacing:1.5px;color:#7a7a7e;text-align:center}
.ic{font-weight:800}
.e{font-family:'Noto Color Emoji','Segoe UI Emoji','Apple Color Emoji';font-weight:400;letter-spacing:0;line-height:1;text-transform:none}
.tiles{position:absolute;left:80px;right:80px;display:flex;justify-content:center;gap:var(--g,22px)}
.tile{flex:0 0 var(--w);overflow:hidden;border:2px solid var(--line);background:var(--panel)}
.tile .ph{position:relative;height:var(--h);background:radial-gradient(circle 190px at 50% 45%,rgba(198,244,50,.08),transparent 100%),radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);display:flex;align-items:center;justify-content:center}
.tile .ph:after{content:'';position:absolute;left:50%;bottom:6%;width:70%;height:24px;transform:translateX(-50%);border-radius:50%;background:rgba(0,0,0,.5);filter:blur(16px)}
.tile .ph img{position:relative;z-index:1;max-height:84%;max-width:84%;filter:drop-shadow(0 22px 30px rgba(0,0,0,.6))}
.tile .ft{background:var(--l);color:var(--bk);padding:10px 16px 12px;text-align:center}
.tile .ft .b{font-size:21px;font-weight:700;letter-spacing:.3px;line-height:1.15;text-transform:uppercase}
.tile .ft .p{font-family:'Archivo Black';font-size:46px;line-height:1.1;margin-top:2px}
.tile .cat{background:var(--panel2);color:var(--l);font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-align:center;padding:12px 8px 14px}
"""

def E(c, size=None):
    """Emoji a color (Noto Color Emoji). Ej: E('🔥', 120). Usar como ícono/ilustración, no como relleno."""
    st = f' style="font-size:{size}px"' if size else ''
    return f'<span class="e"{st}>{c}</span>'

def tiles(items, top, w, h, gap=22):
    """Recuadros GRISES con el producto. items: [(archivo_sin_png, pie_html)]"""
    cells = ''.join(f'<div class="tile"><div class="ph"><img src="assets/{f}.png"></div>{ft}</div>' for f, ft in items)
    return f'<div class="tiles" style="top:{top}px;--w:{w}px;--h:{h}px;--g:{gap}px">{cells}</div>'

pf = lambda brand, price: f'<div class="ft"><div class="b">{brand}</div><div class="p">{price}</div></div>'
cf = lambda cat, fs=26: f'<div class="cat" style="font-size:{fs}px">{cat}</div>'

def page(n, body, nxt=True, total=1, story=False, legal=True):
    """Fondo + header con la marca BASE + contador n/total. nxt=True agrega el botón DESLIZÁ."""
    cnt = f'<div class="cnt"><b>{n}</b> / {total}</div>' if total > 1 else ''
    p = f'<div class="btn" style="right:80px;bottom:76px">DESLIZÁ {ARROW}</div>' if nxt else ''
    lg = f'<div class="legal">{LEGAL_TXT}</div>' if legal else ''
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s{' story' if story else ''}">
<div class="grid"></div>
<div class="hd"><div class="br">{MARK.format(s=64)}<span>BASE<small>SUPLEMENTOS</small></span></div>{cnt}</div>
{body}{p}{lg}
</div></body></html>"""

CHECK_JS = r"""() => {
  const s = document.querySelector('.s'); const W = s.clientWidth, H = s.clientHeight; const issues = [];
  const nm = e => ((e.className && e.className.baseVal === undefined ? e.className : e.tagName) + ' «' + (e.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 45) + '»');
  for (const e of s.querySelectorAll('*')) {
    const r = e.getBoundingClientRect(); if (r.width < 1 || r.height < 1) continue;
    if (r.left < -1 || r.top < -1 || r.right > W + 1 || r.bottom > H + 1) issues.push('Se sale de la imagen: ' + nm(e));
    const cs = getComputedStyle(e);
    if (cs.overflow !== 'visible' && (e.scrollWidth > e.clientWidth + 2 || e.scrollHeight > e.clientHeight + 2)) issues.push('Contenido cortado: ' + nm(e));
  }
  const kids = [...s.children].filter(e => !e.classList.contains('grid') && e.tagName !== 'STYLE').map(e => [e, e.getBoundingClientRect()]).filter(([e, r]) => r.width > 0 && r.height > 0);
  for (let i = 0; i < kids.length; i++) for (let j = i + 1; j < kids.length; j++) {
    const [a, ra] = kids[i], [b, rb] = kids[j];
    const w = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left), h = Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top);
    if (w > 2 && h > 2) issues.push('Elementos que se pisan: ' + nm(a) + ' / ' + nm(b));
  }
  for (const b of s.querySelectorAll('.tile .ft .b')) { const lh = parseFloat(getComputedStyle(b).lineHeight) || 24; if (b.getBoundingClientRect().height > lh * 1.5) issues.push('Nombre de producto partido en dos líneas: ' + nm(b)); }
  for (const img of s.querySelectorAll('img')) if (!img.complete || img.naturalWidth === 0) issues.push('Imagen que no cargó: ' + img.getAttribute('src'));
  return {issues, text: s.innerText, emojis: [...s.querySelectorAll('.e')].map(e => e.textContent)};
}"""

def render(pages, prefix, w=1080, h=1350):
    """Renderiza cada página a PNG. Si existe la variable de entorno BASE_CHECK=<archivo.json>,
    además corre los chequeos de diseño (textos cortados, elementos pisados, fuera de imagen,
    imágenes rotas) y agrega el resultado a ese JSON."""
    from playwright.async_api import async_playwright
    import json
    check = os.environ.get('BASE_CHECK')
    async def go():
        async with async_playwright() as p:
            b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': w, 'height': h})
            outs, reps = [], []
            for i, html in enumerate(pages, 1):
                fn = os.path.join(D, f'_tmp_{os.getpid()}_{i}.html'); open(fn, 'w').write(html)
                await pg.goto('file://' + fn); await pg.wait_for_timeout(500)
                o = f'{prefix}_{i}.png' if len(pages) > 1 else f'{prefix}.png'
                await pg.screenshot(path=o); outs.append(o)
                if check:
                    r = await pg.evaluate(CHECK_JS); r['png'] = os.path.basename(o); r['size'] = [w, h]; reps.append(r)
                os.remove(fn)
            await b.close()
            if check:
                prev = json.load(open(check)) if os.path.exists(check) else []
                json.dump(prev + reps, open(check, 'w'), ensure_ascii=False, indent=1)
            return outs
    return asyncio.run(go())
