"""
Audio generado por código (100 % propio, sin derechos de terceros): una base electrónica a tempo y efectos
sincronizados con las animaciones (golpes, swipes, pops, cuenta regresiva).
"""
import wave
import numpy as np

SR = 48000
rng = np.random.default_rng(7)


def _env(n, a=0.002, r=0.2):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / max(r, 1e-4))
    return e


def _sine(f, n, f2=None):
    t = np.arange(n) / SR
    if f2 is None:
        return np.sin(2 * np.pi * f * t)
    k = np.log(f2 / f) / (n / SR)
    return np.sin(2 * np.pi * f * (np.exp(k * t) - 1) / k)


def _noise(n):
    return rng.uniform(-1, 1, n)


def _lp(x, alpha):
    y = np.empty_like(x)
    acc = 0.0
    for i, v in enumerate(x):
        acc += alpha * (v - acc)
        y[i] = acc
    return y


def kick(n=int(.35 * SR)):
    return _sine(150, n, 42) * _env(n, .001, .12) * 1.0


def clap(n=int(.22 * SR)):
    x = _noise(n)
    x = x - _lp(x, .25)
    return x * _env(n, .001, .05) * .45


def hat(n=int(.06 * SR)):
    x = _noise(n)
    x = x - _lp(x, .6)
    return x * _env(n, .0005, .012) * .22


def bass(f, n):
    t = np.arange(n) / SR
    x = np.sign(np.sin(2 * np.pi * f * t)) * .5 + np.sin(2 * np.pi * f * t) * .5
    return _lp(x, .08) * _env(n, .005, .25) * .38


SFX = {}


def _sfx(nombre):
    if nombre in SFX:
        return SFX[nombre]
    if nombre == 'whoosh':
        n = int(.45 * SR)
        x = _noise(n)
        alphas = np.linspace(.02, .35, n)
        y = np.empty(n); acc = 0.0
        for i in range(n):
            acc += alphas[i] * (x[i] - acc); y[i] = acc
        s = y * np.sin(np.linspace(0, np.pi, n)) * .9
    elif nombre == 'swipe':
        n = int(.22 * SR)
        x = _noise(n); s = (x - _lp(x, .3)) * np.sin(np.linspace(0, np.pi, n)) * .35
    elif nombre == 'hit':
        n = int(.6 * SR)
        s = _sine(110, n, 35) * _env(n, .001, .18) * 1.0 + _lp(_noise(n), .2) * _env(n, .001, .06) * .6
    elif nombre == 'stamp':
        n = int(.35 * SR)
        s = _sine(220, n, 60) * _env(n, .001, .08) * .8 + _noise(n) * _env(n, .001, .02) * .35
    elif nombre == 'pop':
        n = int(.12 * SR)
        s = _sine(900, n, 300) * _env(n, .001, .04) * .45
    elif nombre == 'tick':
        n = int(.08 * SR)
        s = _sine(1800, n) * _env(n, .0005, .015) * .35
    elif nombre == 'ding':
        n = int(.9 * SR)
        s = (_sine(1318, n) * .5 + _sine(1976, n) * .3) * _env(n, .002, .3) * .55
    elif nombre == 'riser':
        n = int(1.2 * SR)
        x = _noise(n); s = (x - _lp(x, .15)) * np.linspace(0, 1, n) ** 2 * .3 + _sine(200, n, 800) * np.linspace(0, 1, n) ** 2 * .12
    else:
        s = np.zeros(1)
    SFX[nombre] = s.astype(np.float64)
    return SFX[nombre]


def _add(buf, x, t):
    i = int(t * SR)
    if i >= len(buf) or i < 0:
        return
    j = min(len(buf), i + len(x))
    buf[i:j] += x[:j - i]


def pista(total, eventos, bpm=124, musica=True):
    """Devuelve el audio (float, mono) de `total` segundos: base a `bpm` + efectos en (segundo, tipo)."""
    n = int(total * SR) + SR
    mus = np.zeros(n)
    fx = np.zeros(n)
    if musica:
        beat = 60 / bpm
        notas = [55.0, 55.0, 65.41, 49.0]  # La, La, Do, Sol (graves)
        k, hk, ck, b = kick(), hat(), clap(), 0
        t = 0.0
        while t < total + beat:
            _add(mus, k, t)
            if b % 2 == 1:
                _add(mus, ck, t)
            _add(mus, hk, t + beat / 2)
            if b % 4 == 0:
                _add(mus, bass(notas[(b // 4) % 4], int(beat * 4 * SR)), t)
            t += beat
            b += 1
        # bombeo (sidechain) en cada negra para que "respire"
        tt = np.arange(n) / SR
        fase = (tt % beat) / beat
        mus *= 0.55 + 0.45 * np.minimum(1, fase * 4)
        mus *= .55
    for t, tipo in eventos:
        _add(fx, _sfx(tipo), t)
    y = mus + fx
    y = y[:int(total * SR)]
    # fundidos
    f = int(.08 * SR)
    y[:f] *= np.linspace(0, 1, f)
    y[-int(.4 * SR):] *= np.linspace(1, 0, int(.4 * SR))
    pk = np.max(np.abs(y)) or 1
    return np.tanh(y / pk * 1.4) * .89


def guardar(y, ruta):
    d = (np.clip(y, -1, 1) * 32767).astype(np.int16)
    est = np.repeat(d[:, None], 2, axis=1)
    with wave.open(str(ruta), 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(est.tobytes())
