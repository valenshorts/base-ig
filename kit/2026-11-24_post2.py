"""24/11/2026 19:30 [PRODUCTOS] guía de compra «¿Qué creatina me llevo?» 4 slides 1080×1350.
Precios transferencia/efectivo de kit/README.md. Todas son creatina monohidrato (según sus etiquetas). EFSA: al menos 3 g por día."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.g4{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:22px}
.g4 .tile .ph{height:205px}
.duo{position:absolute;left:80px;right:80px;display:flex;gap:26px}
.duo .tile{flex:1}
.duo .tile .ph{height:470px}
.duo .tile .ph img{max-height:86%}
.d4 .tile .ph{height:400px}
.duo .tile .ft .b{font-size:24px}.duo .tile .ft .p{font-size:58px}
.chip{position:absolute;left:12px;top:12px;z-index:2;background:var(--bk);border:2px solid var(--l);color:#fff;font-size:22px;font-weight:900;letter-spacing:1.5px;padding:6px 12px}
.tip{position:absolute;left:80px;right:80px;font-size:29px;font-weight:700;line-height:1.35;color:#d6d6d8;border-left:6px solid var(--l);padding-left:24px}
.tip b{color:var(--l)}
.fine{position:absolute;left:80px;right:80px;font-size:22px;font-weight:600;color:#8b8b8f;line-height:1.4}
</style>'''

def tl(f, chip, nombre, precio):
    c = f'<div class="chip">{chip}</div>' if chip else ''
    return f'<div class="tile"><div class="ph">{c}<img src="assets/{f}.png"></div>{pf(nombre, precio)}</div>'

# 1 · PORTADA
s1 = ST + '<div class="eb" style="top:200px">Guía de compra</div>'
s1 += '<div class="t" style="top:250px;font-size:80px">¿Qué creatina<br><span class="box">me llevo?</span></div>'
s1 += ('<div class="g4" style="top:500px">' + tl('creatina_gold_300g', '', 'Gold 300 g', '$22.900') + tl('creatina_star_300g', '', 'Star 300 g', '$23.800')
       + tl('gold_creapure200', '', 'Gold Creapure 200 g', '$31.900') + tl('star_crea1kg', '', 'Star 1 kg', '$84.900') + '</div>')

# 2 · PARA ARRANCAR
s2 = ST + '<div class="eb" style="top:200px">Si recién arrancás</div>'
s2 += '<div class="t" style="top:250px;font-size:76px">Las más<br><span class="box">accesibles</span></div>'
s2 += ('<div class="duo" style="top:500px">' + tl('creatina_gold_300g', '300 G', 'Creatina Gold', '$22.900')
       + tl('creatina_star_300g', '300 G', 'Creatina Star', '$23.800') + '</div>')
s2 += '<div class="tip" style="top:1115px">Doypack de 300 g: rinde <b>100 días</b> tomando 3 g por día.</div>'

# 3 · CREAPURE / IMPORTADA
s3 = ST + '<div class="eb" style="top:200px">Si buscás algo distinto</div>'
s3 += '<div class="t" style="top:250px;font-size:76px">Creapure<br>o <span class="box">importada</span></div>'
s3 += ('<div class="duo" style="top:500px">' + tl('gold_creapure200', '200 G', 'Gold Creapure', '$31.900')
       + tl('on_creatine', '317 G', 'ON Micronised', '$28.900') + '</div>')
s3 += '<div class="tip" style="top:1115px">Creapure es una marca de creatina monohidrato fabricada en Alemania.</div>'

# 4 · PARA NO COMPRAR SEGUIDO
s4 = ST + '<div class="eb" style="top:200px">Si ya la tomás siempre</div>'
s4 += '<div class="t" style="top:250px;font-size:76px">Formato<br><span class="box">de 1 kg</span></div>'
s4 += ('<div class="duo d4" style="top:480px">' + tl('gold_crea1kg', '1 KG', 'Creatina Gold', '$57.900')
       + tl('star_crea1kg', '1 KG', 'Creatina Star', '$84.900') + '</div>')
s4 += '<div class="fine" style="top:1035px">Todas son creatina monohidrato. Precios por transferencia o efectivo (por Mercado Pago en la web, precio de lista). La creatina aumenta el rendimiento físico en series sucesivas de ejercicios cortos de alta intensidad (con al menos 3 g por día).</div>'
s4 += f'<div class="btn" style="left:80px;bottom:76px;font-size:27px">{E("🛒",27)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/post2'))
