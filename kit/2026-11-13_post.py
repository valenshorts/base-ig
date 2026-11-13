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
.src{position:absolute;left:80px;right:80px;font-size:24px;font-weight:600;color:#b0b0b4;letter-spacing:.5px}
.cups{position:absolute;left:80px;right:80px;height:220px;display:flex;align-items:center;justify-content:center;gap:22px}
.cups .e{font-size:88px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.cups .eq{font-family:'Archivo Black';font-size:70px;color:var(--l);margin:0 6px}
.cups .mg{font-family:'Archivo Black';font-size:68px;line-height:1;white-space:nowrap}
.cups .mg small{display:block;font-family:Montserrat;font-weight:800;font-size:21px;letter-spacing:2.5px;color:#a9a9ad;margin-top:8px}
.pt{position:absolute;left:80px;right:80px;display:flex;gap:28px;align-items:center}
.pt .k{flex:0 0 104px;height:104px;background:var(--panel);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.pt .k .e{font-size:58px}
.pt .n{font-size:29px;font-weight:500;line-height:1.34;color:#d6d6d8}.pt .n b{color:#fff;font-weight:800}.pt .n em{font-style:normal;color:var(--l);font-weight:700}
.sale{position:absolute;left:80px;right:80px;display:flex;gap:30px}
.sale .tile{flex:0 0 400px}
.sale .tile .ph{height:410px}
.sale .tile .ph img{max-height:72%;margin-top:40px}
.sale .tips{flex:1;display:flex;flex-direction:column;gap:20px}
.sale .tp{flex:1;background:var(--panel);border:2px solid var(--line);display:flex;align-items:center;gap:18px;padding:0 20px}
.sale .tp .e{font-size:58px}
.sale .tp div{font-size:24px;font-weight:600;line-height:1.3;color:#d6d6d8}.sale .tp b{display:block;color:#fff;font-weight:900;text-transform:uppercase;font-size:25px}
.chip{position:absolute;left:12px;top:12px;z-index:2;background:var(--bk);border:2px solid var(--l);color:var(--w);font-size:18px;font-weight:800;letter-spacing:1.5px;padding:6px 10px;display:flex;align-items:center;gap:8px}
.chip .e{font-size:20px}
.claim{position:absolute;left:80px;right:80px;font-size:23px;line-height:1.35;color:#bdbdc0;font-weight:500}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.2}
.cta span{color:var(--l)}
</style>'''

# Taza chica de espresso con plato (no hay emoji que la muestre bien)
ESP = '''<svg viewBox="0 0 120 100" width="{w}" height="{h}" style="filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))">
<path d="M46 10c-4 6 4 9 0 15M62 6c-4 7 4 11 0 18" fill="none" stroke="#bdbdc0" stroke-width="3.5" stroke-linecap="round" opacity=".8"/>
<ellipse cx="58" cy="86" rx="50" ry="9" fill="#d9d8d2"/><ellipse cx="58" cy="84" rx="40" ry="5" fill="#f3f2ed"/>
<path d="M82 46h6a11 11 0 0 1 0 22h-8" fill="none" stroke="#f3f2ed" stroke-width="7"/>
<path d="M30 38h56l-6 34a10 10 0 0 1-10 9H46a10 10 0 0 1-10-9z" fill="#f3f2ed"/>
<ellipse cx="58" cy="38" rx="28" ry="6" fill="#6b3b1f"/><ellipse cx="58" cy="37" rx="22" ry="3.6" fill="#b07a4a"/>
<rect x="44" y="58" width="28" height="5" fill="#C6F432"/></svg>'''
# Taza de té negro con saquito (la tetera no muestra "taza")
TEA = '''<svg viewBox="0 0 120 100" width="{w}" height="{h}" style="filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))">
<path d="M48 8c-4 6 4 9 0 15M64 4c-4 7 4 11 0 18" fill="none" stroke="#bdbdc0" stroke-width="3.5" stroke-linecap="round" opacity=".8"/>
<ellipse cx="56" cy="88" rx="50" ry="8" fill="#d9d8d2"/>
<path d="M86 42h6a13 13 0 0 1 0 26h-8" fill="none" stroke="#f3f2ed" stroke-width="7"/>
<path d="M20 32h72l-6 42a12 12 0 0 1-12 10H38a12 12 0 0 1-12-10z" fill="#f3f2ed"/>
<ellipse cx="56" cy="32" rx="36" ry="7" fill="#8a3b12"/><ellipse cx="56" cy="31" rx="29" ry="4" fill="#b5561f"/>
<path d="M70 30L80 8" stroke="#bdbdc0" stroke-width="2"/><rect x="74" y="0" width="16" height="12" fill="#C6F432"/></svg>'''
def ic(e, big=True):
    if e == 'ESP': return ESP.format(w=150 if big else 92, h=125 if big else 77)
    if e == 'TEA': return TEA.format(w=150 if big else 92, h=125 if big else 77)
    return E(e)

# 1 · QUIZ
s1 = ST + '<div class="eb" style="top:200px">Quiz rápido</div>'
s1 += '<div class="t" style="top:250px;font-size:80px">¿Cuál tiene más<br><span class="box">cafeína?</span></div>'
s1 += '<div style="position:absolute;left:80px;top:500px;font-size:28px;font-weight:700;letter-spacing:2px;color:#d6d6d8;text-transform:uppercase">Una porción de cada uno</div>'
ops = [('A', '☕', 'Café<br>filtrado', 'TAZA<br>240 ML'), ('B', 'ESP', 'Espresso', '1 SHOT<br>30 ML'),
       ('C', 'TEA', 'Té<br>negro', 'TAZA<br>240 ML'), ('D', '🍵', 'Té<br>verde', 'TAZA<br>240 ML')]
s1 += '<div class="op4" style="top:570px">' + ''.join(
    f'<div class="o"><div class="ph">{ic(e)}</div><div class="lt">{l}</div><div class="nm">{n}<small>{s}</small></div></div>' for l, e, n, s in ops) + '</div>'
s1 += f'<div class="cta" style="top:1218px">Comentá <span>A, B, C o D</span> {E("👇",30)}</div>'

# 2 · RESPUESTA
s2 = ST + '<div class="eb" style="top:200px">La respuesta</div>'
s2 += f'<div class="t" style="top:250px;font-size:84px">Gana el café<br><span class="box">filtrado {E("☕",72)}</span></div>'
rk = [('☕', 'A · Café filtrado', '~95 mg', 95, True), ('ESP', 'B · Espresso', '~63 mg', 63, False),
      ('TEA', 'C · Té negro', '~47 mg', 47, False), ('🍵', 'D · Té verde', '~28 mg', 28, False)]
top = 520
for e, n, v, x, w in rk:
    s2 += f'<div class="rk{" win" if w else ""}" style="top:{top}px"><div class="k">{ic(e, False)}</div><div class="bw"><div class="nm">{n}<b>{v}</b></div><div class="bar"><i style="width:{x/95*100:.1f}%"></i></div></div></div>'
    top += 138
s2 += '<div class="txt" style="top:1062px;font-size:29px">El espresso es más concentrado, <em>pero la taza grande trae más en total.</em></div>'
s2 += '<div class="src" style="top:1158px">Valores aproximados. Fuente: USDA FoodData Central.</div>'
s2 += f'<div class="cta" style="top:1220px;font-size:28px">¿Cuánto es mucho? {E("👉",28)}</div>'

# 3 · ¿CUÁNTO ES MUCHO?
s3 = ST + '<div class="eb" style="top:200px">Ojo con la suma</div>'
s3 += '<div class="t" style="top:250px;font-size:80px">¿Cuánto es<br><span class="box">mucho?</span></div>'
s3 += f'<div class="cups panel" style="top:500px">{E("☕")}{E("☕")}{E("☕")}{E("☕")}<div class="eq">≈</div><div class="mg">400 MG<small>POR DÍA</small></div></div>'
pts = [('👤', '<b>Adultos sanos:</b> hasta <em>400 mg por día</em> en total y hasta <em>200 mg de una sola vez.</em>'),
       ('🤰', '<b>Embarazo y lactancia:</b> hasta <em>200 mg por día.</em> Menores: consultá con tu médico.'),
       ('🌙', '<b>A la noche:</b> la cafeína cerca de la hora de dormir puede afectar el sueño en algunas personas.')]
top = 752
for k, t in pts:
    s3 += f'<div class="pt" style="top:{top}px"><div class="k">{E(k)}</div><div class="n">{t}</div></div>'
    top += 124
s3 += '<div class="src" style="top:1150px">Sumá café, mate, té, gaseosas y pre-entreno. Fuente: EFSA 2015.</div>'
s3 += f'<div class="cta" style="top:1220px;font-size:28px">Guardalo para después {E("📌",28)}</div>'

# 4 · VENTA
s4 = ST + '<div class="eb" style="top:200px">¿Usás pre-entreno?</div>'
s4 += f'<div class="t" style="top:250px;font-size:80px">Sumalo a<br><span class="box">la cuenta {E("🧮",68)}</span></div>'
s4 += ('<div class="sale" style="top:500px">'
       f'<div class="tile"><div class="ph"><div class="chip">{E("⚡")} PRE-ENTRENO</div><img src="assets/tnt_dynamite_star.png"></div>{pf("TNT Dynamite Star · 240 g", "$24.900")}</div>'
       '<div class="tips">'
       f'<div class="tp">{E("🏷️")}<div><b>Leé la etiqueta</b>Fijate cuánta cafeína trae cada servicio.</div></div>'
       f'<div class="tp">{E("➕")}<div><b>Sumá el resto</b>Café, mate y gaseosas del día también cuentan.</div></div>'
       f'<div class="tp">{E("🌙")}<div><b>¿Entrenás de noche?</b>Tenelo en cuenta para tu descanso.</div></div>'
       '</div></div>')
s4 += '<div class="claim" style="top:1040px">Seguí el modo de uso del envase. Precio por transferencia o efectivo.</div>'
s4 += f'<div class="btn" style="left:80px;top:1112px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s4 += f'<div style="position:absolute;left:80px;top:1207px;font-size:23px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8">{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">11 2178-9431</span> · SOLO MENSAJES</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/cafeina_quiz'))
