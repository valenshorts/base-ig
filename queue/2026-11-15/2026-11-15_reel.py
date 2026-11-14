"""Reel del 15/11/2026 20:30: colágeno vs whey en 15 segundos (5 imágenes 1080×1920)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.duo{position:absolute;left:80px;right:80px;height:520px;display:flex;align-items:center;justify-content:center;gap:30px}
.duo .bx{width:380px;height:520px;display:flex;flex-direction:column}
.duo .bx .ph{flex:1;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);display:flex;align-items:center;justify-content:center}
.duo .bx .ph .e{font-size:210px;filter:drop-shadow(0 18px 26px rgba(0,0,0,.6))}
.duo .bx .nm{height:100px;background:var(--panel2);display:flex;align-items:center;justify-content:center;font-size:42px;font-weight:900;letter-spacing:1px;text-transform:uppercase}
.duo .bx.on{border-color:var(--l)} .duo .bx.on .nm{color:var(--l)}
.duo .op{font-family:'Archivo Black';font-size:110px;color:var(--l)}
.hero{position:absolute;left:80px;right:80px;display:flex;align-items:center;justify-content:center;gap:40px}
.hero .e{filter:drop-shadow(0 20px 28px rgba(0,0,0,.6))}
.mk{width:230px;height:230px;display:flex;align-items:center;justify-content:center;font-family:'Archivo Black';font-size:150px}
.mk.y{background:var(--l);color:var(--bk)} .mk.n{border:6px solid #6a6a6e;color:#d6d6d8}
.big{position:absolute;left:80px;right:80px;font-size:58px;font-weight:900;text-transform:uppercase;line-height:1.1;text-align:center}
.big span{color:var(--l)}
.sub{position:absolute;left:80px;right:80px;text-align:center;font-size:38px;font-weight:700;color:#d6d6d8;line-height:1.3}
.sub b{color:var(--l)}
.rt .tile .ph img{max-height:80%}
.rt .tile .ft .b{font-size:24px}
.wa{position:absolute;left:80px;right:80px;text-align:center;font-size:27px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8}
.wa span{color:var(--l)}
</style>'''
LEG = f'<div class="legal" style="bottom:auto;top:1690px">{LEGAL_TXT}</div>'
R = 'right:140px'  # margen derecho extra: ahí van los botones de Instagram en los reels

# 1 · GANCHO
r1 = ST + '<div class="eb" style="top:300px">En 15 segundos</div>'
r1 += f'<div class="t" style="top:360px;{R};font-size:118px">¿Colágeno<br>= <span class="box">whey?</span></div>'
r1 += f'''<div class="duo" style="top:760px;{R}"><div class="bx panel" style="position:relative"><div class="ph">{E("🦴")}</div><div class="nm">Colágeno</div></div>
 <div class="op">?</div><div class="bx panel" style="position:relative"><div class="ph">{E("🥛")}</div><div class="nm">Whey</div></div></div>'''
r1 += f'<div class="big" style="top:1380px;{R}">Spoiler: <span>no</span></div>'
r1 += LEG

# 2 · LAS DOS SON PROTEÍNA
r2 = ST + '<div class="eb" style="top:300px">Lo que tienen en común</div>'
r2 += f'<div class="t" style="top:360px;{R};font-size:112px">Las dos son<br><span class="box">proteína</span></div>'
r2 += f'<div class="hero" style="top:800px;{R};height:420px">{E("🦴",200)}<div class="mk y">✓</div>{E("🥛",200)}</div>'
r2 += f'<div class="sub" style="top:1330px;{R}">Pero <b>no son iguales</b> por dentro</div>'
r2 += LEG

# 3 · WHEY
r3 = ST + '<div class="eb" style="top:300px">Whey</div>'
r3 += f'<div class="t" style="top:360px;{R};font-size:104px">Trae los 9<br><span class="box">esenciales</span></div>'
r3 += f'<div class="hero" style="top:800px;{R};height:420px">{E("🥛",260)}<div class="mk y">9</div></div>'
r3 += f'<div class="sub" style="top:1330px;{R}">Trae los 9 aminoácidos esenciales<br>y se destaca por la <b>leucina</b></div>'
r3 += LEG

# 4 · COLÁGENO
r4 = ST + '<div class="eb" style="top:300px">Colágeno</div>'
r4 += f'<div class="t" style="top:360px;{R};font-size:100px">Le falta el<br><span class="box">triptófano</span></div>'
r4 += f'<div class="hero" style="top:800px;{R};height:420px">{E("🦴",260)}<div class="mk n">✕</div></div>'
r4 += f'<div class="sub" style="top:1330px;{R}">Uno de los 9 esenciales.<br>Por eso <b>no reemplaza a tu whey</b></div>'
r4 += LEG

# 5 · CTA
r5 = ST + '<div class="eb" style="top:300px">Conocé las dos</div>'
r5 += f'<div class="t" style="top:360px;{R};font-size:100px">Mirá qué trae<br><span class="box">cada una</span></div>'
r5 += tiles([('collagen', pf('Colágeno · 210 g', '$18.900')), ('ena_prot_vain', pf('ENA Whey 907 g', '$66.900'))],
            640, 400, 400, 20).replace('class="tiles" style="', f'class="tiles rt" style="{R};')
r5 += f'<div class="btn" style="left:80px;{R};justify-content:center;top:1250px;font-size:32px;padding:26px 30px">{E("🛒",36)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
r5 += f'<div class="wa" style="top:1390px;{R}">{E("💬",26)} WHATSAPP <span>11 2178-9431</span> · SOLO MENSAJES</div>'
r5 += f'<div class="wa" style="top:1450px;{R};font-size:24px;color:#a9a9ad">Precios por transferencia o efectivo</div>'
r5 += LEG

print(render([page(1, r, nxt=False, total=1, story=True, legal=False) for r in (r1, r2, r3, r4, r5)], f'{OUT}/reel', 1080, 1920))
