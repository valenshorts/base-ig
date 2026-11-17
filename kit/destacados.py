"""Historias para DESTACADOS (17/11/2026): Catálogo, Ofertas, Mayoristas, Envíos, Cómo comprar. 1080×1920.
Datos: kit/README.md (precios combos transferencia/efectivo) + confirmados por Valentín (envíos a todo el país a cargo del
comprador, 10 % OFF transferencia/efectivo, mayoristas con MAYORISTA al mismo WhatsApp). Si cambian precios, rehacer «Ofertas».
También genera las portadas cuadradas de los destacados (portada_*.png)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.tag{position:absolute;left:80px;top:250px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:34px;letter-spacing:2px;padding:10px 22px 12px}
.grid3{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.grid3 .tile .ph{height:290px}
.grid3 .tile .ft .b{font-size:19px}.grid3 .tile .ft .p{font-size:36px}
.combo{position:absolute;left:80px;right:80px;height:300px;display:flex;border:2px solid var(--line);background:var(--panel)}
.combo .ph{flex:0 0 400px;background:radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);display:flex;align-items:center;justify-content:center;border-right:2px solid var(--line)}
.combo .ph img{max-height:84%;max-width:46%;filter:drop-shadow(0 18px 24px rgba(0,0,0,.6))}
.combo .ph img + img{max-width:40%;max-height:66%;margin-left:-16px;align-self:flex-end;margin-bottom:30px}
.combo .in{flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 34px;gap:8px}
.combo .in b{font-family:'Archivo Black';font-size:46px;text-transform:uppercase;line-height:1}
.combo .in small{font-size:24px;font-weight:600;color:#bdbdc0}
.combo .in s{text-decoration:none;font-family:'Archivo Black';font-size:72px;color:var(--l);line-height:1}
.combo .in i{font-style:normal;align-self:flex-start;background:var(--l);color:var(--bk);font-weight:900;font-size:24px;letter-spacing:1px;padding:6px 12px}
.st{position:absolute;left:80px;right:80px;display:flex;gap:30px;align-items:center;height:200px;border:2px solid var(--line);background:var(--panel);padding:0 34px}
.st i{flex:0 0 112px;height:112px;background:var(--l);color:var(--bk);font-style:normal;font-family:'Archivo Black';font-size:64px;display:flex;align-items:center;justify-content:center}
.st p{font-size:33px;font-weight:600;line-height:1.28;color:#d6d6d8}.st p b{display:block;color:#fff;font-weight:900;font-size:42px;text-transform:uppercase;margin-bottom:6px}
.st p em{font-style:normal;color:var(--l);font-weight:800}
.big{position:absolute;left:80px;right:80px;display:flex;flex-direction:column;align-items:center;text-align:center}
.big .e{font-size:300px}
.wa{position:absolute;left:80px;right:80px;height:170px;background:var(--l);color:var(--bk);display:flex;align-items:center;justify-content:center;gap:24px}
.wa .e{font-size:72px}
.wa div{font-family:'Archivo Black';font-size:60px;line-height:1}.wa small{display:block;font-family:Montserrat;font-weight:800;font-size:25px;letter-spacing:2px;margin-bottom:8px}
.note{position:absolute;left:80px;right:80px;font-size:28px;font-weight:600;color:#a9a9ad;line-height:1.4;text-align:center}
.cta{position:absolute;left:80px;right:80px;text-align:center;font-size:40px;font-weight:900;text-transform:uppercase}.cta span{color:var(--l)}
</style>'''
WAB = lambda top, sub='SOLO MENSAJES · NO LLAMADAS': f'<div class="wa" style="top:{top}px">{E("💬")}<div><small>{sub}</small>{WA}</div></div>'

# CATÁLOGO
c = ST + '<div class="tag">CATÁLOGO</div>'
c += '<div class="t" style="top:350px;font-size:96px">Todo el<br>catálogo en<br><span class="box">la web</span></div>'
prods = [('whey_star_2lb_vainilla', 'Star Whey 2 lb', '$81.900'), ('creatina_gold_300g', 'Creatina Gold', '$22.900'),
         ('on_gold_standard', 'ON Gold Std.', '$60.900'), ('ena_truemade_vainilla', 'ENA Truemade', '$90.900'),
         ('creatina_star_300g', 'Creatina Star', '$23.800'), ('star_citratomg', 'Magnesio Star', '$10.900')]
c += '<div class="grid3" style="top:760px">' + ''.join(f'<div class="tile"><div class="ph"><img src="assets/{f}.png"></div>{pf(n, p)}</div>' for f, n, p in prods) + '</div>'
c += '<div class="cta" style="top:1590px">Precios y combos: <span>link en la bio</span> 👆</div>'

# OFERTAS (combos del README)
o = ST + '<div class="tag">OFERTAS</div>'
o += '<div class="t" style="top:350px;font-size:96px">Combos que<br><span class="box">te ahorran</span></div>'
combos = [('ena_prot_vain', 'ena_crea_neutra', 'Combo ENA', 'Proteína 907 g + creatina 300 g', '$85.900', '$7.900'),
          ('whey_star_2lb_vainilla', 'creatina_star_300g', 'Combo Star', 'Whey 2 lb + creatina 300 g', '$99.900', '$5.800'),
          ('creatina_star_300g', 'creatina_star_300g', '2× Creatina Star', '300 g cada una', '$44.900', '$2.700')]
top = 640
for a, b, n, d, p, s in combos:
    o += (f'<div class="combo" style="top:{top}px"><div class="ph"><img src="assets/{a}.png"><img src="assets/{b}.png"></div>'
          f'<div class="in"><b>{n}</b><small>{d}</small><s>{p}</s><i>AHORRÁS {s}</i></div></div>')
    top += 330
o += '<div class="note" style="top:1640px">Precios por transferencia o efectivo. Consultá stock por WhatsApp.</div>'

# MAYORISTAS
m = ST + '<div class="tag">MAYORISTAS</div>'
m += '<div class="t" style="top:350px;font-size:92px">¿Tenés un<br>gimnasio, dietética<br>o <span class="box">tienda?</span></div>'
m += ('<div class="st" style="top:780px"><i>1</i><p><b>Escribinos</b>Mandá <em>MAYORISTA</em> por WhatsApp.</p></div>'
      '<div class="st" style="top:1000px"><i>2</i><p><b>Contanos</b>Qué negocio tenés y qué te interesa.</p></div>'
      '<div class="st" style="top:1220px"><i>3</i><p><b>Recibí la lista</b>Con las condiciones para tu caso.</p></div>')
m += WAB(1460, 'MANDÁ «MAYORISTA» · SOLO MENSAJES')

# ENVÍOS
e = ST + '<div class="tag">ENVÍOS</div>'
e += '<div class="t" style="top:350px;font-size:96px">Enviamos a<br><span class="box">todo el país</span></div>'
e += f'<div class="big" style="top:640px">{E("📦")}</div>'
e += ('<div class="st" style="top:1010px"><i style="font-size:60px">🚚</i><p><b>A todo el país</b>Coordinamos el envío por WhatsApp.</p></div>'
      '<div class="st" style="top:1230px"><i style="font-size:60px">💵</i><p><b>Costo del envío</b>Lo paga quien compra.</p></div>')
e += WAB(1460)

# CÓMO COMPRAR
h = ST + '<div class="tag">CÓMO COMPRAR</div>'
h += '<div class="t" style="top:350px;font-size:96px">Comprar es<br><span class="box">así de fácil</span></div>'
h += ('<div class="st" style="top:660px"><i>1</i><p><b>Elegí</b>En el <em>catálogo</em>: link en la bio.</p></div>'
      '<div class="st" style="top:880px"><i>2</i><p><b>Escribinos</b>Por WhatsApp, qué querés.</p></div>'
      '<div class="st" style="top:1100px"><i>3</i><p><b>Pagá y recibí</b><em>10% OFF</em> por transferencia o efectivo.</p></div>')
h += WAB(1360)

pages = [page(1, x, nxt=False, total=1, story=True) for x in (c, o, m, e, h)]
names = ['catalogo', 'ofertas', 'mayoristas', 'envios', 'como_comprar']
outs = []
for nm, pg in zip(names, pages):
    outs += render([pg], f'{OUT}/destacado_{nm}', 1080, 1920)

os.environ.pop('BASE_CHECK', None)
# Portadas (círculo de IG): fondo negro, ícono lima grande
ICON = {'catalogo': '🛒', 'ofertas': '💸', 'mayoristas': '🤝', 'envios': '📦', 'como_comprar': '🛍️'}
for nm, ic in ICON.items():
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} body{{margin:0}}'
            '.c{width:1080px;height:1080px;background:#0B0B0C;display:flex;align-items:center;justify-content:center}'
            '.r{width:760px;height:760px;border-radius:50%;background:#C6F432;display:flex;align-items:center;justify-content:center}'
            '.r .e{font-size:400px}</style></head><body><div class="c"><div class="r">' + E(ic) + '</div></div></body></html>')
    outs += render([html], f'{OUT}/portada_{nm}', 1080, 1080)
print(outs)
