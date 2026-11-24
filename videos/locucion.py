"""Locución con la VOZ DE VALENTÍN (ElevenLabs, voz clonada «Valentin») sobre un reel ya renderizado.

Uso:
  python videos/locucion.py GUION.json REEL_SIN_VOZ.mp4 SALIDA.mp4 [--tomas DIR]

GUION.json es el mismo guion de hacer_reel.py, con "voz_propia": true y, en cada escena que habla,
"voz": "frase que se dice en esa escena".

De dónde sale cada toma (en este orden):
  1. --tomas DIR con archivos escena1.mp3, escena2.mp3… (por ejemplo generados a mano en ElevenLabs).
  2. API de ElevenLabs con la variable de entorno ELEVENLABS_API_KEY (secreto de GitHub, NUNCA en el repo).

Cada frase arranca 0,1 s después del comienzo de su escena. En un quiz arranca recién cuando se
revela la respuesta (para no adelantarla). La música baja sola mientras habla (sidechain).
"""
import argparse, base64, json, os, re, subprocess, sys, tempfile, urllib.request, urllib.error

AQUI = os.path.dirname(os.path.abspath(__file__))
MARCA = json.load(open(os.path.join(AQUI, 'marca.json'), encoding='utf-8'))
VOZ = MARCA.get('voz_valentin', {})
VOICE_ID = os.environ.get('ELEVENLABS_VOICE_ID') or VOZ.get('voice_id', 'qmpwT5HT1XfyskglZrAE')
MODELOS = [m for m in [os.environ.get('ELEVENLABS_MODEL')] + VOZ.get('modelos', ['eleven_v3', 'eleven_multilingual_v2']) if m]
BEAT = 60 / MARCA.get('bpm', 124)
HOSTS = ['api.elevenlabs.io', 'api.us.elevenlabs.io']   # la cuenta de Valentín usa api.us


def run(*a):
    subprocess.run(a, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def duracion(f):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))


def tts(texto, previo, siguiente, dst):
    key = os.environ.get('ELEVENLABS_API_KEY')
    if not key:
        raise SystemExit('Falta ELEVENLABS_API_KEY (y no hay tomas grabadas).')
    ultimo = None
    for host, modelo in [(h, m) for h in HOSTS for m in MODELOS]:
        cuerpo = {'text': texto, 'model_id': modelo,
                  'voice_settings': {'stability': VOZ.get('stability', 0.5), 'similarity_boost': VOZ.get('similarity', 0.75)}}
        if modelo != 'eleven_v3':   # v3 no acepta texto previo/siguiente
            cuerpo.update(previous_text=previo or None, next_text=siguiente or None)
        req = urllib.request.Request(
            f'https://{host}/v1/text-to-speech/{VOICE_ID}/with-timestamps?output_format=mp3_44100_128',
            data=json.dumps(cuerpo).encode(), method='POST',
            headers={'xi-api-key': key, 'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                res = json.loads(r.read())
            open(dst, 'wb').write(base64.b64decode(res['audio_base64']))
            return modelo, palabras_de(res.get('alignment') or res.get('normalized_alignment'))
        except urllib.error.HTTPError as e:
            ultimo = f'{host} {modelo}: HTTP {e.code} {e.read()[:200]!r}'
            print('  probando otro modelo →', ultimo)
    raise SystemExit('ElevenLabs no generó la voz: ' + str(ultimo))


def palabras_de(al):
    """alignment de ElevenLabs (caracteres con tiempos) → [(palabra, inicio, fin)]."""
    if not al:
        return None
    out, w, t0, t1 = [], '', None, None
    for c, a, b in zip(al['characters'], al['character_start_times_seconds'], al['character_end_times_seconds']):
        if c.isspace():
            if w:
                out.append((w, t0, t1))
            w, t0 = '', None
            continue
        if t0 is None:
            t0 = a
        w += c; t1 = b
    if w:
        out.append((w, t0, t1))
    return out or None


def estimar(texto, d):
    """Sin timestamps (tomas grabadas): reparte la duración según el largo de cada palabra."""
    ws = texto.split()
    pesos = [len(x) + 2 for x in ws]
    tot, t, out = sum(pesos), 0.0, []
    for x, p in zip(ws, pesos):
        dd = d * p / tot
        out.append((x, t, t + dd)); t += dd
    return out


def ass_tiempo(t):
    t = max(0, t)
    return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'


def subtitulos_ass(palabras, ruta, total):
    """Subtítulos estilo reel: 1 o 2 palabras por vez, en mayúsculas, la palabra que se dice en lima."""
    grupos, g = [], []
    for w in palabras:
        g.append(w)
        if len(g) == 2 or re.search(r'[.,;:?!¿¡]$', w[0]):
            grupos.append(g); g = []
    if g:
        grupos.append(g)
    lim = lambda x: x.upper().replace('{', '').replace('}', '')
    ev = []
    for k, g in enumerate(grupos):
        fin_g = min(g[-1][2] + 0.35, grupos[k + 1][0][1] if k + 1 < len(grupos) else total)
        for i, (w, a, b) in enumerate(g):
            hasta = g[i + 1][1] if i + 1 < len(g) else fin_g
            txt = ' '.join(('{\\c&H32F4C6&}' + lim(x) + '{\\c&HFFFFFF&}') if j == i else lim(x) for j, (x, _, _) in enumerate(g))
            ev.append(f'Dialogue: 0,{ass_tiempo(a)},{ass_tiempo(max(hasta, a + 0.05))},Sub,,0,0,0,,{txt}')
    cab = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Archivo Black,80,&H00FFFFFF,&H00FFFFFF,&H280C0B0B,&H00000000,0,0,0,0,100,100,1,0,3,14,0,2,60,60,215,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    open(ruta, 'w', encoding='utf-8').write(cab + '\n'.join(ev) + '\n')


def arranques(escenas):
    """[(indice, segundo_de_arranque_de_la_voz, fin_de_la_escena)] para cada escena con "voz"."""
    t, out = 0.0, []
    for i, e in enumerate(escenas):
        d = e['dur']
        if e.get('voz'):
            off = 0.1
            if e['plantilla'] == 'quiz':
                off = e['datos'].get('revelar') or (d - 2.5 * BEAT)
                off += 0.07
            out.append((i, t + off, t + d))
        t += d
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('guion'); ap.add_argument('video'); ap.add_argument('salida')
    ap.add_argument('--tomas', help='carpeta con escenaN.mp3 ya grabadas')
    a = ap.parse_args()
    g = json.load(open(a.guion, encoding='utf-8'))
    esc = g['escenas']
    plan = arranques(esc)
    if not plan:
        raise SystemExit('El guion no tiene ninguna escena con "voz".')
    frases = [esc[i]['voz'] for i, _, _ in plan]
    tmp = tempfile.mkdtemp()
    tomas = []
    for k, (i, t0, fin) in enumerate(plan):
        crudo = os.path.join(tmp, f'c{i}.mp3')
        grabada = a.tomas and os.path.join(a.tomas, f'escena{i + 1}.mp3')
        pal = None
        if grabada and os.path.exists(grabada):
            crudo = grabada
        else:
            m, pal = tts(esc[i]['voz'], ' '.join(frases[:k])[-300:], ' '.join(frases[k + 1:])[:300], crudo)
            print(f'  escena {i + 1}: voz generada ({m})')
        limpio = os.path.join(tmp, f'v{i}.wav')
        # sin silencios en las puntas
        run('ffmpeg', '-v', 'error', '-y', '-i', crudo, '-af',
            'silenceremove=start_periods=1:start_threshold=-40dB,areverse,silenceremove=start_periods=1:start_threshold=-40dB,areverse',
            '-ar', '44100', '-ac', '2', limpio)
        dl = duracion(limpio)
        if pal:   # pasar los tiempos al audio recortado: del inicio de la 1.ª palabra al final de la última
            a0, a1 = pal[0][1], pal[-1][2]
            f = dl / max(a1 - a0, 0.1)
            pal = [(w, (a - a0) * f, (b - a0) * f) for w, a, b in pal]
        else:
            pal = estimar(esc[i]['voz'], dl)
        tomas.append((i, t0, fin, limpio, dl, pal))

    # que ninguna frase pise a la siguiente: si no entra, se acelera un poco (máx. 15 %) y si igual no entra, avisa
    filtros, etiquetas, total = [], [], duracion(a.video)
    todas = []
    for k, (i, t0, fin, f, d, pal) in enumerate(tomas):
        limite = (tomas[k + 1][1] - 0.08) if k + 1 < len(tomas) else total - 0.15
        lugar = limite - t0
        tempo = 1.0
        if d > lugar:
            tempo = min(1.15, d / lugar)
            if d / tempo > lugar + 0.05:
                print(f'  ⚠ escena {i + 1}: la frase dura {d:.2f} s y entra en {lugar:.2f} s → alargá la escena o acortá la frase')
        todas += [(w, t0 + a / tempo, t0 + b / tempo) for w, a, b in pal]
        ms = int(t0 * 1000)
        filtros.append(f'[{k + 1}:a]atempo={tempo:.3f},afade=t=in:d=0.02,adelay={ms}|{ms}[v{k}]')
        etiquetas.append(f'[v{k}]')
        print(f'  escena {i + 1}: {t0:5.2f}s → {t0 + d / tempo:5.2f}s  «{esc[i]["voz"]}»')
    filtros.append(''.join(etiquetas) + f'amix=inputs={len(tomas)}:normalize=0,volume=1.6,asplit=2[voz][sc]')
    filtros.append('[0:a]volume=0.9[mus];[mus][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=300[duck]')
    filtros.append('[duck][voz]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]')
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', a.video]
    for _, _, _, f, _, _ in tomas:
        cmd += ['-i', f]
    if g.get('subtitulos', True):
        ass = os.path.join(tmp, 'subs.ass')
        subtitulos_ass(todas, ass, total)
        fuentes = os.path.join(AQUI, 'fonts')
        filtros.append(f"[0:v]ass={ass}:fontsdir={fuentes}[vid]")
        vmap, vcod = '[vid]', ['-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-movflags', '+faststart']
    else:
        vmap, vcod = '0:v', ['-c:v', 'copy']
    cmd += ['-filter_complex', ';'.join(filtros), '-map', vmap, '-map', '[a]', *vcod,
            '-c:a', 'aac', '-b:a', '192k', '-shortest', a.salida]
    subprocess.run(cmd, check=True)
    print('Listo:', a.salida)


if __name__ == '__main__':
    main()
