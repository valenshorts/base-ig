"""Comparativa: colágeno vs whey, ¿son lo mismo? (4 slides 1080×1350) · 15/11/2026 19:30."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.cv .tile .ph img{max-height:80%}
.vsb{position:absolute;left:50%;transform:translateX(-50%);width:110px;height:110px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:48px;display:flex;align-items:center;justify-content:center;z-index:3;border:6px solid var(--bk)}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.2}.cta span{color:var(--l)}
.tb{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:200px 1fr 1fr;gap:0}
.tb > div{border-bottom:2px solid var(--line);padding:18px 20px;display:flex;align-items:center}
.tb .hdr{height:150px;flex-direction:column;justify-content:center;gap:6px;background:var(--panel);border:2px solid var(--line)}
.tb .hdr .e{font-size:70px}
.tb .hdr b{font-size:28px;font-weight:900;letter-spacing:1px;text-transform:uppercase}
.tb .hdr.on{border-color:var(--l)} .tb .hdr.on b{color:var(--l)}
.tb .rk{flex-direction:column;align-items:flex-start;justify-content:center;gap:6px;font-size:21px;font-weight:800;letter-spacing:2px;color:#a9a9ad;text-transform:uppercase;line-height:1.2}
.tb .rk .e{font-size:44px}
.tb .v{height:158px;font-size:26px;font-weight:600;line-height:1.3;color:#d6d6d8;gap:14px}
.tb .v b{color:#fff;font-weight:900}
.tb .v .ic{flex:0 0 46px;height:46px;display:flex;align-items:center;justify-content:center;font-size:28px}
.tb .v .ic.y{background:var(--l);color:var(--bk)} .tb .v .ic.n{border:2px solid #6a6a6e;color:#d6d6d8}
.pt{position:absolute;left:80px;right:80px;display:flex;gap:28px;align-items:center}
.pt .k{flex:0 0 120px;height:120px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.pt .k .e{font-size:68px}
.pt .n{font-size:29px;font-weight:500;line-height:1.34;color:#d6d6d8}.pt .n b{color:#fff;font-weight:800}.pt .n em{font-style:normal;color:var(--l);font-weight:700}
.claim{position:absolute;left:80px;right:80px;font-size:23px;line-height:1.35;color:#bdbdc0;font-weight:500}
.t4 .tile .ph img{max-height:78%}
</style>'''

# 1 · PORTADA
s1 = ST + '<div class="eb" style="top:200px">Comparativa</div>'
s1 += '<div class="t" style="top:250px;font-size:84px">Colágeno<br>y whey: ¿son<br><span class="box">lo mismo?</span></div>'
s1 += tiles([('collagen', cf('Colágeno', 30)), ('ena_prot_vain', cf('Whey', 30))], 640, 420, 380, 28).replace('class="tiles"', 'class="tiles cv"')[:-6] + '<div class="vsb" style="top:130px">VS</div></div>'
s1 += f'<div class="cta" style="top:1196px">Las <span>3 diferencias</span> {E("👉",30)}</div>'

# 2 · TABLA
s2 = ST + '<div class="eb" style="top:200px">Las diferencias</div>'
s2 += '<div class="t" style="top:250px;font-size:72px">Las dos son proteína,<br><span class="box">pero no iguales</span></div>'
rows = [('📍', 'Origen', '<span><b>Suero de la leche</b></span>', '<span><b>Piel y huesos</b> de animales (vaca, cerdo, pescado)</span>'),
        ('🧩', 'Esenciales', '<span class="ic y">✓</span><span><b>Trae los 9</b> aminoácidos esenciales</span>',
         '<span class="ic n">✕</span><span><b>Le falta el triptófano</b>, uno de los 9</span>'),
        ('⭐', 'Se destaca por', '<span><b>Leucina</b></span>', '<span><b>Glicina, prolina</b> e hidroxiprolina</span>')]
tb = '<div></div>'
tb += f'<div class="hdr on">{E("🥛")}<b>Whey</b></div><div class="hdr">{E("🦴")}<b>Colágeno</b></div>'
for e, k, a, b in rows:
    tb += f'<div class="rk">{E(e)}{k}</div><div class="v">{a}</div><div class="v">{b}</div>'
s2 += f'<div class="tb" style="top:510px">{tb}</div>'
s2 += f'<div class="cta" style="top:1196px;font-size:29px">¿Entonces cuál? <span>Deslizá</span> {E("👉",29)}</div>'

# 3 · CONCLUSIÓN
s3 = ST + '<div class="eb" style="top:200px">Entonces</div>'
s3 += '<div class="t" style="top:250px;font-size:80px">No se<br><span class="box">reemplazan</span></div>'
pts = [('🥛', 'Entre estas dos, la que trae <b>los 9 esenciales</b> (proteína completa) es la <em>whey</em>.'),
       ('🦴', 'El <b>colágeno no reemplaza</b> a tu whey: si lo tomás, no cuenta como tu proteína completa.'),
       ('🔍', 'Mirá la etiqueta: muchos colágenos vienen <b>combinados con otros ingredientes</b> (el de Star trae resveratrol).')]
top = 520
for k, t in pts:
    s3 += f'<div class="pt" style="top:{top}px"><div class="k">{E(k)}</div><div class="n">{t}</div></div>'
    top += 190
s3 += f'<div class="cta" style="top:1196px;font-size:28px">Guardalo y compartilo {E("📌",28)}</div>'

# 4 · VENTA
s4 = ST + '<div class="eb" style="top:200px">Conocé las dos</div>'
s4 += '<div class="t" style="top:250px;font-size:84px">Mirá qué trae<br><span class="box">cada una</span></div>'
s4 += tiles([('collagen', pf('Colágeno · 210 g', '$18.900')),
             ('ena_prot_vain', pf('ENA Whey 907 g', '$66.900')),
             ('whey_star_2lb_vainilla', pf('Star Whey 2 lb', '$81.900'))], 510, 292, 380).replace('class="tiles"', 'class="tiles t4"')
s4 += '<div class="claim" style="top:1028px">Whey: la proteína contribuye a aumentar y mantener la masa muscular. Precios por transferencia o efectivo.</div>'
s4 += f'<div class="btn" style="left:80px;top:1112px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s4 += f'<div style="position:absolute;left:80px;top:1207px;font-size:23px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8">{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">11 2178-9431</span> · SOLO MENSAJES</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/colageno'))
