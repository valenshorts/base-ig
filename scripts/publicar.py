"""Publica en Instagram las publicaciones APROBADAS (las que ya están en la rama main).

- Con plan.json: cada contenido (post, historia o reel) sale a partir de su hora (hora Argentina).
  Las historias solo salen el día que corresponden; los posts y reels atrasados salen igual.
- Formato viejo: la historia sale apenas se aprueba (si es del día) y el post a partir de HORA_POST (19:30).
- Guarda queue/AAAA-MM-DD/estado.json para no publicar dos veces.

Variables de entorno (en GitHub van como Secrets / Variables):
  IG_USER_ID      ID de la cuenta profesional de Instagram (número)
  IG_TOKEN        token de acceso con permiso instagram_content_publish
  GRAPH_VERSION   opcional, por defecto v21.0
  MEDIA_BASE_URL  opcional, URL pública desde donde Instagram baja las imágenes.
                  Por defecto: https://raw.githubusercontent.com/$GITHUB_REPOSITORY/$GITHUB_SHA
  HORA_POST       opcional, por defecto 19:30
  DRY_RUN=1       no publica nada, solo muestra qué haría
  VERIFICAR=1     solo prueba el token y el ID (no publica)
  Nunca publica entre las 00:00 y las 09:00 (hora Argentina), aunque GitHub demore una corrida.
  AHORA           opcional, solo para pruebas: simula la hora (ej. 2026-11-14T16:00)
"""
import datetime as dt, json, os, sys, time
import requests

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLA = os.path.join(RAIZ, 'queue')
ART = dt.timezone(dt.timedelta(hours=-3))  # Argentina no usa horario de verano
DRY = os.environ.get('DRY_RUN') == '1'
VER = os.environ.get('GRAPH_VERSION', 'v21.0')
API = f'https://graph.facebook.com/{VER}'


def base_url():
    b = os.environ.get('MEDIA_BASE_URL')
    if b:
        return b.rstrip('/')
    return f"https://raw.githubusercontent.com/{os.environ['GITHUB_REPOSITORY']}/{os.environ['GITHUB_SHA']}"


def api(method, path, **params):
    if DRY:
        print(f'  [simulado] {method} {path} {dict((k, v) for k, v in params.items() if k != "caption")}')
        return {'id': f'sim_{int(time.time() * 1000) % 10**8}', 'status_code': 'FINISHED'}
    params['access_token'] = os.environ['IG_TOKEN']
    r = requests.request(method, f'{API}/{path}', data=params if method == 'POST' else None,
                         params=params if method == 'GET' else None, timeout=60)
    j = r.json()
    if r.status_code >= 400 or 'error' in j:
        raise RuntimeError(f'Error de la API de Instagram en {path}: {j.get("error", j)}')
    return j


def esperar(cid, intentos=30, pausa=4):
    for _ in range(intentos):
        st = api('GET', cid, fields='status_code').get('status_code')
        if st == 'FINISHED':
            return
        if st in ('ERROR', 'EXPIRED'):
            raise RuntimeError(f'Instagram no pudo procesar el contenedor {cid} ({st}).')
        time.sleep(pausa)
    raise RuntimeError(f'El contenedor {cid} no terminó de procesarse a tiempo.')


def crear(intentos=30, pausa=4, **p):
    cid = api('POST', f"{os.environ.get('IG_USER_ID', 'IG_USER_ID')}/media", **p)['id']
    esperar(cid, intentos, pausa)
    return cid


def publicar_contenedor(cid):
    return api('POST', f"{os.environ.get('IG_USER_ID', 'IG_USER_ID')}/media_publish", creation_id=cid)['id']


def url(carpeta, archivo):
    if archivo.endswith('.mp4') and not os.environ.get('MEDIA_BASE_URL'):
        # raw.githubusercontent.com sirve los videos sin tipo «video/mp4»; jsDelivr sí (y es un CDN)
        return f"https://cdn.jsdelivr.net/gh/{os.environ['GITHUB_REPOSITORY']}@{os.environ['GITHUB_SHA']}/queue/{carpeta}/{archivo}"
    return f'{base_url()}/queue/{carpeta}/{archivo}'


def publicar_historia(carpeta, archivo='historia.jpg'):
    return publicar_contenedor(crear(media_type='STORIES', image_url=url(carpeta, archivo)))


def publicar_post(carpeta, posts, texto):
    if len(posts) == 1:
        cid = crear(image_url=url(carpeta, posts[0]), caption=texto)
    else:
        hijos = [crear(image_url=url(carpeta, p), is_carousel_item='true') for p in posts]
        cid = crear(media_type='CAROUSEL', children=','.join(hijos), caption=texto)
    return publicar_contenedor(cid)


def publicar_reel(carpeta, video, texto):
    # Los videos tardan más en procesarse: hasta ~6 minutos
    cid = crear(intentos=60, pausa=6, media_type='REELS', video_url=url(carpeta, video), caption=texto, share_to_feed='true')
    return publicar_contenedor(cid)


def verificar():
    ig = os.environ.get('IG_USER_ID', '')
    j = api('GET', ig, fields='username,name')
    print(f"Conexión OK con Instagram: @{j.get('username')} ({j.get('name')}) · id {ig}")


def leer(d, nom):
    return open(os.path.join(d, nom), encoding='utf-8').read().strip()


def dia_con_plan(carpeta, d, fecha, hoy, ahora, estado):
    """Publica los contenidos de plan.json cuya hora ya llegó. Devuelve la cantidad de fallas."""
    plan = json.load(open(os.path.join(d, 'plan.json'), encoding='utf-8'))
    fallas = 0
    hechos = set()  # como máximo uno de cada tipo por corrida, así los atrasados salen espaciados (cada ~30 min)
    for it in sorted(plan['items'], key=lambda x: x['hora']):
        iid, tipo = it['id'], it['tipo']
        if iid in estado:
            continue
        if tipo in hechos:
            print(f'  {tipo} «{iid}»: atrasado, sale en la próxima corrida.')
            continue
        hh, mm = map(int, it['hora'].split(':'))
        momento = dt.datetime.combine(fecha, dt.time(hh, mm), ART)
        if ahora < momento:
            print(f'  {it["hora"]} {tipo} «{iid}»: programado.')
            continue
        try:
            if tipo == 'historia':
                if fecha != hoy:
                    estado[iid] = {'omitida': 'se aprobó después de su día'}
                    print(f'  historia «{iid}»: omitida (era de otro día).')
                    continue
                pid = publicar_historia(carpeta, it['imagen'])
            elif tipo == 'post':
                pid = publicar_post(carpeta, it['imagenes'], leer(d, it['texto']))
            elif tipo == 'reel':
                pid = publicar_reel(carpeta, it['video'], leer(d, it['texto']))
            else:
                raise RuntimeError(f'tipo desconocido {tipo}')
            estado[iid] = {'id': pid, 'hora': ahora.isoformat(timespec='minutes')}
            hechos.add(tipo)
            print(f'  {tipo} «{iid}» publicado.')
        except Exception as e:
            fallas += 1
            print(f'  ERROR en {tipo} «{iid}»: {e}')
    return fallas


def dia_simple(carpeta, d, fecha, hoy, ahora, estado, hh, mm):
    archivos = os.listdir(d)
    posts = sorted([a for a in archivos if a.startswith('post_') and a.endswith('.jpg')], key=lambda a: int(a[5:-4]))
    try:
        if 'historia.jpg' in archivos and 'historia' not in estado:
            if fecha == hoy:
                estado['historia'] = {'id': publicar_historia(carpeta), 'hora': ahora.isoformat(timespec='minutes')}
                print('  Historia publicada.')
            else:
                estado['historia'] = {'omitida': 'se aprobó después de su día'}
        if posts and 'post' not in estado:
            if ahora >= dt.datetime.combine(fecha, dt.time(hh, mm), ART):
                estado['post'] = {'id': publicar_post(carpeta, posts, leer(d, 'texto.txt')), 'hora': ahora.isoformat(timespec='minutes')}
                print('  Post publicado.')
            else:
                print(f'  El post queda programado para las {hh:02d}:{mm:02d}.')
        return 0
    except Exception as e:
        print(f'  ERROR: {e}')
        return 1


def main():
    if os.environ.get('VERIFICAR') == '1':
        verificar()
        return
    ahora = dt.datetime.fromisoformat(os.environ['AHORA']).replace(tzinfo=ART) if os.environ.get('AHORA') else dt.datetime.now(ART)
    hoy = ahora.date()
    hh, mm = map(int, os.environ.get('HORA_POST', '19:30').split(':'))
    if ahora.hour < 9:
        # Freno nocturno: si GitHub demora una corrida y cae de madrugada, no se publica nada
        print(f'Son las {ahora:%H:%M} en Argentina: no se publica entre las 00:00 y las 09:00.')
        return
    fallas = 0
    for carpeta in sorted(os.listdir(COLA)) if os.path.isdir(COLA) else []:
        try:
            fecha = dt.date.fromisoformat(carpeta[:10])
        except ValueError:
            continue
        if fecha > hoy or (hoy - fecha).days > 3:
            continue
        d = os.path.join(COLA, carpeta)
        ruta_estado = os.path.join(d, 'estado.json')
        estado = json.load(open(ruta_estado)) if os.path.exists(ruta_estado) else {}
        print(f'— {carpeta} (ya publicado: {", ".join(estado) or "nada"})')
        if os.path.exists(os.path.join(d, 'plan.json')):
            fallas += dia_con_plan(carpeta, d, fecha, hoy, ahora, estado)
        else:
            fallas += dia_simple(carpeta, d, fecha, hoy, ahora, estado, hh, mm)
        if not DRY:
            json.dump(estado, open(ruta_estado, 'w'), ensure_ascii=False, indent=1)
    sys.exit(1 if fallas else 0)


if __name__ == '__main__':
    main()
