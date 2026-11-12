import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.two{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:26px}
.two .o{height:400px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column}
.two .o .ph{flex:1;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-bottom:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.two .o .ph .e{font-size:140px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.two .o .nm{height:100px;display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:900;text-transform:uppercase}
.vote{position:absolute;left:80px;right:80px;text-align:center;color:var(--l);font-weight:800;letter-spacing:4px;font-size:26px}
.feed{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:26px;background:var(--panel);border:2px solid var(--l);padding:22px 26px}
.feed .e{font-size:64px}
.feed .tx{font-size:27px;font-weight:700;line-height:1.3;color:#d6d6d8}.feed .tx b{color:var(--l);font-weight:900;text-transform:uppercase;display:block;font-size:30px}
</style>'''
b = ST + '<div class="eb" style="top:270px">Esto o esto</div>'
b += '<div class="t" style="top:325px;font-size:100px">¿Cuándo<br><span class="box">entrenás?</span></div>'
b += '<div class="two" style="top:610px">' + ''.join(
    f'<div class="o"><div class="ph">{E(e)}</div><div class="nm">{n}</div></div>' for e,n in [('☀️','De día'),('🌙','De noche')]) + '</div>'
b += f'<div class="vote" style="top:1050px">VOTÁ ACÁ ABAJO {E("👇",30)}</div>'
b += f'<div class="feed" style="top:1500px">{E("⏱️")}<div class="tx"><b>Nuevo en el feed</b>¿Tenés 30 minutos para tomar la whey? Entrá al perfil.</div></div>'
print(render([page(1, b, nxt=False, total=1, story=True)], f'{OUT}/historia_horario', 1080, 1920))
