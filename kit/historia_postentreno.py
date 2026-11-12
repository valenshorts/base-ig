import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.op4{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.op4 .o{position:relative;height:290px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column}
.op4 .o .ph{height:170px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-bottom:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.op4 .o .ph .e{font-size:90px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.op4 .o .lt{position:absolute;left:0;top:0;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:26px;width:44px;height:44px;display:flex;align-items:center;justify-content:center}
.op4 .o .nm{flex:1;display:flex;align-items:center;justify-content:center;font-size:24px;line-height:1.15;padding:0 8px;font-weight:900;text-transform:uppercase;letter-spacing:-.3px;text-align:center}
.vote{position:absolute;left:80px;right:80px;text-align:center;color:var(--l);font-weight:800;letter-spacing:4px;font-size:26px}
.feed{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:26px;background:var(--panel);border:2px solid var(--l);padding:22px 26px}
.feed .e{font-size:64px}
.feed .tx{font-size:27px;font-weight:700;line-height:1.3;color:#d6d6d8}.feed .tx b{color:var(--l);font-weight:900;text-transform:uppercase;display:block;font-size:30px}
</style>'''
b = ST + '<div class="eb" style="top:270px">Encuesta</div>'
b += '<div class="t" style="top:325px;font-size:96px">¿Qué comés<br><span class="box">post entreno?</span></div>'
ops = [('A','🥤','Un shake'),('B','🍌','Fruta'),('C','🍽️','Comida<br>completa'),('D','🤷','Nada')]
b += '<div class="op4" style="top:600px">' + ''.join(
    f'<div class="o"><div class="ph">{E(e)}</div><div class="lt">{l}</div><div class="nm">{n}</div></div>' for l,e,n in ops) + '</div>'
b += f'<div class="vote" style="top:930px">VOTÁ ACÁ ABAJO {E("👇",30)}</div>'
b += f'<div class="feed" style="top:1590px">{E("🧀")}<div class="tx"><b>Nuevo quiz en el feed</b>¿Cuál tiene más proteína? Entrá al perfil y comentá.</div></div>'
print(render([page(1, b, nxt=False, total=1, story=True)], f'{OUT}/historia_postentreno', 1080, 1920))
