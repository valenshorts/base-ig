"""
Plantillas de escena para los reels de BASE. Cada una recibe la duración (d), el contexto (ctx) y sus datos,
y devuelve (html, sonidos). `sonidos` es una lista de (segundo, tipo) para sincronizar los efectos de audio.

Textos: *palabra* sale en lima y [palabra] en caja lima. Productos: `foto` = nombre de archivo de kit/assets
(sin .png), por ejemplo "creatina_star_300g". Si no hay foto fiel, usar `emoji`.
"""
from anim import page, palabras, burst, flash, foto as _foto, MARCA


def _tile(x, y, w, h, foto=None, emoji=None, pie=None, precio=None, anim='', extra=''):
    img = f'<img src="{_foto(foto)}">' if foto else f'<span class="e" style="position:absolute;left:0;right:0;top:{h * .22:.0f}px;text-align:center;font-size:{min(h * .42, w * .52):.0f}px">{emoji}</span>'
    ft = ''
    if pie or precio:
        ft = f'<div class="ft">{f"<b>{pie}</b>" if pie else ""}{f"<s>{precio}</s>" if precio else ""}</div>'
    return (f'<div class="tile" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{anim}">{img}'
            f'<div class="shine" style="animation:shine .9s ease-in-out .55s both"></div>{ft}{extra}</div>')


def gancho(d, ctx, texto, eb='', emoji='', foto='', pie=''):
    """Gancho del principio: texto que golpea palabra por palabra + emoji gigante o producto."""
    primera = ctx.get('primera')
    words, tfin = palabras(texto, -0.34 if primera else 0.08, 0.07 if primera else 0.1)
    tfin = max(tfin, 0.12)
    css = '.big{position:absolute;left:0;right:0;text-align:center;top:960px;font-size:420px;animation:pop .5s cubic-bezier(.2,1.6,.4,1) var(--t) both,bob 1.4s ease-in-out .6s infinite alternate}'
    body = (f'<div class="eb" style="top:420px">{eb}</div>' if eb else '')
    body += f'<div class="k" style="top:470px;font-size:112px">{words}</div>'
    snd = [(0, 'hit')] if primera else [(0, 'whoosh')] + [(0.08 + i * 0.1, 'tick') for i in range(len(texto.split()))]
    if foto:
        body += _tile(170, 820, 740, 760, foto=foto, pie=pie, anim=f'animation:slamup .55s cubic-bezier(.2,1.5,.35,1) {tfin:.2f}s both')
        body += '<div class="ring" style="left:90px;top:740px;width:900px;height:900px;z-index:-1"></div>'
        css += '@keyframes slamup{from{transform:translateY(900px) rotate(8deg)}to{transform:none}} .tile img{animation:flt 1.6s ease-in-out .7s infinite alternate} @keyframes flt{from{translate:0 0;rotate:-2deg}to{translate:0 -24px;rotate:2deg}}'
    elif emoji:
        body += f'<span class="e big" style="--t:{tfin:.2f}s">{emoji}</span>'
    body += burst(540, 1200, tfin + 0.25, 26, 1) + flash(tfin + 0.2)
    snd.append((tfin + 0.2, 'hit'))
    return page(body, d, ctx, css, golpes=[tfin + .2]), snd


def numero(d, ctx, valor, unidad, texto='', decimales=0, emoji='', foto=''):
    """Número que cuenta desde 0 con un anillo que gira y golpe al final (5 g, 25 %, 300 g)."""
    dur = max(min(d * 0.35, 1.0), 0.6)
    css = """
    .num{position:absolute;left:0;right:0;top:700px;text-align:center;font-family:'Archivo Black';font-size:480px;line-height:1;
      color:var(--l);text-shadow:0 14px 0 rgba(0,0,0,.45)}
    .unit{position:absolute;left:70px;right:70px;top:1230px;text-align:center;font-size:92px;text-transform:uppercase;letter-spacing:-1px;animation:up .4s ease-out var(--t) both}
    .ico{position:absolute;left:0;right:0;text-align:center;top:1360px;font-size:200px;animation:pop .45s cubic-bezier(.2,1.6,.4,1) var(--t) both,bob 1.3s ease-in-out 1s infinite alternate}
    .hit{animation:shake .32s linear var(--t) both}"""
    words, _ = palabras(texto, 0.1, 0.1)
    fin = 0.25 + dur
    body = f'<div class="k" style="top:480px;font-size:104px">{words}</div>'
    body += '<div class="ring" style="left:150px;top:600px;width:780px;height:780px"></div>'
    body += (f'<div class="hit" style="--t:{fin:.2f}s;position:absolute;inset:0">'
             f'<div class="num" data-count="0,{valor},0.25,{dur:.2f},{decimales}">0</div></div>')
    body += f'<div class="unit" style="--t:{fin:.2f}s">{unidad}</div>'
    if foto:
        body += _tile(330, 1270, 420, 380, foto=foto, anim=f'animation:pop .5s cubic-bezier(.2,1.6,.4,1) {fin + .1:.2f}s both')
    elif emoji:
        body += f'<span class="e ico" style="--t:{fin + .1:.2f}s">{emoji}</span>'
    body += burst(540, 920, fin, 24, 2) + flash(fin)
    snd = [(0, 'whoosh')] + [(0.25 + dur * (1 - (1 - k / 6) ** .5), 'tick') for k in range(6)] + [(fin, 'hit')]
    return page(body, d, ctx, css, golpes=[fin]), snd


def lista(d, ctx, texto, items):
    """Hasta 4 puntos que entran de costados, con ícono grande. items = [["⚡", "Más energía"], ...]."""
    css = """
    .it{position:absolute;left:90px;right:150px;height:170px;display:flex;align-items:center;gap:34px;
      font-weight:900;font-size:62px;text-transform:uppercase;letter-spacing:-1px;background:#111112;border:3px solid #2a2a2d;padding-right:30px}
    .it .ic{flex:0 0 166px;height:164px;display:flex;align-items:center;justify-content:center;
      background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%);border-right:3px solid #2a2a2d}
    .it .ic .e{font-size:100px}
    @keyframes inl{from{transform:translateX(-1100px)}to{transform:none}}
    @keyframes inr{from{transform:translateX(1100px)}to{transform:none}}"""
    words, t = palabras(texto, 0.1, 0.1)
    n = min(len(items), 4)
    step = min((d - 0.6) * 0.75 / max(n, 1), 0.9)
    body = f'<div class="k" style="top:460px;font-size:104px">{words}</div>'
    snd = [(0, 'whoosh')]
    for k, (e, txt) in enumerate(items[:4]):
        tk = t + 0.15 + k * step
        lado = 'inl' if k % 2 == 0 else 'inr'
        body += (f'<div class="it" style="top:{720 + k * 200}px;animation:{lado} .42s cubic-bezier(.2,1.3,.35,1) {tk:.2f}s both">'
                 f'<div class="ic"><span class="e">{e}</span></div>{txt}</div>')
        snd.append((tk, 'swipe'))
        snd.append((tk + 0.3, 'pop'))
    return page(body, d, ctx, css), snd


def producto(d, ctx, foto, nombre, detalle='', precio='', chip='', foto2=''):
    """Producto real en recuadro gris que entra con golpe, brillo y sello de precio."""
    css = """
    @keyframes slamup{from{transform:translateY(1100px) rotate(10deg)}70%{transform:translateY(-30px) rotate(-2deg)}to{transform:none}}
    .stamp{position:absolute;right:110px;top:470px;z-index:5;background:var(--l);color:var(--bk);font-family:'Archivo Black';
      font-size:84px;padding:14px 34px 18px;transform:rotate(-8deg);animation:stamp .4s cubic-bezier(.2,1.8,.4,1) var(--t) both;
      box-shadow:0 18px 40px rgba(0,0,0,.5)}
    @keyframes stamp{from{transform:scale(3) rotate(-25deg);opacity:0}to{transform:scale(1) rotate(-8deg);opacity:1}}
    .chip{position:absolute;left:160px;top:1290px;z-index:5;border:4px solid var(--l);background:var(--bk);color:#fff;font-size:44px;
      padding:10px 22px;letter-spacing:2px;animation:pop .4s cubic-bezier(.2,1.6,.4,1) var(--t) both}
    .nm{position:absolute;left:70px;right:70px;top:1395px;text-align:center;font-size:74px;text-transform:uppercase;letter-spacing:-1px;animation:up .4s ease-out var(--t) both}
    .dt{position:absolute;left:70px;right:70px;top:1480px;text-align:center;font-size:40px;font-weight:700;color:#bdbdc0;animation:up .4s ease-out var(--t) both}"""
    body = '<div class="ring" style="left:120px;top:480px;width:840px;height:840px"></div>'
    extra = ''
    if foto2:   # combos "2×": dos paquetes superpuestos
        css += '.duo img.a{left:37%;top:47%;max-width:64%;max-height:68%} .duo img.b{left:64%;top:55%;max-width:64%;max-height:68%} @keyframes popc{from{transform:translate(-50%,-50%) scale(0) rotate(-15deg)}to{transform:translate(-50%,-50%) scale(1)}}'
        extra = f'<img class="b" src="{_foto(foto2)}" style="animation:popc .4s cubic-bezier(.2,1.6,.4,1) .5s both">'
    tile = _tile(190, 520, 700, 840, foto=foto, anim='animation:slamup .7s cubic-bezier(.2,1,.3,1) .1s both', extra=extra)
    if foto2:
        tile = tile.replace('class="tile"', 'class="tile duo"', 1).replace('<img ', '<img class="a" ', 1)
    body += tile
    t1 = 0.75
    body += f'<div class="nm" style="--t:{t1:.2f}s">{nombre}</div>'
    if detalle:
        body += f'<div class="dt" style="--t:{t1 + .15:.2f}s">{detalle}</div>'
    snd = [(0, 'whoosh'), (0.55, 'hit')]
    if chip:
        body += f'<div class="chip" style="--t:{t1 + .3:.2f}s">{chip}</div>'
        snd.append((t1 + .3, 'pop'))
    if precio:
        tp = min(t1 + 0.7, d - 0.6)
        body += f'<div class="stamp" style="--t:{tp:.2f}s">{precio}</div>' + burst(760, 530, tp + 0.1, 20, 4) + flash(tp + .05)
        snd.append((tp, 'stamp'))
    return page(body, d, ctx, css, golpes=[0.55] + ([tp] if precio else [])), snd


def comparacion(d, ctx, texto, izq, der, ganador=''):
    """A vs B. izq/der = {"foto": "...", "texto": "..."} o {"emoji": "🥛", "texto": "..."}. ganador = "izq" o "der"."""
    css = """
    @keyframes inl{from{transform:translateX(-900px) rotate(-12deg)}to{transform:none}}
    @keyframes inr{from{transform:translateX(900px) rotate(12deg)}to{transform:none}}
    .vs{position:absolute;left:440px;top:780px;width:200px;height:200px;background:var(--l);color:var(--bk);z-index:6;
      font-family:'Archivo Black';font-size:96px;display:flex;align-items:center;justify-content:center;transform:rotate(-6deg);
      animation:stamp .4s cubic-bezier(.2,1.8,.4,1) var(--t) both}
    @keyframes stamp{from{transform:scale(3) rotate(-30deg);opacity:0}to{transform:scale(1) rotate(-6deg);opacity:1}}
    .lb{position:absolute;width:440px;text-align:center;top:1320px;font-size:58px;text-transform:uppercase;letter-spacing:-1px;animation:up .4s ease-out var(--t) both}
    .lose{animation:dim .4s ease-out var(--t) both}
    @keyframes dim{to{opacity:.35;filter:grayscale(1)}}
    .win{position:absolute;border:8px solid var(--l);z-index:7;animation:pop .4s cubic-bezier(.2,1.6,.4,1) var(--t) both}
    .ok{position:absolute;z-index:8;width:130px;height:130px;background:var(--l);color:var(--bk);font-size:90px;display:flex;align-items:center;justify-content:center;
      animation:pop .4s cubic-bezier(.2,1.8,.4,1) var(--t) both}"""
    words, t = palabras(texto, 0.1, 0.1)
    body = f'<div class="k" style="top:400px;font-size:92px">{words}</div>'
    ta, tb, tv = t + 0.1, t + 0.35, t + 0.65
    for lado, dato, x, anim, tt in (('izq', izq, 80, 'inl', ta), ('der', der, 560, 'inr', tb)):
        cls = ''
        tw = tv + 0.9
        if ganador and ganador != lado:
            cls = f'class="lose" style="--t:{tw:.2f}s;position:absolute;inset:0"'
        pr = dato.get('precio')
        tile = _tile(x, 640, 440, 700, foto=dato.get('foto'), emoji=dato.get('emoji'),
                     pie=dato.get('texto') if pr else None, precio=pr,
                     anim=f'animation:{anim} .5s cubic-bezier(.2,1.2,.35,1) {tt:.2f}s both')
        lb = '' if pr else f'<div class="lb" style="left:{x}px;--t:{tt + .3:.2f}s">{dato.get("texto", "")}</div>'
        body += f'<div {cls}>{tile}{lb}</div>' if cls else tile + lb
    body += f'<div class="vs" style="--t:{tv:.2f}s">VS</div>' + flash(tv)
    snd = [(0, 'whoosh'), (ta, 'swipe'), (tb, 'swipe'), (tv, 'hit')]
    golpes = [tv]
    if ganador:
        tw = tv + 0.9
        x = 80 if ganador == 'izq' else 560
        body += f'<div class="win" style="left:{x - 10}px;top:690px;width:460px;height:620px;--t:{tw:.2f}s"></div>'
        body += f'<div class="ok" style="left:{x + 330}px;top:640px;--t:{tw + .1:.2f}s">✓</div>' + burst(x + 220, 1000, tw + .1, 22, 5)
        snd.append((tw, 'ding'))
    return page(body, d, ctx, css, golpes=golpes), snd


def quiz(d, ctx, pregunta, opciones, correcta, revelar=None):
    """Pregunta con 4 opciones A/B/C/D, cuenta regresiva 3-2-1 y respuesta revelada. correcta = índice (0-3)."""
    css = """
    .op{position:absolute;width:440px;height:300px;background:#111112;border:3px solid #2a2a2d;animation:pop .4s cubic-bezier(.2,1.6,.4,1) var(--t) both}
    .op .ic{position:absolute;left:0;right:0;top:20px;height:180px;display:flex;align-items:center;justify-content:center;
      background:radial-gradient(ellipse at 50% 45%,#3A3A3E 0%,#232326 60%,#141416 100%)}
    .op .ic .e{font-size:120px} .op .ic img{max-height:86%;max-width:80%}
    .op .tx{position:absolute;left:10px;right:10px;bottom:16px;text-align:center;font-size:40px;text-transform:uppercase;letter-spacing:-.5px}
    .op .lt{position:absolute;left:0;top:0;width:66px;height:66px;background:var(--l);color:var(--bk);font-family:'Archivo Black';font-size:40px;
      display:flex;align-items:center;justify-content:center;z-index:2}
    .cd{position:absolute;left:390px;top:1400px;width:300px;height:300px;border-radius:50%;background:var(--l);color:var(--bk);display:flex;align-items:center;justify-content:center;font-family:'Archivo Black';font-size:210px;opacity:0;box-shadow:0 0 80px rgba(198,244,50,.55)}
    @keyframes cnt{0%{transform:scale(2.2);opacity:0}25%{transform:scale(1);opacity:1}85%{opacity:1}100%{opacity:0;transform:scale(.8)}}
    .lose{animation:dim .35s ease-out var(--t) both}
    @keyframes dim{to{opacity:.25;filter:grayscale(1)}}
    .win{animation:winp .45s cubic-bezier(.2,1.6,.4,1) var(--t) both}
    @keyframes winp{to{border-color:var(--l);background:#1c2408;transform:scale(1.06)}}
    .ans{position:absolute;left:70px;right:70px;top:1420px;text-align:center;font-size:80px;text-transform:uppercase;letter-spacing:-1px;animation:pop .45s cubic-bezier(.2,1.6,.4,1) var(--t) both}
    .ans b{color:var(--bk);background:var(--l);padding:2px 18px 8px}"""
    words, t = palabras(pregunta, 0.1, 0.1)
    body = f'<div class="k" style="top:430px;font-size:88px">{words}</div>'
    snd = [(0, 'whoosh')]
    b = ctx.get('beat', .4839)
    rev = revelar or max(d - 2.5 * b, t + 0.9 + 3 * b)
    pos = [(80, 720), (560, 720), (80, 1060), (560, 1060)]
    for k, ((x, y), op) in enumerate(zip(pos, opciones[:4])):
        e, txt = op[0], op[1]
        ic = f'<img src="{_foto(e[5:])}">' if e.startswith('foto:') else f'<span class="e">{e}</span>'
        tk = t + 0.05 + k * 0.12
        wrap_cls = 'win' if k == correcta else 'lose'
        body += (f'<div style="--t:{rev:.2f}s;position:absolute;left:{x}px;top:{y}px;width:440px;height:300px" class="{wrap_cls}">'
                 f'<div class="op" style="left:0;top:0;--t:{tk:.2f}s"><div class="lt">{"ABCD"[k]}</div><div class="ic">{ic}</div>'
                 f'<div class="tx">{txt}</div></div></div>')
        snd.append((tk, 'pop'))
    for i, n in enumerate((3, 2, 1)):
        tc = rev - (3 - i) * b
        if tc > t:
            body += f'<div class="cd" style="animation:cnt {b:.3f}s ease-out {tc:.2f}s both">{n}</div>'
            snd.append((tc, 'stamp'))
    snd.append((rev - 3 * b, 'riser'))
    body += f'<div class="ans" style="--t:{rev:.2f}s">Es la <b>{"ABCD"[correcta]}</b></div>'
    x, y = pos[correcta]
    body += burst(x + 220, y + 150, rev + .05, 24, 6) + flash(rev)
    snd += [(rev, 'ding'), (rev, 'hit')]
    return page(body, d, ctx, css, golpes=[rev]), snd


def dato(d, ctx, texto, eb='', fuente='', emoji=''):
    """Afirmación grande con subrayado lima que se dibuja debajo, ícono y la fuente."""
    css = """
    .col{position:absolute;left:70px;right:70px;top:470px;display:flex;flex-direction:column;align-items:center;gap:34px}
    .col .eb,.col .k{position:static}
    .ul{width:740px;height:18px;background:var(--l);transform-origin:left;animation:draw .5s ease-out var(--t) both}
    @keyframes draw{from{transform:scaleX(0)}to{transform:scaleX(1)}}
    .src{font-size:32px;font-weight:700;color:#a9a9ad;animation:up .4s ease-out var(--t) both}
    .ico{font-size:230px;animation:pop .45s cubic-bezier(.2,1.6,.4,1) var(--t) both,bob 1.4s ease-in-out 1.2s infinite alternate}"""
    words, t = palabras(texto, 0.1, 0.13)
    body = '<div class="col">' + (f'<div class="eb">{eb}</div>' if eb else '')
    body += f'<div class="k" style="font-size:100px">{words}</div>'
    body += f'<div class="ul" style="--t:{t:.2f}s"></div>'
    if emoji:
        body += f'<span class="e ico" style="--t:{t + .2:.2f}s">{emoji}</span>'
    if fuente:
        body += f'<div class="src" style="--t:{t + .4:.2f}s">Fuente: {fuente}</div>'
    body += '</div>'
    return page(body, d, ctx, css), [(0, 'whoosh'), (t, 'swipe')]


def cierre(d, ctx, texto='Pedí la *tuya*', boton='LINK EN LA BIO', fotos=()):
    """Llamado a la acción: botón que late, flecha que sube al perfil, WhatsApp y productos que pasan."""
    css = """
    .btn{position:absolute;left:120px;right:120px;top:820px;height:190px;background:var(--l);color:var(--bk);
      font-size:76px;display:flex;align-items:center;justify-content:center;gap:24px;letter-spacing:-1px;
      animation:pop .45s cubic-bezier(.2,1.6,.4,1) var(--t) both,pulse .55s ease-in-out 1s infinite alternate}
    .btn .e{font-size:76px}
    .arr{position:absolute;left:0;right:0;top:660px;text-align:center;animation:hop .5s ease-in-out infinite alternate}
    @keyframes hop{from{transform:translateY(20px)}to{transform:translateY(-30px)}}
    .wa{position:absolute;left:60px;right:60px;top:1060px;text-align:center;font-size:38px;font-weight:800;letter-spacing:1px;color:#d6d6d8;animation:up .4s ease-out var(--t) both}
    .wa b{color:var(--l)}
    .rail{position:absolute;left:0;top:1170px;display:flex;gap:24px;animation:rail var(--d) linear both}
    @keyframes rail{from{transform:translateX(0)}to{transform:translateX(-520px)}}
    .rail .tile{position:relative}"""
    words, t = palabras(texto, 0.1, 0.12)
    body = f'<div class="k" style="top:430px;font-size:110px">{words}</div>'
    body += '<div class="arr"><svg width="120" height="130" viewBox="0 0 120 130"><path d="M60 6 L112 64 H78 V124 H42 V64 H8 Z" fill="#C6F432"/></svg></div>'
    body += f'<div class="btn" style="--t:{t:.2f}s"><span class="e">🛒</span>{boton}</div>'
    body += f'<div class="wa" style="--t:{t + .3:.2f}s">💬 WHATSAPP <b>{MARCA["whatsapp"]}</b> · SOLO MENSAJES</div>'
    if fotos:
        tiles = ''.join(f'<div class="tile" style="width:300px;height:330px;flex:0 0 300px"><img src="{_foto(f)}"></div>' for f in list(fotos) * 2)
        body += f'<div class="rail" style="left:60px">{tiles}</div>'
    body += burst(540, 915, t + .1, 24, 7)
    return page(body, d, ctx, css, golpes=[t]), [(0, 'whoosh'), (t, 'hit')]


def rafaga(d, ctx, palabras_):
    """Una palabra/frase GIGANTE por beat, alternando blanco y caja lima. palabras_ = ["NO ES", "MAGIA", ...]."""
    b = ctx.get('beat', .4839)
    css = """
    .rf{position:absolute;left:50px;right:50px;top:620px;height:680px;display:flex;align-items:center;justify-content:center;text-align:center;
      font-family:'Archivo Black';text-transform:uppercase;line-height:.92;letter-spacing:-3px;opacity:0}
    .rf.l span{background:var(--l);color:var(--bk);padding:10px 40px 26px;display:inline-block;transform:rotate(-3deg)}
    @keyframes rfin{0%{opacity:1;transform:scale(1.9);filter:blur(10px)}18%{transform:scale(.96);filter:none}30%{transform:scale(1)}99.9%{opacity:1}100%{opacity:0}}"""
    n = len(palabras_)
    paso = d / n
    body, snd = '', []
    for i, w in enumerate(palabras_):
        ti = i * paso
        last = i == n - 1
        fs = int(min(300, 1100 / max(len(w), 1)))
        dur = (d - ti) if last else paso
        body += (f'<div class="rf{" l" if i % 2 else ""}" style="font-size:{fs}px;animation:rfin {dur:.3f}s cubic-bezier(.2,1,.3,1) {ti:.3f}s {"forwards" if last else "none"}">'
                 f'<span>{w}</span></div>')
        snd.append((ti, 'stamp' if i % 2 else 'swipe'))
    body += burst(540, 960, (n - 1) * paso + .05, 26, 9)
    return page(body, d, ctx, css, golpes=[i * paso for i in range(1, n, 2)]), snd


PLANTILLAS = {'gancho': gancho, 'numero': numero, 'lista': lista, 'producto': producto,
              'comparacion': comparacion, 'quiz': quiz, 'dato': dato, 'cierre': cierre, 'rafaga': lambda d, ctx, palabras: rafaga(d, ctx, palabras)}
DURACION = {'gancho': 2.4, 'numero': 2.6, 'lista': 3.6, 'producto': 3.0, 'comparacion': 3.4, 'quiz': 6.0, 'dato': 3.0, 'cierre': 3.2, 'rafaga': 1.94}
