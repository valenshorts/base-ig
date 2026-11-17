"""PUBLICACIÓN FIJADA «Somos BASE · Cómo comprar» (17/11/2026). 4 slides 1080×1350, familia CONFIANZA.
Datos confirmados por Valentín: venta por unidad y por mayor; 10 % OFF transferencia o efectivo (vs. tarjeta, kit/README.md);
envíos a todo el país con costo a cargo del comprador; pedidos y consultas por WhatsApp 11 2178-9431 (solo mensajes)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.tag{position:absolute;right:80px;top:192px;border:2px solid var(--l);color:var(--l);font-weight:800;font-size:22px;letter-spacing:4px;padding:8px 16px}
.rail{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.rail .tile .ph{height:300px}
.vals{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px}
.vals div{height:170px;border:2px solid var(--line);background:var(--panel);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center}
.vals .e{font-size:62px} .vals b{font-size:25px;font-weight:900;letter-spacing:.5px;text-transform:uppercase;line-height:1.1}
.st{position:absolute;left:80px;right:80px;display:flex;gap:30px;align-items:center;height:170px;border:2px solid var(--line);background:var(--panel);padding:0 30px}
.st i{flex:0 0 100px;height:100px;background:var(--l);color:var(--bk);font-style:normal;font-family:'Archivo Black';font-size:58px;display:flex;align-items:center;justify-content:center}
.st p{font-size:30px;font-weight:600;line-height:1.28;color:#d6d6d8}.st p b{display:block;color:#fff;font-weight:900;font-size:38px;text-transform:uppercase;margin-bottom:4px}
.st p em{font-style:normal;color:var(--l);font-weight:800}
.card{position:absolute;left:80px;right:80px;height:250px;border:2px solid var(--line);background:var(--panel);display:flex;align-items:center;gap:34px;padding:0 40px}
.card.on{border-color:var(--l);background:linear-gradient(160deg,rgba(198,244,50,.13),var(--panel) 70%)}
.card .e{font-size:110px}
.card h3{font-family:'Archivo Black';font-size:58px;line-height:1;text-transform:uppercase}
.card h3 span{color:var(--l)}
.card p{font-size:28px;font-weight:600;color:#bdbdc0;margin-top:12px;line-height:1.3}
.wa{position:absolute;left:80px;right:80px;height:150px;background:var(--l);color:var(--bk);display:flex;align-items:center;justify-content:center;gap:22px}
.wa .e{font-size:64px}
.wa div{font-family:'Archivo Black';font-size:52px;line-height:1}.wa small{display:block;font-family:Montserrat;font-weight:800;font-size:23px;letter-spacing:2px;margin-bottom:8px}
</style>'''
TAG = '<div class="tag">SOMOS BASE</div>'

# 1 · QUIÉNES SOMOS
s1 = ST + TAG + '<div class="eb" style="top:200px">Bienvenido</div>'
s1 += '<div class="t" style="top:255px;font-size:80px">Suplementos<br>originales,<br><span class="box">sin vueltas</span></div>'
s1 += ('<div class="rail" style="top:600px">' + ''.join(
    f'<div class="tile"><div class="ph"><img src="assets/{f}.png"></div></div>' for f in
    ['whey_star_2lb_vainilla', 'creatina_gold_300g', 'on_gold_standard']) + '</div>')
s1 += (f'<div class="vals" style="top:935px"><div>{E("🛒")}<b>Por unidad<br>o por mayor</b></div>'
       f'<div>{E("💸")}<b>10% OFF<br>transf. o efectivo</b></div><div>{E("📦")}<b>Envíos a<br>todo el país</b></div></div>')

# 2 · CÓMO COMPRAR
s2 = ST + TAG + '<div class="eb" style="top:200px">Cómo comprar</div>'
s2 += '<div class="t" style="top:255px;font-size:80px">En 3 pasos<br><span class="box">y listo</span></div>'
pasos = [('1', 'Elegí', 'Mirá precios y combos en el <em>catálogo</em>: link en la bio.'),
         ('2', 'Escribinos', 'Mandá por WhatsApp qué querés y te confirmamos.'),
         ('3', 'Pagá y recibí', 'Coordinamos el pago y la entrega por mensaje.')]
top = 500
for n, t, d in pasos:
    s2 += f'<div class="st" style="top:{top}px"><i>{n}</i><p><b>{t}</b>{d}</p></div>'
    top += 200

# 3 · PAGO Y ENVÍO
s3 = ST + TAG + '<div class="eb" style="top:200px">Pago y envío</div>'
s3 += '<div class="t" style="top:255px;font-size:80px">Lo que tenés<br>que <span class="box">saber</span></div>'
s3 += (f'<div class="card on" style="top:500px">{E("💸")}<div><h3><span>10% OFF</span><br>transferencia<br>o efectivo</h3></div></div>')
s3 += (f'<div class="card" style="top:780px">{E("📦")}<div><h3>Envíos a<br>todo el país</h3>'
       f'<p>El costo del envío lo paga quien compra.</p></div></div>')

# 4 · CONTACTO
s4 = ST + TAG + '<div class="eb" style="top:200px">Consultas y pedidos</div>'
s4 += '<div class="t" style="top:255px;font-size:80px">Escribinos<br><span class="box">por WhatsApp</span></div>'
s4 += f'<div class="wa" style="top:520px">{E("💬")}<div><small>SOLO MENSAJES · NO LLAMADAS</small>{WA}</div></div>'
s4 += (f'<div class="st" style="top:720px"><i style="font-size:46px">{E("🛒",54)}</i><p><b>Por unidad</b>Mirá el catálogo: <em>link en la bio</em>.</p></div>'
       f'<div class="st" style="top:910px"><i style="font-size:46px">{E("🤝",54)}</i><p><b>Por mayor</b>Mandá <em>MAYORISTA</em> y te pasamos la lista.</p></div>')

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/somos_base'))
