"""Historias para los DESTACADOS «Comprar» (2) y «Envíos» (1), actualizadas con Mercado Pago (19/11/2026). 1080×1920.
Reemplazan a destacado_como_comprar y destacado_envios de destacados.py. Datos: ver fijado_como_comprar.py."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.tag{position:absolute;left:80px;top:250px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:34px;letter-spacing:2px;padding:10px 22px 12px}
.st{position:absolute;left:80px;right:80px;display:flex;gap:30px;align-items:center;height:190px;border:2px solid var(--line);background:var(--panel);padding:0 34px}
.st i{flex:0 0 110px;height:110px;background:var(--l);color:var(--bk);font-style:normal;font-family:'Archivo Black';font-size:62px;display:flex;align-items:center;justify-content:center}
.st p{font-size:32px;font-weight:600;line-height:1.28;color:#d6d6d8}.st p b{display:block;color:#fff;font-weight:900;font-size:42px;text-transform:uppercase;margin-bottom:6px}
.st p em{font-style:normal;color:var(--l);font-weight:800}
.zona{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:22px}
.zona div{height:250px;border:3px solid var(--l);background:var(--panel);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px}
.zona b{font-size:32px;font-weight:900;letter-spacing:1px;text-transform:uppercase;color:#d6d6d8}
.zona s{text-decoration:none;font-family:'Archivo Black';font-size:96px;color:var(--l);line-height:1}
.wa{position:absolute;left:80px;right:80px;height:170px;background:var(--l);color:var(--bk);display:flex;align-items:center;justify-content:center;gap:24px}
.wa .e{font-size:72px}
.wa div{font-family:'Archivo Black';font-size:60px;line-height:1}.wa small{display:block;font-family:Montserrat;font-weight:800;font-size:25px;letter-spacing:2px;margin-bottom:8px}
.note{position:absolute;left:80px;right:80px;font-size:30px;font-weight:600;color:#a9a9ad;line-height:1.4;text-align:center}
.cta{position:absolute;left:80px;right:80px;text-align:center;font-size:42px;font-weight:900;text-transform:uppercase}.cta span{color:var(--l)}
</style>'''
WAB = lambda top, sub='SOLO MENSAJES · NO LLAMADAS': f'<div class="wa" style="top:{top}px">{E("💬")}<div><small>{sub}</small>{WA}</div></div>'

# COMPRAR 1/2 · ONLINE
a = ST + '<div class="tag">CÓMO COMPRAR · 1/2</div>'
a += '<div class="t" style="top:350px;font-size:96px">Online con<br><span class="box">Mercado Pago</span></div>'
a += ('<div class="st" style="top:650px"><i>1</i><p><b>Entrá a la web</b>Tocá el <em>link en la bio</em> y armá tu carrito.</p></div>'
      '<div class="st" style="top:860px"><i>2</i><p><b>Pagá online</b>Tarjeta, débito, dinero en cuenta o efectivo en Mercado Pago.</p></div>'
      '<div class="st" style="top:1070px"><i>3</i><p><b>Envío por zona</b>CABA y GBA <em>$9.900</em> · resto del país <em>$14.900</em>.</p></div>'
      '<div class="st" style="top:1280px"><i>4</i><p><b>Coordinamos</b>Te escribimos por WhatsApp para la entrega.</p></div>')
a += '<div class="note" style="top:1520px">Por Mercado Pago se paga el precio de lista.</div>'

# COMPRAR 2/2 · WHATSAPP 10% OFF
b = ST + '<div class="tag">CÓMO COMPRAR · 2/2</div>'
b += '<div class="t" style="top:350px;font-size:96px">Por WhatsApp<br><span class="box">con 10% OFF</span></div>'
b += ('<div class="st" style="top:650px"><i>1</i><p><b>Elegí</b>Mirá precios y combos en el <em>link en la bio</em>.</p></div>'
      '<div class="st" style="top:860px"><i>2</i><p><b>Escribinos</b>Mandanos tu pedido por mensaje.</p></div>'
      '<div class="st" style="top:1070px"><i>3</i><p><b>Pagá menos</b><em>10% OFF</em> por transferencia o efectivo.</p></div>')
b += WAB(1320)
b += '<div class="note" style="top:1530px">¿Tenés un negocio? Mandá MAYORISTA.</div>'

# ENVÍOS
e = ST + '<div class="tag">ENVÍOS</div>'
e += '<div class="t" style="top:350px;font-size:96px">Enviamos a<br><span class="box">todo el país</span></div>'
e += ('<div class="zona" style="top:650px"><div><b>CABA y GBA</b><s>$9.900</s></div>'
      '<div><b>Resto del país</b><s>$14.900</s></div></div>')
e += ('<div class="st" style="top:960px"><i style="font-size:58px">🛒</i><p><b>Comprando online</b>El envío se suma solo al pagar con Mercado Pago.</p></div>'
      '<div class="st" style="top:1170px"><i style="font-size:58px">💬</i><p><b>Por WhatsApp</b>Te pasamos el costo con tu pedido.</p></div>')
e += WAB(1400)

outs = []
for nm, h in [('comprar_online', a), ('comprar_whatsapp', b), ('envios', e)]:
    outs += render([page(1, h, nxt=False, total=1, story=True)], f'{OUT}/destacado_{nm}', 1080, 1920)
print(outs)
