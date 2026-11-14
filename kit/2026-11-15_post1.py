"""Mito o verdad: ¿la chía tiene el mismo omega 3 que el pescado? (3 slides 1080×1350) · 15/11/2026 13:00."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

# Semillas de chía en un bol (no hay emoji fiel): SVG plano
CHIA = '''<svg viewBox="0 0 140 110" width="{s}" height="{h}">
<path d="M14 50 h112 a56 50 0 0 1 -112 0z" fill="#E9E4D8"/><path d="M14 50 h112 a56 50 0 0 1 -6 22 h-100 a56 50 0 0 1 -6 -22z" fill="#D7D0C0"/>
<path d="M20 51 q50 -40 100 0z" fill="#4A4642"/>
<g fill="#1E1C1B"><ellipse cx="42" cy="44" rx="3.2" ry="2.2"/><ellipse cx="55" cy="37" rx="3.2" ry="2.2"/><ellipse cx="70" cy="33" rx="3.2" ry="2.2"/><ellipse cx="86" cy="37" rx="3.2" ry="2.2"/><ellipse cx="99" cy="44" rx="3.2" ry="2.2"/><ellipse cx="63" cy="44" rx="3.2" ry="2.2"/><ellipse cx="80" cy="45" rx="3.2" ry="2.2"/><ellipse cx="32" cy="48" rx="3" ry="2"/><ellipse cx="108" cy="48" rx="3" ry="2"/></g>
<g fill="#A8A197"><ellipse cx="48" cy="40" rx="3" ry="2"/><ellipse cx="62" cy="38" rx="3" ry="2"/><ellipse cx="77" cy="39" rx="3" ry="2"/><ellipse cx="92" cy="42" rx="3" ry="2"/><ellipse cx="71" cy="46" rx="3" ry="2"/><ellipse cx="52" cy="47" rx="3" ry="2"/><ellipse cx="90" cy="48" rx="3" ry="2"/></g>
</svg>'''
chia = lambda s: CHIA.format(s=s, h=int(s * 110 / 140))

ST = '''<style>
.vs{position:absolute;left:80px;right:80px;height:400px;display:flex;align-items:center;justify-content:center;gap:28px}
.vs .bx{width:360px;height:400px;display:flex;flex-direction:column}
.vs .bx .ph{flex:1;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);display:flex;align-items:center;justify-content:center}
.vs .bx .ph .e{font-size:150px;filter:drop-shadow(0 16px 22px rgba(0,0,0,.6))}
.vs .bx .ph svg{filter:drop-shadow(0 16px 22px rgba(0,0,0,.6))}
.vs .bx .nm{height:84px;background:var(--panel2);display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:900;letter-spacing:1px;text-transform:uppercase;color:var(--w)}
.vs .op{font-family:'Archivo Black';font-size:96px;color:var(--l)}
.mv{position:absolute;left:80px;right:80px;display:flex;gap:28px}
.mv div{flex:1;height:120px;border:3px solid #3a3a3d;display:flex;align-items:center;justify-content:center;font-family:'Archivo Black';font-size:52px;letter-spacing:1px}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.2}.cta span{color:var(--l)}
.ans{position:absolute;right:80px;top:200px;width:300px;height:150px;background:var(--l);color:var(--bk);display:flex;align-items:center;justify-content:center;font-family:'Archivo Black';font-size:72px}
.two{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:24px}
.two .c{height:400px;display:flex;flex-direction:column}
.two .c .ph{height:200px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);display:flex;align-items:center;justify-content:center;border-bottom:2px solid var(--line)}
.two .c .ph .e{font-size:120px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.two .c .bd{flex:1;padding:18px 24px}
.two .c .bd b{display:block;font-family:'Archivo Black';font-weight:400;font-size:46px;line-height:1.05;color:var(--l)}
.two .c .bd p{font-size:24px;font-weight:600;line-height:1.32;color:#d6d6d8;margin-top:8px}
.pt{position:absolute;left:80px;right:80px;display:flex;gap:28px;align-items:center}
.pt .k{flex:0 0 104px;height:104px;background:var(--panel);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.pt .k .e{font-size:58px}
.pt .n{font-size:28px;font-weight:500;line-height:1.34;color:#d6d6d8}.pt .n b{color:#fff;font-weight:800}.pt .n em{font-style:normal;color:var(--l);font-weight:700}
.tip{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:24px;background:var(--panel);border:2px solid var(--l);padding:18px 24px}
.tip .e{font-size:56px}
.tip p{font-size:25px;font-weight:600;line-height:1.32;color:#d6d6d8}.tip p b{color:#fff;font-weight:900}
.t3 .tile .ph img{max-height:80%}
</style>'''

# 1 · PREGUNTA (sin adelantar la respuesta)
s1 = ST + '<div class="eb" style="top:200px">Mito o verdad</div>'
s1 += '<div class="t" style="top:250px;font-size:74px">¿La chía tiene<br>el mismo omega 3<br><span class="box">que el pescado?</span></div>'
s1 += f'''<div class="vs" style="top:560px">
 <div class="bx panel" style="position:relative"><div class="ph">{chia(230)}</div><div class="nm">Semillas de chía</div></div>
 <div class="op">=</div>
 <div class="bx panel" style="position:relative"><div class="ph">{E("🐟")}</div><div class="nm">Pescado</div></div></div>'''
s1 += '<div class="mv" style="top:1000px"><div>MITO</div><div>VERDAD</div></div>'
s1 += f'<div class="cta" style="top:1196px">Comentá <span>MITO</span> o <span>VERDAD</span> {E("👇",30)}</div>'

# 2 · RESPUESTA
s2 = ST + '<div class="eb" style="top:200px">La respuesta</div>'
s2 += '<div class="ans">MITO</div>'
s2 += '<div class="t" style="top:250px;right:400px;font-size:62px">Hay varios<br>tipos de<br><span class="box">omega 3</span></div>'
s2 += f'''<div class="two" style="top:520px">
 <div class="c panel" style="position:relative"><div class="ph">{chia(190)}</div><div class="bd"><b>ALA</b><p>El omega 3 de las plantas: <b style="display:inline;font:inherit;color:#fff;font-weight:800">chía, lino, nueces.</b></p></div></div>
 <div class="c panel" style="position:relative"><div class="ph">{E("🐟")}</div><div class="bd"><b>EPA y DHA</b><p>Los de los pescados grasos: <b style="display:inline;font:inherit;color:#fff;font-weight:800">salmón, caballa, sardina.</b></p></div></div></div>'''
s2 += f'<div class="pt" style="top:950px"><div class="k">{E("🔄")}</div><div class="n">El cuerpo convierte <b>solo una parte chica del ALA en EPA</b>, y todavía menos en DHA. <em>No son intercambiables.</em></div></div>'
s2 += f'<div class="cta" style="top:1196px;font-size:29px">¿Y en cápsulas? <span>Deslizá</span> {E("👉",29)}</div>'

# 3 · VENTA
s3 = ST + '<div class="eb" style="top:200px">Omega 3 en cápsulas</div>'
s3 += '<div class="t" style="top:250px;font-size:80px">Mirá el<br><span class="box">EPA y el DHA</span></div>'
s3 += tiles([('ena_omega3', pf('Omega 3 ENA · 60 caps', '$27.900')),
             ('gold_omega3', pf('Omega 3 Gold · 30 caps', '$28.900'))], 500, 420, 330, 28).replace('class="tiles"', 'class="tiles t3"')
s3 += f'<div class="tip" style="top:960px">{E("🔍")}<p><b>En la etiqueta:</b> cuánto EPA + DHA trae cada porción y cuántas cápsulas son una porción. Precios por transferencia o efectivo.</p></div>'
s3 += f'<div class="btn" style="left:80px;top:1112px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s3 += f'<div style="position:absolute;left:80px;top:1207px;font-size:23px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8">{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">11 2178-9431</span> · SOLO MENSAJES</div>'

print(render([page(1, s1, True, 3), page(2, s2, True, 3), page(3, s3, False, 3)], f'{OUT}/omega'))
