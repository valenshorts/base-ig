"""Sorteo de 3 creatinas (2 Gold + 1 Star) · 14/11 al 27/11/2026.
Genera: post (3 slides 1080×1350) + historia de lanzamiento (1080×1920)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.chip{position:absolute;left:12px;top:12px;z-index:2;background:var(--bk);border:2px solid var(--l);color:var(--w);font-size:22px;font-weight:900;letter-spacing:1.5px;padding:6px 12px;display:flex;align-items:center;gap:8px}
.chip .e{font-size:24px}
.tz .tile .ph img{max-height:76%;margin-top:30px}
.gift{position:absolute;right:80px;top:226px;width:170px;height:170px;display:flex;align-items:center;justify-content:center}
.gift .e{font-size:150px;filter:drop-shadow(0 16px 22px rgba(0,0,0,.55))}
.date{position:absolute;left:80px;right:80px;display:flex;gap:22px}
.date div{flex:1;background:var(--panel);border:2px solid var(--line);padding:18px 22px;display:flex;align-items:center;gap:18px}
.date .e{font-size:54px}
.date b{display:block;font-size:22px;letter-spacing:2px;color:#a9a9ad;font-weight:800;text-transform:uppercase}
.date span{font-family:'Archivo Black';font-size:34px;line-height:1.05;white-space:nowrap}
.date .on{border-color:var(--l)} .date .on span{color:var(--l)}
.st{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:28px;background:var(--panel);border:2px solid var(--line);height:178px;padding-right:26px}
.st .k{flex:0 0 178px;height:174px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-right:2px solid var(--line);display:flex;align-items:center;justify-content:center;position:relative}
.st .k .e{font-size:92px;filter:drop-shadow(0 12px 16px rgba(0,0,0,.55))}
.st .k i{position:absolute;left:0;top:0;width:46px;height:46px;background:var(--l);color:var(--bk);font-style:normal;font-family:'Archivo Black';font-size:28px;display:flex;align-items:center;justify-content:center}
.st .n{font-size:34px;font-weight:900;text-transform:uppercase;line-height:1.08;letter-spacing:-.5px}
.st .n small{display:block;font-size:24px;font-weight:600;text-transform:none;letter-spacing:0;color:#bdbdc0;margin-top:8px;line-height:1.3}
.st .n small b{color:var(--l)}
.tip{position:absolute;left:80px;right:80px;font-size:27px;font-weight:700;line-height:1.35;color:#d6d6d8;border-left:5px solid var(--l);padding-left:22px}
.tip b{color:var(--l)}
.bc{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:22px}
.bc div{background:var(--panel);border:2px solid var(--line);padding:22px 24px;height:190px;display:flex;flex-direction:column;justify-content:space-between}
.bc .e{font-size:62px}
.bc p{font-size:25px;font-weight:600;line-height:1.3;color:#d6d6d8}
.bc p b{color:#fff;font-weight:900;display:block;font-size:27px;text-transform:uppercase;letter-spacing:.5px;margin-bottom:4px}
.fine{position:absolute;left:80px;right:80px;font-size:21px;line-height:1.4;color:#a9a9ad;font-weight:500}
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.2}.cta span{color:var(--l)}
</style>'''

def tile(f, chip, ft):
    return f'<div class="tile"><div class="ph"><div class="chip">{chip}</div><img src="assets/{f}.png"></div>{ft}</div>'

# 1 · ANUNCIO
s1 = ST + '<div class="eb" style="top:200px">Sorteo</div>'
s1 += f'<div class="gift">{E("🎁")}</div>'
s1 += '<div class="t" style="top:250px;right:300px;font-size:86px">Sorteamos<br><span class="box">3 creatinas</span></div>'
s1 += ('<div class="tiles tz" style="top:520px;--w:430px;--h:360px;--g:26px">'
       + tile('creatina_gold_300g', '×2', cf('2 ganadores · Gold 300 g', 24))
       + tile('creatina_star_300g', '×1', cf('1 ganador · Star 300 g', 24)) + '</div>')
s1 += f'''<div class="date" style="top:965px">
 <div>{E("⏳")}<p><b>Participás hasta</b><span>VIE 27/11</span></p></div>
 <div class="on">{E("🚚")}<p><b>Envío gratis</b><span>A TODO EL PAÍS</span></p></div></div>'''
s1 += f'<div class="cta" style="top:1185px">Deslizá y mirá cómo participar {E("👉",30)}</div>'

# 2 · CÓMO PARTICIPAR
s2 = ST + '<div class="eb" style="top:200px">Cómo participar</div>'
s2 += '<div class="t" style="top:250px;font-size:84px">3 pasos<br><span class="box">y ya estás</span></div>'
pasos = [('👤', 'Seguí a @basesuplementos.ar', 'La cuenta tiene que estar siguiéndonos al momento del sorteo.'),
         ('❤️', 'Dale me gusta a este post', 'En este mismo post del sorteo.'),
         ('💬', 'Comentá etiquetando a 2 amigos', 'Cada comentario con <b>2 amigos distintos</b> es una chance más.')]
top = 520
for i, (e, n, d) in enumerate(pasos, 1):
    s2 += f'<div class="st" style="top:{top}px"><div class="k">{E(e)}<i>{i}</i></div><div class="n">{n}<small>{d}</small></div></div>'
    top += 200
s2 += '<div class="tip" style="top:1125px">Etiquetá personas reales: <b>no valen cuentas falsas ni de marcas.</b></div>'

# 3 · FECHAS Y BASES
s3 = ST + '<div class="eb" style="top:200px">Fechas y bases</div>'
s3 += '<div class="t" style="top:250px;font-size:84px">Sorteo en vivo<br><span class="box">sábado 28/11</span></div>'
bases = [('⏳', 'Cierre', 'Viernes 27/11 a las 23:59.'),
         ('🎲', 'Sorteo', 'Al azar, en vivo por historias el sábado 28/11.'),
         ('🚚', 'Envío gratis', 'A todo el país, coordinado por mensaje.'),
         ('🪪', 'Requisitos', 'Mayores de 18 años, con domicilio en Argentina.')]
s3 += '<div class="bc" style="top:520px">' + ''.join(f'<div>{E(e)}<p><b>{t}</b>{d}</p></div>' for e, t, d in bases) + '</div>'
s3 += ('<div class="fine" style="top:960px">Sin obligación de compra. Los ganadores se anuncian el 28/11 y tienen 72 h para responder '
       'por mensaje directo; si no, se sortea un suplente. Este sorteo no está patrocinado, avalado ni administrado por Instagram. '
       'Bases completas en el texto del post.</div>')
s3 += f'<div class="btn" style="left:80px;top:1112px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s3 += f'<div style="position:absolute;left:80px;top:1207px;font-size:23px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8">{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">11 2178-9431</span> · SOLO MENSAJES</div>'

render([page(1, s1, True, 3), page(2, s2, True, 3), page(3, s3, False, 3)], f'{OUT}/sorteo_post')

# HISTORIA DE LANZAMIENTO
h = ST + '<div class="eb" style="top:270px">Sorteo</div>'
h += '<div class="t" style="top:325px;font-size:92px">3 creatinas<br><span class="box">de regalo</span></div>'
h += ('<div class="tiles tz" style="top:600px;--w:430px;--h:420px;--g:26px">'
      + tile('creatina_gold_300g', '×2', cf('Creatina Gold 300 g', 24))
      + tile('creatina_star_300g', '×1', cf('Creatina Star 300 g', 24)) + '</div>')
h += f'<div class="tip" style="top:1150px;font-size:34px">Entrá al <b>último post</b> del perfil y participá: seguí, dale me gusta y etiquetá a 2 amigos {E("👇",34)}</div>'
h += f'''<div class="date" style="top:1400px">
 <div>{E("⏳")}<p><b>Hasta el</b><span>VIE 27/11</span></p></div>
 <div class="on">{E("🚚")}<p><b>Envío gratis</b><span>A TODO EL PAÍS</span></p></div></div>'''
render([page(1, h, nxt=False, total=1, story=True)], f'{OUT}/sorteo_historia', 1080, 1920)
