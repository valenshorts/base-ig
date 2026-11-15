"""Dice cuántos segundos faltan para lo próximo que hay que publicar (lo usa vigia.sh).

Imprime 60 si ya hay algo vencido, los segundos hasta la próxima pieza pendiente,
o nada si no queda nada pendiente en la cola.
"""
import datetime as dt
import json
import os

ART = dt.timezone(dt.timedelta(hours=-3))
COLA = 'queue'

ahora = dt.datetime.fromisoformat(os.environ['AHORA']).replace(tzinfo=ART) if os.environ.get('AHORA') else dt.datetime.now(ART)
hoy = ahora.date()
proximo = None
for carpeta in sorted(os.listdir(COLA)) if os.path.isdir(COLA) else []:
    try:
        fecha = dt.date.fromisoformat(carpeta[:10])
    except ValueError:
        continue
    d = os.path.join(COLA, carpeta)
    if (hoy - fecha).days > 3 or not os.path.exists(os.path.join(d, 'plan.json')):
        continue
    plan = json.load(open(os.path.join(d, 'plan.json'), encoding='utf-8'))
    ruta = os.path.join(d, 'estado.json')
    estado = json.load(open(ruta)) if os.path.exists(ruta) else {}
    for it in plan['items']:
        if it['id'] in estado:
            continue
        if it['tipo'] == 'historia' and fecha < hoy:
            continue  # historias de días pasados no salen
        hh, mm = map(int, it['hora'].split(':'))
        momento = dt.datetime.combine(fecha, dt.time(hh, mm), ART)
        if momento.hour < 9:
            momento = momento.replace(hour=9, minute=0)  # freno nocturno
        if proximo is None or momento < proximo:
            proximo = momento

if proximo is not None:
    print(max(60, int((proximo - ahora).total_seconds()) + 30))
