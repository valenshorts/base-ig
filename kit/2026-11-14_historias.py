"""Historias del 14/11/2026 (1080×1920, sin sticker): 11:00 arranque · 18:00 adelanto · 21:30 cierre.
La de las 15:00 es la del sorteo (kit/2026-11-14_sorteo.py)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.op4{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:26px}
.op4 .o{position:relative;height:330px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column}
.op4 .o .ph{flex:1;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-bottom:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.op4 .o .ph .e{font-size:120px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.op4 .o .lt{position:absolute;left:0;top:0;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:38px;width:62px;height:62px;display:flex;align-items:center;justify-content:center}
.op4 .o .nm{height:90px;display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:900;text-transform:uppercase}
.vote{position:absolute;left:80px;right:80px;text-align:center;font-weight:800;font-size:34px;line-height:1.3}
.vote span{color:var(--l)}
.feed{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:26px;background:var(--panel);border:2px solid var(--l);padding:22px 26px}
.feed .e{font-size:64px}
.feed .tx{font-size:27px;font-weight:700;line-height:1.3;color:#d6d6d8}.feed .tx b{color:var(--l);font-weight:900;text-transform:uppercase;display:block;font-size:30px}
.clock{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:30px}
.clock .k{flex:0 0 250px;height:200px;background:var(--l);color:var(--bk);display:flex;flex-direction:column;align-items:center;justify-content:center}
.clock .k b{font-family:'Archivo Black';font-weight:400;font-size:62px;line-height:1}
.clock .k span{font-size:22px;font-weight:900;letter-spacing:3px;margin-top:6px}
.clock .tx{font-size:36px;font-weight:900;text-transform:uppercase;line-height:1.12}
.clock .tx em{font-style:normal;color:var(--l)}
.big{position:absolute;left:80px;right:80px;height:420px;display:flex;align-items:center;justify-content:center;gap:34px}
.big .bx{width:300px;height:340px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px}
.big .bx .e{font-size:130px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.big .bx b{font-family:'Archivo Black';font-weight:400;font-size:64px;line-height:1}
.big .bx span{font-size:23px;font-weight:800;letter-spacing:3px;color:#a9a9ad;text-transform:uppercase}
.big .op{font-family:'Archivo Black';font-size:80px;color:var(--l)}
.big .qm{background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:170px}
.yn{position:absolute;left:80px;right:80px;display:flex;gap:30px}
.yn div{flex:1;height:130px;display:flex;align-items:center;justify-content:center;gap:18px;font-family:'Archivo Black';font-size:60px;border:3px solid var(--l)}
.yn .e{font-size:54px}
.rem{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:26px;background:var(--panel);border:2px solid var(--line);padding:20px 26px}
.rem .e{font-size:60px}
.rem .tx{font-size:26px;font-weight:700;line-height:1.3;color:#d6d6d8}.rem .tx b{color:#fff;font-weight:900;text-transform:uppercase;display:block;font-size:29px}
.rem .tx em{font-style:normal;color:var(--l)}
</style>'''
CAT = f'<div class="vote" style="top:1610px;font-size:26px;letter-spacing:1.5px;color:#d6d6d8">{E("🛒",26)} VER CATÁLOGO · <span>LINK EN LA BIO</span></div>'
LEG = f'<div class="legal" style="bottom:auto;top:1690px">{LEGAL_TXT}</div>'

def op4(ops, top):
    return f'<div class="op4" style="top:{top}px">' + ''.join(
        f'<div class="o"><div class="ph">{E(e)}</div><div class="lt">{l}</div><div class="nm">{n}</div></div>' for l, e, n in ops) + '</div>'

# 11:00 · ARRANQUE DEL SÁBADO
h1 = ST + '<div class="eb" style="top:270px">Sábado</div>'
h1 += '<div class="t" style="top:325px;font-size:90px">¿Qué plan<br><span class="box">tenés hoy?</span></div>'
h1 += op4([('A', '🏋️', 'Gym'), ('B', '🏃', 'Salir a correr'), ('C', '⚽', 'Fútbol'), ('D', '😴', 'Descanso')], 600)
h1 += f'<div class="vote" style="top:1330px">Respondé esta historia con<br><span>A, B, C o D</span> {E("💬",34)}</div>'
h1 += f'<div class="feed" style="top:1460px">{E("🎁")}<div class="tx"><b>Hoy a las 13:00</b>Sorteo en el feed. Atentos al perfil.</div></div>'
h1 += LEG

# 18:00 · ADELANTO DEL POST DE LA NOCHE
h3 = ST + '<div class="eb" style="top:270px">Pregunta rápida</div>'
h3 += '<div class="t" style="top:325px;font-size:80px">¿Un scoop de 30 g<br><span class="box">trae 30 g de</span><br><span class="box">proteína?</span></div>'
h3 += f'''<div class="big" style="top:690px">
 <div class="bx panel" style="position:relative">{E("🥄")}<b>30 g</b><span>Scoop</span></div><div class="op">=</div>
 <div class="bx qm">?</div></div>'''
h3 += f'<div class="yn" style="top:1140px"><div>{E("👍")} SÍ</div><div>{E("👎")} NO</div></div>'
h3 += f'<div class="vote" style="top:1300px">Respondé esta historia con <span>SÍ o NO</span> {E("💬",34)}</div>'
h3 += f'''<div class="clock" style="top:1400px"><div class="k"><b>19:30</b><span>HOY</span></div>
 <div class="tx">Sale en el feed:<br><em>cómo leer la etiqueta</em><br>de tu proteína {E("🔍",40)}</div></div>'''
h3 += LEG

# 21:30 · CIERRE DEL DÍA
h4 = ST + '<div class="eb" style="top:270px">Antes de comprar</div>'
h4 += '<div class="t" style="top:325px;font-size:84px">¿Mirás la<br><span class="box">etiqueta?</span></div>'
h4 += op4([('A', '✅', 'Siempre'), ('B', '🤔', 'A veces'), ('C', '🙈', 'Nunca'), ('D', '🏷️', 'Solo el precio')], 600)
h4 += f'<div class="vote" style="top:1330px">Respondé esta historia con<br><span>A, B, C o D</span> {E("💬",34)}</div>'
h4 += f'''<div class="rem" style="top:1450px">{E("🎁")}<div class="tx"><b>Sorteo de 3 creatinas</b>Participá en el <em>post del sorteo</em> hasta el viernes 27/11.</div></div>'''
h4 += LEG

for h, nm in [(h1, 'historia_1100'), (h3, 'historia_1800'), (h4, 'historia_2130')]:
    print(render([page(1, h, nxt=False, total=1, story=True, legal=False)], f'{OUT}/{nm}', 1080, 1920))
