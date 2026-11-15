"""Reel del 16/11/2026 20:30: ¿qué tiene más magnesio? en 15 segundos (6 imágenes 1080×1920).
Fuente: USDA FoodData Central (SR Legacy), magnesio cada 100 g."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
# Semillas de zapallo (no hay emoji fiel): SVG plano
PEPITAS = '''<svg viewBox="0 0 140 110" width="{s}" height="{h}">
<g fill="#9BB85A" stroke="#6E8A3A" stroke-width="2">
<ellipse cx="40" cy="38" rx="13" ry="24" transform="rotate(-30 40 38)"/><ellipse cx="72" cy="30" rx="13" ry="24" transform="rotate(8 72 30)"/>
<ellipse cx="103" cy="42" rx="13" ry="24" transform="rotate(38 103 42)"/><ellipse cx="54" cy="74" rx="13" ry="24" transform="rotate(-70 54 74)"/>
<ellipse cx="92" cy="78" rx="13" ry="24" transform="rotate(64 92 78)"/></g>
<g fill="#C3DB86"><ellipse cx="38" cy="34" rx="4" ry="12" transform="rotate(-30 38 34)"/><ellipse cx="71" cy="25" rx="4" ry="12" transform="rotate(8 71 25)"/>
<ellipse cx="104" cy="38" rx="4" ry="12" transform="rotate(38 104 38)"/></g></svg>'''
# Almendras (🌰 es castaña, no almendra): SVG plano
ALM = '''<svg viewBox="0 0 140 110" width="{s}" height="{h}">
<g stroke="#7A4A26" stroke-width="2"><path d="M44 12 C66 30 70 70 44 98 C18 70 22 30 44 12z" fill="#C68A55" transform="rotate(-18 44 55)"/>
<path d="M96 12 C118 30 122 70 96 98 C70 70 74 30 96 12z" fill="#B97A45" transform="rotate(20 96 55)"/></g>
<g stroke="#8E5A30" stroke-width="2" fill="none" stroke-linecap="round"><path d="M40 34 q4 20 0 44" transform="rotate(-18 44 55)"/><path d="M50 36 q3 18 -1 40" transform="rotate(-18 44 55)"/>
<path d="M92 34 q4 20 0 44" transform="rotate(20 96 55)"/><path d="M102 36 q3 18 -1 40" transform="rotate(20 96 55)"/></g></svg>'''
alm = lambda s: ALM.format(s=s, h=int(s * 110 / 140))
pep = lambda s: PEPITAS.format(s=s, h=int(s * 110 / 140))

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
.val{position:absolute;left:80px;font-family:'Archivo Black';font-size:170px;line-height:1;color:var(--l);text-align:center}
.val small{font-size:70px}
.hero svg{filter:drop-shadow(0 20px 28px rgba(0,0,0,.6))}
.rt4 .tile .ph img{max-height:80%}
.rt4 .tile .ft .b{font-size:20px}
</style>'''
R = 'right:140px'  # margen derecho extra: ahí van los botones de Instagram en los reels
LEG = f'<div class="legal" style="bottom:auto;top:1545px;{R}">{LEGAL_TXT}</div>'


def paso(n, eb, titulo, ic, val, sub):
    r = ST + f'<div class="eb" style="top:300px">{eb}</div>'
    r += f'<div class="t" style="top:360px;{R};font-size:104px">{titulo}</div>'
    r += f'<div class="hero" style="top:640px;{R};height:420px">{ic}</div>'
    r += f'<div class="val" style="top:1110px;{R}">{val}<small> mg</small></div>'
    r += f'<div class="sub" style="top:1320px;{R}">{sub}</div>'
    return r + LEG

# 1 · GANCHO
r1 = ST + '<div class="eb" style="top:300px">Desafío rápido</div>'
r1 += f'<div class="t" style="top:360px;{R};font-size:104px">¿Qué tiene<br>más <span class="box">magnesio?</span></div>'
r1 += f'<div class="hero" style="top:720px;{R};height:460px;gap:16px">{E("🍌",190)}{pep(205)}{E("🍫",190)}{alm(205)}</div>'
r1 += f'<div class="big" style="top:1300px;{R}"><span style="color:#fff;text-transform:none">Cada 100 g</span><br><span>¿Adivinás el orden?</span></div>'
r1 += LEG

r2 = paso(2, '4.º lugar', 'Banana', E('🍌', 300), '27', 'Lo suyo es el <b>potasio</b>: 358 mg')
r3 = paso(3, '3.º lugar', 'Chocolate<br>amargo', E('🍫', 280), '228', 'Chocolate <b>70–85 % cacao</b>')
r4 = paso(4, '2.º lugar', 'Almendras', alm(380), '270', 'Un clásico de los <b>frutos secos</b>')
r5 = paso(5, '1.º lugar', 'Semillas<br>de zapallo', pep(380), '592', 'Las que <b>más magnesio</b> traen.<br>Fuente: USDA FoodData Central')
r5 = r5.replace('font-size:104px', 'font-size:96px')

# 6 · CTA
r6 = ST + '<div class="eb" style="top:300px">Magnesio en cápsulas</div>'
r6 += f'<div class="t" style="top:360px;{R};font-size:100px">Citrato o<br><span class="box">glicinato</span></div>'
r6 += tiles([('star_citratomg', pf('Citrato Star', '$10.900')), ('ena_citratomg', pf('Citrato ENA', '$12.900')),
             ('magnesio_glicinato_gold', pf('Glicinato Gold', '$15.900'))],
            620, 276, 470, 16).replace('class="tiles" style="', f'class="tiles rt4" style="{R};')
r6 += f'<div class="btn" style="left:80px;{R};justify-content:center;top:1225px;font-size:32px;padding:26px 30px">{E("🛒",36)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
r6 += f'<div class="wa" style="top:1345px;{R}">{E("💬",26)} WHATSAPP <span>11 2178-9431</span> · SOLO MENSAJES</div>'
r6 += f'<div class="wa" style="top:1400px;{R};font-size:24px;color:#a9a9ad">Precios por transferencia o efectivo</div>'
r6 += LEG

print(render([page(1, r, nxt=False, total=1, story=True, legal=False) for r in (r1, r2, r3, r4, r5, r6)], f'{OUT}/reel', 1080, 1920))
