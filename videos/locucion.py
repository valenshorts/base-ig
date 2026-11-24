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
import argparse, json, os, subprocess, sys, tempfile, urllib.request, urllib.error

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
            f'https://{host}/v1/text-to-speech/{VOICE_ID}?output_format=mp3_44100_128',
            data=json.dumps(cuerpo).encode(), method='POST',
            headers={'xi-api-key': key, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                open(dst, 'wb').write(r.read())
            return modelo
        except urllib.error.HTTPError as e:
            ultimo = f'{host} {modelo}: HTTP {e.code} {e.read()[:200]!r}'
            print('  probando otro modelo →', ultimo)
    raise SystemExit('ElevenLabs no generó la voz: ' + str(ultimo))


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
        if grabada and os.path.exists(grabada):
            crudo = grabada
        else:
            m = tts(esc[i]['voz'], ' '.join(frases[:k])[-300:], ' '.join(frases[k + 1:])[:300], crudo)
            print(f'  escena {i + 1}: voz generada ({m})')
        limpio = os.path.join(tmp, f'v{i}.wav')
        # sin silencios en las puntas
        run('ffmpeg', '-v', 'error', '-y', '-i', crudo, '-af',
            'silenceremove=start_periods=1:start_threshold=-40dB,areverse,silenceremove=start_periods=1:start_threshold=-40dB,areverse',
            '-ar', '44100', '-ac', '2', limpio)
        tomas.append((i, t0, fin, limpio, duracion(limpio)))

    # que ninguna frase pise a la siguiente: si no entra, se acelera un poco (máx. 15 %) y si igual no entra, avisa
    filtros, etiquetas, total = [], [], duracion(a.video)
    for k, (i, t0, fin, f, d) in enumerate(tomas):
        limite = (tomas[k + 1][1] - 0.08) if k + 1 < len(tomas) else total - 0.15
        lugar = limite - t0
        tempo = 1.0
        if d > lugar:
            tempo = min(1.15, d / lugar)
            if d / tempo > lugar + 0.05:
                print(f'  ⚠ escena {i + 1}: la frase dura {d:.2f} s y entra en {lugar:.2f} s → alargá la escena o acortá la frase')
        ms = int(t0 * 1000)
        filtros.append(f'[{k + 1}:a]atempo={tempo:.3f},afade=t=in:d=0.02,adelay={ms}|{ms}[v{k}]')
        etiquetas.append(f'[v{k}]')
        print(f'  escena {i + 1}: {t0:5.2f}s → {t0 + d / tempo:5.2f}s  «{esc[i]["voz"]}»')
    filtros.append(''.join(etiquetas) + f'amix=inputs={len(tomas)}:normalize=0,volume=1.6,asplit=2[voz][sc]')
    filtros.append('[0:a]volume=0.9[mus];[mus][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=300[duck]')
    filtros.append('[duck][voz]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]')
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', a.video]
    for _, _, _, f, _ in tomas:
        cmd += ['-i', f]
    cmd += ['-filter_complex', ';'.join(filtros), '-map', '0:v', '-map', '[a]', '-c:v', 'copy',
            '-c:a', 'aac', '-b:a', '192k', '-shortest', a.salida]
    subprocess.run(cmd, check=True)
    print('Listo:', a.salida)


if __name__ == '__main__':
    main()
