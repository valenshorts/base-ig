"""Historias del 20/11/2026 (viernes): 11:00 pregunta A/B/C/D «¿cómo comés el huevo?», 15:00 producto del día
ON Micronised Creatine 317 g, 18:00 recordatorio del sorteo (20/11 → 27/11 inclusive = quedan 8 días),
21:30 B2B «¿Tenés un negocio? Mandá MAYORISTA» + recordatorio del post de las 19:30 (para gimnasios).
Precios: kit/README.md. Sin stickers: la interacción va escrita."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.op4{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:26px}
.op4 .o{position:relative;height:330px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column}
.op4 .o .ph{flex:1;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-bottom:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.op4 .o .ph .e{font-size:130px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.op4 .o .lt{position:absolute;left:0;top:0;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:38px;width:62px;height:62px;display:flex;align-items:center;justify-content:center}
.op4 .o .nm{height:90px;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:900;text-transform:uppercase}
.vote{position:absolute;left:80px;right:80px;text-align:center;font-weight:800;font-size:34px;line-height:1.3}
.vote span{color:var(--l)}
.feed{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:26px;background:var(--panel);border:2px solid var(--l);padding:16px 26px}
.feed .e{font-size:64px}
.feed .tx{font-size:27px;font-weight:700;line-height:1.3;color:#d6d6d8}.feed .tx b{color:var(--l);font-weight:900;text-transform:uppercase;display:block;font-size:30px}
.pd .tile .ph img{max-height:84%}
.pd .tile .ft .b{font-size:30px}
.pd .tile .ft .p{font-size:76px}
.tipb{position:absolute;left:80px;right:80px;font-size:30px;font-weight:700;line-height:1.35;color:#d6d6d8;border-left:6px solid var(--l);padding-left:24px}
.chip{position:absolute;left:12px;top:12px;z-index:2;background:var(--bk);border:2px solid var(--l);color:var(--w);font-size:26px;font-weight:900;letter-spacing:1.5px;padding:6px 14px}
.sz .tile .ph img{max-height:78%;margin-top:26px}
.c8{position:absolute;left:80px;right:80px;height:330px;border:3px solid var(--l);background:linear-gradient(160deg,rgba(198,244,50,.13),var(--panel) 70%);display:flex;align-items:center;padding:0 40px;gap:36px}
.c8 .n{font-family:'Archivo Black';font-weight:400;font-size:290px;line-height:.8;color:var(--l)}
.c8 .tx{display:flex;flex-direction:column;gap:10px}
.c8 .tx span{font-size:34px;font-weight:900;color:#d6d6d8;text-transform:uppercase;letter-spacing:1px}
.c8 .tx b{font-size:88px;font-weight:900;text-transform:uppercase;line-height:.95}
.dl{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:26px;background:var(--panel);border:2px solid var(--line);padding:20px 26px}
.dl .e{font-size:60px}
.dl .tx{font-size:27px;font-weight:700;line-height:1.3;color:#d6d6d8}.dl .tx b{color:#fff;font-weight:900;text-transform:uppercase;display:block;font-size:30px}
.dl .tx em{font-style:normal;color:var(--l)}
.tag{position:absolute;right:80px;top:262px;border:2px solid var(--l);color:var(--l);font-weight:800;font-size:22px;letter-spacing:4px;padding:8px 16px}
.biz{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:24px}
.biz div{height:290px;border:2px solid var(--line);background:var(--panel);display:flex;flex-direction:column;justify-content:center;align-items:center;gap:18px}
.biz .e{font-size:100px}
.biz b{font-size:32px;font-weight:900;letter-spacing:1px;text-transform:uppercase;text-align:center;line-height:1.1}
.wa{position:absolute;left:80px;right:80px;height:170px;background:var(--l);color:var(--bk);display:flex;align-items:center;justify-content:center;gap:24px}
.wa .e{font-size:70px}
.wa div{font-family:'Archivo Black';font-size:58px;line-height:1}.wa small{display:block;font-family:Montserrat;font-weight:800;font-size:24px;letter-spacing:2px;margin-bottom:8px}
</style>'''
CAT = f'<div class="vote" style="top:1585px;font-size:28px;letter-spacing:1.5px;color:#d6d6d8">{E("🛒",28)} VER CATÁLOGO · <span>LINK EN LA BIO</span></div>'
LEG = f'<div class="legal" style="bottom:auto;top:1690px">{LEGAL_TXT}</div>'


def op4(ops, top):
    return f'<div class="op4" style="top:{top}px">' + ''.join(
        f'<div class="o"><div class="ph">{E(e)}</div><div class="lt">{l}</div><div class="nm">{n}</div></div>' for l, e, n in ops) + '</div>'

def tile(f, chip, ft):
    return f'<div class="tile"><div class="ph"><div class="chip">{chip}</div><img src="assets/{f}.png"></div>{ft}</div>'

# 11:00 · ARRANQUE DEL VIERNES (no adelanta la respuesta del post de las 13:00)
h1 = ST + '<div class="eb" style="top:270px">Pregunta del viernes</div>'
h1 += '<div class="t" style="top:325px;font-size:84px">¿Cómo comés<br>el <span class="box">huevo?</span></div>'
h1 += op4([('A', '🍳', 'A la plancha'), ('B', '🥚', 'Duro'), ('C', '🥪', 'En sándwich'), ('D', '🙅', 'No como huevo')], 640)
h1 += f'<div class="vote" style="top:1345px">Respondé esta historia con<br><span>A, B, C o D</span> {E("💬",34)}</div>'
h1 += f'<div class="feed" style="top:1490px">{E("🤔")}<div class="tx"><b>Hoy a las 13:00</b>¿Clara o yema: cuál tiene más proteína?</div></div>'
h1 += LEG

# 15:00 · PRODUCTO DEL DÍA
h2 = ST + '<div class="eb" style="top:270px">Producto del día</div>'
h2 += '<div class="t" style="top:325px;font-size:84px">ON Micronised<br><span class="box">Creatine</span></div>'
h2 += tiles([('on_creatine', pf('ON Micronised Creatine 317 g', '$28.900'))], 620, 920, 640).replace('class="tiles"', 'class="tiles pd"')
h2 += '<div class="tipb" style="top:1420px">La creatina aumenta el rendimiento físico en series sucesivas de ejercicios cortos de alta intensidad.</div>'
h2 += CAT + LEG

# 18:00 · RECORDATORIO DEL SORTEO (20/11 → 27/11 inclusive = 8 días). Diseño distinto: creatinas arriba, número abajo
h3 = ST + '<div class="eb" style="top:270px">Sorteo de 3 creatinas</div>'
h3 += '<div class="t" style="top:325px;font-size:78px">¿Ya estás<br><span class="box">participando?</span></div>'
h3 += ('<div class="tiles sz" style="top:560px;--w:430px;--h:420px;--g:26px">'
       + tile('creatina_gold_300g', '×2', cf('Creatina Gold 300 g', 28))
       + tile('creatina_star_300g', '×1', cf('Creatina Star 300 g', 28)) + '</div>')
h3 += ('<div class="c8" style="top:1070px"><div class="n">8</div>'
       '<div class="tx"><span>Quedan</span><b>días</b><span style="font-size:26px;color:#bdbdc0">contando hoy</span><span style="font-size:26px;color:#bdbdc0">cierra el 27/11 · 23:59</span></div></div>')
h3 += f'<div class="vote" style="top:1440px">{E("👉",34)} Participá en el <span>post del sorteo</span><br>fijado en nuestro perfil</div>'
h3 += f'<div class="vote" style="top:1580px;font-size:26px;color:#bdbdc0">{E("🚚",26)} Envío gratis a todo el país para los ganadores</div>'
h3 += LEG

# 21:30 · B2B + recordatorio del post de las 19:30
h4 = ST + '<div class="tag">BASE MAYORISTAS</div><div class="eb" style="top:270px">Para negocios</div>'
h4 += '<div class="t" style="top:325px;font-size:80px">¿Tenés un<br><span class="box">negocio?</span></div>'
h4 += (f'<div class="biz" style="top:580px"><div>{E("🏋️")}<b>Gimnasios</b></div><div>{E("🥗")}<b>Dietéticas</b></div>'
       f'<div>{E("🛍️")}<b>Tiendas</b></div><div>{E("🤝")}<b>Revendedores</b></div></div>')
h4 += f'<div class="wa" style="top:1230px">{E("💬")}<div><small>MANDÁ MAYORISTA · SOLO MENSAJES</small>{WA}</div></div>'
h4 += f'<div class="dl" style="top:1450px">{E("👀")}<div class="tx"><b>Mirá el post de hoy</b>Suplementos para tu gimnasio, <em>en 3 pasos.</em></div></div>'
h4 += LEG

for h, nm in [(h1, 'historia_1100'), (h2, 'historia_1500'), (h3, 'historia_1800'), (h4, 'historia_2130')]:
    print(render([page(1, h, nxt=False, total=1, story=True, legal=False)], f'{OUT}/{nm}', 1080, 1920))
