"""Post 19:30 · 20/11/2026 · familia MAYORISTAS (viernes, para gimnasios): «¿Tenés un gimnasio? Sumá suplementos originales».
4 slides 1080×1350 con el estándar kit/estandar_mayoristas.py: portada → 3 categorías para arrancar (con fotos reales)
→ marcas que trabajamos por mayor → cómo pedir la lista (MAYORISTA por WhatsApp).
SIN precios, mínimos, descuentos, márgenes, stock, plazos ni promesas de ventas: no están confirmados."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.tag{position:absolute;right:80px;top:192px;border:2px solid var(--l);color:var(--l);font-weight:800;font-size:22px;letter-spacing:4px;padding:8px 16px}
.lead{position:absolute;left:80px;right:80px;font-size:34px;font-weight:600;line-height:1.38;color:#d6d6d8}.lead b{color:#fff;font-weight:800}.lead em{font-style:normal;color:var(--l);font-weight:800}
.gym{position:absolute;left:80px;right:80px;height:560px;border:2px solid var(--line);background:radial-gradient(circle 340px at 50% 50%,rgba(198,244,50,.10),transparent 100%),radial-gradient(ellipse at 50% 42%,#3A3A3E 0%,#232326 58%,#141416 100%);display:flex;align-items:flex-end;justify-content:center;padding-bottom:50px}
.gym img{filter:drop-shadow(0 22px 30px rgba(0,0,0,.6))}
.gym .a{height:330px;margin-right:10px} .gym .b{height:420px;position:relative;z-index:2} .gym .c{height:300px;margin-left:10px}
.gym .ic{position:absolute;left:30px;top:26px;width:130px;height:130px;border:3px solid var(--l);background:var(--bk);display:flex;align-items:center;justify-content:center}
.gym .ic .e{font-size:84px}
.row{position:absolute;left:80px;right:80px;height:200px;display:flex;border:2px solid var(--line);background:var(--panel)}
.row .ph{flex:0 0 220px;background:radial-gradient(ellipse at 50% 42%,#3A3A3E 0%,#232326 58%,#141416 100%);display:flex;align-items:center;justify-content:center;border-right:2px solid var(--line)}
.row .ph img{max-height:84%;max-width:84%;filter:drop-shadow(0 14px 18px rgba(0,0,0,.6))}
.row .tx{flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 34px;gap:10px}
.row .tx b{font-size:44px;font-weight:900;text-transform:uppercase;line-height:1}
.row .tx p{font-size:27px;font-weight:600;color:#bdbdc0;line-height:1.3}
.row .n{flex:0 0 90px;border-left:2px solid var(--line);display:flex;align-items:center;justify-content:center;font-family:'Archivo Black';font-size:48px;color:var(--l)}
.more{position:absolute;left:80px;right:80px;display:flex;flex-wrap:wrap;gap:14px;align-items:center}
.more small{font-size:20px;font-weight:800;letter-spacing:2px;color:#a9a9ad;text-transform:uppercase;margin-right:6px}
.more span{border:2px solid #3a3a3d;font-size:22px;font-weight:800;letter-spacing:1px;text-transform:uppercase;padding:8px 14px}
.brands{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:repeat(6,1fr);gap:18px}
.brands .tile{grid-column:span 2} .brands .tile:nth-child(4){grid-column:2 / span 2}
.brands .tile .ph{height:250px}
.brands .tile .cat{font-size:22px;padding:10px 6px 12px}
.st{position:absolute;left:80px;right:80px;display:flex;gap:30px;align-items:center}
.st i{flex:0 0 96px;height:96px;border:3px solid var(--l);color:var(--l);font-style:normal;font-family:'Archivo Black';font-size:52px;display:flex;align-items:center;justify-content:center}
.st p{font-size:30px;font-weight:600;line-height:1.3;color:#d6d6d8}.st p b{display:block;color:#fff;font-weight:900;font-size:36px;text-transform:uppercase;letter-spacing:.5px;margin-bottom:4px}
.st p em{font-style:normal;color:var(--l);font-weight:800}
.wa{position:absolute;left:80px;right:80px;height:150px;background:var(--l);color:var(--bk);display:flex;align-items:center;justify-content:center;gap:22px}
.wa .e{font-size:64px}
.wa div{font-family:'Archivo Black';font-size:52px;line-height:1}.wa small{display:block;font-family:Montserrat;font-weight:800;font-size:23px;letter-spacing:2px;margin-bottom:8px}
.cat2{position:absolute;left:80px;right:80px;text-align:center;font-size:28px;font-weight:800;letter-spacing:1.5px;color:#d6d6d8}.cat2 span{color:var(--l)}
.note{position:absolute;left:80px;right:80px;font-size:23px;font-weight:600;color:#a9a9ad;line-height:1.4}
</style>'''
TAG = '<div class="tag">BASE MAYORISTAS</div>'

# 1 · PORTADA: a quién le habla
s1 = ST + TAG + '<div class="eb" style="top:200px">Para gimnasios</div>'
s1 += '<div class="t" style="top:255px;font-size:74px">¿Tenés un<br>gimnasio? Sumá<br><span class="box">suplementos</span></div>'
s1 += (f'<div class="gym" style="top:600px"><div class="ic">{E("🏋️")}</div><img class="a" src="assets/creatina_star_300g.png">'
       '<img class="b" src="assets/ena_truemade_vainilla.png"><img class="c" src="assets/tnt_dynamite_star.png"></div>')

# 2 · POR DÓNDE EMPEZAR: 3 categorías con foto real
s2 = ST + TAG + '<div class="eb" style="top:200px">Por dónde empezar</div>'
s2 += '<div class="t" style="top:255px;font-size:72px">3 categorías<br><span class="box">básicas</span></div>'
cats = [('ena_prot_vain', 'Proteínas', 'Whey de ENA, Star, Gold, Optimum Nutrition y MyProtein.'),
        ('pote300', 'Creatinas', 'Monohidrato en doypack o pote, incluida Creapure.'),
        ('tnt_dynamite_star', 'Pre-entrenos', 'TNT Dynamite de Star Nutrition.')]
top = 440
for i, (f, t, d) in enumerate(cats, 1):
    s2 += f'<div class="row" style="top:{top}px"><div class="ph"><img src="assets/{f}.png"></div><div class="tx"><b>{t}</b><p>{d}</p></div><div class="n">{i}</div></div>'
    top += 218
s2 += ('<div class="more" style="top:1104px"><small>Y también</small>' + ''.join(f'<span>{c}</span>' for c in ['Magnesio', 'Omega 3', 'Colágeno', 'Combos']) + '</div>')

# 3 · MARCAS POR MAYOR (fotos reales)
s3 = ST + TAG + '<div class="eb" style="top:200px">Marcas por mayor</div>'
s3 += '<div class="t" style="top:255px;font-size:72px">5 marcas,<br><span class="box">un solo lugar</span></div>'
marcas = [('ena_truemade_vainilla', 'ENA'), ('whey_star_2lb_vainilla', 'Star Nutrition'), ('gold_creapure200', 'Gold Nutrition'),
          ('on_gold_standard', 'Optimum Nutrition'), ('mp_whey_brownie', 'MyProtein')]
s3 += ('<div class="brands" style="top:470px">' + ''.join(
    f'<div class="tile"><div class="ph"><img src="assets/{f}.png"></div>{cf(n, 22)}</div>' for f, n in marcas) + '</div>')
s3 += '<div class="note" style="top:1100px">Suplementos originales de 5 marcas. Para tu gimnasio, consultanos.</div>'

# 4 · CÓMO PEDIR LA LISTA
s4 = ST + TAG + '<div class="eb" style="top:200px">Cómo pedir</div>'
s4 += '<div class="t" style="top:255px;font-size:72px">Tu lista en<br><span class="box">3 pasos</span></div>'
pasos = [('1', 'Mandá MAYORISTA', 'Por WhatsApp, <em>solo mensajes</em>.'),
         ('2', 'Contanos de tu gimnasio', 'Dónde está y qué productos querés sumar.'),
         ('3', 'Recibí la propuesta', 'Te pasamos la lista para tu caso.')]
top = 500
for n, t, d in pasos:
    s4 += f'<div class="st" style="top:{top}px"><i>{n}</i><p><b>{t}</b>{d}</p></div>'
    top += 160
s4 += f'<div class="wa" style="top:1010px">{E("💬")}<div><small>ESCRIBÍ MAYORISTA · SOLO MENSAJES</small>{WA}</div></div>'
s4 += f'<div class="cat2" style="top:1200px">{E("🛒",28)} VER CATÁLOGO · <span>LINK EN LA BIO</span></div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/post2'))
