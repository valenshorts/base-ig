"""Post 19:30 · 19/11/2026 · familia PRODUCTOS (jueves, producto destacado con precio): Omega 3 ENA 60 caps.
3 slides 1080×1350: producto grande con precio → ¿ENA o Gold? (cápsulas por envase y precio) → qué mirar en la etiqueta + cómo pedir.
Precios: kit/README.md (transferencia o efectivo). Sin claims de salud del omega 3 (el README no tiene frase aprobada):
solo datos de envase y precio. No se compara «precio por cápsula» porque la dosis por cápsula puede no ser la misma."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.hero{position:absolute;left:80px;right:80px;border:2px solid var(--line);background:radial-gradient(circle 330px at 50% 46%,rgba(198,244,50,.12),transparent 100%),radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);display:flex;align-items:center;justify-content:center}
.hero img{position:relative;filter:drop-shadow(0 26px 34px rgba(0,0,0,.6))}
.hero .sv{position:absolute;right:-2px;top:-2px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:34px;padding:12px 22px 14px}
.pr{position:absolute;left:80px;right:80px;display:flex;align-items:flex-end;justify-content:space-between;gap:20px}
.pr .nm{font-family:'Archivo Black';font-size:54px;text-transform:uppercase;line-height:1}
.pr .nm small{display:block;font-family:Montserrat;font-weight:700;font-size:26px;color:#bdbdc0;text-transform:none;margin-top:10px;letter-spacing:0}
.pr .p{font-family:'Archivo Black';font-size:104px;line-height:.9;color:var(--l);white-space:nowrap}
.fine{position:absolute;left:80px;right:80px;font-size:24px;line-height:1.35;color:#bdbdc0;font-weight:600}
.vs .tile .ph img{max-height:80%}
.vs .tile .ft .b{font-size:24px}
.vs .tile .ft .p{font-size:58px}
.vs .tile .cat{font-size:26px}
.badge{position:absolute;z-index:3;background:var(--bk);border:3px solid var(--l);color:var(--w);font-family:'Archivo Black';font-size:40px;padding:6px 18px 10px;line-height:1}
.badge small{display:block;font-family:Montserrat;font-weight:800;font-size:18px;letter-spacing:2px;color:var(--l)}
.chk{position:absolute;left:80px;right:80px;display:flex;flex-direction:column;gap:18px}
.chk div{height:150px;display:flex;align-items:center;gap:30px;background:var(--panel);border:2px solid var(--line);padding:0 32px}
.chk .e{font-size:76px;flex:0 0 90px;text-align:center}
.chk b{display:block;font-size:36px;font-weight:900;text-transform:uppercase;line-height:1.05}
.chk p{font-size:25px;font-weight:600;color:#bdbdc0;margin-top:6px;line-height:1.3}
.pay{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:22px;border:2px solid var(--l);background:linear-gradient(160deg,rgba(198,244,50,.13),var(--panel) 70%);padding:20px 28px;font-size:28px;font-weight:700;color:#d6d6d8;line-height:1.3}
.pay .e{font-size:56px}.pay b{color:#fff;font-weight:900}
.wa{position:absolute;left:80px;right:80px;font-size:25px;font-weight:800;letter-spacing:.5px;color:#d6d6d8}.wa span{color:var(--l)}
</style>'''

# 1 · PRODUCTO DESTACADO: foto grande (más de media slide) + precio grande
s1 = ST + '<div class="eb" style="top:190px">Producto destacado</div>'
s1 += '<div class="t" style="top:240px;font-size:84px">Omega 3 <span class="box">ENA</span></div>'
s1 += '<div class="hero" style="top:360px;height:620px"><img src="assets/ena_omega3.png" style="height:520px"><div class="sv">60 CÁPSULAS</div></div>'
s1 += '<div class="pr" style="top:1010px"><div class="nm">Omega 3 ENA<small>60 cápsulas blandas</small></div><div class="p">$27.900</div></div>'
s1 += f'<div class="fine" style="top:1132px;right:420px">Precio por transferencia o efectivo.<br>Más opciones en el catálogo · link en la bio {E("🛒",24)}</div>'

# 2 · ¿ENA O GOLD? dos tiles con cápsulas por envase y precio (sin «precio por cápsula»)
s2 = ST + '<div class="eb" style="top:190px">¿Cuál te llevás?</div>'
s2 += '<div class="t" style="top:240px;font-size:76px">¿ENA o <span class="box">Gold?</span></div>'
s2 += (tiles([('ena_omega3', pf('Omega 3 ENA', '$27.900') + cf('60 cápsulas')),
              ('gold_omega3', pf('Omega 3 Gold', '$28.900') + cf('30 cápsulas'))], 400, 430, 470, 32)
       .replace('class="tiles"', 'class="tiles vs"'))
s2 += '<div class="txt" style="top:1080px;font-size:30px">Las dos son <b>cápsulas de omega 3</b>. Antes de elegir, mirá en la etiqueta <em>cuántas cápsulas es la porción</em>.</div>'

# 3 · QUÉ MIRAR EN LA ETIQUETA + CÓMO PEDIR
s3 = ST + '<div class="eb" style="top:190px">Antes de comprar</div>'
s3 += '<div class="t" style="top:240px;font-size:72px">Qué mirar en<br>la <span class="box">etiqueta</span></div>'
s3 += ('<div class="chk" style="top:470px">'
       f'<div>{E("🐟")}<span><b>EPA y DHA</b><p>Son los omega 3 del pescado: fijate cuántos mg trae la porción.</p></span></div>'
       f'<div>{E("💊")}<span><b>La porción</b><p>Cuántas cápsulas por día indica el envase.</p></span></div>'
       f'<div><span class="e" style="flex:0 0 90px;display:flex;justify-content:center"><svg viewBox="0 0 80 100" width="70" height="88"><rect x="18" y="4" width="44" height="16" fill="#d6d6d8"/><rect x="10" y="22" width="60" height="74" fill="#fff"/><rect x="10" y="44" width="60" height="26" fill="#C6F432"/><ellipse cx="32" cy="57" rx="9" ry="6" fill="#E8A317"/><ellipse cx="50" cy="57" rx="9" ry="6" fill="#E8A317"/></svg></span><span><b>Cápsulas por envase</b><p>Así sabés para cuántos días te alcanza.</p></span></div></div>')
s3 += f'<div class="pay" style="top:986px">{E("💵")}<div>Precios con <b>10 % OFF</b> por transferencia o efectivo.</div></div>'
s3 += f'<div class="btn" style="left:80px;top:1112px;font-size:27px">{E("🛒",27)} PEDÍ EL TUYO · LINK EN LA BIO {ARROW}</div>'
s3 += f'<div class="wa" style="top:1212px">{E("💬",24)} WHATSAPP <span>{WA}</span> · SOLO MENSAJES</div>'

print(render([page(1, s1, True, 3), page(2, s2, True, 3), page(3, s3, False, 3)], f'{OUT}/omega_ena'))
