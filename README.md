# BASE · Instagram automático (con tu OK)

Publicación diaria del flyer y la historia de **@basesuplementos.ar**, con revisiones antes de publicar y aprobación tuya desde el celu.

## Cómo funciona

```
16:31  La rutina de Claude arma el contenido de MAÑANA: 2 posts + 4 historias + 1 reel
        └─ revisa todo (chequeos automáticos + director de arte + segundo revisor)
        └─ abre UN Pull Request: «Contenido 2026-11-14: …»
         ↓
       GitHub corre la revisión automática (workflow «revisar»)
        └─ comenta en el PR con el resultado, los horarios, la vista previa y los textos
        └─ si algo falla, el PR queda en rojo ❌
         ↓
Vos    Abrís el PR desde la app de GitHub y tocás «Merge» = aprobado ✅
         ↓
       Workflow «publicar» (corre cada 30 min de 10:05 a 23:35)
        └─ 11:00 historia · 13:00 post · 15:00 historia · 18:00 historia
           19:30 post · 20:30 reel · 21:30 historia
```

Si no aprobás, no se publica nada. Para frenar algo, cerrá el PR. Si aprobás tarde, lo atrasado sale espaciado (una pieza de cada tipo cada 30 min); las historias de un día que ya pasó no se publican.

## Carpetas

| carpeta | qué tiene |
|---|---|
| `kit/` | kit de diseño de BASE (lib.py, assets, fonts, README con reglas y precios, historial) |
| `queue/AAAA-MM-DD/` | un día: `plan.json` (piezas y horarios), JPG de posts e historias, `reel.mp4`, textos `.txt`, los `.py` que generaron las imágenes y `estado.json` (lo escribe el bot al publicar) |
| `scripts/armar.py` | arma la carpeta del día desde un plan (convierte PNG → JPG) |
| `scripts/reel.py` | arma el reel MP4 1080×1920 a partir de imágenes |
| `scripts/revisar.py` | revisión automática |
| `scripts/publicar.py` | publica con la API oficial de Instagram |
| `docs/` | instrucciones de la tarea diaria y una publicación de ejemplo |

## Qué revisa `revisar.py`

- Medidas (1080×1350 o 1080×1080 el post, 1080×1920 la historia), formato JPG, peso, numeración del carrusel (máx. 10).
- Vuelve a renderizar con los scripts y mide cada elemento: **textos cortados, elementos que se pisan, cosas que se salen de la imagen, imágenes que no cargan, nombres de producto partidos en dos líneas**.
- **Emojis** que la fuente no tiene (se verían como cuadraditos).
- **Precios** iguales a los del `kit/README.md`, **leyenda legal**, **WhatsApp** correcto.
- **Palabras prohibidas**: Nutristock, One Fit, «más vendido», «en stock», promesas de salud (cura, adelgaza, quema grasa…).
- **Texto del post**: «link en la bio», WhatsApp aclarando «solo mensajes», leyenda legal, pregunta al final, máx. 2200 caracteres y 30 hashtags.

Probalo vos: `python scripts/revisar.py docs/ejemplo_cola/2026-11-12`

---

## Configuración (una sola vez)

> Los nombres de los menús de Meta cambian seguido; si algo no aparece igual, buscá la opción más parecida o avisame.

### 1. Instagram profesional + página de Facebook
1. En la app de Instagram: **Configuración → Tipo de cuenta y herramientas → Cambiar a cuenta profesional** (Empresa).
2. Vinculala a una **página de Facebook** de BASE (si no tenés, creá una): en Instagram, **Editar perfil → Página**.

### 2. App de Meta y token
1. Entrá a <https://developers.facebook.com> con tu Facebook → **Mis apps → Crear app** → tipo **Empresa** (Business). Nombre: `BASE publicador`.
2. Dentro de la app, agregá el producto **Instagram** (opción *API con inicio de sesión de Facebook / Instagram Graph API*).
3. Token que no vence (recomendado): en <https://business.facebook.com/settings> → **Usuarios → Usuarios del sistema → Agregar** (rol Administrador).
   - **Asignar activos**: la página de Facebook, la cuenta de Instagram y la app, con control total.
   - **Generar token** → elegí la app → caducidad **Nunca** → permisos: `instagram_basic`, `instagram_content_publish`, `pages_show_list`, `pages_read_engagement`, `business_management`.
   - Copiá el token (**no se lo pases a nadie, tampoco por chat**).
4. ID de Instagram: en <https://developers.facebook.com/tools/explorer> pegá el token y consultá `me/accounts?fields=name,instagram_business_account`. El número dentro de `instagram_business_account` es tu **IG_USER_ID**.

### 3. Repo en GitHub
1. Creá un repo **público** llamado `base-ig` (tiene que ser público para que Instagram pueda bajar las imágenes; el token queda guardado aparte como secreto y nunca se ve).
2. Subí todo el contenido de esta carpeta (con **GitHub Desktop** es lo más fácil; asegurate de que se suba la carpeta oculta `.github`).

### 4. Secretos
En el repo: **Settings → Secrets and variables → Actions → New repository secret**:
- `IG_USER_ID` → el número del paso 2.4
- `IG_TOKEN` → el token del paso 2.3

### 5. Que no se pueda aprobar si la revisión falla
**Settings → Branches → Add branch protection rule** → `main` → marcá **Require status checks to pass before merging** y elegí **revisar**.

### 6. Prueba sin publicar
**Actions → publicar → Run workflow** con *Simulación* tildado: tiene que terminar en verde mostrando lo que haría.

### 7. Tarea diaria de Claude con el repo
En <https://claude.ai/code> creá una **tarea programada** con el repositorio **base-ig** seleccionado, todos los días a las 16:31, y pegá como instrucción el texto de `docs/tarea_diaria.md`. Así Claude trabaja directo sobre el repo (no necesita tu compu prendida) y abre el PR todos los días.

## Límites a tener en cuenta
- **Las historias salen sin sticker** de encuesta o quiz (Instagram no lo permite por API). Van con «Respondé esta historia con A, B, C o D».
- Instagram permite hasta 50 publicaciones por día por API; acá usamos 2.
- GitHub a veces demora unos minutos los workflows programados: el post puede salir 19:35–19:45.
- Si Instagram no puede bajar las imágenes de `raw.githubusercontent.com`, creá la variable `MEDIA_BASE_URL` = `https://cdn.jsdelivr.net/gh/TU_USUARIO/base-ig@main` (Settings → Variables).
