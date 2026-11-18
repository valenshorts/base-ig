"""Post 19:30 · 18/11/2026 · familia PRODUCTOS (miércoles, guía de compra): «¿Qué te llevás según tu presupuesto?»
4 slides 1080×1350: portada + 3 escalones (hasta 25 / 70 / 90 mil pesos) con UN producto protagonista cada uno.
Todos los precios salen de kit/README.md (transferencia o efectivo). Frases de salud solo las del README."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.lv{position:absolute;left:80px;right:80px;display:flex;flex-direction:column;gap:22px}
.lv div{display:flex;align-items:center;gap:30px;height:170px;border:2px solid var(--line);background:var(--panel);padding:0 34px}
.lv .e{font-size:76px}
.lv b{font-family:'Archivo Black';font-weight:400;font-size:64px;line-height:1}
.lv small{display:block;font-family:Montserrat;font-weight:800;font-size:24px;letter-spacing:3px;color:#a9a9ad;margin-bottom:8px}
.lv .q{margin-left:auto;width:96px;height:96px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:64px;display:flex;align-items:center;justify-content:center}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.25}.cta span{color:var(--l)}
.bud{position:absolute;right:80px;top:192px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:34px;padding:10px 20px 12px}
.hero{position:absolute;left:80px;right:80px;height:500px;border:2px solid var(--line);background:radial-gradient(circle 330px at 50% 46%,rgba(198,244,50,.12),transparent 100%),radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);display:flex;align-items:center;justify-content:center}
.hero img{position:relative;filter:drop-shadow(0 26px 34px rgba(0,0,0,.6))}
.hero .a{height:410px} .hero .b{height:290px;margin-left:24px;align-self:flex-end;margin-bottom:70px}
.hero .sv{position:absolute;right:-2px;top:-2px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:34px;padding:12px 22px 14px}
.pr{position:absolute;left:80px;right:80px;display:flex;align-items:flex-end;justify-content:space-between;gap:20px}
.pr .nm{font-family:'Archivo Black';font-size:50px;text-transform:uppercase;line-height:1}
.pr .nm small{display:block;font-family:Montserrat;font-weight:700;font-size:25px;color:#bdbdc0;text-transform:none;margin-top:10px;letter-spacing:0}
.pr .p{font-family:'Archivo Black';font-size:92px;line-height:.9;color:var(--l);white-space:nowrap}
.alt{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:18px;border-top:2px solid var(--line);padding-top:18px;font-size:26px;font-weight:700;color:#d6d6d8}
.alt i{font-style:normal;border:2px solid var(--l);color:var(--l);font-size:20px;font-weight:900;letter-spacing:2px;padding:6px 12px}.alt b{color:var(--l);font-weight:900}
.fine{position:absolute;left:80px;right:80px;font-size:24px;line-height:1.3;color:#bdbdc0;font-weight:600}
</style>'''

# 1 · PORTADA
s1 = ST + '<div class="eb" style="top:200px">Guía de compra</div>'
s1 += '<div class="t" style="top:250px;font-size:78px">¿Qué te llevás<br>según tu<br><span class="box">presupuesto?</span></div>'
lv = [('💵', 'HASTA', '25 MIL'), ('💰', 'HASTA', '70 MIL'), ('🛍️', 'HASTA', '90 MIL')]
s1 += '<div class="lv" style="top:610px">' + ''.join(
    f'<div>{E(e)}<span><small>{k}</small><b>{v}</b></span><i class="q">?</i></div>' for e, k, v in lv) + '</div>'
s1 += f'<div class="cta" style="top:1200px">Deslizá y mirá <span>qué entra</span> {E("👉",30)}</div>'

def tier(n, bud, eb, titulo, hero, nombre, sub, precio, alt, fine, last=False):
    s = ST + f'<div class="eb" style="top:200px">{eb}</div><div class="bud">{bud}</div>'
    s += f'<div class="t" style="top:250px;font-size:72px">{titulo}</div>'
    s += f'<div class="hero" style="top:450px">{hero}</div>'
    s += f'<div class="pr" style="top:985px"><div class="nm">{nombre}<small>{sub}</small></div><div class="p">{precio}</div></div>'
    s += f'<div class="alt" style="top:1085px"><i>OTRA OPCIÓN</i><span>{alt}</span></div>'
    if last:
        s += f'<div class="btn" style="left:80px;top:1158px;font-size:27px">{E("🛒",27)} PEDÍ EL TUYO · LINK EN LA BIO {ARROW}</div>'
        s += f'<div class="fine" style="top:1252px;font-size:24px;color:#d6d6d8;font-weight:700;letter-spacing:.5px">{fine}</div>'
    else:
        s += f'<div class="fine" style="top:1168px;right:400px">{fine}</div>'
    return s

s2 = tier(2, 'HASTA 25 MIL', 'Para arrancar', 'Tu primera<br><span class="box">creatina</span>',
          '<img class="a" src="assets/creatina_gold_300g.png">', 'Creatina Gold', 'Doypack 300 g', '$22.900',
          '<b>Creatina Star doypack 300 g · $23.800</b>',
          'La creatina aumenta el rendimiento físico en series sucesivas de ejercicios cortos de alta intensidad. Precio por transferencia o efectivo.')
s3 = tier(3, 'HASTA 70 MIL', 'Un paso más', 'Tu primera<br><span class="box">proteína</span>',
          '<img class="a" src="assets/ena_prot_vain.png">', 'ENA 100% Whey', '907 g', '$66.900',
          '<b>ON Gold Standard ~310 g · $60.900</b>',
          'La proteína contribuye a aumentar y mantener la masa muscular. Precios por transferencia o efectivo.')
s4 = tier(4, 'HASTA 90 MIL', 'Proteína + creatina', 'Las dos<br><span class="box">en combo</span>',
          '<img class="a" src="assets/ena_prot_vain.png"><img class="b" src="assets/ena_crea_neutra.png"><div class="sv">AHORRÁS $7.900</div>',
          'Combo ENA', 'Proteína 907 g + creatina 300 g', '$85.900',
          '<b>Combo Gold · $88.900</b> (whey 2 lb + creatina 300 g)',
          f'{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">{WA}</span> · SOLO MENSAJES', last=True)

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/presupuesto'))
