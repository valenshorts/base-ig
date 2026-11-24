"""24/11/2026 13:00 [EDUCA] «¿Cuánta proteína necesitás por día?» 4 slides 1080×1350.
Fuente: ISSN, posición sobre proteína y ejercicio (Jäger et al., 2017): 1,4 a 2,0 g por kg de peso por día para la mayoría de las
personas que entrenan; repartir en dosis de 20–40 g cada 3–4 h. USDA FoodData Central: pechuga de pollo cocida ≈ 31 g / 100 g;
huevo grande ≈ 6,3 g. Precio: kit/README.md (Star Whey 2 lb $81.900 transferencia o efectivo)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.qcard{position:absolute;left:80px;right:80px;height:500px;border:2px solid var(--line);background:radial-gradient(circle 320px at 50% 45%,rgba(198,244,50,.12),transparent 100%),radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);display:flex;align-items:center;justify-content:center;gap:40px}
.qcard .e{font-size:150px;filter:drop-shadow(0 18px 24px rgba(0,0,0,.55))}
.qcard .q{position:absolute;right:40px;top:40px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:72px;padding:6px 26px 10px;transform:rotate(-6deg)}
.mv{position:absolute;left:80px;right:80px;font-size:34px;font-weight:800;line-height:1.3}.mv span{color:var(--l)}
.big{position:absolute;left:80px;right:80px;text-align:center}
.big b{display:block;white-space:nowrap;font-family:'Archivo Black';font-size:150px;line-height:.95;color:var(--l)}
.big span{display:block;font-size:46px;font-weight:900;text-transform:uppercase;margin-top:14px}
.src{position:absolute;left:80px;right:80px;font-size:24px;font-weight:600;color:#8b8b8f;line-height:1.4}.src b{color:#d6d6d8}
.tb{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1.4fr;border:2px solid var(--line)}
.tb div{height:118px;display:flex;align-items:center;padding:0 34px;border-bottom:2px solid var(--line);font-size:34px;font-weight:800}
.tb div:nth-child(odd){border-right:2px solid var(--line);color:#d6d6d8}
.tb .h{height:90px;background:var(--panel2);font-size:24px;letter-spacing:2px;color:#a9a9ad;text-transform:uppercase}
.tb .v{font-family:'Archivo Black';font-size:52px;color:var(--l)} .tb .v small{font-family:Montserrat;font-size:26px;font-weight:800;color:#bdbdc0;margin-left:10px}
.tb div:nth-last-child(-n+2){border-bottom:0}
.ref{position:absolute;left:80px;right:80px;display:flex;gap:22px}
.ref div{flex:1;height:200px;border:2px solid var(--line);background:var(--panel);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px}
.ref .e{font-size:66px} .ref b{font-family:'Archivo Black';font-size:44px;color:var(--l)} .ref p{font-size:22px;font-weight:700;color:#bdbdc0;text-align:center;line-height:1.2}
.pr{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:30px;border:2px solid var(--l);background:var(--panel);padding:18px 26px}
.pr .ph{flex:0 0 220px;height:230px;background:radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);display:flex;align-items:center;justify-content:center}
.pr .ph img{max-height:88%;max-width:88%;filter:drop-shadow(0 16px 22px rgba(0,0,0,.6))}
.pr b{display:block;font-family:'Archivo Black';font-size:40px;text-transform:uppercase;line-height:1}
.pr s{text-decoration:none;display:block;font-family:'Archivo Black';font-size:66px;color:var(--l);margin-top:8px}
.pr small{display:block;font-size:22px;font-weight:600;color:#a9a9ad;margin-top:6px;line-height:1.3}
</style>'''

# 1 · PORTADA
s1 = ST + '<div class="eb" style="top:200px">Guía rápida</div>'
s1 += '<div class="t" style="top:250px;font-size:76px">¿Cuánta proteína<br>necesitás<br><span class="box">por día?</span></div>'
s1 += f'<div class="qcard" style="top:580px">{E("🍗")}{E("🥚")}{E("🥛")}<div class="q">? g</div></div>'
s1 += f'<div class="mv" style="top:1125px">Spoiler: <span>depende de tu peso</span> {E("👉",32)}</div>'

# 2 · LA CUENTA
s2 = ST + '<div class="eb" style="top:200px">La cuenta</div>'
s2 += '<div class="t" style="top:250px;font-size:72px">Si entrenás,<br>multiplicá tu <span class="box">peso</span></div>'
s2 += '<div class="big" style="top:520px"><b>1,4 a 2 g</b><span>por kilo de peso, por día</span></div>'
s2 += '<div class="txt" style="top:860px;font-size:32px">Ejemplo: si pesás <b>70 kg</b> → entre <em>98 y 140 g</em> de proteína al día, sumando todo lo que comés.</div>'
s2 += '<div class="src" style="top:1060px">Fuente: <b>ISSN</b> (Sociedad Internacional de Nutrición Deportiva), posición sobre proteína y ejercicio, 2017.</div>'

# 3 · TABLA
s3 = ST + '<div class="eb" style="top:200px">Tu número</div>'
s3 += '<div class="t" style="top:250px;font-size:76px">Buscá tu<br><span class="box">peso</span></div>'
filas = [('60 kg', '84 a 120'), ('70 kg', '98 a 140'), ('80 kg', '112 a 160'), ('90 kg', '126 a 180')]
tb = '<div class="h">Tu peso</div><div class="h">Proteína por día</div>'
for p, g in filas:
    tb += f'<div>{p}</div><div class="v">{g}<small>g</small></div>'
s3 += f'<div class="tb" style="top:480px">{tb}</div>'
s3 += '<div class="src" style="top:1100px">Rango ISSN 1,4–2 g/kg para personas que entrenan. Es una guía general: cada caso puede variar.</div>'

# 4 · CÓMO LLEGAR + producto
s4 = ST + '<div class="eb" style="top:200px">¿Cómo llegar?</div>'
s4 += '<div class="t" style="top:250px;font-size:70px">Repartila en<br><span class="box">3 o 4 comidas</span></div>'
s4 += (f'<div class="ref" style="top:470px"><div>{E("🍗")}<b>≈31 g</b><p>100 g de pechuga<br>cocida</p></div>'
       f'<div>{E("🥚")}<b>≈6 g</b><p>1 huevo<br>grande</p></div>'
       f'<div>{E("🥤")}<b>Scoop</b><p>mirá la etiqueta<br>de tu whey</p></div></div>')
s4 += '<div class="src" style="top:690px">Ideal: 20 a 40 g por comida (ISSN). Valores de alimentos: USDA FoodData Central.</div>'
s4 += ('<div class="pr" style="top:790px"><div class="ph"><img src="assets/whey_star_2lb_vainilla.png"></div>'
       '<div><b>Star Whey<br>Protein 2 lb</b><s>$81.900</s><small>Transferencia o efectivo. La proteína contribuye a aumentar y mantener la masa muscular.</small></div></div>')
s4 += f'<div class="btn" style="left:80px;bottom:76px;font-size:27px">{E("🛒",27)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/post1'))
