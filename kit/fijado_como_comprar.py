"""PUBLICACIÓN FIJADA «Cómo comprar en BASE» (19/11/2026). 4 slides 1080×1350, familia CONFIANZA.
Reemplaza a «Somos BASE · Cómo comprar» (borrada). Datos (web/public/index.html y docs del proyecto, 18/11):
- ONLINE: web basesuplementos.netlify.app (link en la bio) → Mercado Pago (tarjeta, débito, dinero en cuenta o efectivo en MP) a PRECIO DE LISTA;
  envío fijo que se suma en el pago: CABA y GBA $9.900 · resto del país $14.900; después del pago se coordina la entrega por WhatsApp.
- POR WHATSAPP: 11 2178-9431 (solo mensajes) → transferencia o efectivo con 10 % OFF.
- Mayoristas: escribir MAYORISTA al mismo WhatsApp."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.tag{position:absolute;right:80px;top:192px;border:2px solid var(--l);color:var(--l);font-weight:800;font-size:22px;letter-spacing:4px;padding:8px 16px}
.op{position:absolute;left:80px;right:80px;height:270px;border:2px solid var(--line);background:var(--panel);display:flex;align-items:center;gap:34px;padding:0 40px}
.op.on{border-color:var(--l);background:linear-gradient(160deg,rgba(198,244,50,.13),var(--panel) 70%)}
.op .n{flex:0 0 120px;height:120px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:72px;display:flex;align-items:center;justify-content:center}
.op .e{font-size:96px}
.op h3{font-family:'Archivo Black';font-size:50px;line-height:1.02;text-transform:uppercase}
.op h3 span{color:var(--l)}
.op p{font-size:28px;font-weight:600;color:#bdbdc0;margin-top:12px;line-height:1.3}.op p b{color:#fff}
.st{position:absolute;left:80px;right:80px;display:flex;gap:28px;align-items:center;height:150px;border:2px solid var(--line);background:var(--panel);padding:0 30px}
.st i{flex:0 0 90px;height:90px;background:var(--l);color:var(--bk);font-style:normal;font-family:'Archivo Black';font-size:52px;display:flex;align-items:center;justify-content:center}
.st p{font-size:28px;font-weight:600;line-height:1.28;color:#d6d6d8}.st p b{display:block;color:#fff;font-weight:900;font-size:36px;text-transform:uppercase;margin-bottom:4px}
.st p em{font-style:normal;color:var(--l);font-weight:800}
.zona{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:22px}
.zona div{height:190px;border:2px solid var(--l);background:var(--panel);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px}
.zona b{font-size:28px;font-weight:900;letter-spacing:1px;text-transform:uppercase;color:#d6d6d8}
.zona s{text-decoration:none;font-family:'Archivo Black';font-size:72px;color:var(--l);line-height:1}
.cmp{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;border:2px solid var(--line)}
.cmp div{padding:22px 24px;border-bottom:2px solid var(--line);font-size:27px;font-weight:600;color:#d6d6d8;line-height:1.3}
.cmp div:nth-child(odd){border-right:2px solid var(--line)}
.cmp .h{font-family:'Archivo Black';font-size:34px;color:#fff;text-transform:uppercase;background:var(--panel2)}
.cmp .h.on{color:var(--bk);background:var(--l)}
.cmp div b{color:#fff;font-weight:900}
.cmp div:nth-last-child(-n+2){border-bottom:0}
.wa{position:absolute;left:80px;right:80px;height:130px;background:var(--l);color:var(--bk);display:flex;align-items:center;justify-content:center;gap:22px}
.wa .e{font-size:58px}
.wa div{font-family:'Archivo Black';font-size:50px;line-height:1}.wa small{display:block;font-family:Montserrat;font-weight:800;font-size:22px;letter-spacing:2px;margin-bottom:6px}
.nota{position:absolute;left:80px;right:80px;font-size:25px;font-weight:600;color:#a9a9ad;line-height:1.4}
</style>'''
TAG = '<div class="tag">CÓMO COMPRAR</div>'

# 1 · PORTADA: dos formas
s1 = ST + TAG + '<div class="eb" style="top:200px">Guía rápida</div>'
s1 += '<div class="t" style="top:255px;font-size:84px">¿Cómo<br>comprar en<br><span class="box">BASE?</span></div>'
s1 += (f'<div class="op on" style="top:600px"><div class="n">1</div><div><h3>Online con<br><span>Mercado Pago</span></h3>'
       f'<p>Desde la web, al toque.</p></div></div>')
s1 += (f'<div class="op" style="top:900px"><div class="n">2</div><div><h3>Por WhatsApp<br><span>con 10% OFF</span></h3>'
       f'<p>Transferencia o efectivo.</p></div></div>')

# 2 · OPCIÓN 1: ONLINE
s2 = ST + TAG + '<div class="eb" style="top:200px">Opción 1 · Online</div>'
s2 += '<div class="t" style="top:255px;font-size:80px">Pagás con<br><span class="box">Mercado Pago</span></div>'
pasos = [('1', 'Elegí en la web', 'Entrá al <em>link en la bio</em> y armá tu carrito.'),
         ('2', 'Pagá online', 'Tarjeta, débito, dinero en cuenta o efectivo en Mercado Pago.'),
         ('3', 'Sumá el envío', 'Se agrega según tu zona (mirá la próxima).'),
         ('4', 'Coordinamos', 'Te escribimos por WhatsApp para la entrega.')]
top = 480
for n, t, d in pasos:
    s2 += f'<div class="st" style="top:{top}px"><i>{n}</i><p><b>{t}</b>{d}</p></div>'
    top += 170
s2 += '<div class="nota" style="top:1150px;right:420px">Por Mercado Pago se paga el precio de lista.</div>'

# 3 · ENVÍOS
s3 = ST + TAG + '<div class="eb" style="top:200px">Envíos a todo el país</div>'
s3 += '<div class="t" style="top:255px;font-size:80px">¿Cuánto sale<br>el <span class="box">envío?</span></div>'
s3 += ('<div class="zona" style="top:500px"><div><b>CABA y GBA</b><s>$9.900</s></div>'
       '<div><b>Resto del país</b><s>$14.900</s></div></div>')
s3 += ('<div class="st" style="top:740px"><i style="font-size:44px">🚚</i><p><b>Lo paga quien compra</b>En la web se suma solo al pagar con Mercado Pago.</p></div>'
       '<div class="st" style="top:910px"><i style="font-size:44px">💬</i><p><b>Por WhatsApp</b>Te pasamos el costo del envío con tu pedido.</p></div>')

# 4 · OPCIÓN 2 + COMPARATIVA
s4 = ST + TAG + '<div class="eb" style="top:200px">Opción 2 · Por WhatsApp</div>'
s4 += '<div class="t" style="top:255px;font-size:80px">Pagá menos<br>con <span class="box">10% OFF</span></div>'
s4 += ('<div class="cmp" style="top:480px">'
       '<div class="h">Online</div><div class="h on">WhatsApp</div>'
       '<div>Mercado Pago:<br><b>tarjeta, débito, dinero en cuenta</b></div><div><b>Transferencia o efectivo</b></div>'
       '<div><b>Precio de lista</b></div><div><b>10% OFF</b></div>'
       '<div>Pedís desde la web</div><div>Mandás tu pedido por mensaje</div></div>')
s4 += f'<div class="wa" style="top:1000px">{E("💬")}<div><small>WHATSAPP · SOLO MENSAJES</small>{WA}</div></div>'
s4 += '<div class="nota" style="top:1150px">¿Tenés un negocio? Mandá <b style="color:var(--l)">MAYORISTA</b> y te pasamos la lista.</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/como_comprar'))
