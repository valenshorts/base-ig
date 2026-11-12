import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.eq{position:absolute;left:80px;right:80px;display:flex;align-items:center;justify-content:space-between}
.eq .op{font-family:'Archivo Black';font-size:72px;color:var(--l)}
.eq .bx{width:250px;height:290px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px}
.eq .bx .lb{font-size:22px;font-weight:800;letter-spacing:3px;color:#a9a9ad;text-transform:uppercase}
.eq .ph{width:250px;height:290px;border:2px solid var(--line);background:radial-gradient(circle 150px at 50% 45%,rgba(198,244,50,.08),transparent 100%),radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);display:flex;align-items:center;justify-content:center}
.eq .ph img{max-height:82%;max-width:82%;filter:drop-shadow(0 18px 24px rgba(0,0,0,.6))}
.eq .qm{background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:150px}
.q{position:absolute;left:80px;right:80px;font-size:50px;font-weight:900;line-height:1.1;text-transform:uppercase;letter-spacing:-1px}
.q .hl{color:var(--l)}
.vs{position:absolute;left:80px;right:80px;display:flex;gap:30px}
.vs div{flex:1;height:124px;display:flex;align-items:center;justify-content:center;gap:18px;font-family:'Archivo Black';font-size:56px;border:3px solid var(--l)}
.vs .e{font-size:50px}
.egg{position:absolute;left:80px;right:80px;height:250px;display:flex;align-items:center;justify-content:center;gap:40px}
.egg .c{text-align:center}.egg .c .e{font-size:120px}
.egg .c div{font-size:24px;font-weight:800;letter-spacing:3px;margin-top:14px;color:#d6d6d8}
.egg .ar{font-family:'Archivo Black';font-size:90px;color:var(--l)}
.egg .rs{border-left:2px solid var(--line);padding-left:40px;font-size:29px;white-space:nowrap;font-weight:800;line-height:1.25;text-transform:uppercase}
.egg .rs span{color:var(--l)}
.pt{position:absolute;left:80px;right:80px;display:flex;gap:30px;align-items:center}
.pt .k{flex:0 0 100px;height:100px;background:var(--panel);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.pt .k .e{font-size:56px}
.pt .n{font-size:30px;font-weight:500;line-height:1.36;color:#d6d6d8}.pt .n b{color:#fff;font-weight:800}.pt .n em{font-style:normal;color:var(--l);font-weight:700}
.rc{position:absolute;left:80px;right:80px;height:190px;display:flex;align-items:center;gap:30px;padding:0 30px 0 0}
.rc .ic{flex:0 0 190px;height:186px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-right:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.rc .ic .e{font-size:104px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.rc .nm{font-size:35px;font-weight:900;text-transform:uppercase;letter-spacing:-.5px}
.rc .tm{display:inline-block;font-size:19px;font-weight:800;letter-spacing:2.5px;color:var(--bk);background:var(--l);padding:4px 10px;margin-left:12px;vertical-align:6px}
.rc .in{font-size:25px;font-weight:600;color:#d6d6d8;line-height:1.36;margin-top:10px}
.rc .in b{color:var(--l);font-weight:800}
.claim{position:absolute;left:80px;right:80px;font-size:23px;line-height:1.35;color:#bdbdc0;font-weight:500}
.chip{position:absolute;left:12px;top:12px;z-index:2;background:var(--bk);border:2px solid var(--l);color:var(--w);font-size:19px;font-weight:800;letter-spacing:1.5px;padding:6px 10px;display:flex;align-items:center;gap:8px}
.chip .e{font-size:22px}
.t4 .tile .ph img{max-height:72%;margin-top:44px}
</style>'''
# E() viene de lib.py

# 1 · PREGUNTA
s1 = ST + '<div class="eb" style="top:200px">Mito o verdad</div>'
s1 += '<div class="t" style="top:250px;font-size:88px">¿La whey se<br><span class="box">puede cocinar?</span></div>'
s1 += f'''<div class="eq" style="top:510px">
 <div class="ph"><img src="assets/ena_prot_vain.png"></div><div class="op">+</div>
 <div class="bx panel" style="position:relative">{E("🔥",130)}<div class="lb">Calor</div></div><div class="op">=</div>
 <div class="bx qm">?</div></div>'''
s1 += '<div class="q" style="top:850px">“Si la calentás, <span class="hl">pierde<br>la proteína</span> y no sirve más.”</div>'
s1 += f'<div class="vs" style="top:1000px"><div>{E("🙅")} MITO</div><div>{E("🙋")} VERDAD</div></div>'
s1 += f'<div style="position:absolute;left:80px;top:1205px;font-size:31px;font-weight:800;line-height:1.2">Comentá <span style="color:var(--l)">MITO o VERDAD</span> {E("👇",30)}</div>'

# 2 · RESPUESTA
s2 = ST + '<div class="eb" style="top:200px">La respuesta</div>'
s2 += '<div class="t" style="top:250px;font-size:100px">Es mito.<br><span class="box">Se puede</span></div>'
s2 += f'''<div class="egg panel" style="top:525px">
 <div class="c">{E("🥚")}<div>CRUDO</div></div><div class="ar">→</div><div class="c">{E("🍳")}<div>COCIDO</div></div>
 <div class="rs">Cambia la forma.<br><span>La proteína<br>sigue ahí.</span></div></div>'''
pts = [('🔥', '<b>El calor “desnaturaliza”</b> la proteína: cambia su forma, pero <em>los aminoácidos siguen estando.</em>'),
       ('⚠️', '<b>El truco:</b> no la tires en líquido hirviendo porque se hacen grumos. <em>Mezclala tibia o en la masa.</em>')]
top = 820
for k, t in pts:
    s2 += f'<div class="pt" style="top:{top}px"><div class="k">{E(k)}</div><div class="n">{t}</div></div>'
    top += 150
s2 += f'<div style="position:absolute;left:80px;top:1125px;font-size:31px;font-weight:800">Deslizá y probá <span style="color:var(--l)">3 recetas</span> {E("👉",30)}</div>'

MUG = '''<svg viewBox="0 0 120 120" width="150" height="150" style="filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))">
<path d="M44 8c-4 6 4 9 0 15M60 2c-4 7 4 11 0 18M76 8c-4 6 4 9 0 15" fill="none" stroke="#bdbdc0" stroke-width="3.5" stroke-linecap="round" opacity=".8"/>
<path d="M84 56h8a14 14 0 0 1 0 28h-8" fill="none" stroke="#f3f2ed" stroke-width="8"/>
<path d="M22 52h66v40a14 14 0 0 1-14 14H36a14 14 0 0 1-14-14z" fill="#f3f2ed"/>
<path d="M22 52h66v10H22z" fill="#d9d8d2"/>
<path d="M17 56c0-18 12-26 38-26s38 8 38 26c0 4-4 6-9 6H26c-5 0-9-2-9-6z" fill="#5a3320"/>
<path d="M27 46c6-7 16-10 28-10" fill="none" stroke="#7a4a2e" stroke-width="4" stroke-linecap="round"/>
<circle cx="44" cy="49" r="2.6" fill="#2e1a10"/><circle cx="62" cy="46" r="2.6" fill="#2e1a10"/><circle cx="74" cy="51" r="2.6" fill="#2e1a10"/>
<rect x="38" y="74" width="34" height="5" fill="#C6F432"/></svg>'''
# 3 · RECETAS
s3 = ST + '<div class="eb" style="top:200px">Recetas con whey</div>'
s3 += '<div class="t" style="top:250px;font-size:92px">3 ideas<br><span class="box">en 5 minutos</span></div>'
rcs = [('🥞', 'Panqueques', 'SARTÉN', '1 banana pisada + 2 huevos + <b>1 scoop de whey vainilla</b> + canela. Vuelta y vuelta.'),
       ('MUG', 'Brownie en taza', 'MICRO', '<b>1 scoop de whey chocolate</b> + 1 huevo + 1 cda de cacao + 2 cdas de leche. 60 a 90 seg.'),
       ('🥣', 'Avena proteica', 'OLLA', 'Cociná la avena, sacala del fuego, esperá 1 minuto y sumá <b>1 scoop de whey</b>.')]
top = 530
for em, nm, tm, ing in rcs:
    s3 += f'<div class="rc panel" style="top:{top}px"><div class="ic">{MUG if em == 'MUG' else E(em)}</div><div><div class="nm">{nm}<span class="tm">{tm}</span></div><div class="in">{ing}</div></div></div>'
    top += 215
s3 += f'<div style="position:absolute;left:80px;top:1205px;font-size:28px;font-weight:800">Guardalo para después {E("📌",28)}</div>'

# 4 · VENTA
def tile(f, chip, ft):
    return f'<div class="tile"><div class="ph"><div class="chip">{chip}</div><img src="assets/{f}.png"></div>{ft}</div>'
s4 = ST + '<div class="eb" style="top:200px">Para tus recetas</div>'
s4 += f'<div class="t" style="top:250px;font-size:92px">Vainilla {E("🍦",80)} o<br><span class="box">chocolate {E("🍫",80)}</span></div>'
s4 += ('<div class="tiles t4" style="top:545px;--w:292px;--h:330px;--g:22px">'
       + tile('ena_prot_vain', f'{E("🍦")} VAINILLA', pf('ENA · 907 g', '$66.900'))
       + tile('mp_whey_brownie', f'{E("🍫")} BROWNIE', pf('MyProtein · 1 kg', '$78.900'))
       + tile('on_gs_choc', f'{E("🍫")} CHOCOLATE', pf('ON · 310 g', '$60.900')) + '</div>')
s4 += '<div class="claim" style="top:1028px">La proteína contribuye a aumentar y mantener la masa muscular. Precios por transferencia o efectivo.</div>'
s4 += f'<div class="btn" style="left:80px;top:1112px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s4 += f'<div style="position:absolute;left:80px;top:1207px;font-size:23px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8">{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">11 2178-9431</span> · SOLO MENSAJES</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/whey_cocinar'))
