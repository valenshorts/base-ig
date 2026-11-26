"""27/11/2026 · post1 13:00 [EDUCA] esto o aquello «¿yogur griego o común: cuál tiene más proteína?»
· post2 19:30 [MAYORISTAS] «¿Tenés una dietética? Sumá suplementos» (para dietéticas y revendedores).
Datos (USDA FoodData Central, SR Legacy, cada 100 g, natural y descremado):
yogur griego natural descremado 10,19 g proteína · 59 kcal; yogur natural descremado 5,73 g · 56 kcal.
En 200 g: 20,4 g vs 11,5 g. El griego se cuela (se escurre parte del suero líquido) y queda más concentrado.
MAYORISTAS: SIN precios, mínimos, descuentos, márgenes, stock, plazos ni promesas de ventas."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.ring{position:absolute;left:80px;right:80px;height:470px;background:radial-gradient(ellipse at 50% 55%,#2c2c30 0%,#17171a 60%,#0f0f11 100%);border:2px solid var(--line);display:flex;justify-content:space-around;align-items:flex-end;padding:0 60px 30px}
.ring .g{display:flex;flex-direction:column;align-items:center;gap:16px}
.ring .g b{font-family:'Archivo Black';font-weight:400;font-size:40px;letter-spacing:1px;text-transform:uppercase}
.ring .g i{font-style:normal;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:34px;width:58px;height:58px;display:flex;align-items:center;justify-content:center}
.ring .q{position:absolute;left:50%;top:40%;transform:translate(-50%,-50%) rotate(-6deg);width:140px;height:140px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:100px;display:flex;align-items:center;justify-content:center;box-shadow:0 18px 40px rgba(0,0,0,.5)}
.mv{position:absolute;left:80px;right:80px;display:flex;gap:28px}
.mv div{flex:1;height:100px;border:3px solid #4a4a4e;display:flex;align-items:center;justify-content:center;font-family:'Archivo Black';font-size:44px;letter-spacing:2px}
.big{position:absolute;left:80px;font-family:'Archivo Black';font-size:118px;line-height:1;text-transform:uppercase;letter-spacing:-2px}
.big span{background:var(--l);color:var(--bk);padding:0 24px 8px;display:inline-block}
.cmp{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:260px 1fr 1fr}
.cmp > div{height:110px;display:flex;align-items:center;justify-content:center;border-bottom:2px solid var(--line)}
.cmp .c0{justify-content:flex-start}
.cmp .chip{border:3px solid var(--l);color:var(--l);font-weight:900;font-size:26px;letter-spacing:2px;padding:8px 14px}
.cmp .h{font-family:'Archivo Black';font-size:38px;text-transform:uppercase;letter-spacing:.5px}
.cmp .k{justify-content:flex-start;font-size:27px;font-weight:800;letter-spacing:1.5px;color:#a9a9ad;text-transform:uppercase}
.cmp .v{font-family:'Archivo Black';font-size:56px;color:#d6d6d8}
.cmp .v small{font-family:Montserrat;font-weight:800;font-size:26px;margin-left:8px;color:#8b8b8f}
.cmp .on{background:var(--l);color:var(--bk);border-bottom-color:var(--l)} .cmp .on small{color:var(--bk)}
.cmp .k.on{color:var(--bk);padding-left:22px}
.src{position:absolute;left:80px;right:80px;font-size:23px;font-weight:600;color:#a9a9ad;line-height:1.4}.src b{color:#fff}
.flow{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:14px}
.flow .c{flex:1;height:300px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;padding:0 12px}
.flow .c.on{border-color:var(--l);background:linear-gradient(160deg,rgba(198,244,50,.13),var(--panel) 70%)}
.flow .c .e{font-size:96px}
.flow .c b{font-size:27px;font-weight:900;text-transform:uppercase;text-align:center;line-height:1.12}
.flow .ar{flex:0 0 34px;font-size:46px;font-weight:900;color:var(--l);text-align:center}
.vs2{position:absolute;left:80px;right:80px;display:flex;gap:28px}
.vs2 .c{flex:1;height:250px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px}
.vs2 .c small{font-size:24px;font-weight:800;letter-spacing:3px;color:#a9a9ad;text-transform:uppercase}
.vs2 .c b{font-family:'Archivo Black';font-weight:400;font-size:96px;line-height:1}
.vs2 .c b i{font-style:normal;font-family:Montserrat;font-weight:800;font-size:36px;margin-left:6px;color:#a9a9ad}
.vs2 .c.on{border-color:var(--l)} .vs2 .c.on b{color:var(--l)}
.st{position:absolute;left:80px;right:80px;display:flex;gap:28px;align-items:center;height:150px;border:2px solid var(--line);background:var(--panel);padding:0 30px}
.st .e{font-size:76px;flex:0 0 100px;text-align:center}
.st p{font-size:27px;font-weight:600;line-height:1.28;color:#d6d6d8}.st p b{display:block;color:#fff;font-weight:900;font-size:32px;text-transform:uppercase;margin-bottom:4px}
.st p em{font-style:normal;color:var(--l);font-weight:800}
.cta{position:absolute;left:80px;right:80px;font-size:30px;font-weight:800;line-height:1.38}.cta span{color:var(--l)}
/* MAYORISTAS */
.tag{position:absolute;right:80px;top:192px;border:2px solid var(--l);color:var(--l);font-weight:800;font-size:22px;letter-spacing:4px;padding:8px 16px}
.shelf{position:absolute;left:80px;right:80px;height:560px;border:2px solid var(--line);background:radial-gradient(circle 340px at 50% 50%,rgba(198,244,50,.10),transparent 100%),radial-gradient(ellipse at 50% 42%,#3A3A3E 0%,#232326 58%,#141416 100%);display:flex;align-items:flex-end;justify-content:center;gap:6px;padding-bottom:56px}
.shelf img{filter:drop-shadow(0 22px 30px rgba(0,0,0,.6))}
.shelf .a{height:290px} .shelf .b{height:400px;position:relative;z-index:2} .shelf .c{height:300px} .shelf .d{height:270px}
.shelf .ic{position:absolute;left:30px;top:26px;width:130px;height:130px;border:3px solid var(--l);background:var(--bk);display:flex;align-items:center;justify-content:center}
.shelf .ic .e{font-size:84px}
.row{position:absolute;left:80px;right:80px;height:150px;display:flex;border:2px solid var(--line);background:var(--panel)}
.row .ph{flex:0 0 190px;background:radial-gradient(ellipse at 50% 42%,#3A3A3E 0%,#232326 58%,#141416 100%);display:flex;align-items:center;justify-content:center;border-right:2px solid var(--line)}
.row .ph img{max-height:86%;max-width:80%;filter:drop-shadow(0 12px 16px rgba(0,0,0,.6))}
.row .tx{flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 30px;gap:6px}
.row .tx b{font-size:36px;font-weight:900;text-transform:uppercase;line-height:1}
.row .tx p{font-size:25px;font-weight:600;color:#bdbdc0;line-height:1.25}
.row .n{flex:0 0 84px;border-left:2px solid var(--line);display:flex;align-items:center;justify-content:center;font-family:'Archivo Black';font-size:44px;color:var(--l)}
.ok3{position:absolute;left:80px;right:80px;display:flex;gap:26px;align-items:center;height:170px;border:2px solid var(--line);background:var(--panel);padding:0 30px}
.ok3 .e{font-size:80px;flex:0 0 100px;text-align:center}
.ok3 p{font-size:28px;font-weight:600;line-height:1.3;color:#d6d6d8}.ok3 p b{display:block;color:#fff;font-weight:900;font-size:34px;text-transform:uppercase;margin-bottom:4px}
.pst{position:absolute;left:80px;right:80px;display:flex;gap:30px;align-items:center}
.pst i{flex:0 0 96px;height:96px;border:3px solid var(--l);color:var(--l);font-style:normal;font-family:'Archivo Black';font-size:52px;display:flex;align-items:center;justify-content:center}
.pst p{font-size:30px;font-weight:600;line-height:1.3;color:#d6d6d8}.pst p b{display:block;color:#fff;font-weight:900;font-size:35px;text-transform:uppercase;letter-spacing:.5px;margin-bottom:4px}
.pst p em{font-style:normal;color:var(--l);font-weight:800}
.wa{position:absolute;left:80px;right:80px;height:150px;background:var(--l);color:var(--bk);display:flex;align-items:center;justify-content:center;gap:22px}
.wa .e{font-size:64px}
.wa div{font-family:'Archivo Black';font-size:52px;line-height:1}.wa small{display:block;font-family:Montserrat;font-weight:800;font-size:23px;letter-spacing:2px;margin-bottom:8px}
.cat2{position:absolute;left:80px;right:80px;text-align:center;font-size:27px;font-weight:800;letter-spacing:1.5px;color:#d6d6d8}.cat2 span{color:var(--l)}
.note{position:absolute;left:80px;right:80px;font-size:23px;font-weight:600;color:#a9a9ad;line-height:1.4}
</style>'''


def bowl(w=230):
    """Bowl SVG plano con yogur blanco y cuchara (no hay emoji fiel de yogur)."""
    return f'''<svg viewBox="0 0 220 180" width="{w}" height="{w * 180 / 220:.0f}">
<path d="M150 18 L176 4 L182 12 L158 30 Z" fill="#c9c9cc"/><rect x="128" y="22" width="40" height="22" transform="rotate(-30 148 33)" fill="#e3e3e6"/>
<ellipse cx="110" cy="70" rx="92" ry="22" fill="#F7F6F0"/>
<path d="M36 64 Q70 38 110 50 Q150 36 184 64 Q150 58 110 66 Q70 58 36 64 Z" fill="#FFFFFF"/>
<path d="M14 72 L206 72 Q200 150 128 166 L92 166 Q20 150 14 72 Z" fill="#3a3a3e" stroke="#5a5a5e" stroke-width="3"/>
<path d="M30 92 Q110 108 190 92" stroke="#C6F432" stroke-width="7" fill="none"/>
<rect x="78" y="166" width="64" height="10" fill="#2a2a2d"/></svg>'''


# ===== POST 1 · EDUCA: ¿YOGUR GRIEGO O COMÚN? =====
# 1 · Portada: pregunta corta, dos bowls iguales (no adelanta la respuesta)
a1 = ST + '<div class="eb" style="top:190px">Esto o aquello</div>'
a1 += '<div class="t" style="top:240px;font-size:74px">Yogur griego<br>o común: ¿cuál tiene<br>más <span class="box">proteína?</span></div>'
a1 += (f'<div class="ring" style="top:580px"><div class="g">{bowl(250)}<b>Griego</b><i>A</i></div>'
       f'<div class="g">{bowl(250)}<b>Común</b><i>B</i></div><div class="q">?</div></div>')
a1 += f'<div class="mv" style="top:1082px"><div style="font-size:40px">COMENTÁ A O B {E("👇",40)}</div></div>'

# 2 · Respuesta + tabla cada 100 g (misma base: natural y descremado)
a2 = ST + '<div class="eb" style="top:190px">La respuesta</div>'
a2 += '<div class="big" style="top:240px">El <span>griego</span></div>'
a2 += '<div class="txt" style="top:390px;font-size:33px">Casi <b>el doble de proteína</b>, con calorías <em>muy parecidas.</em></div>'
cmp = '<div class="c0"><span class="chip">CADA 100 g</span></div><div class="h">Griego</div><div class="h">Común</div>'
for k, a, b, u, on in [('Proteína', '10,2', '5,7', 'g', True), ('Calorías', '59', '56', 'kcal', False)]:
    c = ' on' if on else ''
    cmp += f'<div class="k{c}">{k}</div><div class="v{c}">{a}<small>{u}</small></div><div class="v{c}">{b}<small>{u}</small></div>'
a2 += f'<div class="cmp" style="top:510px">{cmp}</div>'
a2 += (f'<div class="st" style="top:880px;height:150px">{E("🥄")}<p><b>En un bowl de 200 <span style="text-transform:none">g</span></b>'
       f'Griego <em>≈ 20 g</em> de proteína · común <em>≈ 11 g</em>.</p></div>')
a2 += '<div class="src" style="top:1062px">Yogur natural (sin azúcar agregada) y descremado, valores <b>cada 100 g</b>.<br>Fuente: <b>USDA FoodData Central</b>.</div>'

# 3 · ¿Por qué? Se cuela: sale parte del suero líquido
a3 = ST + '<div class="eb" style="top:190px">¿Por qué?</div>'
a3 += '<div class="t" style="top:240px;font-size:76px">Porque<br>se <span class="box">cuela</span></div>'
a3 += (f'<div class="flow" style="top:470px"><div class="c">{E("🥛")}<b>Leche<br>fermentada</b></div><div class="ar">→</div>'
       f'<div class="c">{E("💧")}<b>Se escurre<br>parte del suero</b></div><div class="ar">→</div>'
       f'<div class="c on">{bowl(150)}<b>Queda más<br>concentrado</b></div></div>')
a3 += '<div class="txt" style="top:830px;font-size:33px">Con menos líquido, cada cucharada trae <b>más proteína</b> y la textura queda <em>más espesa.</em></div>'
a3 += '<div class="src" style="top:990px">Suero: el líquido que se separa al colar el yogur.<br>Valores: <b>USDA FoodData Central</b>.</div>'

# 4 · Cómo elegir en la góndola + cierre (guardar / compartir / comentar)
a4 = ST + '<div class="eb" style="top:190px">En la góndola</div>'
a4 += '<div class="t" style="top:240px;font-size:72px">Leé la<br><span class="box">etiqueta</span></div>'
a4 += (f'<div class="st" style="top:440px">{E("🔎")}<p><b>Proteína cada 100 <span style="text-transform:none">g</span></b>Compará ese número, no el nombre.</p></div>'
       f'<div class="st" style="top:610px">{E("🍬")}<p><b>Azúcares</b>Los saborizados suelen sumar más: <em>fijate la tabla.</em></p></div>'
       f'<div class="st" style="top:780px">{E("🏷️")}<p><b>«Estilo griego»</b>No todos son iguales: <em>compará la tabla.</em></p></div>')
a4 += (f'<div class="cta" style="top:960px">{E("📌",30)} <span>Guardalo</span> para tu próxima compra<br>'
       f'{E("📲",30)} <span>Mandáselo</span> al que desayuna yogur<br>'
       f'{E("👇",30)} ¿Griego o común? <span>Comentá</span></div>')
a4 += f'<div class="btn" style="left:80px;bottom:76px;font-size:27px">{E("🛒",27)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
print(render([page(1, a1, True, 4), page(2, a2, True, 4), page(3, a3, True, 4), page(4, a4, False, 4)], f'{OUT}/post1'))

# ===== POST 2 · MAYORISTAS: PARA DIETÉTICAS Y REVENDEDORES =====
TAG = '<div class="tag">BASE MAYORISTAS</div>'
b1 = ST + TAG + '<div class="eb" style="top:200px">Para dietéticas</div>'
b1 += '<div class="t" style="top:255px;font-size:72px">¿Tenés una<br>dietética? Sumá<br><span class="box">suplementos</span></div>'
b1 += (f'<div class="shelf" style="top:610px"><div class="ic">{E("🏪")}</div><img class="a" src="assets/star_citratomg.png">'
       '<img class="b" src="assets/collagen.png"><img class="c" src="assets/ena_omega3.png"><img class="d" src="assets/magnesio_glicinato_gold.png"></div>')

b2 = ST + TAG + '<div class="eb" style="top:200px">Para tu góndola</div>'
b2 += '<div class="t" style="top:255px;font-size:72px">4 categorías<br><span class="box">para sumar</span></div>'
cats = [('magnesio_glicinato_gold', 'Magnesio', 'Citrato y glicinato, en cápsulas.'),
        ('ena_omega3', 'Omega 3', 'En cápsulas, de ENA y Gold.'),
        ('collagen', 'Colágeno', 'Star, con resveratrol.'),
        ('ena_prot_vain', 'Proteínas y creatinas', 'Para clientes que entrenan.')]
top = 450
for i, (f, t, d) in enumerate(cats, 1):
    b2 += f'<div class="row" style="top:{top}px"><div class="ph"><img src="assets/{f}.png"></div><div class="tx"><b>{t}</b><p>{d}</p></div></div>'
    top += 168
b2 += '<div class="note" style="top:1125px;right:400px">Marcas por mayor: ENA, Star Nutrition, Gold Nutrition, Optimum Nutrition y MyProtein.</div>'

b3 = ST + TAG + '<div class="eb" style="top:200px">Cómo trabajamos</div>'
b3 += '<div class="t" style="top:255px;font-size:72px">Simple y<br><span class="box">directo</span></div>'
b3 += (f'<div class="ok3" style="top:470px">{E("✅")}<p><b>Originales</b>Suplementos de marcas reconocidas.</p></div>'
       f'<div class="ok3" style="top:665px">{E("📦")}<p><b>Por unidad y por mayor</b>Para tu local o para revender.</p></div>'
       f'<div class="ok3" style="top:860px">{E("💬")}<p><b>Atención directa</b>Por WhatsApp, solo mensajes.</p></div>')
b3 += '<div class="note" style="top:1070px">Envíos a todo el país, a cargo de quien compra. Lista y condiciones: consultanos.</div>'

b4 = ST + TAG + '<div class="eb" style="top:200px">Cómo pedir</div>'
b4 += '<div class="t" style="top:255px;font-size:72px">Tu lista en<br><span class="box">3 pasos</span></div>'
pasos = [('1', 'Mandá MAYORISTA', 'Por WhatsApp, <em>solo mensajes</em>.'),
         ('2', 'Contanos de tu negocio', 'Dietética, tienda o reventa, y dónde estás.'),
         ('3', 'Recibí la propuesta', 'Te pasamos la lista para tu caso.')]
top = 490
for n, t, d in pasos:
    b4 += f'<div class="pst" style="top:{top}px"><i>{n}</i><p><b>{t}</b>{d}</p></div>'
    top += 160
b4 += f'<div class="wa" style="top:1000px">{E("💬")}<div><small>ESCRIBÍ MAYORISTA · SOLO MENSAJES</small>{WA}</div></div>'
b4 += f'<div class="cat2" style="top:1190px">{E("🛒",28)} VER CATÁLOGO · <span>LINK EN LA BIO</span></div>'
print(render([page(1, b1, True, 4), page(2, b2, True, 4), page(3, b3, True, 4), page(4, b4, False, 4)], f'{OUT}/post2'))
