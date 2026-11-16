"""Reel del 17/11/2026 20:30: ¿whey concentrada o isolate? en 15 segundos (5 imágenes 1080×1920).
Fuente: US Dairy Export Council (WPC 80 ≈ 80 % de proteína; WPI 90 % o más, base seca). Precios: kit/README.md."""
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
.val{position:absolute;left:80px;font-family:'Archivo Black';font-size:170px;line-height:1;color:var(--l);text-align:center}
.val small{font-size:70px}
.hero svg{filter:drop-shadow(0 20px 28px rgba(0,0,0,.6))}
.rt4 .tile .ph img{max-height:80%}
.rt4 .tile .ft .b{font-size:20px}
.big2{position:absolute;left:80px;font-family:'Archivo Black';font-size:220px;line-height:1;color:var(--l);text-align:center}
.lab{position:absolute;left:80px;text-align:center;font-size:44px;font-weight:900;text-transform:uppercase;letter-spacing:2px}
.dec{position:absolute;left:80px;display:flex;flex-direction:column;gap:30px}
.dec .r{display:flex;align-items:center;gap:30px;background:var(--panel);border:2px solid var(--line);padding:26px 30px}
.dec .r .e{font-size:110px}
.dec .r p{font-size:40px;font-weight:700;line-height:1.25;color:#d6d6d8}.dec .r p b{color:var(--l);font-weight:900;text-transform:uppercase}
</style>'''
R = 'right:140px'  # margen derecho extra: ahí van los botones de Instagram en los reels
LEG = f'<div class="legal" style="bottom:auto;top:1545px;{R}">{LEGAL_TXT}</div>'



# 1 · GANCHO
r1 = ST + '<div class="eb" style="top:300px">En 15 segundos</div>'
r1 += f'<div class="t" style="top:360px;{R};font-size:100px">¿Whey<br>concentrada<br>o <span class="box">isolate?</span></div>'
r1 += f'<div class="hero" style="top:820px;{R};height:380px">{E("🥛",260)}</div>'
r1 += f'<div class="big" style="top:1290px;{R}">Las dos son whey.<br><span>¿Qué cambia?</span></div>'
r1 += LEG

def tipo(eb, sigla, nombre, pct, sub):
    r = ST + f'<div class="eb" style="top:300px">{eb}</div>'
    r += f'<div class="t" style="top:360px;{R};font-size:110px">{nombre}</div>'
    r += f'<div class="lab" style="top:560px;{R};color:#a9a9ad">{sigla}</div>'
    r += f'<div class="big2" style="top:720px;{R}">{pct}</div>'
    r += f'<div class="lab" style="top:960px;{R}">de proteína</div>'
    r += f'<div class="sub" style="top:1110px;{R}">{sub}</div>'
    return r + LEG

r2 = tipo('Opción 1', 'WPC · menos filtrada', 'Concentrada', '≈80 %', 'Varía: <b>la más común</b> ronda el 80 %.<br>Trae <b>algo más de lactosa</b> y grasa.')
r3 = tipo('Opción 2', 'WPI · filtrado extra', 'Isolate', '90 %+', 'Un filtrado extra.<br><b>Muy poca lactosa</b> y grasa.')
r2 = r2.replace('</div>' + LEG, '<br><span style="font-size:28px;color:#a9a9ad">Base seca · fuente: US Dairy Export Council</span></div>' + LEG)
r3 = r3.replace('</div>' + LEG, '<br><span style="font-size:28px;color:#a9a9ad">Base seca · fuente: US Dairy Export Council</span></div>' + LEG)

# 4 · CÓMO ELEGIR
r4 = ST + '<div class="eb" style="top:300px">¿Cuál elegir?</div>'
r4 += f'<div class="t" style="top:360px;{R};font-size:104px">Depende<br>de <span class="box">vos</span></div>'
r4 += (f'<div class="dec" style="top:700px;{R}">'
       f'<div class="r">{E("👍")}<p>¿La leche te cae bien?<br><b>Concentrada</b>, más accesible</p></div>'
       f'<div class="r">{E("🥛")}<p>¿La lactosa te cae pesada?<br><b>Isolate</b>, trae menos</p></div></div>')
r4 += f'<div class="sub" style="top:1260px;{R}">Muchas son <b>mezcla</b>: mirá<br>el primer ingrediente</div>'
r4 += LEG

# 5 · CTA
r5 = ST + '<div class="eb" style="top:300px">Whey en BASE</div>'
r5 += f'<div class="t" style="top:360px;{R};font-size:100px">Elegí<br><span class="box">la tuya</span></div>'
r5 += tiles([('on_gold_standard', pf('ON Gold Standard', '$60.900')), ('ena_truemade_vainilla', pf('ENA Truemade', '$90.900')),
             ('platinum1kg_vainilla', pf('Star Platinum', '$93.900'))],
            620, 276, 470, 16).replace('class="tiles" style="', f'class="tiles rt4" style="{R};')
r5 += f'<div class="btn" style="left:80px;{R};justify-content:center;top:1225px;font-size:32px;padding:26px 30px">{E("🛒",36)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
r5 += f'<div class="wa" style="top:1345px;{R}">{E("💬",26)} WHATSAPP <span>11 2178-9431</span> · SOLO MENSAJES</div>'
r5 += f'<div class="wa" style="top:1400px;{R};font-size:24px;color:#a9a9ad">Precios por transferencia o efectivo</div>'
r5 += LEG

print(render([page(1, r, nxt=False, total=1, story=True, legal=False) for r in (r1, r2, r3, r4, r5)], f'{OUT}/reel', 1080, 1920))
