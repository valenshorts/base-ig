"""Post 13:00 · 18/11/2026 · familia CONFIANZA (miércoles): «Tu pedido en un solo mensaje» (qué mandarnos por WhatsApp).
4 slides 1080×1350. Solo datos reales de kit/README.md: pedidos y pagos se coordinan por WhatsApp 11 2178-9431 (solo mensajes);
10 % OFF por transferencia o efectivo; envíos a todo el país con costo a cargo de quien compra. Sin plazos ni promesas de tiempos de respuesta.
El mensaje de la slide 3 es un EJEMPLO rotulado como tal (no es un cliente real)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.tag{position:absolute;right:80px;top:192px;border:2px solid var(--l);color:var(--l);font-weight:800;font-size:22px;letter-spacing:4px;padding:8px 16px}
.phone{position:absolute;left:50%;transform:translateX(-50%);width:760px;height:440px;border:2px solid var(--line);background:radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);display:flex;flex-direction:column;justify-content:center;gap:26px;padding:0 44px}
.bub{max-width:520px;padding:24px 30px;font-size:38px;font-weight:700;line-height:1.25}
.bub.me{align-self:flex-end;background:var(--l);color:var(--bk)}
.bub.ot{align-self:flex-start;background:#2c2c30;color:#fff;border:2px solid #3a3a3d}
.bub .e{font-size:34px}
.dots{display:flex;gap:14px}.dots i{width:22px;height:22px;background:#8b8b8f;display:block}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.25}.cta span{color:var(--l)}
.ck{position:absolute;left:80px;right:80px;height:118px;display:flex;align-items:center;gap:28px;border:2px solid var(--line);background:var(--panel);padding:0 28px}
.ck .k{flex:0 0 84px;height:84px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.ck .k .e{font-size:52px}
.ck p{font-size:27px;font-weight:600;color:#bdbdc0;line-height:1.25}.ck p b{display:block;color:#fff;font-weight:900;font-size:33px;text-transform:uppercase}
.chat{position:absolute;left:80px;right:80px;height:560px;border:2px solid var(--line);background:var(--panel);display:flex;flex-direction:column;justify-content:center;gap:26px;padding:0 40px}
.chat .bub{max-width:760px;font-size:31px;padding:22px 26px}
.chat .lab{position:absolute;left:-2px;top:-2px;background:var(--l);color:var(--bk);font-weight:900;font-size:22px;letter-spacing:3px;padding:8px 16px}
.chat .bub.me b{font-weight:900}
.note{position:absolute;left:80px;right:80px;font-size:25px;font-weight:600;color:#a9a9ad;line-height:1.35}.note b{color:#fff}
.wa{position:absolute;left:80px;right:80px;height:190px;background:var(--l);color:var(--bk);display:flex;align-items:center;justify-content:center;gap:26px}
.wa .e{font-size:84px}
.wa div{display:flex;flex-direction:column}.wa small{font-size:24px;font-weight:900;letter-spacing:3px}
.wa b{font-family:'Archivo Black';font-weight:400;font-size:84px;line-height:1}
.mini{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:22px}
.mini div{height:200px;border:2px solid var(--line);background:var(--panel);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center;padding:0 16px}
.mini .e{font-size:64px}.mini b{font-size:26px;font-weight:900;text-transform:uppercase;line-height:1.15}.mini b span{color:var(--l)}
</style>'''
TAG = '<div class="tag">CÓMO COMPRAR</div>'

# 1 · PORTADA
s1 = ST + TAG + '<div class="eb" style="top:200px">Pedí fácil</div>'
s1 += '<div class="t" style="top:255px;font-size:84px">Tu pedido<br>en un solo<br><span class="box">mensaje</span></div>'
s1 += (f'<div class="phone" style="top:680px"><div class="bub me">Hola BASE {E("👋")}<br>Quiero hacer un pedido</div>'
       '<div class="bub ot"><div class="dots"><i></i><i></i><i></i></div></div></div>')
s1 += f'<div class="cta" style="top:1200px">Qué mandarnos {E("👉",30)}</div>'

# 2 · CHECKLIST (íconos en vez de números)
s2 = ST + TAG + '<div class="eb" style="top:200px">Qué mandarnos</div>'
s2 += '<div class="t" style="top:255px;font-size:76px">5 datos<br><span class="box">y listo</span></div>'
items = [('🛒', 'Producto y tamaño', 'El nombre como figura en el catálogo.'),
         ('🍦', 'Sabor', 'Si el producto tiene sabores.'),
         ('🛍️', 'Cantidad', 'Cuántas unidades de cada uno.'),
         ('📍', 'Tu localidad', 'Para calcular y coordinar el envío.'),
         ('💳', 'Cómo querés pagar', 'Transferencia, efectivo o tarjeta.')]
top = 480
for e, b, t in items:
    s2 += f'<div class="ck" style="top:{top}px"><div class="k">{E(e)}</div><p><b>{b}</b>{t}</p></div>'
    top += 138
s2 += f'<div class="cta" style="top:1200px;font-size:29px">Mirá un ejemplo {E("👉",29)}</div>'

# 3 · EJEMPLO DE MENSAJE (rotulado como ejemplo)
s3 = ST + TAG + '<div class="eb" style="top:200px">Así de simple</div>'
s3 += '<div class="t" style="top:255px;font-size:76px">Un mensaje<br><span class="box">completo</span></div>'
s3 += ('<div class="chat" style="top:480px"><div class="lab">EJEMPLO</div>'
       '<div class="bub me">¡Hola! Quiero <b>2 Creatinas Star doypack 300 g</b> y <b>1 ENA 100% Whey 907 g</b> sabor <b>vainilla</b>. '
       'Soy de <b>Rosario</b>. Pago por <b>transferencia</b>.</div>'
       f'<div class="bub ot">¡Buenísimo! {E("🙌")} Te pasamos el total y coordinamos el envío.</div></div>')
s3 += f'<div class="note" style="top:1070px">{E("💸",26)} <b>10% OFF</b> pagando por transferencia o efectivo.<br>{E("📦",26)} <b>Envíos a todo el país</b>: el costo del envío lo paga quien compra.</div>'

# 4 · CTA ÚNICO: WhatsApp
s4 = ST + TAG + '<div class="eb" style="top:200px">Hacé tu pedido</div>'
s4 += '<div class="t" style="top:255px;font-size:80px">Escribinos<br><span class="box">por WhatsApp</span></div>'
s4 += f'<div class="wa" style="top:520px">{E("💬")}<div><small>SOLO MENSAJES · NO LLAMADAS</small><b>{WA}</b></div></div>'
s4 += (f'<div class="mini" style="top:760px"><div>{E("🛒")}<b>Elegí en el catálogo<br><span>link en la bio</span></b></div>'
       f'<div>{E("📌")}<b>Guardá este post<br><span>para tu próximo pedido</span></b></div></div>')
s4 += f'<div class="btn" style="left:80px;top:1010px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s4 += f'<div class="note" style="top:1120px">Precios publicados: transferencia o efectivo.</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/pedido'))
