import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.op4{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:26px}
.op4 .o{position:relative;height:262px;background:var(--panel);border:2px solid var(--line);display:flex;align-items:center;gap:22px;padding:0 24px 0 0}
.op4 .o .ph{flex:0 0 190px;height:258px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-right:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.op4 .o .ph .e{font-size:112px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.op4 .o .lt{position:absolute;left:0;top:0;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:34px;width:56px;height:56px;display:flex;align-items:center;justify-content:center}
.op4 .o .nm{font-size:33px;font-weight:900;text-transform:uppercase;line-height:1.05;letter-spacing:-.5px}
.op4 .o .nm small{display:block;font-size:21px;font-weight:700;letter-spacing:2px;color:#a9a9ad;margin-top:10px}
.rk{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:24px;height:116px}
.rk .k{flex:0 0 116px;height:116px;background:var(--panel);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.rk .k .e{font-size:66px}
.rk .bw{flex:1}
.rk .nm{font-size:27px;font-weight:800;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;display:flex;justify-content:space-between}
.rk .nm b{font-family:'Archivo Black';font-weight:400;font-size:34px;letter-spacing:0}
.rk .bar{height:28px;background:#2a2a2d}.rk .bar i{display:block;height:100%;background:#6b6b70}
.rk.win .k{border-color:var(--l)} .rk.win .bar i{background:var(--l)} .rk.win .nm b{color:var(--l)}
.src{position:absolute;left:80px;right:80px;font-size:21px;font-weight:600;color:#8b8b8f;letter-spacing:.5px}
.cc{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:24px}
.cc .c{height:224px;background:var(--panel);border:2px solid var(--line);padding:22px 24px;display:flex;flex-direction:column;justify-content:space-between}
.cc .c.on{border-color:var(--l);background:linear-gradient(160deg,rgba(198,244,50,.13),var(--panel) 70%)}
.cc .c .top{display:flex;align-items:center;gap:16px}
.cc .c .top .e{font-size:66px}
.cc .c .q{font-size:26px;font-weight:800;line-height:1.15;text-transform:uppercase}
.cc .c .kc{font-family:'Archivo Black';font-size:58px;line-height:1}
.cc .c .kc small{font-family:Montserrat;font-weight:800;font-size:24px;letter-spacing:2px;margin-left:8px;color:#a9a9ad}
.cc .c.on .kc{color:var(--l)}
.chip{position:absolute;left:12px;top:12px;z-index:2;background:var(--bk);border:2px solid var(--l);color:var(--w);font-size:18px;font-weight:800;letter-spacing:1.5px;padding:6px 10px;display:flex;align-items:center;gap:8px}
.chip .e{font-size:20px}
.t4 .tile .ph img{max-height:72%;margin-top:44px}
.claim{position:absolute;left:80px;right:80px;font-size:23px;line-height:1.35;color:#bdbdc0;font-weight:500}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.2}
.cta span{color:var(--l)}
</style>'''

FIL = '''<svg viewBox="0 0 120 90" width="{w}" height="{h}" style="filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))">
<path d="M14 52C8 30 30 10 62 12c30 2 50 18 46 36-4 20-30 32-60 30C30 77 18 66 14 52z" fill="#E7B47A"/>
<path d="M14 52C8 30 30 10 62 12c30 2 50 18 46 36-4 20-30 32-60 30C30 77 18 66 14 52z" fill="none" stroke="#C98B4B" stroke-width="4"/>
<path d="M30 30l16 40M50 20l18 52M72 18l16 48M92 26l10 28" stroke="#8A5527" stroke-width="6" stroke-linecap="round"/>
<path d="M26 40c10-16 28-22 44-22" fill="none" stroke="#F6D3A6" stroke-width="4" stroke-linecap="round" opacity=".8"/></svg>'''
def ic(e, big=True):
    if e == 'FIL': return FIL.format(w=150 if big else 88, h=112 if big else 66)
    return E(e)

# 1 · QUIZ
s1 = ST + '<div class="eb" style="top:200px">Quiz rápido</div>'
s1 += '<div class="t" style="top:250px;font-size:80px">¿Cuál tiene más<br><span class="box">proteína?</span></div>'
s1 += '<div style="position:absolute;left:80px;top:500px;font-size:28px;font-weight:700;letter-spacing:2px;color:#d6d6d8;text-transform:uppercase">Cada 100 gramos de alimento</div>'
ops = [('A','FIL','Pechuga<br>de pollo','COCIDA, SIN PIEL'),('B','🥚','Huevo','ENTERO'),
       ('C','🧀','Queso<br>parmesano','DURO'),('D','🥜','Maní','SIN SAL')]
s1 += '<div class="op4" style="top:570px">' + ''.join(
    f'<div class="o"><div class="ph">{ic(e)}</div><div class="lt">{l}</div><div class="nm">{n}<small>{s}</small></div></div>' for l,e,n,s in ops) + '</div>'
s1 += f'<div class="cta" style="top:1185px">Comentá <span>A, B, C o D</span> {E("👇",30)}</div>'

# 2 · RESPUESTA
s2 = ST + '<div class="eb" style="top:200px">La respuesta</div>'
s2 += f'<div class="t" style="top:250px;font-size:88px">Gana el<br><span class="box">parmesano {E("🧀",76)}</span></div>'
rk = [('🧀','C · Parmesano','35,8 g',35.75,True),('FIL','A · Pechuga de pollo','31 g',31.0,False),
      ('🥜','D · Maní','25,8 g',25.8,False),('🥚','B · Huevo','12,6 g',12.56,False)]
top = 530
for e,n,v,x,w in rk:
    s2 += f'<div class="rk{" win" if w else ""}" style="top:{top}px"><div class="k">{ic(e,False)}</div><div class="bw"><div class="nm">{n}<b>{v}</b></div><div class="bar"><i style="width:{x/35.75*100:.1f}%"></i></div></div></div>'
    top += 142
s2 += '<div class="src" style="top:1100px">Proteína cada 100 g, valores aproximados. Fuente: USDA FoodData Central.</div>'
s2 += f'<div class="cta" style="top:1185px;font-size:29px">Pero hay un detalle {E("👉",30)}</div>'

# 3 · EL DETALLE
s3 = ST + '<div class="eb" style="top:200px">El detalle</div>'
s3 += '<div class="t" style="top:250px;font-size:74px">Para sumar 30 g<br><span class="box">de proteína…</span></div>'
cc = [('FIL','97 g de pechuga','160',True),('🧀','84 g de parmesano','330',False),
      ('🥚','5 huevos','340',False),('🥜','116 g de maní','660',False)]
s3 += '<div class="cc" style="top:500px">' + ''.join(
    f'<div class="c{" on" if o else ""}"><div class="top">{ic(e,False)}<div class="q">{q}</div></div><div class="kc">~{k}<small>KCAL</small></div></div>' for e,q,k,o in cc) + '</div>'
s3 += '<div class="txt" style="top:996px;font-size:31px">No importa solo cuánta proteína tiene: <em>importa con cuántas calorías viene.</em></div>'
s3 += '<div class="src" style="top:1110px">Valores aproximados. Fuente: USDA FoodData Central.</div>'
s3 += f'<div class="cta" style="top:1185px;font-size:29px">Guardalo para después {E("📌",28)}</div>'

# 4 · VENTA
def tile(f, chip, ft):
    return f'<div class="tile"><div class="ph"><div class="chip">{chip}</div><img src="assets/{f}.png"></div>{ft}</div>'
s4 = ST + '<div class="eb" style="top:200px">¿Te cuesta llegar?</div>'
s4 += f'<div class="t" style="top:250px;font-size:84px">Un scoop,<br><span class="box">cero cocina {E("🥤",72)}</span></div>'
s4 += ('<div class="tiles t4" style="top:525px;--w:292px;--h:330px;--g:22px">'
       + tile('ena_prot_vain', f'{E("🍦")} VAINILLA', pf('ENA · 907 g', '$66.900'))
       + tile('whey_star_2lb_vainilla', f'{E("🍦")} VAINILLA', pf('Star · 2 lb', '$81.900'))
       + tile('mp_whey_brownie', f'{E("🍫")} BROWNIE', pf('MyProtein · 1 kg', '$78.900')) + '</div>')
s4 += '<div class="claim" style="top:1010px">La proteína contribuye a aumentar y mantener la masa muscular. Mirá en la etiqueta cuánta aporta cada scoop. Precios por transferencia o efectivo.</div>'
s4 += f'<div class="btn" style="left:80px;top:1112px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s4 += f'<div style="position:absolute;left:80px;top:1207px;font-size:23px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8">{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">11 2178-9431</span> · SOLO MENSAJES</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/proteina_quiz'))
