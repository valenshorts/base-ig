"""Publica en Instagram las publicaciones APROBADAS (las que ya están en la rama main).

- La historia sale apenas se aprueba (si es del día).
- El post sale a partir de HORA_POST (19:30 hora Argentina) del día de la carpeta.
- Guarda queue/AAAA-MM-DD/estado.json para no publicar dos veces.

Variables de entorno (en GitHub van como Secrets / Variables):
  IG_USER_ID      ID de la cuenta profesional de Instagram (número)
  IG_TOKEN        token de acceso con permiso instagram_content_publish
  GRAPH_VERSION   opcional, por defecto v21.0
  MEDIA_BASE_URL  opcional, URL pública desde donde Instagram baja las imágenes.
                  Por defecto: https://raw.githubusercontent.com/$GITHUB_REPOSITORY/$GITHUB_SHA
  HORA_POST       opcional, por defecto 19:30
  DRY_RUN=1       no publica nada, solo muestra qué haría
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


def esperar(cid):
    for _ in range(30):
        st = api('GET', cid, fields='status_code').get('status_code')
        if st == 'FINISHED':
            return
        if st in ('ERROR', 'EXPIRED'):
            raise RuntimeError(f'Instagram no pudo procesar el contenedor {cid} ({st}).')
        time.sleep(4)
    raise RuntimeError(f'El contenedor {cid} no terminó de procesarse a tiempo.')


def crear(**p):
    cid = api('POST', f"{os.environ.get('IG_USER_ID', 'IG_USER_ID')}/media", **p)['id']
    esperar(cid)
    return cid


def publicar_contenedor(cid):
    return api('POST', f"{os.environ.get('IG_USER_ID', 'IG_USER_ID')}/media_publish", creation_id=cid)['id']


def url(carpeta, archivo):
    return f'{base_url()}/queue/{carpeta}/{archivo}'


def publicar_historia(carpeta):
    cid = crear(media_type='STORIES', image_url=url(carpeta, 'historia.jpg'))
    return publicar_contenedor(cid)


def publicar_post(carpeta, posts, texto):
    if len(posts) == 1:
        cid = crear(image_url=url(carpeta, posts[0]), caption=texto)
    else:
        hijos = [crear(image_url=url(carpeta, p), is_carousel_item='true') for p in posts]
        cid = crear(media_type='CAROUSEL', children=','.join(hijos), caption=texto)
    return publicar_contenedor(cid)


def main():
    ahora = dt.datetime.now(ART)
    hoy = ahora.date()
    hh, mm = map(int, os.environ.get('HORA_POST', '19:30').split(':'))
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
        archivos = os.listdir(d)
        posts = sorted([a for a in archivos if a.startswith('post_') and a.endswith('.jpg')], key=lambda a: int(a[5:-4]))
        print(f'— {carpeta}: {len(posts)} slide(s), historia: {"historia.jpg" in archivos}, estado: {estado}')
        try:
            if 'historia.jpg' in archivos and 'historia' not in estado:
                if fecha == hoy:
                    estado['historia'] = {'id': publicar_historia(carpeta), 'hora': ahora.isoformat(timespec='minutes')}
                    print('  Historia publicada.')
                else:
                    estado['historia'] = {'omitida': 'se aprobó después de su día'}
            hora_post = dt.datetime.combine(fecha, dt.time(hh, mm), ART)
            if posts and 'post' not in estado and ahora >= hora_post:
                texto = open(os.path.join(d, 'texto.txt'), encoding='utf-8').read().strip()
                estado['post'] = {'id': publicar_post(carpeta, posts, texto), 'hora': ahora.isoformat(timespec='minutes')}
                print('  Post publicado.')
            elif posts and 'post' not in estado:
                print(f'  El post queda programado para las {hh:02d}:{mm:02d}.')
        except Exception as e:
            fallas += 1
            print(f'  ERROR: {e}')
        if not DRY:
            json.dump(estado, open(ruta_estado, 'w'), ensure_ascii=False, indent=1)
    sys.exit(1 if fallas else 0)


if __name__ == '__main__':
    main()
