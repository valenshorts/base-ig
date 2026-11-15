"""Historias del 16/11/2026 (1080×1920, sin sticker): 11:00 arranque · 15:00 producto del día ·
18:00 recordatorio del sorteo (quedan 12 días) · 21:30 cierre."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.op4{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:26px}
.op4 .o{position:relative;height:330px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column}
.op4 .o .ph{flex:1;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-bottom:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.op4 .o .ph .e{font-size:120px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.op4 .o .lt{position:absolute;left:0;top:0;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:38px;width:62px;height:62px;display:flex;align-items:center;justify-content:center}
.op4 .o .nm{height:90px;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:900;text-transform:uppercase}
.vote{position:absolute;left:80px;right:80px;text-align:center;font-weight:800;font-size:34px;line-height:1.3}
.vote span{color:var(--l)}
.feed{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:26px;background:var(--panel);border:2px solid var(--l);padding:22px 26px}
.feed .e{font-size:64px}
.feed .tx{font-size:27px;font-weight:700;line-height:1.3;color:#d6d6d8}.feed .tx b{color:var(--l);font-weight:900;text-transform:uppercase;display:block;font-size:30px}
.pd .tile .ph img{max-height:82%}
.pd .tile .ft .b{font-size:30px}
.pd .tile .ft .p{font-size:76px}
.chip2{position:absolute;right:80px;top:262px;background:var(--l);color:var(--bk);font-weight:900;font-size:24px;letter-spacing:3px;padding:10px 18px}
.tipb{position:absolute;left:80px;right:80px;font-size:30px;font-weight:700;line-height:1.35;color:#d6d6d8;border-left:6px solid var(--l);padding-left:24px}
.tipb b{color:var(--l)}
.cd{position:absolute;left:80px;right:80px;height:300px;display:flex;align-items:stretch;gap:0}
.cd .n{flex:0 0 330px;background:var(--l);color:var(--bk);display:flex;flex-direction:column;align-items:center;justify-content:center}
.cd .n b{font-family:'Archivo Black';font-weight:400;font-size:190px;line-height:.9}
.cd .n span{font-size:30px;font-weight:900;letter-spacing:6px;margin-top:10px}
.cd .tx{flex:1;background:var(--panel);border:2px solid var(--line);border-left:0;display:flex;flex-direction:column;justify-content:center;padding:0 34px;gap:12px}
.cd .tx b{font-size:44px;font-weight:900;text-transform:uppercase;line-height:1.05}
.cd .tx p{font-size:27px;font-weight:600;color:#bdbdc0;line-height:1.3}.cd .tx p em{font-style:normal;color:var(--l);font-weight:800}
.chip{position:absolute;left:12px;top:12px;z-index:2;background:var(--bk);border:2px solid var(--l);color:var(--w);font-size:26px;font-weight:900;letter-spacing:1.5px;padding:6px 14px}
.sz .tile .ph img{max-height:76%;margin-top:30px}
.stp{position:absolute;left:80px;right:80px;display:flex;gap:20px}
.stp div{flex:1;background:var(--panel);border:2px solid var(--line);height:170px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px}
.stp .e{font-size:64px}
.stp p{font-size:24px;font-weight:900;text-transform:uppercase;letter-spacing:.5px;text-align:center;line-height:1.1}
.rem{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:26px;background:var(--panel);border:2px solid var(--line);padding:20px 26px}
.rem .e{font-size:60px}
.rem .tx{font-size:26px;font-weight:700;line-height:1.3;color:#d6d6d8}.rem .tx b{color:#fff;font-weight:900;text-transform:uppercase;display:block;font-size:29px}
.rem .tx em{font-style:normal;color:var(--l)}
.big12{position:absolute;left:80px;right:80px;height:260px;display:flex;align-items:center;justify-content:center;gap:40px;background:var(--panel);border:2px solid var(--l)}
.big12 b{font-family:'Archivo Black';font-weight:400;font-size:200px;line-height:.9;color:var(--l)}
.big12 div{display:flex;align-items:center;gap:26px}
.big12 span{font-size:40px;font-weight:900;text-transform:uppercase;line-height:1.1}
</style>'''
CAT = f'<div class="vote" style="top:1585px;font-size:28px;letter-spacing:1.5px;color:#d6d6d8">{E("🛒",28)} VER CATÁLOGO · <span>LINK EN LA BIO</span></div>'
LEG = f'<div class="legal" style="bottom:auto;top:1690px">{LEGAL_TXT}</div>'


def op4(ops, top):
    return f'<div class="op4" style="top:{top}px">' + ''.join(
        f'<div class="o"><div class="ph">{E(e)}</div><div class="lt">{l}</div><div class="nm">{n}</div></div>' for l, e, n in ops) + '</div>'

def tile(f, chip, ft):
    return f'<div class="tile"><div class="ph"><div class="chip">{chip}</div><img src="assets/{f}.png"></div>{ft}</div>'

# 11:00 · ARRANQUE DEL LUNES
h1 = ST + '<div class="eb" style="top:270px">Arranca la semana</div>'
h1 += '<div class="t" style="top:325px;font-size:80px">¿Cuántos días<br>entrenás<br><span class="box">por semana?</span></div>'
h1 += op4([('A', '🚶', '1–2 días'), ('B', '🏃', '3 días'), ('C', '🏋️', '4–5 días'), ('D', '🔥', '6 o más')], 690)
h1 += f'<div class="vote" style="top:1400px">Respondé esta historia con<br><span>A, B, C o D</span> {E("💬",34)}</div>'
h1 += f'<div class="feed" style="top:1525px;padding:16px 26px">{E("🧩")}<div class="tx"><b>Hoy a las 13:00</b>Un desafío de magnesio en el feed.</div></div>'
h1 += LEG

# 15:00 · PRODUCTO DEL DÍA
h2 = ST + '<div class="eb" style="top:270px">Producto del día</div>'
h2 += '<div class="t" style="top:325px;font-size:88px">Creatina<br><span class="box">+ electrolitos</span></div>'
h2 += tiles([('ena_creaelec_bluelemon', pf('ENA Creatina + electrolitos', '$28.900'))], 620, 760, 560).replace('class="tiles"', 'class="tiles pd"')
h2 += '<div class="tipb" style="top:1400px">La creatina aumenta el rendimiento físico en series sucesivas de ejercicios cortos de alta intensidad.<br>Precio por transferencia o efectivo.</div>'
h2 += CAT + LEG

# 18:00 · RECORDATORIO DEL SORTEO (16/11 → 27/11 inclusive = 12 días)
h3 = ST + '<div class="eb" style="top:270px">Sorteo de 3 creatinas</div>'
h3 += f'''<div class="big12" style="top:330px">{E("⏳",150)}<div><b>12</b><span>días para<br>participar</span></div></div>'''
h3 += ('<div class="tiles sz" style="top:640px;--w:430px;--h:420px;--g:26px">'
       + tile('creatina_gold_300g', '×2', cf('Creatina Gold 300 g', 28))
       + tile('creatina_star_300g', '×1', cf('Creatina Star 300 g', 28)) + '</div>')
h3 += f'''<div class="rem" style="top:1170px">{E("🏁")}<div class="tx"><b>Cierra el viernes 27/11 a las 23:59</b>Sorteo en vivo el sábado 28/11. <em>Envío gratis a todo el país.</em></div></div>'''
h3 += f'<div class="vote" style="top:1360px">{E("👉",34)} Participá en el<br><span>post del sorteo</span></div>'
h3 += f'<div class="vote" style="top:1490px;font-size:28px;color:#bdbdc0">Lo encontrás en nuestro perfil (posteo del 14/11)</div>'
h3 += LEG

# 21:30 · CIERRE DEL DÍA
h4 = ST + '<div class="eb" style="top:270px">Para cerrar el lunes</div>'
h4 += '<div class="t" style="top:325px;font-size:80px">¿Mirás si tu<br>creatina dice<br><span class="box">monohidrato?</span></div>'
h4 += op4([('A', '✅', 'Siempre'), ('B', '🤷', 'A veces'), ('C', '🙈', 'Nunca miré'), ('D', '🙅', 'No tomo')], 690)
h4 += f'<div class="vote" style="top:1400px">Respondé esta historia con<br><span>A, B, C o D</span> {E("💬",34)}</div>'
h4 += f'<div class="rem" style="top:1525px;padding:14px 26px">{E("🏷️")}<div class="tx"><b>¿Qué es Creapure?</b>Mirá el post de hoy: <em>es una marca, no otra creatina.</em></div></div>'
h4 += LEG

for h, nm in [(h1, 'historia_1100'), (h2, 'historia_1500'), (h3, 'historia_1800'), (h4, 'historia_2130')]:
    print(render([page(1, h, nxt=False, total=1, story=True, legal=False)], f'{OUT}/{nm}', 1080, 1920))
