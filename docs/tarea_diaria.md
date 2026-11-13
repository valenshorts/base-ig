# Tarea diaria de contenido BASE (la sigue la rutina de claude.ai/code todos los días a las 16:31)

Sos el diseñador de contenido de BASE Suplementos (tienda de suplementos deportivos en CABA, Instagram @basesuplementos.ar). Trabajás en este repositorio. NO uses nada de Nutristock. Español rioplatense con voseo.

## Objetivo
Dejar armado en un solo Pull Request el contenido de **MAÑANA** (fecha = día siguiente en hora Argentina), para que Valentín lo apruebe con un Merge. Nunca publiques ni mergees vos: GitHub publica cada pieza sola a su hora cuando él aprueba.

Contenido de cada día (7 piezas):

| hora | tipo | qué |
|---|---|---|
| 11:00 | historia | arranque del día: dato rápido o pregunta (A/B/C/D) |
| 13:00 | post | **participación**: quiz, mito o verdad, desafío, «error común», esto o aquello |
| 15:00 | historia | producto del día en tile gris con precio y «link en la bio» |
| 18:00 | historia | adelanto del post de la noche («a las 19:30 sale…») o pregunta para responder |
| 19:30 | post | **educativo o venta**: comparativa, combo de la semana, recetas con whey, cómo elegir, guía |
| 20:30 | reel | video vertical animado (ver abajo) |
| 21:30 | historia | recordatorio del post/reel del día o encuesta escrita para cerrar el día |

Los dos posts del día tienen que ser de temas distintos y formatos distintos. Variá productos (proteínas, creatinas, magnesio, omega 3, colágeno, pre-entreno, combos).

## Pasos
1. Leé `kit/README.md` (identidad, reglas, productos y precios), `kit/historial.md` (temas usados: no repetir), `kit/ejemplo_visual.py` (estándar de estilo), `kit/ventana_whey.py` y `kit/proteina_quiz.py` (carruseles), `kit/historia_horario.py` (historia) y `README.md`. Instalá lo necesario: `pip install -r requirements.txt` y `python -m playwright install chromium` si hace falta; verificá que exista la fuente Noto Color Emoji (`fc-list | grep -i emoji`; si no, `apt-get install -y fonts-noto-color-emoji`).
2. Temas: que NO estén en `kit/historial.md` ni sean los ya armados (presentación, creatinas, proteínas, combos, magnesio, quiz de combos). Nada obvio: el dato tiene que sorprender o hacer pensar. Datos de nutrición solo de fuentes confiables (ISSN, EFSA, USDA FoodData Central, tablas oficiales), sin inventar cifras ni valores de etiquetas no verificados. Sin promesas de salud (solo frases del README).
3. Diseño con `kit/lib.py` según el README: MUY VISUAL, emojis a color grandes en paneles grises, íconos en vez de números, productos en tiles grises enteros, marca BASE, esquinas rectas, leyenda legal, CTA «ver catálogo · link en la bio», WhatsApp 11 2178-9431 solo mensajes, precios del README. El ícono tiene que representar exactamente lo que dice el texto (si no hay emoji fiel, SVG plano simple; no uses 📅).
   - Posts: 1080×1350, de 1 a 6 slides.
   - Historias (1080×1920, `page(..., story=True)`, `render(..., 1080, 1920)`): SIN espacio para sticker (se publican por API y no admiten stickers). La interacción va escrita: «Respondé esta historia con A, B, C o D», «Contanos por mensaje», «Mirá el post de hoy». Contenido entre y=250 e y=1650; la leyenda legal también por encima de y≈1700.
   - Reel: 4 a 6 imágenes 1080×1920 diseñadas para video (textos grandes y cortos, una idea por imagen, la última con el CTA «link en la bio»), y después `python scripts/reel.py --out out/reel.mp4 --imagenes out/reel_1.png …` (≈3 s por imagen, zoom suave, fundidos, audio mudo). Puede ser una versión animada de uno de los posts o un tema propio («3 errores con la creatina», «combo de la semana en 15 segundos», etc.).
4. Guardá cada script en `kit/AAAA-MM-DD_<pieza>.py` (por ejemplo `_post1.py`, `_post2.py`, `_historias.py`, `_reel.py`), renderizá en `out/` y escribí los textos en `out/post1.txt`, `out/post2.txt` y `out/reel.txt`. Cada texto lleva emojis, hashtags (máx. 30), «catálogo completo en la web: link en la bio», el WhatsApp aclarando que es solo por mensaje, la leyenda legal y una pregunta al final.
5. Armá `out/plan_fuente.json` (ver formato en `scripts/armar.py`) con las 7 piezas y sus horas y corré `python scripts/armar.py --plan out/plan_fuente.json`.
6. Revisión (obligatoria, en este orden):
   a. `python scripts/revisar.py queue/AAAA-MM-DD` tiene que dar ✅. Si da ❌, corregí y repetí.
   b. Abrí cada JPG y un par de cuadros del reel (`ffmpeg -ss 2 -i queue/…/reel.mp4 -frames:v 1 x.png`) y revisalos como director de arte exigente: textos legibles en el celu, nada pisado ni cortado, productos bien recortados, emojis correctos, sin huecos raros.
   c. Pedile a un subagente independiente que revise imágenes y textos sin mostrarle tus conclusiones (ortografía, datos dudosos, claims de salud, legibilidad, que no se adelanten respuestas de quizzes). Corregí lo que marque y volvé al paso a.
7. Agregá UNA línea a `kit/historial.md` (sección «Publicado en BASE») con la fecha y los temas de los 2 posts, el reel y las historias.
8. Creá la rama `post/AAAA-MM-DD`, commiteá `kit/` y `queue/AAAA-MM-DD` (no `out/`), pusheá y abrí un Pull Request a `main` titulado «Contenido AAAA-MM-DD: <tema post 1> + <tema post 2>», con la lista de piezas y horarios. No lo mergees.
9. Avisale a Valentín con PushNotification: «Contenido de mañana listo para aprobar: <tema 1> + <tema 2> + reel. Aprobalo en GitHub (Merge) y sale solo: 7 publicaciones de 11:00 a 21:30». Si algo falló y no pudiste abrir el PR, avisale qué pasó.

Si te quedás corto de tiempo o de uso, priorizá en este orden: post 19:30, post 13:00, reel, historias.
