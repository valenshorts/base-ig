"""Desafío: ordená de más a menos magnesio cada 100 g (4 slides 1080×1350) · 16/11/2026 13:00.
Fuente: USDA FoodData Central (SR Legacy): semillas de zapallo secas 592 mg · almendras 270 mg ·
chocolate amargo 70–85 % 228 mg · banana cruda 27 mg (magnesio) y 358 mg (potasio), cada 100 g."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

# Semillas de zapallo (no hay emoji fiel): SVG plano
PEPITAS = '''<svg viewBox="0 0 140 110" width="{s}" height="{h}">
<g fill="#9BB85A" stroke="#6E8A3A" stroke-width="2">
<ellipse cx="40" cy="38" rx="13" ry="24" transform="rotate(-30 40 38)"/><ellipse cx="72" cy="30" rx="13" ry="24" transform="rotate(8 72 30)"/>
<ellipse cx="103" cy="42" rx="13" ry="24" transform="rotate(38 103 42)"/><ellipse cx="54" cy="74" rx="13" ry="24" transform="rotate(-70 54 74)"/>
<ellipse cx="92" cy="78" rx="13" ry="24" transform="rotate(64 92 78)"/></g>
<g fill="#C3DB86"><ellipse cx="38" cy="34" rx="4" ry="12" transform="rotate(-30 38 34)"/><ellipse cx="71" cy="25" rx="4" ry="12" transform="rotate(8 71 25)"/>
<ellipse cx="104" cy="38" rx="4" ry="12" transform="rotate(38 104 38)"/></g></svg>'''
# Almendras (🌰 es castaña, no almendra): SVG plano
ALM = '''<svg viewBox="0 0 140 110" width="{s}" height="{h}">
<g stroke="#7A4A26" stroke-width="2"><path d="M44 12 C66 30 70 70 44 98 C18 70 22 30 44 12z" fill="#C68A55" transform="rotate(-18 44 55)"/>
<path d="M96 12 C118 30 122 70 96 98 C70 70 74 30 96 12z" fill="#B97A45" transform="rotate(20 96 55)"/></g>
<g stroke="#8E5A30" stroke-width="2" fill="none" stroke-linecap="round"><path d="M40 34 q4 20 0 44" transform="rotate(-18 44 55)"/><path d="M50 36 q3 18 -1 40" transform="rotate(-18 44 55)"/>
<path d="M92 34 q4 20 0 44" transform="rotate(20 96 55)"/><path d="M102 36 q3 18 -1 40" transform="rotate(20 96 55)"/></g></svg>'''
alm = lambda s: ALM.format(s=s, h=int(s * 110 / 140))
pep = lambda s: PEPITAS.format(s=s, h=int(s * 110 / 140))

ST = '''<style>
.g4{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:24px}
.g4 .o{position:relative;height:300px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column}
.g4 .o .ph{flex:1;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-bottom:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.g4 .o .ph .e{font-size:120px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.g4 .o .ph svg{filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.g4 .o .lt{position:absolute;left:0;top:0;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:38px;width:62px;height:62px;display:flex;align-items:center;justify-content:center}
.g4 .o .nm{height:76px;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:900;text-transform:uppercase}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.25}.cta span{color:var(--l)}
.rk{position:absolute;left:80px;right:80px;display:flex;flex-direction:column;gap:18px}
.rk .r{display:flex;align-items:center;gap:22px;height:132px}
.rk .r .ic{flex:0 0 132px;height:132px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.rk .r .ic .e{font-size:76px}
.rk .r .bd{flex:1;display:flex;flex-direction:column;gap:10px}
.rk .r .bd .tp{display:flex;justify-content:space-between;align-items:baseline}
.rk .r .bd .tp b{font-size:29px;font-weight:900;text-transform:uppercase}
.rk .r .bd .tp span{font-family:'Archivo Black';font-size:40px;color:var(--l)}
.rk .r .bar{height:26px;background:#1d1d1f;border:2px solid var(--line)}
.rk .r .bar i{display:block;height:100%;background:var(--l)}
.rk .r.lo .bar i{background:#6a6a6e} .rk .r.lo .tp span{color:#d6d6d8}
.src{position:absolute;left:80px;right:80px;font-size:21px;font-weight:600;color:#8b8b8f;letter-spacing:.5px}
.pt{position:absolute;left:80px;right:80px;display:flex;gap:28px;align-items:center}
.pt .k{flex:0 0 120px;height:120px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.pt .k .e{font-size:68px}
.pt .n{font-size:29px;font-weight:500;line-height:1.34;color:#d6d6d8}.pt .n b{color:#fff;font-weight:800}.pt .n em{font-style:normal;color:var(--l);font-weight:700}
.claim{position:absolute;left:80px;right:80px;font-size:23px;line-height:1.35;color:#bdbdc0;font-weight:500}
.t4 .tile .ph img{max-height:80%}
.t4 .tile .ft .b{font-size:22px}
</style>'''

def g4(ops, top):
    return f'<div class="g4" style="top:{top}px">' + ''.join(
        f'<div class="o"><div class="ph">{ic}</div><div class="lt">{l}</div><div class="nm">{n}</div></div>' for l, ic, n in ops) + '</div>'

# 1 · DESAFÍO (sin adelantar la respuesta: todos iguales)
s1 = ST + '<div class="eb" style="top:200px">Desafío</div>'
s1 += '<div class="t" style="top:250px;font-size:70px">Ordenalos de más<br>a menos <span class="box">magnesio</span></div>'
s1 += '<div class="src" style="top:440px">Cada 100 g de alimento</div>'
s1 += g4([('A', E('🍌'), 'Banana'), ('B', pep(170), 'Semillas de zapallo'),
          ('C', E('🍫'), 'Chocolate amargo'), ('D', alm(170), 'Almendras')], 490)
s1 += f'<div class="cta" style="top:1160px">Comentá tu orden con las letras {E("👇",30)}<br><span style="font-size:26px;color:#bdbdc0">Por ejemplo: A · B · C · D</span></div>'

# 2 · RESPUESTA
s2 = ST + '<div class="eb" style="top:200px">La respuesta</div>'
s2 += '<div class="t" style="top:250px;font-size:72px">De más<br><span class="box">a menos</span></div>'
rows = [('B · Semillas de zapallo', pep(110), '592 mg', 100, ''),
        ('D · Almendras', alm(110), '270 mg', 46, ''),
        ('C · Chocolate amargo', E('🍫'), '228 mg', 39, ''),
        ('A · Banana', E('🍌'), '27 mg', 5, ' lo')]
rk = ''.join(f'<div class="r{c}"><div class="ic">{ic}</div><div class="bd"><div class="tp"><b>{n}</b><span>{v}</span></div>'
             f'<div class="bar"><i style="width:{w}%"></i></div></div></div>' for n, ic, v, w, c in rows)
s2 += f'<div class="rk" style="top:470px">{rk}</div>'
s2 += '<div class="src" style="top:1090px">Magnesio cada 100 g · chocolate 70–85 % cacao · semillas secas. Fuente: USDA FoodData Central.</div>'
s2 += f'<div class="cta" style="top:1180px;font-size:29px">¿Y la banana? <span>Deslizá</span> {E("👉",29)}</div>'

# 3 · EL GIRO
s3 = ST + '<div class="eb" style="top:200px">El giro</div>'
s3 += '<div class="t" style="top:250px;font-size:74px">La banana es<br>famosa por<br><span class="box">otro mineral</span></div>'
pts = [('🍌', 'Lo que más trae la banana es <b>potasio</b>: <em>358 mg cada 100 g</em>, contra 27 mg de magnesio.'),
       ('🥜', 'El magnesio abunda en <b>semillas, frutos secos, legumbres</b> y cereales integrales.'),
       ('🔍', 'Los valores son cada 100 g: <b>nadie come 100 g de semillas</b> de una. Mirá también la porción.')]
top = 560
for k, t in pts:
    s3 += f'<div class="pt" style="top:{top}px"><div class="k">{E(k)}</div><div class="n">{t}</div></div>'
    top += 190
s3 += f'<div class="cta" style="top:1180px;font-size:28px">Guardalo y compartilo {E("📌",28)}</div>'

# 4 · VENTA
s4 = ST + '<div class="eb" style="top:200px">Magnesio en cápsulas</div>'
s4 += '<div class="t" style="top:250px;font-size:80px">Citrato o<br><span class="box">glicinato</span></div>'
s4 += tiles([('star_citratomg', pf('Citrato Star', '$10.900')),
             ('ena_citratomg', pf('Citrato ENA', '$12.900')),
             ('magnesio_glicinato_gold', pf('Glicinato Gold', '$15.900'))], 500, 292, 380).replace('class="tiles"', 'class="tiles t4"')
s4 += '<div class="claim" style="top:1010px">El magnesio contribuye a disminuir el cansancio y la fatiga y al funcionamiento normal de los músculos. Los tres vienen en frascos de 60 cápsulas. Precios por transferencia o efectivo.</div>'
s4 += f'<div class="btn" style="left:80px;top:1112px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s4 += f'<div style="position:absolute;left:80px;top:1207px;font-size:23px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8">{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">11 2178-9431</span> · SOLO MENSAJES</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/magnesio'))
