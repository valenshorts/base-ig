# Videos BASE — reels animados con código

Reels 1080×1920, 30 fps, H.264 + AAC, listos para Instagram. Todo se arma desde un guion JSON:
animaciones HTML/CSS filmadas cuadro a cuadro, fotos reales de los productos y audio generado por código
(base electrónica + efectos sincronizados, sin derechos de terceros).

## Uso
```bash
pip install playwright numpy            # + ffmpeg instalado
python videos/hacer_reel.py videos/guiones/ejemplo_creatina.json --preview out/prev   # fotos de cada escena (rápido)
python videos/hacer_reel.py videos/guiones/ejemplo_creatina.json --out out/reel.mp4   # video final
```
Primero revisá con `--preview`, después renderizá el video (unos 2–4 min para un reel de 20 s).

## Guion
```json
{"voz": false, "musica": true, "escenas": [
  {"plantilla": "gancho", "datos": {"texto": "¿Qué hace la [creatina]?", "foto": "creatina_star_300g"}},
  {"plantilla": "cierre", "datos": {"fotos": ["creatina_gold_300g", "creatina_star_300g"]}}
]}
```
- `dur` (segundos) es opcional; si falta, se usa la duración sugerida.
- En los textos, `*palabra*` se pinta en lima y `[palabra]` va en caja lima.
- Las fotos son los nombres de `kit/assets/*.png` sin la extensión.
- El reel completo tiene que durar entre 3 y 90 s (ideal 12–25 s).

## Plantillas
| plantilla | datos | qué hace |
|---|---|---|
| gancho | texto, eb, emoji, foto, pie | Frase de impacto + foto con golpe (la 1ª escena ya arranca llena: frena el scroll) |
| rafaga | palabras[] | Una palabra/frase GIGANTE por beat, alternando blanco y caja lima («NO ES / MAGIA / ES / CIENCIA») |
| numero | valor, unidad, texto, decimales, emoji, foto | Contador que sube hasta el número |
| lista | texto, items[] | Ítems que entran uno por uno con tilde |
| producto | foto, foto2, nombre, detalle, precio, chip | Producto con sello de precio (foto2 = segundo paquete para combos 2×) |
| comparacion | texto, izq{foto/emoji,texto,precio}, der{…}, ganador | A vs B con choque en el medio (con precio en el pie lima) |
| quiz | pregunta, opciones[], correcta (0-3), revelar | Cuenta regresiva 3-2-1 y revela la respuesta |
| dato | texto, eb, fuente, emoji | Dato con fuente (nada de promesas de salud) |
| cierre | texto, boton, fotos[] | CTA "link en la bio" + WhatsApp + carrusel de productos |

## Ritmo (lo que lo hace adictivo)
- Cada escena dura un número entero de beats (124 bpm ≈ 0,484 s): todos los cortes caen en el bombo.
  Duraciones típicas: 1,94 s (4 beats), 2,42 s (5), 2,9 s (6), 4,35 s (9, quiz).
- La cámara se acerca todo el tiempo, todo late con cada beat y hay sacudón en cada impacto: nunca hay un cuadro quieto.
- Estructura ganadora (18–22 s): gancho → ráfaga → dato/quiz → número → comparación con precios → oferta → cierre «Pedí la tuya».
- Nunca adelantar la respuesta de un quiz en una escena anterior.

## Marca
Colores, @ de Instagram, WhatsApp, tempo de la música y voz: `marca.json`. Leyenda legal y barra de progreso van
siempre arriba. Reglas: precios de `kit/README.md`, sin promesas de salud, CTA "link en la bio".

## Voz (opcional)
`"voz": true` y un `"texto"` por escena genera locución con edge-tts (voz es-AR). Es un servicio de Microsoft sin
licencia comercial clara: para usarla en publicidad conviene grabar la voz propia. Por defecto va sin voz
(los reels con texto en pantalla + música funcionan igual o mejor sin sonido).
