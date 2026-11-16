"""Mito o verdad: ¿la leche descremada tiene menos proteína que la entera? (4 slides 1080×1350) · 17/11/2026 13:00.
Fuente: USDA FoodData Central (SR Legacy), cada 100 g: leche entera 3,25 % grasa: proteína 3,15 g · 61 kcal · grasa 3,25 g;
leche descremada (nonfat): proteína 3,37 g · 34 kcal · grasa 0,08 g. Vaso de 200 ml ≈ 206 g → entera ≈ 6,5 g y ≈ 125 kcal;
descremada ≈ 7 g y ≈ 70 kcal. Precios de combos: kit/README.md."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.duo{position:absolute;left:80px;right:80px;display:flex;gap:28px}
.duo .o{flex:1;height:440px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column}
.duo .o .ph{flex:1;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-bottom:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.duo .o .ph .e{font-size:170px;filter:drop-shadow(0 16px 22px rgba(0,0,0,.55))}
.duo .o .nm{height:96px;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:900;letter-spacing:1px;text-transform:uppercase}
.mv{position:absolute;left:80px;right:80px;display:flex;gap:28px}
.mv div{flex:1;height:110px;border:3px solid #4a4a4e;display:flex;align-items:center;justify-content:center;font-family:'Archivo Black';font-size:52px;letter-spacing:2px}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.25}.cta span{color:var(--l)}
.cmp{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:250px 1fr 1fr}
.cmp > div{height:128px;border-bottom:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.cmp .h{height:120px;flex-direction:column;gap:4px;background:var(--panel);border:2px solid var(--line)}
.cmp .h .e{font-size:54px} .cmp .h b{font-size:25px;font-weight:900;letter-spacing:1px;text-transform:uppercase}
.cmp .k{justify-content:flex-start;gap:16px;font-size:25px;font-weight:800;letter-spacing:1.5px;color:#a9a9ad;text-transform:uppercase}
.cmp .k .e{font-size:46px}
.cmp .v{font-family:'Archivo Black';font-size:52px}
.cmp .v small{font-family:Montserrat;font-weight:800;font-size:26px;margin-left:8px;color:#bdbdc0}
.cmp .v.on{color:var(--l)}
.src{position:absolute;left:80px;right:80px;font-size:21px;font-weight:600;color:#8b8b8f;letter-spacing:.5px;line-height:1.35}
.pt{position:absolute;left:80px;right:80px;display:flex;gap:28px;align-items:center}
.pt .k{flex:0 0 120px;height:120px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.pt .k .e{font-size:68px}
.pt .n{font-size:29px;font-weight:500;line-height:1.34;color:#d6d6d8}.pt .n b{color:#fff;font-weight:800}.pt .n em{font-style:normal;color:var(--l);font-weight:700}
.claim{position:absolute;left:80px;right:80px;font-size:23px;line-height:1.35;color:#bdbdc0;font-weight:500}
.cb{position:absolute;left:80px;right:80px;display:flex;gap:28px}
.cb .tile{flex:1}
.cb .tile .ph{height:330px;gap:0}
.cb .tile .ph img{max-width:46%;max-height:80%}
.cb .tile .ph img + img{max-width:38%;max-height:62%;margin-left:-14px;align-self:flex-end;margin-bottom:44px}
.cb .tile .ft .b{font-size:24px}
.cb .sv{background:var(--panel2);color:var(--l);font-size:24px;font-weight:800;letter-spacing:1px;text-transform:uppercase;text-align:center;padding:10px 8px 12px}
</style>'''

# 1 · MITO O VERDAD (sin adelantar: botones iguales, sin resaltar)
s1 = ST + '<div class="eb" style="top:200px">Mito o verdad</div>'
s1 += '<div class="t" style="top:250px;font-size:66px">La leche descremada<br>tiene menos<br><span class="box">proteína</span></div>'
s1 += f'<div class="duo" style="top:560px"><div class="o"><div class="ph">{E("🥛")}</div><div class="nm">Entera</div></div><div class="o"><div class="ph">{E("🥛")}</div><div class="nm">Descremada</div></div></div>'
s1 += '<div class="mv" style="top:1030px"><div>MITO</div><div>VERDAD</div></div>'
s1 += f'<div class="cta" style="top:1185px">Comentá <span>MITO</span> o <span>VERDAD</span> {E("👇",30)}</div>'

# 2 · RESPUESTA
s2 = ST + '<div class="eb" style="top:200px">La respuesta</div>'
s2 += '<div class="t" style="top:250px;font-size:78px">Es <span class="box">mito</span></div>'
s2 += '<div class="txt" style="top:385px;font-size:31px">Al descremarla le sacan <b>la grasa</b>, no la proteína.</div>'
cmp = f'<div></div><div class="h">{E("🥛")}<b>Entera</b></div><div class="h">{E("🥛")}<b>Descremada</b></div>'
for ic, k, a, b, on in [('💪', 'Proteína', '3,2', '3,4', ' on'), ('🔥', 'Calorías', '61', '34', ''), ('🧈', 'Grasa', '3,3', '0,1', '')]:
    u = 'kcal' if k == 'Calorías' else 'g'
    cmp += f'<div class="k">{E(ic)}{k}</div><div class="v{on}">{a}<small>{u}</small></div><div class="v{on}">{b}<small>{u}</small></div>'
s2 += f'<div class="cmp" style="top:500px">{cmp}</div>'
s2 += '<div class="src" style="top:1035px">Cada 100 g · leche entera 3,25 % grasa vs. descremada.<br>Fuente: USDA FoodData Central.</div>'
s2 += f'<div class="cta" style="top:1185px;font-size:29px">¿Y en tu shake? <span>Deslizá</span> {E("👉",29)}</div>'

# 3 · EL GIRO: ¿AGUA O LECHE EN EL SHAKE?
s3 = ST + '<div class="eb" style="top:200px">¿Y en tu shake?</div>'
s3 += '<div class="t" style="top:250px;font-size:76px">¿Agua<br>o <span class="box">leche?</span></div>'
pts = [('💧', 'Con <b>agua</b>: sumás solo lo que trae tu scoop. <em>Cero calorías extra.</em>'),
       ('🥛', 'Un vaso de <b>200 ml de leche</b> suma <em>≈ 6,5 a 7 g de proteína</em>: ≈ 125 kcal la entera y ≈ 70 kcal la descremada.'),
       ('⚖️', 'Las dos sirven: <b>elegí según tus calorías</b> y cómo te cae. Si la lactosa te cae pesada, probá con agua y una whey <em>isolate</em> (trae menos).')]
top = 500
for k, t in pts:
    s3 += f'<div class="pt" style="top:{top}px"><div class="k">{E(k)}</div><div class="n">{t}</div></div>'
    top += 200
s3 += f'<div class="cta" style="top:1185px;font-size:28px">Guardalo y compartilo {E("📌",28)}</div>'

# 4 · VENTA: COMBOS (proteína + creatina)
def combo(a, b, nom, precio, ahorro):
    return (f'<div class="tile"><div class="ph"><img src="assets/{a}.png"><img src="assets/{b}.png"></div>'
            f'{pf(nom, precio)}<div class="sv">Ahorrás {ahorro}</div></div>')
s4 = ST + '<div class="eb" style="top:200px">Para tu shake</div>'
s4 += '<div class="t" style="top:250px;font-size:74px">Proteína +<br>creatina en <span class="box">combo</span></div>'
s4 += ('<div class="cb" style="top:470px">' + combo('ena_prot_vain', 'ena_crea_neutra', 'Combo ENA', '$85.900', '$7.900')
       + combo('whey_star_2lb_vainilla', 'creatina_star_300g', 'Combo Star', '$99.900', '$5.800') + '</div>')
s4 += '<div class="claim" style="top:1002px">ENA: proteína 907 g + creatina 300 g · Star: whey 2 lb + creatina 300 g. La proteína contribuye a aumentar y mantener la masa muscular. Precios por transferencia o efectivo.</div>'
s4 += f'<div class="btn" style="left:80px;top:1112px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s4 += f'<div style="position:absolute;left:80px;top:1207px;font-size:23px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8">{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">11 2178-9431</span> · SOLO MENSAJES</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/leche'))
