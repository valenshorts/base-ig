"""Guía: cómo leer la etiqueta de tu proteína (4 slides 1080×1350) · 14/11/2026 19:30."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.lbl{position:absolute;left:80px;width:520px;background:#F3F2ED;color:#0B0B0C;padding:26px 30px;border:3px solid #0B0B0C;box-shadow:12px 12px 0 rgba(198,244,50,.9)}
.lbl h4{font-size:34px;font-weight:900;letter-spacing:-.5px;border-bottom:10px solid #0B0B0C;padding-bottom:8px;text-transform:uppercase}
.lbl .r{display:flex;justify-content:space-between;font-size:27px;font-weight:600;padding:9px 0;border-bottom:2px solid #0B0B0C}
.lbl .r b{font-weight:900}
.lbl .r.big{font-size:30px;font-weight:900;border-bottom:6px solid #0B0B0C}
.lbl .r.mk{background:var(--l);margin:0 -12px;padding:9px 12px}
.lbl small{display:block;font-size:19px;font-weight:700;letter-spacing:1px;margin-top:10px;color:#555}
.lens{position:absolute;display:flex;align-items:center;justify-content:center}
.lens .e{filter:drop-shadow(0 16px 22px rgba(0,0,0,.6))}
.side{position:absolute;right:80px;width:320px;display:flex;flex-direction:column;gap:16px}
.side div{background:var(--panel);border:2px solid var(--line);height:105px;display:flex;align-items:center;gap:18px;padding:0 20px}
.side .e{font-size:52px}
.side p{font-size:23px;font-weight:800;line-height:1.15;text-transform:uppercase}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.2}.cta span{color:var(--l)}
.mth{position:absolute;left:80px;right:80px;height:250px;display:flex;align-items:center;justify-content:center;gap:24px}
.mth .bx{width:250px;height:250px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px}
.mth .bx .e{font-size:96px}
.mth .bx b{font-family:'Archivo Black';font-weight:400;font-size:54px;line-height:1}
.mth .bx span{font-size:21px;font-weight:800;letter-spacing:2.5px;color:#a9a9ad;text-transform:uppercase}
.mth .op{font-family:'Archivo Black';font-size:64px;color:var(--l)}
.mth .rs{background:var(--l);color:var(--bk)} .mth .rs span{color:var(--bk)}
.fx{position:absolute;left:80px;right:80px;text-align:center;font-size:30px;font-weight:800;letter-spacing:1px;color:#d6d6d8}
.fx b{color:var(--l)}
.pt{position:absolute;left:80px;right:80px;display:flex;gap:28px;align-items:center}
.pt .k{flex:0 0 104px;height:104px;background:var(--panel);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.pt .k .e{font-size:58px}
.pt .n{font-size:29px;font-weight:500;line-height:1.34;color:#d6d6d8}.pt .n b{color:#fff;font-weight:800}.pt .n em{font-style:normal;color:var(--l);font-weight:700}
.rc{position:absolute;left:80px;right:80px;height:200px;display:flex;align-items:center;gap:30px;padding:0 30px 0 0}
.rc .ic{flex:0 0 190px;height:196px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-right:2px solid var(--line);display:flex;align-items:center;justify-content:center;position:relative}
.rc .ic .e{font-size:100px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.rc .ic i{position:absolute;left:0;top:0;width:48px;height:48px;background:var(--l);color:var(--bk);font-style:normal;font-family:'Archivo Black';font-size:28px;display:flex;align-items:center;justify-content:center}
.rc .nm{font-size:34px;font-weight:900;text-transform:uppercase;letter-spacing:-.5px}
.rc .in{font-size:25px;font-weight:600;color:#d6d6d8;line-height:1.36;margin-top:10px}
.rc .in b{color:var(--l);font-weight:800}
.claim{position:absolute;left:80px;right:80px;font-size:23px;line-height:1.35;color:#bdbdc0;font-weight:500}
.t4 .tile .ph img{max-height:76%}
</style>'''

# 1 · PORTADA
s1 = ST + '<div class="eb" style="top:200px">Guía rápida</div>'
s1 += '<div class="t" style="top:250px;font-size:84px">Cómo leer la<br>etiqueta de tu<br><span class="box">proteína</span></div>'
s1 += f'''<div class="lbl" style="top:640px">
 <h4>Información nutricional</h4>
 <div class="r big"><span>Porción</span><b>? g</b></div>
 <div class="r"><span>Valor energético</span><b>? kcal</b></div>
 <div class="r mk"><span>Proteínas</span><b>? g</b></div>
 <div class="r"><span>Carbohidratos</span><b>? g</b></div>
 <div class="r"><span>Grasas totales</span><b>? g</b></div>
 <small>INGREDIENTES: ? · ? · ?</small>
 <div class="lens" style="right:-70px;top:-90px;width:180px;height:180px">{E("🔍",150)}</div></div>'''
s1 += f'''<div class="side" style="top:660px">
 <div>{E("🥄")}<p>Porción</p></div>
 <div>{E("📋")}<p>Ingredientes</p></div>
 <div>{E("📦")}<p>Proteína del envase</p></div>
 <div>{E("🏷️")}<p>Precio por gramo</p></div></div>'''
s1 += f'<div class="cta" style="top:1208px;font-size:29px"><span>4 cosas</span> para mirar {E("👉",29)}</div>'

# 2 · PORCIÓN ≠ PROTEÍNA
s2 = ST + '<div class="eb" style="top:200px">1 · La porción</div>'
s2 += '<div class="t" style="top:250px;font-size:80px">Un scoop no es<br><span class="box">todo proteína</span></div>'
s2 += f'''<div class="mth" style="top:510px">
 <div class="bx panel" style="position:relative"><b style="font-size:76px">24 g</b><span>Proteína</span></div><div class="op">÷</div>
 <div class="bx panel" style="position:relative">{E("🥄")}<b>30 g</b><span>Porción</span></div><div class="op">=</div>
 <div class="bx rs"><b style="font-size:84px">80 %</b><span>Proteína</span></div></div>'''
s2 += '<div class="fx" style="top:790px">EJEMPLO · <b>proteína ÷ porción × 100</b></div>'
pts = [('🧩', 'El resto son <b>carbohidratos, grasas, saborizantes y otros ingredientes</b>. Por eso el % cambia de una marca a otra.'),
       ('⚖️', '<b>Cada marca usa su propio tamaño de porción.</b> Para comparar dos proteínas, <em>calculá el % de cada una</em>.')]
top = 880
for k, t in pts:
    s2 += f'<div class="pt" style="top:{top}px"><div class="k">{E(k)}</div><div class="n">{t}</div></div>'
    top += 150
s2 += f'<div class="cta" style="top:1205px"><span>3 cosas más</span> {E("👉",30)}</div>'

# 3 · INGREDIENTES, PORCIONES, PRECIO
s3 = ST + '<div class="eb" style="top:200px">2, 3 y 4</div>'
s3 += '<div class="t" style="top:250px;font-size:84px">Lo que casi<br><span class="box">nadie mira</span></div>'
rcs = [('📋', '2', 'El orden importa', 'Los ingredientes van <b>de mayor a menor cantidad</b>. En una whey, lo primero debería ser la proteína (ej.: concentrado de proteína de suero).'),
       ('📦', '3', 'Proteína del envase', '<b>Porciones × g de proteína por porción</b> = cuánta proteína trae el pote entero.'),
       ('🏷️', '4', 'Precio por gramo', '<b>Precio ÷ proteína del envase</b> = lo que pagás cada gramo de proteína. Así comparás de verdad.')]
top = 510
for em, n, nm, ing in rcs:
    s3 += f'<div class="rc panel" style="top:{top}px"><div class="ic">{E(em)}<i>{n}</i></div><div><div class="nm">{nm}</div><div class="in">{ing}</div></div></div>'
    top += 222
s3 += f'<div class="cta" style="top:1205px;font-size:28px">Guardalo para tu próxima compra {E("📌",28)}</div>'

# 4 · VENTA
s4 = ST + '<div class="eb" style="top:200px">Mirá las etiquetas</div>'
s4 += '<div class="t" style="top:250px;font-size:84px">Elegí tu<br><span class="box">proteína</span></div>'
s4 += tiles([('ena_prot_vain', pf('ENA · 907 g', '$66.900')),
             ('whey_star_2lb_vainilla', pf('Star · 2 lb', '$81.900')),
             ('mp_whey_brownie', pf('MyProtein · 1 kg', '$78.900'))], 510, 292, 380).replace('class="tiles"', 'class="tiles t4"')
s4 += '<div class="claim" style="top:1028px">La proteína contribuye a aumentar y mantener la masa muscular. Precios por transferencia o efectivo.</div>'
s4 += f'<div class="btn" style="left:80px;top:1112px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s4 += f'<div style="position:absolute;left:80px;top:1207px;font-size:23px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8">{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">11 2178-9431</span> · SOLO MENSAJES</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/etiqueta'))
