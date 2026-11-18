"""Post 13:00 · 19/11/2026 · familia EDUCA (jueves, curiosidad): «¿De dónde sale la whey?»
4 slides 1080×1350: portada con opciones (sin adelantar) → sale de hacer queso → solo ~20 % de la proteína de la leche es suero
→ del suero líquido al polvo (se filtra y se seca) + guardar/compartir.
Fuente: U.S. Dairy Export Council, «Reference Manual for U.S. Whey and Lactose Products» (caseína ≈ 80 % y proteínas del suero
≈ 20 % de la proteína de la leche; el suero es el líquido que queda al hacer queso; se concentra por filtración y se seca)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

# Embudo plano (no hay emoji fiel para «filtrar»)
FUNNEL = '''<svg viewBox="0 0 120 120" width="{s}" height="{s}"><path d="M10 14h100L70 62v36l-20 12V62Z" fill="#C6F432"/>
<path d="M10 14h100" stroke="#0B0B0C" stroke-width="0"/><rect x="18" y="22" width="84" height="8" fill="#0B0B0C" opacity=".25"/></svg>'''

ST = '''<style>
.hero{position:absolute;left:80px;right:80px;height:470px;border:2px solid var(--line);background:radial-gradient(circle 300px at 50% 46%,rgba(198,244,50,.12),transparent 100%),radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);display:flex;align-items:center;justify-content:center}
.hero img{height:390px;filter:drop-shadow(0 26px 34px rgba(0,0,0,.6))}
.hero .q{position:absolute;right:120px;top:60px;width:130px;height:130px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:96px;display:flex;align-items:center;justify-content:center;transform:rotate(8deg);box-shadow:0 18px 40px rgba(0,0,0,.5)}
.ops{position:absolute;left:80px;right:80px;display:flex;gap:22px}
.ops div{flex:1;height:200px;background:var(--panel);border:2px solid var(--line);position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px}
.ops .e{font-size:80px}
.ops b{font-size:27px;font-weight:900;text-transform:uppercase;letter-spacing:.5px}
.ops i{position:absolute;left:0;top:0;width:50px;height:50px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-style:normal;font-size:30px;display:flex;align-items:center;justify-content:center}
.cta{position:absolute;left:80px;font-size:30px;font-weight:800;line-height:1.25}.cta span{color:var(--l)}
.big{position:absolute;left:80px;font-family:'Archivo Black';font-size:118px;line-height:1;text-transform:uppercase;letter-spacing:-2px}
.big span{background:var(--l);color:var(--bk);padding:0 22px 8px;display:inline-block}
.eq{position:absolute;left:80px;right:80px;height:360px;display:flex;align-items:center;justify-content:space-between;background:var(--panel);border:2px solid var(--line);padding:0 40px}
.eq .c{display:flex;flex-direction:column;align-items:center;gap:16px;width:230px}
.eq .c .e{font-size:130px}
.eq .c b{font-size:29px;font-weight:900;text-transform:uppercase;text-align:center;line-height:1.1}
.eq .c b small{display:block;font-size:22px;color:#a9a9ad;font-weight:800;letter-spacing:1px;margin-top:6px}
.eq .c.on b{color:var(--l)}
.eq .op{font-family:'Archivo Black';font-size:80px;color:#6d6d72}
.src{position:absolute;left:80px;right:80px;font-size:23px;font-weight:600;color:#a9a9ad;line-height:1.4}.src b{color:#fff}
.n20{position:absolute;left:80px;display:flex;align-items:flex-end;gap:26px}
.n20 b{font-family:'Archivo Black';font-weight:400;font-size:230px;line-height:.82;color:var(--l)}
.n20 span{font-size:40px;font-weight:900;text-transform:uppercase;line-height:1.05;padding-bottom:8px}
.bar{position:absolute;left:80px;right:80px;height:250px;display:flex}
.bar div{display:flex;flex-direction:column;justify-content:center;padding:0 30px;gap:10px}
.bar .a{flex:0 0 80%;background:var(--panel);border:2px solid var(--line)}
.bar .b{flex:0 0 20%;background:var(--l);color:var(--bk);align-items:center;padding:0}
.bar .a .e,.bar .b .e{font-size:64px}
.bar strong{font-family:'Archivo Black';font-weight:400;font-size:56px;line-height:1}
.bar small{font-size:23px;font-weight:800;letter-spacing:1px;text-transform:uppercase}
.bar .a small{color:#a9a9ad}
.bar .row{flex-direction:row;align-items:center;gap:22px;padding:0}
.stp{position:absolute;left:80px;right:80px;display:flex;flex-direction:column;gap:20px}
.stp > div{height:180px;display:flex;align-items:center;gap:34px;background:var(--panel);border:2px solid var(--line);padding:0 34px}
.stp .ic{flex:0 0 120px;height:120px;display:flex;align-items:center;justify-content:center}
.stp .ic .e{font-size:96px}
.stp .ic.g{background:radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);border:2px solid var(--line);height:150px;flex-basis:130px}
.stp .ic img{height:124px;filter:drop-shadow(0 10px 14px rgba(0,0,0,.6))}
.stp b{display:block;font-size:40px;font-weight:900;text-transform:uppercase;line-height:1.05}
.stp p{font-size:26px;font-weight:600;color:#bdbdc0;line-height:1.3;margin-top:6px}
.stp .on{border-color:var(--l)} .stp .on b{color:var(--l)}
.save{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:22px;font-size:30px;font-weight:800;line-height:1.25}
.save span{color:var(--l)}
</style>'''

# 1 · PORTADA: pregunta + pote de whey con «?» y tres opciones sin resaltar ninguna
s1 = ST + '<div class="eb" style="top:190px">Curiosidad</div>'
s1 += '<div class="t" style="top:240px;font-size:84px">¿De dónde<br>sale la <span class="box">whey?</span></div>'
s1 += '<div class="hero" style="top:490px"><img src="assets/whey_star_2lb_vainilla.png"><div class="q">?</div></div>'
s1 += '<div class="ops" style="top:982px">' + ''.join(
    f'<div><i>{l}</i>{E(e)}<b>{t}</b></div>' for l, e, t in [('A', '🧪', 'Laboratorio'), ('B', '🌱', 'Soja'), ('C', '🧀', 'Queso')]) + '</div>'
s1 += f'<div class="cta" style="top:1206px">Comentá tu letra y <span>deslizá</span> {E("👉",30)}</div>'

# 2 · RESPUESTA: sale de hacer queso (ecuación visual leche → queso + suero)
s2 = ST + '<div class="eb" style="top:190px">La respuesta</div>'
s2 += '<div class="big" style="top:240px;font-size:92px">Es la C:<br><span>de hacer queso</span></div>'
s2 += '<div class="txt" style="top:530px;font-size:33px"><b>Whey</b> quiere decir <em>suero</em>: el líquido que queda cuando la leche se corta para hacer queso.</div>'
s2 += (f'<div class="eq" style="top:720px"><div class="c">{E("🥛")}<b>Leche</b></div><div class="op">→</div>'
       f'<div class="c">{E("🧀")}<b>Queso<small>LA CUAJADA</small></b></div><div class="op">+</div>'
       f'<div class="c on">{E("💧")}<b>Suero<small>LA WHEY</small></b></div></div>')
s2 += '<div class="src" style="top:1120px">Fuente: <b>U.S. Dairy Export Council</b>.</div>'

# 3 · EL DATO: de toda la proteína de la leche, solo ~20 % es del suero
s3 = ST + '<div class="eb" style="top:190px">El dato que pocos saben</div>'
s3 += '<div class="n20" style="top:250px"><b>20%</b><span>de la proteína<br>de la leche<br>es whey</span></div>'
s3 += ('<div class="bar" style="top:560px">'
       f'<div class="a"><div class="row">{E("🧀")}<span><strong>≈ 80 %</strong><br><small>Caseína · se va al queso</small></span></div></div>'
       f'<div class="b">{E("💧")}<strong style="font-size:40px">≈ 20 %</strong><small style="font-size:20px">Suero</small></div></div>')
s3 += '<div class="txt" style="top:880px;font-size:33px">La mayor parte de la proteína <b>se queda en el queso</b>. La whey es la parte chica que viaja en el suero.</div>'
s3 += '<div class="src" style="top:1090px">Proporciones aproximadas de la proteína de la leche de vaca.<br>Fuente: <b>U.S. Dairy Export Council</b>.</div>'

# 4 · DEL SUERO AL POLVO + guardar / compartir
s4 = ST + '<div class="eb" style="top:190px">Del suero al pote</div>'
s4 += '<div class="t" style="top:240px;font-size:72px">¿Cómo se hace<br><span class="box">polvo?</span></div>'
s4 += ('<div class="stp" style="top:440px">'
       f'<div><div class="ic">{E("💧")}</div><span><b>Suero líquido</b><p>Lo que queda después de hacer el queso.</p></span></div>'
       f'<div><div class="ic">{FUNNEL.format(s=110)}</div><span><b>Se filtra</b><p>Se le saca parte del agua, la lactosa y los minerales.</p></span></div>'
       '<div class="on"><div class="ic g"><img src="assets/whey_star_2lb_vainilla.png"></div><span><b>Se seca</b><p>Y queda el polvo que mezclás en tu shake.</p></span></div></div>')
s4 += f'<div class="save" style="top:1046px">{E("📌",40)}<div>Guardalo y <span>compartilo</span> con alguien que toma whey.</div></div>'
s4 += f'<div class="btn" style="left:80px;bottom:76px;font-size:27px">{E("🛒",27)} VER PROTEÍNAS · LINK EN LA BIO {ARROW}</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/whey_origen'))
