"""
Motor de animación de BASE Suplementos: cada escena es una página HTML con animaciones CSS que se filma
cuadro por cuadro con Chromium (Playwright) y se codifica con ffmpeg (1080×1920, 30 fps).

Identidad BASE: negro #0B0B0C, lima #C6F432, blanco; Montserrat 900 y Archivo Black; esquinas rectas;
productos SIEMPRE en recuadros grises; marca BASE arriba; leyenda legal abajo.
"""
import base64, json, random, shutil, subprocess
from functools import lru_cache
from pathlib import Path

W, H, FPS = 1080, 1920, 30
HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / 'kit' / 'assets'          # fotos recortadas de los productos (las del kit de diseño)
MARCA = json.loads((HERE / 'marca.json').read_text(encoding='utf-8'))
LEGAL = 'SUPLEMENTA DIETAS INSUFICIENTES. CONSULTE A SU MÉDICO Y/O FARMACÉUTICO.'


def ffmpeg():
    f = shutil.which('ffmpeg')
    if f:
        return f
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def _b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode()


def _fonts():
    f = HERE / 'fonts'
    css = ''
    for w in (700, 800, 900):
        css += f"@font-face{{font-family:'Montserrat';font-weight:{w};src:url(data:font/ttf;base64,{_b64(f / f'Montserrat-{w}.ttf')})}}"
    css += f"@font-face{{font-family:'Archivo Black';src:url(data:font/ttf;base64,{_b64(f / 'ArchivoBlack.ttf')})}}"
    return css


FONT_CSS = _fonts()


@lru_cache(maxsize=64)
def foto(nombre):
    """Foto de producto del kit (assets/<nombre>.png) como data URI."""
    p = ASSETS / f'{nombre}.png'
    if not p.exists():
        raise FileNotFoundError(f'No existe la foto {p}. Fotos disponibles: {", ".join(sorted(x.stem for x in ASSETS.glob("*.png")))}')
    return f'data:image/png;base64,{_b64(p)}'


MARK = ('<svg viewBox="0 0 36 36" width="{s}" height="{s}"><rect width="36" height="36" fill="#C6F432"/>'
        '<rect x="10" y="25" width="16" height="4" fill="#0B0B0C"/></svg>')

BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:var(--bk)}
body{font-family:'Montserrat','Noto Color Emoji',sans-serif;font-weight:900;color:#fff}
.bg{position:absolute;inset:-200px;background:radial-gradient(ellipse 900px 700px at 80% 12%,rgba(198,244,50,.16),transparent 65%),
  radial-gradient(ellipse 800px 600px at 10% 95%,rgba(198,244,50,.08),transparent 60%),var(--bk)}
.grid{position:absolute;inset:-200px;background-image:linear-gradient(rgba(255,255,255,.035) 2px,transparent 2px),
  linear-gradient(90deg,rgba(255,255,255,.035) 2px,transparent 2px);background-size:90px 90px;
  animation:gridmove var(--d) linear both}
@keyframes gridmove{from{transform:translate(0,0)}to{transform:translate(-90px,-180px)}}
.cam{position:absolute;inset:0;transform-origin:50% 45%;animation:push var(--d) cubic-bezier(.3,0,.7,1) both}
@keyframes push{from{transform:scale(1)}to{transform:scale(1.07)}}
.beat{position:absolute;inset:0;transform-origin:50% 45%;animation:thump var(--beat) cubic-bezier(.1,.9,.3,1) infinite}
@keyframes thump{0%{scale:1.03}100%{scale:1}}
.shk{position:absolute;inset:0}
.bg{animation:glow var(--beat) ease-out infinite}
@keyframes glow{0%{filter:brightness(1.6)}100%{filter:brightness(1)}}
.stage{position:absolute;inset:0;transform-origin:50% 48%;animation:punch .5s cubic-bezier(.2,1.4,.3,1) both,drift var(--d) linear both}
@keyframes punch{from{transform:scale(1.18)}to{transform:scale(1)}}
@keyframes drift{from{translate:0 0}to{translate:0 -24px}}
.shake{animation:shake .32s linear both}
@keyframes shake{0%{transform:translate(0,0)}20%{transform:translate(-14px,8px)}40%{transform:translate(12px,-10px)}
  60%{transform:translate(-8px,6px)}80%{transform:translate(6px,-4px)}100%{transform:translate(0,0)}}
/* cortina lima de transición al empezar cada escena */
.wipe{position:absolute;inset:0;background:var(--l);z-index:50;animation:wipe .34s cubic-bezier(.7,0,.3,1) both}
@keyframes wipe{0%{transform:translateX(0)}100%{transform:translateX(105%)}}
.flash{position:absolute;inset:0;background:#fff;z-index:49;opacity:0;pointer-events:none}
@keyframes flash{0%{opacity:.45}100%{opacity:0}}
.flash{background:radial-gradient(circle at 50% 50%,#f4ffd0 0%,rgba(198,244,50,.6) 45%,transparent 80%);mix-blend-mode:screen}
/* header y pie fijos de la marca */
.hd{position:absolute;left:70px;right:70px;top:120px;display:flex;align-items:center;justify-content:space-between;z-index:40}
.br{display:flex;align-items:center;gap:18px}
.br span{font-family:'Archivo Black';font-size:46px;line-height:.9;display:flex;flex-direction:column;letter-spacing:-.5px}
.br small{font-family:'Montserrat';font-weight:800;font-size:14px;letter-spacing:6px;color:var(--l);margin-top:7px}
.ig{font-weight:800;font-size:26px;letter-spacing:2px;color:#a9a9ad}
.bar{position:absolute;left:70px;right:70px;top:230px;height:8px;background:rgba(255,255,255,.12);z-index:40}
.bar i{position:absolute;left:0;top:0;bottom:0;background:var(--l);animation:barfill var(--d) linear both}
@keyframes barfill{from{width:var(--p0)}to{width:var(--p1)}}
.legal{position:absolute;left:60px;right:60px;top:256px;text-align:center;font-weight:700;font-size:19px;
  letter-spacing:1.5px;color:#8b8b8f;z-index:40}
/* tipografía */
.k{position:absolute;left:70px;right:70px;font-weight:900;text-transform:uppercase;line-height:1.0;letter-spacing:-2px;text-align:center}
.k .w{display:inline-block;margin:0 .12em;animation:slam .38s cubic-bezier(.2,1.6,.35,1) both}
@keyframes slam{0%{transform:scale(2.6) rotate(-6deg);opacity:0;filter:blur(12px)}100%{transform:none;opacity:1;filter:none}}
.k .hl{color:var(--l)}
.k .w .box{display:inline-block}
.k .box{background:var(--l);color:var(--bk);padding:4px 22px 10px;display:inline-block}
.eb{position:absolute;left:0;right:0;text-align:center;color:var(--l);font-weight:800;font-size:32px;letter-spacing:7px;
  text-transform:uppercase;animation:up .4s ease-out both}
@keyframes up{from{transform:translateY(40px);opacity:0}to{transform:none;opacity:1}}
.e{font-family:'Noto Color Emoji';font-weight:400;line-height:1;display:inline-block}
@keyframes bob{from{transform:translateY(0) rotate(-5deg)}to{transform:translateY(-26px) rotate(5deg)}}
@keyframes pop{0%{transform:scale(0) rotate(-12deg);opacity:0}70%{transform:scale(1.15) rotate(3deg);opacity:1}100%{transform:scale(1) rotate(0)}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes pulse{from{transform:scale(1)}to{transform:scale(1.07)}}
/* recuadro gris de producto (regla de marca) */
.tile{position:absolute;background:radial-gradient(circle 300px at 50% 45%,rgba(198,244,50,.14),transparent 100%),
  radial-gradient(ellipse at 50% 40%,#3A3A3E 0%,#232326 55%,#141416 100%);border:3px solid #2a2a2d;overflow:hidden}
.tile img{position:absolute;left:50%;top:50%;max-width:80%;max-height:80%;transform:translate(-50%,-50%);
  filter:drop-shadow(0 30px 40px rgba(0,0,0,.65))}
.tile .shine{position:absolute;top:-20%;bottom:-20%;width:30%;left:-40%;
  background:linear-gradient(100deg,transparent,rgba(255,255,255,.28),transparent);transform:skewX(-18deg)}
@keyframes shine{from{left:-40%}to{left:130%}}
.tile .ft{position:absolute;left:0;right:0;bottom:0;background:var(--l);color:var(--bk);text-align:center;padding:14px 10px 16px}
.tile .ft b{display:block;font-size:30px;font-weight:800;letter-spacing:.5px;text-transform:uppercase}
.tile .ft s{display:block;text-decoration:none;font-family:'Archivo Black';font-size:70px;line-height:1.05}
.ring{position:absolute;border:6px dashed rgba(198,244,50,.35);border-radius:50%;animation:spin 6s linear infinite}
.sq{position:absolute;width:var(--s);height:var(--s);background:var(--c);opacity:0}
@keyframes burst{0%{transform:translate(0,0) rotate(0) scale(1);opacity:0}2%{opacity:1}100%{transform:translate(var(--x),var(--y)) rotate(var(--r)) scale(.3);opacity:0}}
"""

JS = """
window.setTime = (t) => {
  for (const a of document.getAnimations()) { a.pause(); a.currentTime = t * 1000; }
  for (const e of document.querySelectorAll('[data-count]')) {
    const [a, b, s, d, dec] = e.dataset.count.split(',').map(Number);
    const k = Math.min(1, Math.max(0, (t - s) / d)), v = a + (b - a) * (1 - Math.pow(1 - k, 3));
    e.textContent = v.toFixed(dec).replace('.', ',');
  }
};
"""


def palabras(texto, t0=0.15, paso=0.11, clase=''):
    """Texto que entra palabra por palabra con golpe. *palabra* sale en lima; [palabra] sale en caja lima."""
    import re
    out, t = [], t0
    for w in texto.split():
        m = re.fullmatch(r'([¿¡"(]*)(\*|\[)(.+?)(\*|\])([?!.,:;")]*)', w)
        if m and (m.group(2), m.group(4)) in (('*', '*'), ('[', ']')):
            cls = 'hl' if m.group(2) == '*' else 'box'
            w = f'{m.group(1)}<span class="{cls}">{m.group(3)}</span>{m.group(5)}'
        out.append(f'<span class="w" style="animation-delay:{t:.2f}s">{w}</span>')
        t += paso
    return ''.join(out), t


def burst(x, y, t, n=18, seed=1, colores=('#C6F432', '#ffffff', '#C6F432')):
    """Explosión de cuadraditos de la marca en (x, y) en el segundo t."""
    r = random.Random(seed)
    out = []
    for i in range(n):
        ang = r.uniform(0, 6.283)
        dist = r.uniform(180, 460)
        import math
        out.append(f'<i class="sq" style="left:{x}px;top:{y}px;--s:{r.randint(14, 34)}px;--c:{r.choice(colores)};'
                   f'--x:{math.cos(ang) * dist:.0f}px;--y:{math.sin(ang) * dist:.0f}px;--r:{r.randint(-540, 540)}deg;'
                   f'animation:burst {r.uniform(.6, 1.0):.2f}s cubic-bezier(.1,.8,.3,1) {t:.2f}s both"></i>')
    return ''.join(out)


def flash(t):
    return f'<div class="flash" style="animation:flash .18s ease-out {t:.2f}s forwards"></div>'


def page(body, secs, ctx, css='', golpes=()):
    """Arma la página de una escena. ctx = {'t0', 'total', 'beat', 'primera'}. golpes = segundos con sacudón de cámara."""
    shk = (" style='animation:" + ",".join(f"shake .32s linear {t:.2f}s" for t in golpes) + "'") if golpes else ''

    p0 = ctx['t0'] / ctx['total'] * 100
    p1 = min(100, (ctx['t0'] + secs) / ctx['total'] * 100)
    v = f"--beat:{ctx.get('beat', 60 / MARCA.get('bpm', 124)):.4f}s;--d:{secs:.2f}s;--bk:{MARCA['negro']};--l:{MARCA['lima']};--p0:{p0:.2f}%;--p1:{p1:.2f}%"
    wipe = '' if ctx.get('primera') else '<div class="wipe"></div>'
    head = (f'<div class="hd"><div class="br">{MARK.format(s=72)}<span>BASE<small>SUPLEMENTOS</small></span></div>'
            f'<div class="ig">{MARCA["instagram"]}</div></div><div class="bar"><i></i></div>')
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONT_CSS}{BASE_CSS}{css}</style></head>"
            f"<body style='{v}'><div class='bg'></div><div class='grid'></div><div class='cam'><div class='beat'><div class='shk'{shk}><div class='stage'>{body}</div></div></div></div>"
            f"{head}<div class='legal'>{LEGAL}</div>{wipe}<script>{JS}</script></body></html>")


def render_scene(html, secs, dest, browser):
    """Filma la página y la guarda en un mp4 de exactamente `secs` segundos."""
    dest = Path(dest)
    tmp = dest.with_name(dest.stem + '.part.mp4')
    pg = browser.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
    pg.set_content(html, wait_until='load')
    pg.evaluate('document.fonts.ready')
    ff = subprocess.Popen([ffmpeg(), '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg',
                           '-i', '-', '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt', 'yuv420p',
                           '-r', str(FPS), str(tmp)], stdin=subprocess.PIPE)
    try:
        for f in range(int(round(secs * FPS))):
            pg.evaluate(f'setTime({f / FPS:.4f})')
            ff.stdin.write(pg.screenshot(type='jpeg', quality=92))
    finally:
        ff.stdin.close()
        ok = ff.wait() == 0
        pg.close()
    if not ok:
        raise RuntimeError(f'ffmpeg falló filmando {dest.name}')
    tmp.replace(dest)
    return dest


def snapshot(html, t, dest, browser):
    """Una foto de la escena en el segundo t (para revisar el diseño sin renderizar todo)."""
    pg = browser.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
    pg.set_content(html, wait_until='load')
    pg.evaluate('document.fonts.ready')
    pg.evaluate(f'setTime({t:.3f})')
    pg.screenshot(path=str(dest))
    pg.close()
