import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.flow{position:absolute;left:80px;right:80px;display:flex;align-items:center;justify-content:space-between}
.flow .bx{width:250px;height:280px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;position:relative}
.flow .bx .e{font-size:120px}
.flow .bx .lb{font-size:22px;font-weight:800;letter-spacing:3px;color:#a9a9ad;text-transform:uppercase}
.flow .op{font-family:'Archivo Black';font-size:66px;color:var(--l)}
.flow .clk{font-family:'Archivo Black';font-size:66px;line-height:1;color:var(--w)}
.flow .qm{background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:150px}
.q{position:absolute;left:80px;right:80px;font-size:48px;font-weight:900;line-height:1.1;text-transform:uppercase;letter-spacing:-1px}
.q .hl{color:var(--l)}
.vs{position:absolute;left:80px;right:80px;display:flex;gap:30px}
.vs div{flex:1;height:120px;display:flex;align-items:center;justify-content:center;gap:18px;font-family:'Archivo Black';font-size:54px;border:3px solid var(--l)}
.vs .e{font-size:48px}
.pt{position:absolute;left:80px;right:80px;display:flex;gap:30px;align-items:center}
.pt .k{flex:0 0 116px;height:116px;background:var(--panel);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.pt .k .e{font-size:64px}
.pt .n{font-size:30px;font-weight:500;line-height:1.36;color:#d6d6d8}.pt .n b{color:#fff;font-weight:800}.pt .n em{font-style:normal;color:var(--l);font-weight:700}
.day{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.day .d{height:250px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px}
.day .d .e{font-size:84px}
.day .d .h{font-size:22px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#d6d6d8;text-align:center;line-height:1.2}
.day .d .h b{display:block;color:var(--l);font-family:'Archivo Black';font-weight:400;font-size:30px;letter-spacing:0;margin-top:4px}
.src{position:absolute;left:80px;right:80px;font-size:21px;font-weight:600;color:#8b8b8f}
.chip{position:absolute;left:12px;top:12px;z-index:2;background:var(--bk);border:2px solid var(--l);color:var(--w);font-size:18px;font-weight:800;letter-spacing:1.5px;padding:6px 10px;display:flex;align-items:center;gap:8px}
.chip .e{font-size:20px}
.t4 .tile .ph img{max-height:72%;margin-top:44px}
.claim{position:absolute;left:80px;right:80px;font-size:23px;line-height:1.35;color:#bdbdc0;font-weight:500}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.2}.cta span{color:var(--l)}
</style>'''

# 1 · GANCHO
s1 = ST + '<div class="eb" style="top:200px">Error común</div>'
s1 += '<div class="t" style="top:250px;font-size:84px">¿Tenés 30 min<br><span class="box">para la whey?</span></div>'
s1 += f'''<div class="flow" style="top:510px">
 <div class="bx panel" style="position:relative">{E("🏋️")}<div class="lb">Entrenás</div></div><div class="op">→</div>
 <div class="bx panel" style="position:relative"><div class="clk">30:00</div>{E("⏱️",64)}</div><div class="op">→</div>
 <div class="bx qm">?</div></div>'''
s1 += '<div class="q" style="top:850px">“Si no la tomás apenas terminás, <span class="hl">perdiste el entreno</span>.”</div>'
s1 += f'<div class="vs" style="top:1020px"><div>{E("✅")} CIERTO</div><div>{E("❌")} FALSO</div></div>'
s1 += f'<div class="cta" style="top:1195px">Comentá <span>CIERTO o FALSO</span> {E("👇",30)}</div>'

# 2 · RESPUESTA
s2 = ST + '<div class="eb" style="top:200px">La respuesta</div>'
s2 += '<div class="t" style="top:250px;font-size:84px">Falso: la ventana<br><span class="box">es más amplia</span></div>'
pts = [('🧮', '<b>Lo que más pesa</b> es la proteína <em>que sumás en todo el día</em>, no el minuto exacto del shake.'),
       ('🍽️', '<b>Repartila:</b> la ISSN sugiere tomas de <em>20 a 40 g cada 3 a 4 horas</em>.'),
       ('🌅', '<b>Excepción:</b> si entrenaste en ayunas, ahí sí <em>conviene no esperar tanto</em> para comer.')]
top = 530
for k, t in pts:
    s2 += f'<div class="pt" style="top:{top}px"><div class="k">{E(k)}</div><div class="n">{t}</div></div>'
    top += 175
s2 += '<div class="src" style="top:1075px">Fuente: ISSN, posturas sobre proteína y ejercicio y sobre nutrient timing (2017).</div>'
s2 += f'<div class="cta" style="top:1195px;font-size:29px">Mirá cómo repartirla {E("👉",30)}</div>'

# 3 · EL DÍA
s3 = ST + '<div class="eb" style="top:200px">Un día tipo</div>'
s3 += '<div class="t" style="top:250px;font-size:80px">Repartí tu<br><span class="box">proteína así</span></div>'
dd = [('🍳','Desayuno'),('🍝','Almuerzo'),('🥤','Merienda<br>o post'),('🍗','Cena')]
s3 += '<div class="day" style="top:530px">' + ''.join(f'<div class="d">{E(e)}<div class="h">{h}<b>20–40 g</b></div></div>' for e,h in dd) + '</div>'
s3 += '<div class="txt" style="top:830px;font-size:31px">Si entrenás a la tarde, <b>el shake puede ser tu merienda</b>. Si entrenás de noche, <em>la cena ya cumple ese rol.</em></div>'
s3 += '<div class="txt" style="top:1010px;font-size:25px;color:#a9a9ad">Ejemplo orientativo: la cantidad total depende de tu peso y tu objetivo. Consultá con un profesional.</div>'
s3 += f'<div class="cta" style="top:1195px;font-size:29px">Guardalo para después {E("📌",28)}</div>'

# 4 · VENTA
def tile(f, chip, ft):
    return f'<div class="tile"><div class="ph"><div class="chip">{chip}</div><img src="assets/{f}.png"></div>{ft}</div>'
s4 = ST + '<div class="eb" style="top:200px">Tu merienda resuelta</div>'
s4 += f'<div class="t" style="top:250px;font-size:84px">Un shake y<br><span class="box">a seguir {E("🥤",72)}</span></div>'
s4 += ('<div class="tiles t4" style="top:525px;--w:292px;--h:330px;--g:22px">'
       + tile('on_gs_choc', f'{E("🍫")} CHOCOLATE', pf('ON · 310 g', '$60.900'))
       + tile('ena_truemade_vainilla', f'{E("🍦")} VAINILLA', pf('ENA · 930 g', '$90.900'))
       + tile('platinum1kg_vainilla', f'{E("🍦")} VAINILLA', pf('Star Platinum · 2 lb', '$93.900')) + '</div>')
s4 += '<div class="claim" style="top:1010px">La proteína contribuye a aumentar y mantener la masa muscular. Precios por transferencia o efectivo.</div>'
s4 += f'<div class="btn" style="left:80px;top:1112px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s4 += f'<div style="position:absolute;left:80px;top:1207px;font-size:23px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8">{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">11 2178-9431</span> · SOLO MENSAJES</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/ventana_whey'))
