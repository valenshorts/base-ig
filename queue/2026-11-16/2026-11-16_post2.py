"""Guía: ¿qué es Creapure? (4 slides 1080×1350) · 16/11/2026 19:30.
Creapure® es una marca registrada de creatina monohidrato fabricada en Alemania (AlzChem).
Creatina monohidrato: la forma más estudiada (ISSN, posición 2017)."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
ST = '''<style>
.cta{position:absolute;left:80px;font-size:31px;font-weight:800;line-height:1.2}.cta span{color:var(--l)}
.pt{position:absolute;left:80px;right:80px;display:flex;gap:28px;align-items:center}
.pt .k{flex:0 0 120px;height:120px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border:2px solid var(--line);display:flex;align-items:center;justify-content:center}
.pt .k .e{font-size:68px}
.pt .n{font-size:29px;font-weight:500;line-height:1.34;color:#d6d6d8}.pt .n b{color:#fff;font-weight:800}.pt .n em{font-style:normal;color:var(--l);font-weight:700}
.cp .tile .ph img{max-height:82%}
.qq{position:absolute;right:80px;width:330px;display:flex;flex-direction:column;gap:20px}
.qq div{height:118px;background:var(--panel);border:2px solid var(--line);display:flex;align-items:center;gap:18px;padding:0 20px;font-size:26px;font-weight:800;text-transform:uppercase;line-height:1.15}
.qq .e{font-size:58px}
.eq{position:absolute;left:80px;right:80px;display:flex;align-items:center;justify-content:center;gap:22px}
.eq .bx{width:270px;height:270px;background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border:2px solid var(--line);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px}
.eq .bx .e{font-size:110px}
.eq .bx b{font-size:24px;font-weight:900;text-transform:uppercase;letter-spacing:1px;text-align:center;line-height:1.15}
.eq .bx.on{border-color:var(--l)} .eq .bx.on b{color:var(--l)}
.eq .op{font-family:'Archivo Black';font-size:80px;color:var(--l)}
.ck{position:absolute;left:80px;right:80px;display:flex;flex-direction:column;gap:30px}
.ck .r{display:flex;align-items:center;gap:28px;background:var(--panel);border:2px solid var(--line);padding:32px 28px}
.ck .r .e{font-size:78px}
.ck .r p{font-size:30px;font-weight:600;line-height:1.3;color:#d6d6d8}.ck .r p b{color:#fff;font-weight:900}
.claim{position:absolute;left:80px;right:80px;font-size:23px;line-height:1.35;color:#bdbdc0;font-weight:500}
.t4 .tile .ph img{max-height:80%}
.t4 .tile .ft .b{font-size:20px}
</style>'''

# 1 · PORTADA
s1 = ST + '<div class="eb" style="top:200px">Guía rápida</div>'
s1 += '<div class="t" style="top:250px;font-size:84px">¿Qué es<br><span class="box">Creapure?</span></div>'
s1 += tiles([('gold_creapure200', cf('Creatina Creapure', 28))], 500, 520, 560).replace('class="tiles"', 'class="tiles cp" style="justify-content:flex-start"').replace('style="justify-content:flex-start" style="', 'style="right:460px;justify-content:flex-start;')
s1 += f'''<div class="qq" style="top:500px"><div>{E("🤔")}Qué es</div><div>{E("🔍")}Cómo elegir</div><div>{E("🛒")}Opciones</div></div>'''
s1 += f'<div class="cta" style="top:1196px">En 3 slides {E("👉",30)}</div>'

# 2 · QUÉ ES
s2 = ST + '<div class="eb" style="top:200px">Qué es</div>'
s2 += '<div class="t" style="top:250px;font-size:72px">Es una marca,<br><span class="box">no otra creatina</span></div>'
s2 += f'''<div class="eq" style="top:520px"><div class="bx on">{E("🏷️")}<b>Creapure</b></div><div class="op">→</div>
 <div class="bx">{E("🧪")}<b>Creatina<br>monohidrato</b></div></div>'''
pts = [('🏭', '<b>Creapure</b> es una marca registrada de creatina monohidrato que <b>se fabrica en Alemania</b>.'),
       ('📚', 'La <em>creatina monohidrato</em> es la forma <b>más estudiada</b> (posición de la ISSN, 2017).')]
top = 860
for k, t in pts:
    s2 += f'<div class="pt" style="top:{top}px"><div class="k">{E(k)}</div><div class="n">{t}</div></div>'
    top += 160
s2 += f'<div class="cta" style="top:1196px;font-size:29px">¿Y cómo elijo? {E("🤔",29)}</div>'

# 3 · CÓMO ELEGIR
s3 = ST + '<div class="eb" style="top:200px">Cómo elegir</div>'
s3 += '<div class="t" style="top:250px;font-size:74px">3 cosas para<br><span class="box">mirar en el envase</span></div>'
ck = [('🧪', '<b>Que diga «creatina monohidrato».</b> Con o sin sello Creapure, esa es la forma más estudiada.'),
      ('🏷️', '<b>El sello Creapure</b> te dice quién la fabricó: es un origen conocido, no una creatina distinta.'),
      ('⚖️', '<b>Gramos y precio:</b> compará cuántos gramos trae cada envase antes de mirar solo el precio.')]
s3 += '<div class="ck" style="top:520px">' + ''.join(f'<div class="r">{E(e)}<p>{t}</p></div>' for e, t in ck) + '</div>'
s3 += f'<div class="cta" style="top:1196px;font-size:28px">Guardalo y compartilo {E("📌",28)}</div>'

# 4 · VENTA
s4 = ST + '<div class="eb" style="top:200px">Elegí la tuya</div>'
s4 += '<div class="t" style="top:250px;font-size:80px">Con sello<br><span class="box">o sin sello</span></div>'
s4 += tiles([('gold_creapure200', pf('Gold Creapure 200 g', '$31.900')),
             ('creatina_gold_300g', pf('Creatina Gold 300 g', '$22.900')),
             ('creatina_star_300g', pf('Creatina Star 300 g', '$23.800'))], 500, 292, 380).replace('class="tiles"', 'class="tiles t4"')
s4 += '<div class="claim" style="top:1010px">La creatina aumenta el rendimiento físico en series sucesivas de ejercicios cortos de alta intensidad. Precios por transferencia o efectivo.</div>'
s4 += f'<div class="btn" style="left:80px;top:1112px">{E("🛒",30)} VER CATÁLOGO · LINK EN LA BIO {ARROW}</div>'
s4 += f'<div style="position:absolute;left:80px;top:1207px;font-size:23px;font-weight:700;letter-spacing:1.5px;color:#d6d6d8">{E("💬",22)} CONSULTAS POR WHATSAPP <span style="color:var(--l)">11 2178-9431</span> · SOLO MENSAJES</div>'

print(render([page(1, s1, True, 4), page(2, s2, True, 4), page(3, s3, True, 4), page(4, s4, False, 4)], f'{OUT}/creapure'))
