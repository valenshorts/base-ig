"""Historias del 26/11/2026 (1080×1920): 11:00 ¿cómo pesás tu comida? · 15:00 producto del día Omega 3 Gold 30 caps
· 18:00 sorteo (quedan 2 días, contando hoy) · 21:30 recordatorio del reel «3 errores con la creatina».
Precios: kit/README.md. Frase de creatina permitida (EFSA). Sorteo: campanas/sorteo-creatinas/bases.md."""
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
.pd .tile .ph img{max-height:84%}
.pd .tile .ft .b{font-size:30px}
.pd .tile .ft .p{font-size:76px}
.tipb{position:absolute;left:80px;right:80px;font-size:30px;font-weight:700;line-height:1.35;color:#d6d6d8;border-left:6px solid var(--l);padding-left:24px}
.tipb b{color:var(--l)}
.chip{position:absolute;left:12px;top:12px;z-index:2;background:var(--bk);border:2px solid var(--l);color:var(--w);font-size:26px;font-weight:900;letter-spacing:1.5px;padding:6px 14px}
.sz .tile .ph img{max-height:76%;margin-top:30px}
.cd{position:absolute;left:80px;right:80px;height:320px;display:flex}
.cd .n{flex:0 0 340px;background:var(--l);color:var(--bk);display:flex;flex-direction:column;align-items:center;justify-content:center}
.cd .n b{font-family:'Archivo Black';font-weight:400;font-size:220px;line-height:.85}
.cd .n span{font-size:32px;font-weight:900;letter-spacing:6px;margin-top:8px}
.cd .tx{flex:1;background:var(--panel);border:2px solid var(--line);border-left:0;display:flex;flex-direction:column;justify-content:center;padding:0 34px;gap:14px}
.cd .tx b{font-size:46px;font-weight:900;text-transform:uppercase;line-height:1.05}
.cd .tx p{font-size:28px;font-weight:600;color:#bdbdc0;line-height:1.3}.cd .tx p em{font-style:normal;color:var(--l);font-weight:800}
.stp{position:absolute;left:80px;right:80px;display:flex;gap:20px}
.stp div{flex:1;background:var(--panel);border:2px solid var(--line);height:190px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px}
.stp .e{font-size:68px}
.stp p{font-size:24px;font-weight:900;text-transform:uppercase;letter-spacing:.5px;text-align:center;line-height:1.1}
.rem{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:28px;background:var(--panel);border:2px solid var(--line);padding:44px 28px}
.rem .e{font-size:72px;flex:0 0 90px;text-align:center}
.rem .tx{font-size:28px;font-weight:700;line-height:1.3;color:#d6d6d8}.rem .tx b{color:#fff;font-weight:900;text-transform:uppercase;display:block;font-size:32px}
.rem .tx em{font-style:normal;color:var(--l)}
</style>'''
CAT = f'<div class="vote" style="top:1585px;font-size:28px;letter-spacing:1.5px;color:#d6d6d8">{E("🛒",28)} VER CATÁLOGO · <span>LINK EN LA BIO</span></div>'
LEG = f'<div class="legal" style="bottom:auto;top:1690px">{LEGAL_TXT}</div>'


BAL = ('<svg viewBox="0 0 120 120" width="130" height="130"><rect x="38" y="18" width="44" height="8" fill="#d6d6d8"/>'
       '<rect x="56" y="26" width="8" height="18" fill="#9a9a9e"/><rect x="14" y="44" width="92" height="62" fill="#e8e8ea"/>'
       '<rect x="30" y="58" width="60" height="26" fill="#0B0B0C"/><rect x="38" y="66" width="44" height="10" fill="#C6F432"/></svg>')


def op4(ops, top):
    return f'<div class="op4" style="top:{top}px">' + ''.join(
        f'<div class="o"><div class="ph">{E(e)}</div><div class="lt">{l}</div><div class="nm">{n}</div></div>' for l, e, n in ops) + '</div>'

def tile(f, chip, ft):
    return f'<div class="tile"><div class="ph"><div class="chip">{chip}</div><img src="assets/{f}.png"></div>{ft}</div>'


# 11:00 · ARRANQUE (pregunta A/B/C/D, adelanta el tema del post de las 13:00 sin dar la respuesta)
h1 = ST + '<div class="eb" style="top:270px">Pregunta del jueves</div>'
h1 += '<div class="t" style="top:325px;font-size:84px">¿Cómo pesás<br>tu <span class="box">comida?</span></div>'
h1 += op4([('A', BAL, 'En crudo'), ('B', '🍽️', 'En cocido'), ('C', '👀', 'A ojo'), ('D', '🤷', 'No la peso')], 640)
h1 += f'<div class="vote" style="top:1370px">Respondé esta historia con<br><span>A, B, C o D</span> {E("💬",34)}</div>'
h1 += f'<div class="vote" style="top:1530px;font-size:28px;color:#bdbdc0">A las 13:00 te contamos por qué importa</div>'
h1 += LEG

# 15:00 · PRODUCTO DEL DÍA
h2 = ST + '<div class="eb" style="top:270px">Producto del día</div>'
h2 += '<div class="t" style="top:325px;font-size:92px">Omega 3<br><span class="box">Gold</span></div>'
h2 += tiles([('gold_omega3', pf('Omega 3 Gold 30 caps', '$28.900'))], 620, 760, 560).replace('class="tiles"', 'class="tiles pd"')
h2 += '<div class="tipb" style="top:1400px">Mirá en la etiqueta cuánto EPA y DHA trae cada porción.<br><b>Precio por transferencia o efectivo.</b></div>'
h2 += CAT + LEG

# 18:00 · SORTEO (quedan 2 días: hoy jueves y mañana viernes 27/11)
h3 = ST + '<div class="eb" style="top:270px">Sorteo de 3 creatinas</div>'
h3 += '<div class="t" style="top:325px;font-size:80px">Se termina<br><span class="box">el sorteo</span></div>'
h3 += '<div class="cd" style="top:560px"><div class="n"><b>2</b><span>DÍAS</span></div><div class="tx"><b>Hoy y mañana</b><p>Cierra el <em>viernes 27/11 a las 23:59</em>. Envío gratis.</p></div></div>'
h3 += ('<div class="tiles sz" style="top:920px;--w:430px;--h:360px;--g:26px">'
       + tile('creatina_gold_300g', '×2', cf('Creatina Gold 300 g', 28))
       + tile('creatina_star_300g', '×1', cf('Creatina Star 300 g', 28)) + '</div>')
h3 += f'<div class="vote" style="top:1400px">{E("👉",34)} Participá en el <span>post del sorteo</span><br><span style="color:#d6d6d8;font-size:30px">fijado en nuestro perfil</span></div>'
h3 += f'<div class="vote" style="top:1530px;font-size:28px;color:#bdbdc0">Seguinos, dale me gusta y comentá etiquetando a 2 personas</div>'
h3 += LEG

# 21:30 · RECORDATORIO DEL REEL
h4 = ST + '<div class="eb" style="top:270px">Reel de hoy</div>'
h4 += '<div class="t" style="top:325px;font-size:84px">3 errores<br>con la <span class="box">creatina</span></div>'
h4 += (f'<div class="rem" style="top:620px">{E("🏋️")}<div class="tx"><b>1 · Solo los días de gym</b>Va <em>todos los días</em>.</div></div>'
       f'<div class="rem" style="top:840px">{E("⏳")}<div class="tx"><b>2 · Carga obligatoria</b>Con <em>3 g por día</em> también llegás.</div></div>'
       f'<div class="rem" style="top:1060px">{E("🥄")}<div class="tx"><b>3 · Tomarla a ojo</b>Medí la porción: <em>3 g</em>.</div></div>')
h4 += f'<div class="vote" style="top:1310px">¿Cuál cometías?<br><span>Contanos por mensaje</span> {E("💬",34)}</div>'
h4 += f'<div class="vote" style="top:1490px;font-size:28px;color:#bdbdc0">Mirá el reel completo en nuestro perfil<br>Fuente: ISSN 2017</div>'
h4 += LEG

for h, nm in [(h1, 'historia_1100'), (h2, 'historia_1500'), (h3, 'historia_1800'), (h4, 'historia_2130')]:
    print(render([page(1, h, nxt=False, total=1, story=True, legal=False)], f'{OUT}/{nm}', 1080, 1920))
