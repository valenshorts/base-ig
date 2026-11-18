"""Historias del 18/11/2026 que faltaban: 11:00 (pregunta A/B/C/D ¿cómo pagás?), 15:00 (producto del día: Colágeno Star) y 21:30 (cierre A/B/C/D ¿qué te llevás en tu próxima compra?).
La de las 18:00 (sorteo) ya estaba en 2026-11-18_historias.py y no se toca. Precios: kit/README.md."""
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
.qd{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:30px}
.qd .nn{font-family:'Archivo Black';font-size:300px;line-height:.82;color:var(--l)}
.qd .tx{display:flex;flex-direction:column;gap:10px}
.qd .tx span{font-size:34px;color:#d6d6d8;font-weight:900;text-transform:uppercase;line-height:1}
.qd .tx b{font-size:96px;font-weight:900;text-transform:uppercase;line-height:.95}
.qd .e{margin-left:auto;font-size:150px}
.tip2{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:26px;background:linear-gradient(160deg,rgba(198,244,50,.13),var(--panel) 70%);border:2px solid var(--l);padding:22px 26px}
.tip2 .e{font-size:64px}
.tip2 .tx{font-size:28px;font-weight:700;line-height:1.3;color:#d6d6d8}.tip2 .tx b{color:#fff;font-weight:900}
.wp{font-family:'Archivo Black';font-weight:400;font-size:96px;color:var(--l);letter-spacing:2px}
.tnt .tile .ph img{max-height:84%}
</style>'''
CAT = f'<div class="vote" style="top:1585px;font-size:28px;letter-spacing:1.5px;color:#d6d6d8">{E("🛒",28)} VER CATÁLOGO · <span>LINK EN LA BIO</span></div>'
LEG = f'<div class="legal" style="bottom:auto;top:1690px">{LEGAL_TXT}</div>'


def op4(ops, top):
    return f'<div class="op4" style="top:{top}px">' + ''.join(
        f'<div class="o"><div class="ph">{E(e)}</div><div class="lt">{l}</div><div class="nm">{n}</div></div>' for l, e, n in ops) + '</div>'

def tile(f, chip, ft):
    return f'<div class="tile"><div class="ph"><div class="chip">{chip}</div><img src="assets/{f}.png"></div>{ft}</div>'

# 11:00 · ARRANQUE DEL MIÉRCOLES
h1 = ST + '<div class="eb" style="top:270px">Pregunta del miércoles</div>'
h1 += '<div class="t" style="top:325px;font-size:84px">¿Cómo pagás<br>tus <span class="box">suplementos?</span></div>'
h1 += op4([('A', '🏦', 'Transferencia'), ('B', '💵', 'Efectivo'), ('C', '💳', 'Tarjeta'), ('D', '🤔', 'Todavía no compré')], 660)
h1 = h1.replace('<div class="nm">Todavía no compré</div>', '<div class="nm" style="font-size:27px">Todavía no compré</div>')
h1 += f'<div class="vote" style="top:1365px">Respondé esta historia con<br><span>A, B, C o D</span> {E("💬",34)}</div>'
h1 += f'<div class="feed" style="top:1500px;padding:16px 26px">{E("💬")}<div class="tx"><b>Hoy a las 13:00</b>Tu pedido en un solo mensaje: qué mandarnos.</div></div>'
h1 += LEG

# 15:00 · PRODUCTO DEL DÍA
h2 = ST + '<div class="eb" style="top:270px">Producto del día</div>'
h2 += '<div class="t" style="top:325px;font-size:92px">Colágeno<br><span class="box">Star</span></div>'
h2 += tiles([('collagen', pf('Colágeno Star con resveratrol 210 g', '$18.900'))], 600, 920, 640).replace('class="tiles"', 'class="tiles pd"')
h2 += '<div class="tipb" style="top:1400px">Respetá la porción que indica la etiqueta.<br>Precio por transferencia o efectivo.</div>'
h2 += CAT + LEG

# 21:30 · CIERRE DEL DÍA
h4 = ST + '<div class="eb" style="top:270px">Para cerrar el miércoles</div>'
h4 += '<div class="t" style="top:325px;font-size:80px">¿Qué te llevás<br>en tu <span class="box">próxima compra?</span></div>'
h4 += op4([('A', '🧂', 'Creatina'), ('B', '🥛', 'Proteína'), ('C', '🛍️', 'Combo'), ('D', '🤔', 'No sé todavía')], 660)
h4 = h4.replace(f'<div class="ph">{E("🧂")}</div><div class="lt">A</div>', '<div class="ph"><img src="assets/creatina_star_300g.png" style="height:200px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))"></div><div class="lt">A</div>')
h4 = h4.replace(f'<div class="ph">{E("🥛")}</div><div class="lt">B</div>', '<div class="ph"><img src="assets/ena_prot_vain.png" style="height:200px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))"></div><div class="lt">B</div>')
h4 = h4.replace('<div class="nm">No sé todavía</div>', '<div class="nm" style="font-size:28px">No sé todavía</div>')
h4 += f'<div class="vote" style="top:1365px">Respondé esta historia con<br><span>A, B, C o D</span> {E("💬",34)}</div>'
h4 += f'<div class="rem" style="top:1500px;padding:16px 26px">{E("👀")}<div class="tx"><b>Mirá el post de las 19:30</b>Qué te llevás <em>según tu presupuesto.</em></div></div>'
h4 += LEG

for h, nm in [(h1, 'historia_1100'), (h2, 'historia_1500'), (h4, 'historia_2130')]:
    print(render([page(1, h, nxt=False, total=1, story=True, legal=False)], f'{OUT}/{nm}', 1080, 1920))
