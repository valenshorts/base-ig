"""ESTÁNDAR FAMILIA «BASE MAYORISTAS» (aprobado 17/11 por Valentín, publicado ese día) · BASE MAYORISTAS: «¿Tenés un gimnasio, dietética o tienda? Conocé BASE». 4 slides 1080×1350.
Familia visual MAYORISTAS: misma marca, más institucional (contornos, numeración, menos bloques de precio).
SIN precios, mínimos, descuentos, stock ni plazos: no están confirmados."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.tag{position:absolute;right:80px;top:192px;border:2px solid var(--l);color:var(--l);font-weight:800;font-size:22px;letter-spacing:4px;padding:8px 16px}
.biz{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:24px}
.biz div{height:220px;border:2px solid var(--line);background:var(--panel);display:flex;flex-direction:column;justify-content:center;align-items:center;gap:18px}
.biz .e{font-size:92px}
.biz b{font-size:32px;font-weight:900;letter-spacing:1px;text-transform:uppercase;text-align:center;line-height:1.1}
.lead{position:absolute;left:80px;right:80px;font-size:34px;font-weight:600;line-height:1.38;color:#d6d6d8}.lead b{color:#fff;font-weight:800}.lead em{font-style:normal;color:var(--l);font-weight:800}
.cats{position:absolute;left:80px;right:80px;display:flex;flex-wrap:wrap;gap:14px}
.cats span{border:2px solid #3a3a3d;font-size:27px;font-weight:800;letter-spacing:1px;text-transform:uppercase;padding:12px 20px}
.brands{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.brands .tile .ph{height:230px}
.brands .tile .cat{font-size:22px;padding:10px 6px 12px}
.st{position:absolute;left:80px;right:80px;display:flex;gap:30px;align-items:center}
.st i{flex:0 0 96px;height:96px;border:3px solid var(--l);color:var(--l);font-style:normal;font-family:'Archivo Black';font-size:52px;display:flex;align-items:center;justify-content:center}
.st p{font-size:31px;font-weight:600;line-height:1.3;color:#d6d6d8}.st p b{display:block;color:#fff;font-weight:900;font-size:36px;text-transform:uppercase;letter-spacing:.5px;margin-bottom:4px}
.st p em{font-style:normal;color:var(--l);font-weight:800}
.wa{position:absolute;left:80px;right:80px;height:150px;background:var(--l);color:var(--bk);display:flex;align-items:center;justify-content:center;gap:22px}
.wa .e{font-size:64px}
.wa div{font-family:'Archivo Black';font-size:52px;line-height:1}.wa small{display:block;font-family:Montserrat;font-weight:800;font-size:23px;letter-spacing:2px;margin-bottom:8px}
.note{position:absolute;left:80px;right:80px;font-size:23px;font-weight:600;color:#a9a9ad;line-height:1.4}
</style>'''
TAG = '<div class="tag">BASE MAYORISTAS</div>'

# 1 · PORTADA: a quién le habla, en una pregunta
s1 = ST + TAG + '<div class="eb" style="top:200px">Para negocios</div>'
s1 += '<div class="t" style="top:255px;font-size:70px">¿Tenés un gimnasio,<br>dietética o tienda?<br><span class="box">Conocé BASE</span></div>'
s1 += (f'<div class="biz" style="top:600px"><div>{E("🏋️")}<b>Gimnasios</b></div><div>{E("🥗")}<b>Dietéticas</b></div>'
       f'<div>{E("🛍️")}<b>Tiendas de<br>suplementos</b></div><div>{E("🤝")}<b>Entrenadores y<br>revendedores</b></div></div>')

# 2 · QUÉ ES BASE
s2 = ST + TAG + '<div class="eb" style="top:200px">Quiénes somos</div>'
s2 += '<div class="t" style="top:255px;font-size:76px">Suplementos<br><span class="box">originales</span></div>'
s2 += ('<div class="lead" style="top:500px">BASE vende suplementos deportivos y nutricionales <b>por unidad y por mayor</b>, '
       'con atención directa por WhatsApp.</div>')
s2 += '<div class="eb" style="top:760px">Categorías</div>'
s2 += ('<div class="cats" style="top:810px">' + ''.join(f'<span>{c}</span>' for c in
       ['Proteínas', 'Creatinas', 'Magnesio', 'Omega 3', 'Colágeno', 'Pre-entrenos', 'Combos']) + '</div>')

# 3 · MARCAS DEL CATÁLOGO (fotos reales)
s3 = ST + TAG + '<div class="eb" style="top:200px">Marcas del catálogo</div>'
s3 += '<div class="t" style="top:255px;font-size:76px">Las marcas<br>que <span class="box">se piden</span></div>'
marcas = [('ena_truemade_vainilla', 'ENA'), ('whey_star_2lb_vainilla', 'Star Nutrition'), ('gold_crea1kg', 'Gold Nutrition'),
          ('on_gold_standard', 'Optimum Nutrition'), ('mp_whey_brownie', 'MyProtein'), ('magnesio_glicinato_gold', 'Gold · Magnesio')]
s3 += ('<div class="brands" style="top:500px">' + ''.join(
    f'<div class="tile"><div class="ph"><img src="assets/{f}.png"></div>{cf(n, 22)}</div>' for f, n in marcas) + '</div>')
s3 += '<div class="note" style="top:1110px">Disponibilidad y variedad para tu negocio: consultanos.</div>'

# 4 · CÓMO PEDIR CONDICIONES
s4 = ST + TAG + '<div class="eb" style="top:200px">Cómo empezar</div>'
s4 += '<div class="t" style="top:255px;font-size:76px">Pedí tu lista<br><span class="box">mayorista</span></div>'
pasos = [('1', 'Escribinos', 'Mandá <em>MAYORISTA</em> por WhatsApp.'),
         ('2', 'Contanos tu negocio', 'Qué tipo de local tenés y qué productos te interesan.'),
         ('3', 'Recibí la propuesta', 'Te pasamos lista y condiciones para tu caso.')]
top = 490
for n, t, d in pasos:
    s4 += f'<div class="st" style="top:{top}px"><i>{n}</i><p><b>{t}</b>{d}</p></div>'
    top += 160
s4 += (f'<div class="wa" style="top:990px">{E("💬")}<div><small>WHATSAPP · SOLO MENSAJES</small>{WA}</div></div>')

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/mayoristas'))
