"""Le pone la VOZ DE VALENTÍN a los reels de la cola que todavía no la tienen (lo corre el workflow «voz»).

Para cada queue/AAAA-MM-DD/ de hoy en adelante (hora Argentina) con reel.mp4, guion *_reel.json con
"voz_propia": true, sin voz.ok y con el reel todavía sin publicar:
  python videos/locucion.py <guion> reel.mp4 reel_voz.mp4 [--tomas queue/…/voz]
y reemplaza reel.mp4 por la versión con voz. Deja voz.ok para no repetirlo.
Si no hay ELEVENLABS_API_KEY ni tomas grabadas, no toca nada (el reel sale sin voz).
"""
import datetime, glob, json, os, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
hoy = (datetime.datetime.utcnow() - datetime.timedelta(hours=3)).date().isoformat()
hechos = 0
for d in sorted(glob.glob(os.path.join(RAIZ, 'queue', '20*'))):
    fecha = os.path.basename(d)
    if fecha < hoy or os.path.exists(os.path.join(d, 'voz.ok')):
        continue
    reel = os.path.join(d, 'reel.mp4')
    guiones = glob.glob(os.path.join(d, '*_reel.json'))
    if not (os.path.exists(reel) and guiones):
        continue
    g = json.load(open(guiones[0], encoding='utf-8'))
    if not g.get('voz_propia'):
        continue
    est = os.path.join(d, 'estado.json')
    if os.path.exists(est) and 'reel' in json.load(open(est, encoding='utf-8')):
        continue
    tomas = os.path.join(d, 'voz')
    if not os.environ.get('ELEVENLABS_API_KEY') and not os.path.isdir(tomas):
        print(f'{fecha}: sin ELEVENLABS_API_KEY ni tomas grabadas → el reel queda sin voz')
        continue
    salida = os.path.join(d, 'reel_voz.mp4')
    cmd = [sys.executable, os.path.join(RAIZ, 'videos', 'locucion.py'), guiones[0], reel, salida]
    if os.path.isdir(tomas):
        cmd += ['--tomas', tomas]
    print(f'== {fecha}')
    r = subprocess.run(cmd)
    if r.returncode != 0 or not os.path.exists(salida):
        print(f'{fecha}: falló la voz, el reel queda como estaba')
        continue
    os.replace(salida, reel)
    open(os.path.join(d, 'voz.ok'), 'w').write(f'voz de Valentín agregada {datetime.datetime.utcnow().isoformat()}Z\n')
    hechos += 1
print(f'Reels con voz nuevos: {hechos}')
