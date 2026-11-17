"""
Arma un reel de BASE (1080×1920, 30 fps, H.264 + AAC) desde un guion en JSON.

Uso:
  python videos/hacer_reel.py videos/guiones/ejemplo_creatina.json --out out/reel.mp4
  python videos/hacer_reel.py guion.json --preview out/preview     # solo fotos de cada escena para revisar (rápido)

Guion:
{
  "voz": false,                 # true = locución con voz sintética (ver README: licencia)
  "musica": true,               # base electrónica generada por código
  "escenas": [
    {"plantilla": "gancho", "dur": 2.4, "datos": {...}, "texto": "frase que se dice (solo si hay voz)"},
    ...
  ]
}
Plantillas y datos: ver videos/plantillas.py. Si "dur" falta, se usa la duración sugerida de la plantilla
(o lo que tarda la voz en decir "texto").
"""
import argparse, asyncio, json, shutil, subprocess, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from anim import render_scene, snapshot, ffmpeg, MARCA  # noqa: E402
from plantillas import PLANTILLAS, DURACION  # noqa: E402
import audio  # noqa: E402


def run(cmd):
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr[-2000:])
    return r.stderr


def dur_audio(p):
    import re
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', run([ffmpeg(), '-hide_banner', '-i', p, '-f', 'null', '-']))
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


async def _tts(text, path, voice, rate):
    import edge_tts
    for i in range(5):
        try:
            await edge_tts.Communicate(text, voice, rate=rate).save(str(path))
            if path.stat().st_size > 1000:
                return
        except Exception:
            if i == 4:
                raise
        await asyncio.sleep(4 * (i + 1))


def voces(escenas, work):
    """Una toma de voz por escena (sin silencios en las puntas). Devuelve [(wav, duración)]."""
    out = []
    for i, e in enumerate(escenas):
        mp3, wav = work / f'v{i}.mp3', work / f'v{i}.wav'
        asyncio.run(_tts(e['texto'], mp3, MARCA['voz'], MARCA.get('velocidad', '+10%')))
        run([ffmpeg(), '-v', 'error', '-y', '-i', mp3, '-af',
             'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,apad=pad_dur=0.15',
             '-ar', '48000', '-ac', '1', wav])
        out.append((wav, dur_audio(wav)))
    return out


def armar(guion, salida=None, preview=None):
    g = json.loads(Path(guion).read_text(encoding='utf-8'))
    escenas = g['escenas']
    for e in escenas:
        if e['plantilla'] not in PLANTILLAS:
            raise SystemExit(f"Plantilla desconocida: {e['plantilla']} (hay: {', '.join(PLANTILLAS)})")
    work = Path(tempfile.mkdtemp(prefix='reel_'))
    con_voz = bool(g.get('voz'))
    tomas = voces(escenas, work) if con_voz and not preview else None
    beat = 60 / MARCA.get('bpm', 124)
    durs = []
    for i, e in enumerate(escenas):
        d = float(e.get('dur') or DURACION[e['plantilla']])
        if tomas:
            d = max(d, tomas[i][1] + 0.2)
        # cada escena dura un número entero de beats → todos los cortes caen justo en el bombo
        nb = max(3, round(d / beat)) if not tomas else max(3, -(-d // beat))
        durs.append(round(nb * beat * 30) / 30)
    total = sum(durs)
    if not 3 <= total <= 90:
        raise SystemExit(f'El reel dura {total:.1f} s: tiene que durar entre 3 y 90 segundos (ideal 12–25).')

    from playwright.sync_api import sync_playwright
    clips, eventos, t0 = [], [], 0.0
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        for k, (e, d) in enumerate(zip(escenas, durs)):
            ctx = {'t0': t0, 'total': total, 'primera': k == 0, 'beat': beat}
            html, snd = PLANTILLAS[e['plantilla']](d, ctx, **e.get('datos', {}))
            eventos += [(t0 + t, tipo) for t, tipo in snd if t < d]
            if preview:
                Path(preview).mkdir(parents=True, exist_ok=True)
                for j, frac in enumerate((0.35, 0.95)):
                    snapshot(html, d * frac, Path(preview) / f'escena{k + 1}_{j + 1}.png', br)
            else:
                clips.append(render_scene(html, d, work / f'e{k + 1}.mp4', br))
                print(f'escena {k + 1}/{len(escenas)} ({e["plantilla"]}, {d:.1f} s) lista', flush=True)
            t0 += d
        br.close()
    if preview:
        print('Fotos de revisión en', preview)
        return

    lst = work / 'lista.txt'
    lst.write_text(''.join(f"file '{c.as_posix()}'\n" for c in clips))
    video = work / 'video.mp4'
    run([ffmpeg(), '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', video])

    pista = audio.pista(total, eventos, MARCA.get('bpm', 124), g.get('musica', True))
    if tomas:
        import numpy as np, wave
        voz = []
        for (wav, dv), d in zip(tomas, durs):
            with wave.open(str(wav)) as w:
                x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float) / 32768
            seg = np.zeros(int(d * audio.SR)); seg[:min(len(x), len(seg))] = x[:len(seg)]
            voz.append(seg)
        v = np.concatenate(voz)[:len(pista)]
        v = np.pad(v, (0, len(pista) - len(v)))
        env = np.convolve(np.abs(v), np.ones(4800) / 4800, mode='same')
        pista = pista * np.where(env > 0.02, 0.35, 0.8) + v * 1.1
        pista = np.tanh(pista * 1.1) * .9
    wav = work / 'audio.wav'
    audio.guardar(pista, wav)
    out = Path(salida or Path(guion).with_suffix('.mp4'))
    out.parent.mkdir(parents=True, exist_ok=True)
    run([ffmpeg(), '-v', 'error', '-y', '-i', video, '-i', wav, '-map', '0:v', '-map', '1:a', '-t', f'{total:.2f}',
         '-c:v', 'libx264', '-crf', '19', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-profile:v', 'high',
         '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out])
    shutil.rmtree(work, ignore_errors=True)
    print(f'Listo: {out} ({total:.1f} s)')
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('guion')
    ap.add_argument('--out')
    ap.add_argument('--preview')
    a = ap.parse_args()
    armar(a.guion, a.out, a.preview)
