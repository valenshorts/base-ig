"""Post 13:00 · 20/11/2026 · familia EDUCA (viernes, esto o aquello): «¿Clara o yema? ¿Cuál tiene más proteína cada 100 g?»
4 slides 1080×1350: portada A/B sin adelantar → gana la yema cada 100 g → giro: por unidad gana la clara (pesa casi el doble)
→ huevo entero = las dos juntas + guardar/compartir.
Fuente: USDA FoodData Central (SR Legacy): clara cruda 10,9 g proteína y 52 kcal cada 100 g; yema cruda 15,9 g y 322 kcal cada 100 g;
huevo grande: clara 33 g → 3,6 g de proteína, yema 17 g → 2,7 g, huevo entero 50 g → 6,3 g."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

# Ilustraciones planas: no hay emoji fiel para «clara» ni «yema» sueltas
def clara(s):
    return (f'<svg viewBox="0 0 200 160" width="{s}" height="{s * .8:.0f}"><path d="M30 92C10 60 40 22 82 30c22-22 70-18 86 10 '
            f'30 10 30 58 6 76-16 30-72 34-100 20C40 140 14 120 30 92Z" fill="#F7F7F2"/>'
            f'<path d="M58 54c10-10 26-14 40-10" stroke="#fff" stroke-width="8" fill="none" opacity=".9"/></svg>')

def yema(s):
    return (f'<svg viewBox="0 0 160 160" width="{s}" height="{s}"><circle cx="80" cy="82" r="62" fill="#F6B21A"/>'
            f'<circle cx="80" cy="82" r="62" fill="none" stroke="#E29A0C" stroke-width="6"/>'
            f'<ellipse cx="60" cy="60" rx="18" ry="11" fill="#FFE08A" transform="rotate(-30 60 60)"/></svg>')

ST = '''<style>
.ab{position:absolute;left:80px;right:80px;display:flex;gap:26px}
.ab .o{flex:1;height:520px;position:relative;border:2px solid var(--line);background:radial-gradient(ellipse at 50% 42%,#3A3A3E 0%,#232326 58%,#141416 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:36px}
.ab .o i{position:absolute;left:0;top:0;width:74px;height:74px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-style:normal;font-size:46px;display:flex;align-items:center;justify-content:center}
.ab .o b{font-family:'Archivo Black';font-weight:400;font-size:52px;letter-spacing:1px;text-transform:uppercase}
.ab .o svg{filter:drop-shadow(0 18px 24px rgba(0,0,0,.55))}
.ab .vs{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-6deg);width:120px;height:120px;background:var(--bk);border:4px solid var(--l);color:var(--l);font-family:'Archivo Black';font-size:52px;display:flex;align-items:center;justify-content:center;z-index:2}
.chip{position:absolute;left:80px;border:3px solid var(--l);color:var(--l);font-weight:900;font-size:28px;letter-spacing:3px;padding:10px 18px}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.25}.cta span{color:var(--l)}
.big{position:absolute;left:80px;font-family:'Archivo Black';font-size:110px;line-height:1;text-transform:uppercase;letter-spacing:-2px}
.big span{background:var(--l);color:var(--bk);padding:0 22px 8px;display:inline-block}
.cmp{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:270px 1fr 1fr}
.cmp > div{height:140px;display:flex;align-items:center;justify-content:center;border-bottom:2px solid var(--line)}
.cmp .c0{justify-content:flex-start}
.cmp .h{flex-direction:column;gap:6px;font-family:'Archivo Black';font-size:32px;text-transform:uppercase;height:180px}
.cmp .k{justify-content:flex-start;font-size:27px;font-weight:800;letter-spacing:1.5px;color:#a9a9ad;text-transform:uppercase}
.cmp .v{font-family:'Archivo Black';font-size:64px;color:#d6d6d8}
.cmp .v small{font-family:Montserrat;font-weight:800;font-size:28px;margin-left:8px;color:#8b8b8f}
.cmp .on{background:var(--l);color:var(--bk);border-bottom-color:var(--l)} .cmp .on small{color:var(--bk)}
.cmp .k.on{color:var(--bk);padding-left:22px}
.src{position:absolute;left:80px;right:80px;font-size:23px;font-weight:600;color:#a9a9ad;line-height:1.4}.src b{color:#fff}
.un{position:absolute;left:80px;right:80px;display:flex;gap:26px}
.un .c{flex:1;height:540px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column;align-items:center;padding-top:30px}
.un .c .ill{height:170px;display:flex;align-items:center}
.un .c h3{font-family:'Archivo Black';font-weight:400;font-size:46px;text-transform:uppercase;margin-top:14px}
.un .c .w{margin-top:10px;font-size:26px;font-weight:800;color:#a9a9ad;letter-spacing:2px;text-transform:uppercase}
.un .c .n{margin-top:22px;font-family:'Archivo Black';font-size:96px;line-height:1}
.un .c .n small{font-size:44px}
.un .c .l{font-size:24px;font-weight:800;color:#a9a9ad;letter-spacing:2px;text-transform:uppercase;margin-top:8px}
.un .c.on{border-color:var(--l)} .un .c.on .n{color:var(--l)}
.eq{position:absolute;left:80px;right:80px;height:380px;display:flex;align-items:center;justify-content:space-between;background:var(--panel);border:2px solid var(--line);padding:0 46px}
.eq .c{display:flex;flex-direction:column;align-items:center;gap:16px;width:250px}
.eq .c .ill{height:150px;display:flex;align-items:center}
.eq .c .e{font-size:140px}
.eq .c b{font-family:'Archivo Black';font-weight:400;font-size:52px;line-height:1}
.eq .c small{font-size:23px;font-weight:800;letter-spacing:1.5px;color:#a9a9ad;text-transform:uppercase}
.eq .c.on b{color:var(--l)}
.eq .op{font-family:'Archivo Black';font-size:80px;color:#6d6d72}
.save{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:22px;font-size:30px;font-weight:800;line-height:1.25}
.save span{color:var(--l)}
</style>'''

# 1 · PORTADA: esto o aquello, sin resaltar ninguna opción
s1 = ST + '<div class="eb" style="top:190px">Esto o aquello</div>'
s1 += '<div class="t" style="top:240px;font-size:96px">¿<span class="hl">Clara</span> o<br><span class="hl">yema</span>?</div>'
s1 += '<div class="txt" style="top:500px;font-size:36px;font-weight:700;color:#fff">¿Cuál tiene más <em>proteína</em>?</div>'
s1 += '<div class="chip" style="top:570px">CADA 100 G</div>'
s1 += (f'<div class="ab" style="top:660px"><div class="o"><i>A</i>{clara(300)}<b>Clara</b></div>'
       f'<div class="o"><i>B</i>{yema(220)}<b>Yema</b></div><div class="vs">VS</div></div>')
s1 += f'<div class="cta" style="top:1206px">Comentá <span>A o B</span> y deslizá {E("👉",30)}</div>'

# 2 · RESPUESTA: gana la yema cada 100 g (con calorías como contexto)
s2 = ST + '<div class="eb" style="top:190px">La respuesta</div>'
s2 += '<div class="big" style="top:240px">Gana la B:<br><span>la yema</span></div>'
cmp = (f'<div class="c0"><span class="chip" style="position:static">CADA 100 G</span></div>'
       f'<div class="h">{clara(120)}Clara</div><div class="h">{yema(96)}Yema</div>')
for k, a, b, u, on in [('Proteína', '10,9', '15,9', 'g', True), ('Calorías', '52', '322', 'kcal', False)]:
    c = ' on' if on else ''
    cmp += f'<div class="k{c}">{k}</div><div class="v{c}">{a}<small>{u}</small></div><div class="v{c}">{b}<small>{u}</small></div>'
s2 += f'<div class="cmp" style="top:530px">{cmp}</div>'
s2 += '<div class="txt" style="top:1010px;font-size:31px">La yema también tiene <b>mucha más grasa</b>: por eso suma más calorías.</div>'
s2 += '<div class="src" style="top:1125px">Clara y yema crudas, <b>cada 100 g</b>. Fuente: <b>USDA FoodData Central</b>.</div>'

# 3 · EL GIRO: por unidad gana la clara, porque hay casi el doble
s3 = ST + '<div class="eb" style="top:190px">Pero ojo</div>'
s3 += '<div class="t" style="top:240px;font-size:76px">En un huevo,<br>gana la <span class="box">clara</span></div>'
s3 += ('<div class="un" style="top:480px">'
       f'<div class="c on"><div class="ill">{clara(200)}</div><h3>Clara</h3><div class="w">pesa ≈ 33 g</div><div class="n">3,6<small> g</small></div><div class="l">de proteína</div></div>'
       f'<div class="c"><div class="ill">{yema(150)}</div><h3>Yema</h3><div class="w">pesa ≈ 17 g</div><div class="n">2,7<small> g</small></div><div class="l">de proteína</div></div></div>')
s3 += '<div class="txt" style="top:1050px;font-size:31px">En un huevo grande hay <b>casi el doble de clara</b> que de yema.</div>'
s3 += '<div class="src" style="top:1150px">Huevo grande crudo. Fuente: <b>USDA FoodData Central</b>.</div>'

# 4 · HUEVO ENTERO + guardar / compartir
s4 = ST + '<div class="eb" style="top:190px">La cuenta completa</div>'
s4 += '<div class="t" style="top:240px;font-size:76px">El huevo<br><span class="box">entero</span></div>'
s4 += (f'<div class="eq" style="top:460px"><div class="c"><div class="ill">{clara(170)}</div><b>3,6 g</b><small>Clara</small></div><div class="op">+</div>'
       f'<div class="c"><div class="ill">{yema(120)}</div><b>2,7 g</b><small>Yema</small></div><div class="op">=</div>'
       f'<div class="c on"><div class="ill">{E("🥚")}</div><b>6,3 g</b><small>Huevo grande</small></div></div>')
s4 += '<div class="txt" style="top:880px;font-size:31px">Cada parte aporta lo suyo. Cada 100 g gana la yema; en un huevo, la clara.</div>'
s4 += f'<div class="save" style="top:1050px">{E("📌",40)}<div>Guardalo y <span>compartilo</span> con quien solo come claras.</div></div>'
s4 += f'<div class="btn" style="left:80px;bottom:76px;font-size:27px">{E("🛒",27)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/post1'))
