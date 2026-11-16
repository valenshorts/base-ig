"""Comparativa: ¿whey concentrada o isolate? (4 slides 1080×1350) · 17/11/2026 19:30.
Definiciones de la industria láctea (US Dairy Export Council): concentrado de suero (WPC) entre 34 % y 89 % de proteína
(el más usado en suplementos es el WPC 80, ≈ 80 %); aislado (WPI) 90 % o más, en base seca, con menos lactosa y grasa.
La proteína de suero es completa (trae los 9 aminoácidos esenciales). Sin clasificar productos: no verificamos etiquetas.
Precios: kit/README.md."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.vs2{position:absolute;left:80px;right:80px;display:flex;gap:28px}
.vs2 .o{flex:1;height:470px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column}
.vs2 .o .ph{flex:1;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-bottom:2px solid var(--line);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px}
.vs2 .o .ph .e{font-size:130px;filter:drop-shadow(0 16px 22px rgba(0,0,0,.55))}
.vs2 .o .ph b{font-family:'Archivo Black';font-weight:400;font-size:64px;letter-spacing:2px;color:var(--l)}
.vs2 .o .nm{height:96px;display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:900;letter-spacing:1px;text-transform:uppercase}
.vsb{position:absolute;left:50%;transform:translateX(-50%);width:110px;height:110px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:48px;display:flex;align-items:center;justify-content:center;z-index:3;border:6px solid var(--bk)}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.25}.cta span{color:var(--l)}
.tb{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:210px 1fr 1fr}
.tb > div{border-bottom:2px solid var(--line);padding:14px 18px;display:flex;align-items:center}
.tb .hdr{height:110px;justify-content:center;gap:12px;background:var(--panel);border:2px solid var(--line)}
.tb .hdr b{font-family:'Archivo Black';font-weight:400;font-size:40px;color:var(--l)}
.tb .hdr span{font-size:22px;font-weight:900;letter-spacing:1px;text-transform:uppercase}
.tb .rk{flex-direction:column;align-items:flex-start;justify-content:center;gap:6px;font-size:20px;font-weight:800;letter-spacing:1.5px;color:#a9a9ad;text-transform:uppercase;line-height:1.2}
.tb .rk .e{font-size:42px}
.tb .v{height:132px;font-size:26px;font-weight:600;line-height:1.28;color:#d6d6d8}
.tb .v b{color:#fff;font-weight:900}
.src{position:absolute;left:80px;right:80px;font-size:21px;font-weight:600;color:#8b8b8f;letter-spacing:.5px;line-height:1.35}
.pt{position:absolute;left:80px;right:80px;display:flex;gap:28px;align-items:center}
.pt .k{flex:0 0 120px;height:120px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.pt .k .e{font-size:68px}
.pt .n{font-size:29px;font-weight:500;line-height:1.34;color:#d6d6d8}.pt .n b{color:#fff;font-weight:800}.pt .n em{font-style:normal;color:var(--l);font-weight:700}
.claim{position:absolute;left:80px;right:80px;font-size:23px;line-height:1.35;color:#bdbdc0;font-weight:500}
.t4 .tile .ph img{max-height:80%}
.t4 .tile .ft .b{font-size:20px}
</style>'''

# 1 · PORTADA
s1 = ST + '<div class="eb" style="top:200px">Comparativa</div>'
s1 += '<div class="t" style="top:250px;font-size:80px">Whey<br>concentrada<br>o <span class="box">isolate</span></div>'
s1 += (f'<div class="vs2" style="top:640px"><div class="o"><div class="ph">{E("🥛")}<b>WPC</b></div><div class="nm">Concentrada</div></div>'
       f'<div class="o"><div class="ph">{E("🥛")}<b>WPI</b></div><div class="nm">Isolate</div></div>'
       '<div class="vsb" style="top:180px">VS</div></div>')
s1 += f'<div class="cta" style="top:1185px">Las <span>diferencias</span> {E("👉",30)}</div>'

# 2 · TABLA
s2 = ST + '<div class="eb" style="top:200px">Las diferencias</div>'
s2 += '<div class="t" style="top:250px;font-size:68px">Las dos son whey,<br><span class="box">cambia el filtrado</span></div>'
rows = [('⚙️', 'Proceso', '<span><b>Menos filtrada</b></span>', '<span><b>Un filtrado extra</b></span>'),
        ('💪', 'Proteína', '<span><b>Variable</b>: la más común ronda el <b>80 %</b></span>', '<span><b>90 % o más</b></span>'),
        ('🥛🧈', 'Lactosa y grasa', '<span><b>Algo más</b></span>', '<span><b>Muy poca</b></span>'),
        ('💲', 'Precio', '<span>En general, <b>más accesible</b></span>', '<span>En general, <b>cuesta más</b></span>')]
tb = '<div></div><div class="hdr"><b>WPC</b><span>Concentrada</span></div><div class="hdr"><b>WPI</b><span>Isolate</span></div>'
for e, k, a, b in rows:
    tb += f'<div class="rk">{E(e)}{k}</div><div class="v">{a}</div><div class="v">{b}</div>'
s2 += f'<div class="tb" style="top:470px">{tb}</div>'
s2 += '<div class="src" style="top:1120px">% de proteína en base seca. Fuente: US Dairy Export Council.</div>'
s2 += f'<div class="cta" style="top:1185px;font-size:29px">¿Cuál elegir? <span>Deslizá</span> {E("👉",29)}</div>'

# 3 · CÓMO ELEGIR
s3 = ST + '<div class="eb" style="top:200px">¿Cuál elegir?</div>'
s3 += '<div class="t" style="top:250px;font-size:76px">Depende<br>de <span class="box">vos</span></div>'
pts = [('🧩', 'Las dos son <b>proteína completa</b>: traen <em>los 9 aminoácidos esenciales</em>.'),
       ('🥛', 'Si la <b>lactosa te cae pesada</b>, la isolate trae menos.'),
       ('💲', 'Si la leche te cae bien, la <b>concentrada</b> suele salir <em>más barata</em>.'),
       ('🔍', 'Muchas wheys son <b>mezcla de las dos</b>: mirá el primer ingrediente de la etiqueta.')]
top = 470
for k, t in pts:
    s3 += f'<div class="pt" style="top:{top}px"><div class="k">{E(k)}</div><div class="n">{t}</div></div>'
    top += 165
s3 += f'<div class="cta" style="top:1185px;font-size:28px">Guardalo y compartilo {E("📌",28)}</div>'

# 4 · VENTA
s4 = ST + '<div class="eb" style="top:200px">Elegí la tuya</div>'
s4 += '<div class="t" style="top:250px;font-size:76px">Mirá qué<br>trae <span class="box">cada una</span></div>'
s4 += tiles([('on_gold_standard', pf('ON Gold Standard', '$60.900')),
             ('ena_truemade_vainilla', pf('ENA Truemade', '$90.900')),
             ('platinum1kg_vainilla', pf('Star Platinum', '$93.900'))], 500, 292, 380).replace('class="tiles"', 'class="tiles t4"')
s4 += '<div class="claim" style="top:1000px">ON ~310 g · ENA 930 g · Star 2 lb. Mirá el primer ingrediente de cada una en la web. La proteína contribuye a aumentar y mantener la masa muscular. Precios por transferencia o efectivo.</div>'
s4 += f'<div class="btn" style="left:80px;top:1112px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s4 += f'<div style="position:absolute;left:80px;top:1207px;font-size:23px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8">{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">11 2178-9431</span> · SOLO MENSAJES</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/whey'))
