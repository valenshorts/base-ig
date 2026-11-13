"""Reel del 14/11/2026 20:30: anuncio del sorteo de 3 creatinas (5 imágenes 1080×1920, sin precios)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.chip{position:absolute;left:12px;top:12px;z-index:2;background:var(--bk);border:2px solid var(--l);color:var(--w);font-size:34px;font-weight:900;letter-spacing:1.5px;padding:6px 16px}
.tz .tile .ph img{max-height:78%;margin-top:30px}
.hero{position:absolute;left:80px;right:80px;display:flex;align-items:center;justify-content:center}
.hero .e{filter:drop-shadow(0 20px 28px rgba(0,0,0,.6))}
.ship{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:30px;background:var(--panel);border:3px solid var(--l);padding:26px 32px}
.ship .e{font-size:96px}
.ship p{font-size:46px;font-weight:900;text-transform:uppercase;line-height:1.08}.ship p span{color:var(--l)}
.st{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:34px;background:var(--panel);border:2px solid var(--line);height:240px;padding-right:30px}
.st .k{flex:0 0 240px;height:236px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-right:2px solid var(--line);display:flex;align-items:center;justify-content:center;position:relative}
.st .k .e{font-size:120px;filter:drop-shadow(0 12px 16px rgba(0,0,0,.55))}
.st .k i{position:absolute;left:0;top:0;width:62px;height:62px;background:var(--l);color:var(--bk);font-style:normal;font-family:'Archivo Black';font-size:38px;display:flex;align-items:center;justify-content:center}
.st .n{font-size:50px;font-weight:900;text-transform:uppercase;line-height:1.05;letter-spacing:-.5px}
.dt{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:34px;background:var(--panel);border:2px solid var(--line);padding:30px 34px}
.dt.on{border:3px solid var(--l)}
.dt .e{font-size:110px}
.dt b{display:block;font-size:30px;letter-spacing:3px;color:#a9a9ad;font-weight:800;text-transform:uppercase}
.dt span{display:block;font-family:'Archivo Black';font-size:68px;line-height:1.05;margin-top:6px}
.dt.on span{color:var(--l)}
.big{position:absolute;left:80px;right:80px;font-size:54px;font-weight:900;text-transform:uppercase;line-height:1.1;text-align:center}
.big span{color:var(--l)}
.no{position:absolute;left:80px;right:80px;text-align:center;font-size:36px;font-weight:800;color:#d6d6d8}
.no b{color:var(--l)}
.st,.ship,.dt,.wa,.no{right:140px}
.wa{position:absolute;left:80px;right:80px;text-align:center;font-size:27px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8}
.wa span{color:var(--l)}
</style>'''
LEG = f'<div class="legal" style="bottom:auto;top:1690px">{LEGAL_TXT}</div>'

def tile(f, chip, ft):
    return f'<div class="tile"><div class="ph"><div class="chip">{chip}</div><img src="assets/{f}.png"></div>{ft}</div>'

# 1 · GANCHO
r1 = ST + '<div class="eb" style="top:300px">Sorteo</div>'
r1 += '<div class="t" style="top:360px;font-size:120px">Sorteamos<br><span class="box">3 creatinas</span></div>'
r1 += f'<div class="hero" style="top:760px;height:560px">{E("🎁",420)}</div>'
r1 += '<div class="big" style="top:1420px">Mirá cómo <span>participar</span></div>'
r1 += LEG

# 2 · PREMIOS
r2 = ST + '<div class="eb" style="top:300px">Los premios</div>'
r2 += '<div class="t" style="top:360px;font-size:104px">2 Gold +<br><span class="box">1 Star</span></div>'
r2 += ('<div class="tiles tz" style="top:640px;--w:440px;--h:500px;--g:20px">'
       + tile('creatina_gold_300g', '×2', cf('Creatina Gold 300 g', 30))
       + tile('creatina_star_300g', '×1', cf('Creatina Star 300 g', 30)) + '</div>')
r2 += f'<div class="ship" style="top:1330px">{E("🚚")}<p>Envío gratis<br><span>a todo el país</span></p></div>'
r2 += LEG

# 3 · 3 PASOS
r3 = ST + '<div class="eb" style="top:300px">Cómo participar</div>'
r3 += '<div class="t" style="top:360px;font-size:110px">3 pasos</div>'
pasos = [('👤', 'Seguí a<br><span style="font-size:36px;letter-spacing:0">@basesuplementos.ar</span>'), ('❤️', 'Dale me gusta<br>al post del sorteo'), ('💬', 'Comentá<br>etiquetando<br>a 2 amigos')]
top = 600
for i, (e, n) in enumerate(pasos, 1):
    r3 += f'<div class="st" style="top:{top}px"><div class="k">{E(e)}<i>{i}</i></div><div class="n">{n}</div></div>'
    top += 290
r3 += f'<div class="wa" style="top:1460px;font-size:30px">Más comentarios con amigos distintos<br>= <span>más chances</span></div>'
r3 += LEG

# 4 · FECHAS
r4 = ST + '<div class="eb" style="top:300px">Fechas</div>'
r4 += '<div class="t" style="top:360px;font-size:104px">No te la<br><span class="box">pierdas</span></div>'
r4 += f'<div class="dt on" style="top:720px">{E("⏳")}<p><b>Participás hasta el</b><span>VIE 27/11</span><b style="margin-top:8px">a las 23:59</b></p></div>'
r4 += f'<div class="dt" style="top:1060px">{E("🎲")}<p><b>Sorteo en vivo</b><span>SÁB 28/11</span><b style="margin-top:8px">por historias</b></p></div>'
r4 += '<div class="no" style="top:1360px">Mayores de 18 · Argentina<br><b>sin obligación de compra</b></div>'
r4 += LEG

# 5 · CTA
r5 = ST + '<div class="eb" style="top:300px">Participá</div>'
r5 += '<div class="t" style="top:360px;font-size:100px">Entrá al<br><span class="box">post del</span><br><span class="box">sorteo</span></div>'
r5 += f'<div class="hero" style="top:800px;height:300px">{E("📲",240)}</div>'
r5 += '<div class="no" style="top:1120px">Comentá <b>en el post</b>, no en este reel</div>'
r5 += f'<div class="btn" style="left:80px;right:140px;justify-content:center;top:1230px;font-size:32px;padding:26px 30px">{E("🛒",36)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
r5 += f'<div class="wa" style="top:1370px">{E("💬",26)} WHATSAPP <span>11 2178-9431</span> · SOLO MENSAJES</div>'
r5 += LEG

print(render([page(1, r, nxt=False, total=1, story=True, legal=False) for r in (r1, r2, r3, r4, r5)], f'{OUT}/reel', 1080, 1920))
