"""25/11/2026 · post1 13:00 [CONFIANZA] «Las marcas que encontrás en BASE» · post2 19:30 [PRODUCTOS] «Magnesio: 3 opciones».
Datos: marcas y precios (transferencia/efectivo) de kit/README.md; frase de magnesio permitida (EFSA)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.g6{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px}
.g6 .tile .ph{height:230px}
.g6 .tile .cat{font-size:21px;padding:10px 6px 12px}
.br2{position:absolute;left:80px;right:80px;display:flex;gap:26px}
.br2 .tile{flex:1}
.br2 .tile .ph{height:460px}
.br2 .tile .cat{font-size:26px}
.tip{position:absolute;left:80px;right:80px;font-size:29px;font-weight:700;line-height:1.35;color:#d6d6d8;border-left:6px solid var(--l);padding-left:24px}
.tip b{color:var(--l)}
.st{position:absolute;left:80px;right:80px;display:flex;gap:28px;align-items:center;height:150px;border:2px solid var(--line);background:var(--panel);padding:0 30px}
.st i{flex:0 0 90px;height:90px;background:var(--l);color:var(--bk);font-style:normal;font-family:'Archivo Black';font-size:52px;display:flex;align-items:center;justify-content:center}
.st p{font-size:28px;font-weight:600;line-height:1.28;color:#d6d6d8}.st p b{display:block;color:#fff;font-weight:900;font-size:34px;text-transform:uppercase;margin-bottom:4px}
.st p em{font-style:normal;color:var(--l);font-weight:800}
.tr{position:absolute;left:80px;right:80px;display:flex;gap:22px}
.tr .tile{flex:1}
.tr .tile .ph{height:400px}
.tr .tile .ft .b{font-size:20px}.tr .tile .ft .p{font-size:46px}
.fine{position:absolute;left:80px;right:80px;font-size:23px;font-weight:600;color:#a9a9ad;line-height:1.4}
</style>'''

def tc(f, cat):
    return f'<div class="tile"><div class="ph"><img src="assets/{f}.png"></div>{cf(cat, 21)}</div>'

def tp(f, nombre, precio):
    return f'<div class="tile"><div class="ph"><img src="assets/{f}.png"></div>{pf(nombre, precio)}</div>'

# ===== POST 1 · CONFIANZA: MARCAS =====
a1 = ST + '<div class="eb" style="top:200px">Suplementos originales</div>'
a1 += '<div class="t" style="top:250px;font-size:78px">Las marcas<br>que encontrás<br><span class="box">en BASE</span></div>'
a1 += ('<div class="g6" style="top:600px">' + tc('ena_truemade_vainilla', 'ENA') + tc('whey_star_2lb_vainilla', 'Star Nutrition')
       + tc('creatina_gold_300g', 'Gold Nutrition') + tc('on_gold_standard', 'Optimum Nutrition') + tc('mp_whey_brownie', 'MyProtein')
       + tc('collagen', 'Star · Colágeno') + '</div>')

a2 = ST + '<div class="eb" style="top:200px">Nacionales</div>'
a2 += '<div class="t" style="top:250px;font-size:78px">ENA, Star<br>y <span class="box">Gold</span></div>'
a2 += ('<div class="br2" style="top:500px">' + tc('ena_prot_vain', 'ENA · Proteína') + tc('star_crea1kg', 'Star · Creatina 1 kg') + '</div>')
a2 += '<div class="tip" style="top:1090px">Proteínas, creatinas, magnesio, omega 3, colágeno y <b>pre-entrenos</b>.</div>'

a3 = ST + '<div class="eb" style="top:200px">Importadas</div>'
a3 += '<div class="t" style="top:250px;font-size:78px">ON y<br><span class="box">MyProtein</span></div>'
a3 += ('<div class="br2" style="top:500px">' + tc('on_gold_standard', 'ON · Gold Standard') + tc('mp_whey_brownie', 'MyProtein · Impact Whey') + '</div>')
a3 += '<div class="tip" style="top:1090px">Precios y presentaciones de cada una en el <b>catálogo</b>: link en la bio.</div>'

a4 = ST + '<div class="eb" style="top:200px">¿Cómo comprar?</div>'
a4 += '<div class="t" style="top:250px;font-size:78px">Pedí la tuya<br><span class="box">como quieras</span></div>'
a4 += ('<div class="st" style="top:500px"><i>1</i><p><b>Online</b>En la web con <em>Mercado Pago</em> (precio de lista).</p></div>'
       '<div class="st" style="top:670px"><i>2</i><p><b>Por WhatsApp</b><em>10% OFF</em> por transferencia o efectivo.</p></div>'
       '<div class="st" style="top:840px"><i style="font-size:40px">📦</i><p><b>Envíos a todo el país</b>A cargo de quien compra.</p></div>')
a4 += f'<div class="fine" style="top:1020px">{E("💬",22)} WhatsApp 11 2178-9431 · solo mensajes. ¿Tenés un negocio? Mandá MAYORISTA.</div>'
a4 += f'<div class="btn" style="left:80px;bottom:76px;font-size:27px">{E("🛒",27)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
print(render([page(1, a1, True, 4), page(2, a2, True, 4), page(3, a3, True, 4), page(4, a4, False, 4)], f'{OUT}/post1'))

# ===== POST 2 · PRODUCTOS: MAGNESIO =====
b1 = ST + '<div class="eb" style="top:200px">Guía de compra</div>'
b1 += '<div class="t" style="top:250px;font-size:80px">Magnesio:<br><span class="box">3 opciones</span></div>'
b1 += ('<div class="tr" style="top:520px">' + tp('star_citratomg', 'Star citrato', '$10.900') + tp('ena_citratomg', 'ENA citrato', '$12.900')
       + tp('magnesio_glicinato_gold', 'Gold glicinato', '$15.900') + '</div>')
b1 += '<div class="fine" style="top:1060px">60 cápsulas cada uno. Precios por transferencia o efectivo.</div>'

b2 = ST + '<div class="eb" style="top:200px">Citrato</div>'
b2 += '<div class="t" style="top:250px;font-size:80px">Star o<br><span class="box">ENA</span></div>'
b2 += ('<div class="br2" style="top:500px">' + tp('star_citratomg', 'Magnesio citrato Star 60 caps', '$10.900')
       + tp('ena_citratomg', 'Magnesio citrato ENA 60 caps', '$12.900') + '</div>')
b2 = b2.replace('.br2 .tile .ph{height:460px}', '.br2 .tile .ph{height:440px}')

b3 = ST + '<div class="eb" style="top:200px">Glicinato</div>'
b3 += '<div class="t" style="top:250px;font-size:80px">Gold<br><span class="box">glicinato</span></div>'
b3 += ('<div class="br2" style="top:500px;justify-content:center"><div style="flex:0 0 520px">' + tp('magnesio_glicinato_gold', 'Magnesio glicinato Gold 60 caps', '$15.900') + '</div></div>')
b3 += '<div class="tip" style="top:1100px">Citrato y glicinato son dos formas distintas de magnesio. <b>Leé la etiqueta</b> y respetá la porción.</div>'

b4 = ST + '<div class="eb" style="top:200px">Para qué sirve</div>'
b4 += '<div class="t" style="top:250px;font-size:76px">El magnesio<br><span class="box">contribuye a…</span></div>'
b4 += ('<div class="st" style="top:500px"><i style="font-size:44px">😮‍💨</i><p><b>Menos cansancio</b>Contribuye a disminuir el cansancio y la fatiga.</p></div>'
       '<div class="st" style="top:670px"><i style="font-size:44px">💪</i><p><b>Músculos</b>Contribuye al funcionamiento normal de los músculos.</p></div>')
b4 += '<div class="fine" style="top:860px">Declaraciones autorizadas por la EFSA (Unión Europea). Precios por transferencia o efectivo; por Mercado Pago en la web, precio de lista.</div>'
b4 += f'<div class="btn" style="left:80px;bottom:76px;font-size:27px">{E("🛒",27)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
print(render([page(1, b1, True, 4), page(2, b2, True, 4), page(3, b3, True, 4), page(4, b4, False, 4)], f'{OUT}/post2'))
