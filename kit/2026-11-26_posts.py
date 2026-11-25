"""26/11/2026 · post1 13:00 [EDUCA] error común «¿100 g de fideos = 13 g de proteína?» (crudo vs cocido)
· post2 19:30 [PRODUCTOS] producto destacado MyProtein Impact Whey 1 kg.
Datos (USDA FoodData Central, SR Legacy, cada 100 g): spaghetti seco enriquecido 13,04 g / cocido 5,80 g;
arroz blanco grano largo crudo 7,13 g / cocido 2,69 g; pechuga de pollo cruda 22,5 g / asada 31,02 g.
Precio: kit/README.md (transferencia o efectivo). Frase de proteína permitida (EFSA)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

ST = '''<style>
.ring{position:absolute;left:80px;right:80px;height:480px;background:radial-gradient(ellipse at 50% 55%,#2c2c30 0%,#17171a 60%,#0f0f11 100%);border:2px solid var(--line);display:flex;align-items:center;justify-content:center;gap:60px}
.ring .e{font-size:230px;filter:drop-shadow(0 20px 26px rgba(0,0,0,.55))}
.ring .lab{position:absolute;left:-2px;top:-2px;background:var(--l);color:var(--bk);font-weight:900;font-size:26px;letter-spacing:3px;padding:10px 18px}
.ring .q{width:170px;height:170px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:120px;display:flex;align-items:center;justify-content:center;transform:rotate(-6deg);box-shadow:0 18px 40px rgba(0,0,0,.5)}
.mv{position:absolute;left:80px;right:80px;display:flex;gap:28px}
.mv div{flex:1;height:100px;border:3px solid #4a4a4e;display:flex;align-items:center;justify-content:center;font-family:'Archivo Black';font-size:50px;letter-spacing:2px}
.big{position:absolute;left:80px;font-family:'Archivo Black';font-size:120px;line-height:1;text-transform:uppercase;letter-spacing:-2px}
.big span{background:var(--l);color:var(--bk);padding:0 24px 8px;display:inline-block}
.row{position:absolute;left:80px;right:80px;height:250px;display:flex;align-items:stretch;border:2px solid var(--line);background:var(--panel)}
.row .ic{flex:0 0 190px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-right:2px solid var(--line)}
.row .ic .e{font-size:100px}
.row .ic b{font-size:24px;font-weight:900;letter-spacing:2px;text-transform:uppercase}
.row .c{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px}
.row .c small{font-size:24px;font-weight:800;letter-spacing:3px;color:#a9a9ad;text-transform:uppercase}
.row .c b{font-family:'Archivo Black';font-weight:400;font-size:84px;line-height:1}
.row .c b i{font-style:normal;font-family:Montserrat;font-weight:800;font-size:34px;margin-left:6px;color:#a9a9ad}
.row .ar{flex:0 0 70px;display:flex;align-items:center;justify-content:center;font-size:56px;color:#6a6a6e;font-weight:900}
.row .c.on b{color:var(--l)}
.chipb{position:absolute;right:80px;border:3px solid var(--l);color:var(--l);font-weight:900;font-size:24px;letter-spacing:2px;padding:8px 14px}
.src{position:absolute;left:80px;right:80px;font-size:23px;font-weight:600;color:#a9a9ad;line-height:1.4}.src b{color:#fff}
.why{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:26px;background:linear-gradient(160deg,rgba(198,244,50,.13),var(--panel) 70%);border:2px solid var(--l);padding:22px 28px}
.why .e{font-size:76px}
.why p{font-size:30px;font-weight:700;line-height:1.3;color:#d6d6d8}.why p b{color:#fff;font-weight:900}
.st{position:absolute;left:80px;right:80px;display:flex;gap:28px;align-items:center;height:170px;border:2px solid var(--line);background:var(--panel);padding:0 30px}
.st .e{font-size:84px;flex:0 0 100px;text-align:center}
.st p{font-size:28px;font-weight:600;line-height:1.28;color:#d6d6d8}.st p b{display:block;color:#fff;font-weight:900;font-size:34px;text-transform:uppercase;margin-bottom:4px}
.st p em{font-style:normal;color:var(--l);font-weight:800}
.cta{position:absolute;left:80px;right:80px;font-size:31px;font-weight:800;line-height:1.35}.cta span{color:var(--l)}
.hero{position:absolute;left:80px;right:80px;height:560px;border:2px solid var(--line);background:radial-gradient(circle 330px at 50% 46%,rgba(198,244,50,.12),transparent 100%),radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);display:flex;align-items:center;justify-content:center}
.hero:after{content:'';position:absolute;left:50%;bottom:7%;width:46%;height:30px;transform:translateX(-50%);border-radius:50%;background:rgba(0,0,0,.5);filter:blur(18px)}
.hero img{position:relative;z-index:1;height:470px;filter:drop-shadow(0 26px 34px rgba(0,0,0,.6))}
.hero .sv{position:absolute;right:-2px;top:-2px;z-index:2;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:34px;padding:12px 22px 14px}
.pr{position:absolute;left:80px;right:80px;display:flex;align-items:flex-end;justify-content:space-between}
.pr .nm{font-family:'Archivo Black';font-size:50px;text-transform:uppercase;line-height:1}
.pr .nm small{display:block;font-family:Montserrat;font-weight:700;font-size:25px;color:#bdbdc0;text-transform:none;margin-top:10px;letter-spacing:0}
.pr .p{font-family:'Archivo Black';font-size:96px;line-height:.9;color:var(--l)}
.fine{position:absolute;left:80px;right:80px;font-size:22px;line-height:1.38;color:#9a9a9e;font-weight:600}
.mini{position:absolute;left:80px;width:300px;height:300px;border:2px solid var(--line);background:radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);display:flex;align-items:center;justify-content:center}
.mini img{height:250px;filter:drop-shadow(0 16px 22px rgba(0,0,0,.6))}
</style>'''

BALANZA = ('<svg viewBox="0 0 120 120" width="{w}" height="{w}"><rect x="38" y="18" width="44" height="8" fill="#d6d6d8"/>'
           '<rect x="56" y="26" width="8" height="18" fill="#9a9a9e"/><rect x="14" y="44" width="92" height="62" fill="#e8e8ea"/>'
           '<rect x="30" y="58" width="60" height="26" fill="#0B0B0C"/><rect x="38" y="66" width="44" height="10" fill="#C6F432"/></svg>')
PECHUGA = ('<svg viewBox="0 0 120 120" width="140" height="140"><path d="M20 70 C14 40 40 18 70 22 C98 26 108 52 98 74 C88 98 52 104 34 94 C26 90 22 82 20 70 Z" fill="#F2C6A8" stroke="#D99A78" stroke-width="4"/>'
           '<path d="M40 54 C55 46 72 46 86 54 M38 70 C55 62 74 62 90 70" stroke="#E0A988" stroke-width="4" fill="none"/></svg>')


def fila(top, emoji, nombre, a_lab, a, b_lab, b, on='b'):
    ca = ' on' if on == 'a' else ''
    cb = ' on' if on == 'b' else ''
    return (f'<div class="row" style="top:{top}px"><div class="ic">{emoji if emoji.startswith("<svg") else E(emoji)}<b>{nombre}</b></div>'
            f'<div class="c{ca}"><small>{a_lab}</small><b>{a}<i>g</i></b></div><div class="ar">→</div>'
            f'<div class="c{cb}"><small>{b_lab}</small><b>{b}<i>g</i></b></div></div>')


# ===== POST 1 · EDUCA: CRUDO VS COCIDO =====
# 1 · Portada: pregunta corta, imagen protagonista, sin adelantar la respuesta
a1 = ST + '<div class="eb" style="top:190px">Error común</div>'
a1 += '<div class="t" style="top:240px;font-size:76px">¿100 g de fideos<br>= 13 g de<br><span class="box">proteína?</span></div>'
a1 += f'<div class="ring" style="top:560px"><div class="lab">LO QUE DICE EL PAQUETE</div>{E("🍝")}<div class="q">?</div></div>'
a1 += '<div class="mv" style="top:1080px"><div>SÍ</div><div>NO</div></div>'

# 2 · Respuesta: depende de cómo los pesás
a2 = ST + '<div class="eb" style="top:190px">La respuesta</div>'
a2 += '<div class="big" style="top:240px">Solo <span>secos</span></div>'
a2 += '<div class="txt" style="top:385px;font-size:33px">El paquete habla del producto <b>seco</b>. En el plato los comés <em>cocidos.</em></div>'
a2 += '<div class="chipb" style="top:500px">CADA 100 g · PROTEÍNA</div>'
a2 += fila(570, '🍝', 'Fideos', 'secos', '13', 'cocidos', '5,8')
a2 += fila(850, '🍚', 'Arroz', 'crudo', '7,1', 'cocido', '2,7')
a2 += '<div class="src" style="top:1135px">Fideos tipo spaghetti y arroz blanco, hervidos sin sal.<br>Fuente: <b>USDA FoodData Central</b>.</div>'

# 3 · El porqué + el giro: con la carne pasa al revés
a3 = ST + '<div class="eb" style="top:190px">¿Por qué?</div>'
a3 += '<div class="t" style="top:240px;font-size:72px">El agua<br><span class="box">cambia el peso</span></div>'
a3 += f'<div class="why" style="top:450px">{E("💧")}<p>Los fideos y el arroz, al hervirlos, <b>absorben agua</b>: pesan más, pero la proteína es la misma. Cada 100 g rinde menos.</p></div>'
a3 += '<div class="txt" style="top:660px;font-size:33px"><b>Con la carne pasa al revés:</b> al cocinarse <em>pierde agua.</em></div>'
a3 += fila(790, PECHUGA, 'Pechuga', 'cruda', '22,5', 'asada', '31')
a3 += '<div class="src" style="top:1070px">Pechuga de pollo sin piel, cada 100 g.<br>Fuente: <b>USDA FoodData Central</b>.</div>'

# 4 · Qué hacer + cierre (guardar / compartir / comentar)
a4 = ST + '<div class="eb" style="top:190px">Cómo no errarle</div>'
a4 += '<div class="t" style="top:240px;font-size:72px">Pesá y leé<br><span class="box">igual</span></div>'
a4 += (f'<div class="st" style="top:450px"><div style="flex:0 0 100px;display:flex;justify-content:center">{BALANZA.format(w=96)}</div><p><b>Pesá en crudo</b>y usá la tabla del <em>paquete.</em></p></div>'
       f'<div class="st" style="top:645px">{E("🍽️")}<p><b>¿Pesás en cocido?</b>Usá valores de alimento <em>cocido.</em></p></div>')
a4 += (f'<div class="cta" style="top:880px">{E("📌",30)} <span>Guardalo</span> para tu próxima comida<br>'
       f'{E("📲",30)} <span>Mandáselo</span> al que cuenta la proteína del plato<br>'
       f'{E("👇",30)} ¿Pesás en crudo o en cocido? <span>Comentá</span></div>')
a4 += f'<div class="btn" style="left:80px;bottom:76px;font-size:27px">{E("🛒",27)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
print(render([page(1, a1, True, 4), page(2, a2, True, 4), page(3, a3, True, 4), page(4, a4, False, 4)], f'{OUT}/post1'))

# ===== POST 2 · PRODUCTOS: MYPROTEIN IMPACT WHEY 1 KG =====
b1 = ST + '<div class="eb" style="top:190px">Producto destacado</div>'
b1 += '<div class="t" style="top:240px;font-size:76px">MyProtein<br><span class="box">Impact Whey</span></div>'
b1 += '<div class="hero" style="top:450px"><img src="assets/mp_whey_brownie.png"><div class="sv">1 KG</div></div>'
b1 += '<div class="pr" style="top:1050px"><div class="nm">Impact Whey<small>Por transferencia o efectivo</small></div><div class="p">$78.900</div></div>'

b2 = ST + '<div class="eb" style="top:190px">¿Cómo la tomás?</div>'
b2 += '<div class="t" style="top:240px;font-size:72px">Tres formas<br><span class="box">fáciles</span></div>'
b2 += (f'<div class="st" style="top:450px">{E("🥛")}<p><b>En shake</b>Con agua o con leche, como más te guste.</p></div>'
       f'<div class="st" style="top:645px">{E("🥣")}<p><b>En la avena</b>Mezclala con la avena del desayuno.</p></div>'
       f'<div class="st" style="top:840px">{E("🥞")}<p><b>En panqueques</b>Sumala a la mezcla antes de cocinar.</p></div>')
b2 += '<div class="fine" style="top:1060px">Respetá la porción que indica la etiqueta. La proteína contribuye a aumentar y mantener la masa muscular.</div>'

b3 = ST + '<div class="eb" style="top:190px">Pedí la tuya</div>'
b3 += '<div class="t" style="top:240px;font-size:72px">Así la<br><span class="box">pedís</span></div>'
b3 += '<div class="mini" style="top:450px"><img src="assets/mp_whey_brownie.png"></div>'
b3 += ('<div style="position:absolute;left:410px;right:80px;top:470px"><div style="font-family:\'Archivo Black\';font-size:40px;text-transform:uppercase;line-height:1.05">MyProtein<br>Impact Whey 1 kg</div>'
       '<div style="font-family:\'Archivo Black\';font-size:84px;color:var(--l);margin-top:18px;line-height:1">$78.900</div>'
       '<div style="font-size:24px;font-weight:700;color:#bdbdc0;margin-top:10px">por transferencia o efectivo</div></div>')
b3 += (f'<div class="st" style="top:790px;height:140px">{E("💬")}<p><b>Por WhatsApp</b><em>10% OFF</em> pagando por transferencia o efectivo.</p></div>'
       f'<div class="st" style="top:950px;height:140px">{E("💳")}<p><b>Online en la web</b>Con <em>Mercado Pago</em>, a precio de lista.</p></div>')
b3 += '<div class="fine" style="top:1110px">Envíos a todo el país, a cargo de quien compra. WhatsApp 11 2178-9431, solo mensajes.</div>'
b3 += f'<div class="btn" style="left:80px;bottom:76px;font-size:27px">{E("🛒",27)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
print(render([page(1, b1, True, 3), page(2, b2, True, 3), page(3, b3, False, 3)], f'{OUT}/post2'))
