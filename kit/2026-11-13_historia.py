import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.op4{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;gap:26px}
.op4 .o{position:relative;height:350px;background:var(--panel);border:2px solid var(--line);display:flex;flex-direction:column}
.op4 .o .ph{flex:1;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-bottom:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.op4 .o .ph .e{font-size:120px;filter:drop-shadow(0 14px 18px rgba(0,0,0,.55))}
.op4 .o .lt{position:absolute;left:0;top:0;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:38px;width:62px;height:62px;display:flex;align-items:center;justify-content:center}
.op4 .o .nm{height:90px;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:900;text-transform:uppercase}
.vote{position:absolute;left:80px;right:80px;text-align:center;font-weight:800;font-size:34px;line-height:1.3}
.vote span{color:var(--l)}
.feed{position:absolute;left:80px;right:80px;display:flex;align-items:center;gap:26px;background:var(--panel);border:2px solid var(--l);padding:22px 26px}
.feed .e{font-size:64px}
.feed .tx{font-size:27px;font-weight:700;line-height:1.3;color:#d6d6d8}.feed .tx b{color:var(--l);font-weight:900;text-transform:uppercase;display:block;font-size:30px}
</style>'''
b = ST + '<div class="eb" style="top:270px">Contanos</div>'
b += '<div class="t" style="top:325px;font-size:78px">¿Qué tomás antes<br><span class="box">de entrenar?</span></div>'
ops = [('A', '☕', 'Café'), ('B', '🧉', 'Mate'), ('C', '⚡', 'Pre-entreno'), ('D', '💧', 'Solo agua')]
b += '<div class="op4" style="top:580px">' + ''.join(
    f'<div class="o"><div class="ph">{E(e)}</div><div class="lt">{l}</div><div class="nm">{n}</div></div>' for l, e, n in ops) + '</div>'
b += f'<div class="vote" style="top:1345px">Respondé esta historia con<br><span>A, B, C o D</span> {E("💬",34)}</div>'
b += f'<div class="feed" style="top:1455px">{E("☕")}<div class="tx"><b>Hoy en el feed</b>Quiz: ¿cuál tiene más cafeína? Comentá en el post.</div></div>'
b += f'<div class="vote" style="top:1605px;font-size:26px;letter-spacing:1.5px;color:#d6d6d8">{E("🛒",26)} VER CATÁLOGO · <span>LINK EN LA BIO</span></div>'
b += f'<div class="legal" style="bottom:auto;top:1690px">{LEGAL_TXT}</div>'
print(render([page(1, b, nxt=False, total=1, story=True, legal=False)], f'{OUT}/historia_cafeina', 1080, 1920))
