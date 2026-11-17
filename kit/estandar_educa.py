"""ESTÁNDAR FAMILIA «BASE EDUCA» (aprobado 17/11 por Valentín) · Mito o verdad: ¿la leche descremada tiene menos proteína? 4 slides 1080×1350.
Mismos datos que 2026-11-17_post1.py (USDA FoodData Central, cada 100 g: entera 3,25 % grasa 3,15 g prot · 61 kcal · 3,25 g grasa;
descremada 3,37 g · 34 kcal · 0,08 g; vaso 200 ml ≈ 206 g → 6,5 / 7 g de proteína y ≈ 125 / 70 kcal). Precios: kit/README.md."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

def vaso(leche, w=230):
    """Vaso SVG: la entera más cremosa/amarillenta, la descremada más blanca/azulada."""
    return f'''<svg viewBox="0 0 200 280" width="{w}" height="{w * 1.4:.0f}">
<defs><linearGradient id="g{leche[1:]}" x1="0" x2="1"><stop offset="0" stop-color="{leche}" stop-opacity=".82"/><stop offset=".45" stop-color="{leche}"/><stop offset="1" stop-color="{leche}" stop-opacity=".7"/></linearGradient></defs>
<path d="M30 20 L170 20 L152 264 Q150 272 142 272 L58 272 Q50 272 48 264 Z" fill="rgba(255,255,255,.06)" stroke="rgba(255,255,255,.55)" stroke-width="5"/>
<path d="M39 70 L161 70 L150 258 Q149 264 142 264 L58 264 Q51 264 50 258 Z" fill="url(#g{leche[1:]})"/>
<ellipse cx="100" cy="70" rx="61" ry="9" fill="#fff" opacity=".9"/>
<path d="M52 40 L64 240" stroke="rgba(255,255,255,.35)" stroke-width="7" stroke-linecap="round"/></svg>'''

ST = '''<style>
.ring{position:absolute;left:80px;right:80px;height:500px;background:radial-gradient(ellipse at 50% 55%,#2c2c30 0%,#17171a 60%,#0f0f11 100%);border:2px solid var(--line);display:flex;justify-content:space-around;align-items:flex-end;padding:0 70px 34px}
.ring .g{display:flex;flex-direction:column;align-items:center;gap:22px}
.ring .g b{font-family:'Archivo Black';font-size:38px;letter-spacing:1px;text-transform:uppercase}
.ring .q{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%) rotate(-6deg);width:150px;height:150px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:110px;display:flex;align-items:center;justify-content:center;box-shadow:0 18px 40px rgba(0,0,0,.5)}
.mv{position:absolute;left:80px;right:80px;display:flex;gap:28px}
.mv div{flex:1;height:110px;border:3px solid #4a4a4e;display:flex;align-items:center;justify-content:center;font-family:'Archivo Black';font-size:52px;letter-spacing:2px}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.25}.cta span{color:var(--l)}
.big{position:absolute;left:80px;font-family:'Archivo Black';font-size:150px;line-height:1;text-transform:uppercase;letter-spacing:-2px}
.big span{background:var(--l);color:var(--bk);padding:0 26px 10px;display:inline-block}
.cmp{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:260px 1fr 1fr}
.cmp > div{height:118px;display:flex;align-items:center;justify-content:center;border-bottom:2px solid var(--line)}
.cmp .c0{justify-content:flex-start}
.cmp .chip{border:3px solid var(--l);color:var(--l);font-weight:900;font-size:26px;letter-spacing:2px;padding:8px 14px}
.cmp .h{font-family:'Archivo Black';font-size:34px;text-transform:uppercase;letter-spacing:.5px}
.cmp .k{justify-content:flex-start;font-size:27px;font-weight:800;letter-spacing:1.5px;color:#a9a9ad;text-transform:uppercase}
.cmp .v{font-family:'Archivo Black';font-size:52px;color:#d6d6d8}
.cmp .v small{font-family:Montserrat;font-weight:800;font-size:26px;margin-left:8px;color:#8b8b8f}
.cmp .on{background:var(--l);color:var(--bk);border-bottom-color:var(--l)} .cmp .on small{color:var(--bk)}
.cmp .k.on{color:var(--bk);padding-left:22px}
.src{position:absolute;left:80px;right:80px;font-size:23px;font-weight:600;color:#a9a9ad;line-height:1.4}.src b{color:#fff}
.vs2{position:absolute;left:80px;right:80px;display:flex;gap:28px}
.vs2 .c{flex:1;height:500px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column;align-items:center;padding-top:34px}
.vs2 .c .e{font-size:120px}
.vs2 .c h3{font-family:'Archivo Black';font-size:44px;text-transform:uppercase;margin-top:18px;letter-spacing:.5px}
.vs2 .c h3 small{display:block;text-align:center;font-family:Montserrat;font-weight:800;font-size:24px;color:#a9a9ad;letter-spacing:2px;margin-top:4px}
.vs2 .c .n{margin-top:26px;font-family:'Archivo Black';font-size:50px;line-height:1.15;text-align:center}
.vs2 .c .n small{display:block;font-family:Montserrat;font-weight:800;font-size:24px;color:#a9a9ad;letter-spacing:2px;text-transform:uppercase}
.vs2 .c.on{border-color:var(--l)} .vs2 .c.on .n{color:var(--l)}
.hero{position:absolute;left:80px;right:80px;height:510px;border:2px solid var(--line);background:radial-gradient(circle 330px at 50% 46%,rgba(198,244,50,.12),transparent 100%),radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);display:flex;align-items:center;justify-content:center}
.hero img{position:relative;filter:drop-shadow(0 26px 34px rgba(0,0,0,.6))}
.hero .a{height:410px} .hero .b{height:300px;margin-left:-40px;align-self:flex-end;margin-bottom:70px}
.hero .sv{position:absolute;right:-2px;top:-2px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:34px;padding:12px 22px 14px}
.pr{position:absolute;left:80px;right:80px;display:flex;align-items:flex-end;justify-content:space-between}
.pr .nm{font-family:'Archivo Black';font-size:52px;text-transform:uppercase;line-height:1}
.pr .nm small{display:block;font-family:Montserrat;font-weight:700;font-size:25px;color:#bdbdc0;text-transform:none;margin-top:10px;letter-spacing:0}
.pr .p{font-family:'Archivo Black';font-size:92px;line-height:.9;color:var(--l)}
.fine{position:absolute;left:80px;right:80px;font-size:21px;line-height:1.35;color:#8b8b8f;font-weight:600}
</style>'''

# 1 · PORTADA: pregunta corta + vasos distintos, sin adelantar la respuesta
s1 = ST + '<div class="eb" style="top:190px">Mito o verdad</div>'
s1 += '<div class="t" style="top:240px;font-size:72px">¿La descremada<br>tiene menos<br><span class="box">proteína?</span></div>'
s1 += (f'<div class="ring" style="top:540px"><div class="g">{vaso("#FFF1C9", 200)}<b>Entera</b></div>'
       f'<div class="g">{vaso("#EEF4FB", 200)}<b>Descremada</b></div><div class="q">?</div></div>')
s1 += '<div class="mv" style="top:1072px;height:96px"><div style="height:96px">MITO</div><div style="height:96px">VERDAD</div></div>'

# 2 · RESPUESTA: una sola idea (mito) + tabla con la proteína destacada y la base de cálculo visible
s2 = ST + '<div class="eb" style="top:190px">La respuesta</div>'
s2 += '<div class="big" style="top:240px">Es <span>mito</span></div>'
s2 += '<div class="txt" style="top:420px;font-size:33px">Al descremarla le sacan <b>la grasa</b>, no la proteína.</div>'
cmp = '<div class="c0"><span class="chip">CADA 100 g</span></div><div class="h">Entera</div><div class="h">Descremada</div>'
for k, a, b, u, on in [('Proteína', '3,2', '3,4', 'g', True), ('Calorías', '61', '34', 'kcal', False), ('Grasa', '3,3', '0,1', 'g', False)]:
    c = ' on' if on else ''
    cmp += f'<div class="k{c}">{k}</div><div class="v{c}">{a}<small>{u}</small></div><div class="v{c}">{b}<small>{u}</small></div>'
s2 += f'<div class="cmp" style="top:540px">{cmp}</div>'
s2 += '<div class="src" style="top:1040px">Valores <b>cada 100 g</b> · leche entera 3,25 % grasa vs. descremada.<br>Fuente: <b>USDA FoodData Central</b>.</div>'

# 3 · EL GIRO: agua vs leche, dos tarjetas y una conclusión (sin afirmaciones generales sobre lactosa)
s3 = ST + '<div class="eb" style="top:190px">¿Y en tu shake?</div>'
s3 += '<div class="t" style="top:240px;font-size:84px">¿Agua o<br><span class="box">leche?</span></div>'
s3 += (f'<div class="vs2" style="top:500px"><div class="c">{E("💧")}<h3>Agua<small>CUALQUIER CANTIDAD</small></h3>'
       f'<div class="n">+0 g<small>proteína</small></div><div class="n" style="margin-top:10px">+0<small>kcal</small></div></div>'
       f'<div class="c on">{E("🥛")}<h3>Leche<small>VASO DE 200 ML</small></h3>'
       f'<div class="n">+6,5 a 7 g<small>proteína</small></div><div class="n" style="margin-top:10px">+70 a 125<small>kcal según la leche</small></div></div></div>')
s3 += '<div class="txt" style="top:1040px;font-size:34px">Las dos sirven: <em>elegí según tus calorías.</em></div>'

# 4 · VENTA: un solo combo protagonista, transición natural desde el shake
s4 = ST + '<div class="eb" style="top:190px">Para tu shake</div>'
s4 += '<div class="t" style="top:240px;font-size:74px">Proteína +<br>creatina en <span class="box">combo</span></div>'
s4 += ('<div class="hero" style="top:470px"><img class="a" src="assets/ena_prot_vain.png"><img class="b" src="assets/ena_crea_neutra.png">'
       '<div class="sv">AHORRÁS $7.900</div></div>')
s4 += '<div class="pr" style="top:1004px"><div class="nm">Combo ENA<small>Proteína 907 g + creatina 300 g</small></div><div class="p">$85.900</div></div>'
s4 += '<div class="fine" style="top:1100px">Transferencia o efectivo. La proteína contribuye a aumentar y mantener la masa muscular. Más combos en el catálogo.</div>'
s4 += f'<div class="btn" style="left:80px;bottom:76px;font-size:27px">{E("🛒",27)} VER COMBOS · LINK EN LA BIO {ARROW}</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/leche_v2'))
