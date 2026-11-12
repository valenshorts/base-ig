# Kit de diseño BASE Suplementos: flyer diario

Kit para generar los flyers de Instagram de **BASE Suplementos** (@basesuplementos.ar). Reemplaza al kit de Nutristock desde el 09/11/2026: **no usar nada de la marca Nutristock** (ni el logo, ni el amarillo, ni el nombre).

## Cómo usarlo
```python
import sys; sys.path.insert(0, '<ruta a base_kit>')
from lib import *     # page, tiles, pf, cf, E, render, OK, X, ARROW, WA, IG, LEGAL_TXT
body = ('<div class="eb" style="top:200px">Etiqueta</div>'
        '<div class="t" style="top:250px;font-size:92px">Título<br><span class="box">Segunda línea</span></div>'
        + tiles([('ena_prot_vain', pf('ENA 100% Whey 907 g', '$66.900'))], 560, 440, 360))
render([page(1, body, nxt=False, total=1)], 'salida')   # 1080x1350; historia: page(..., story=True) y render([...], 'x', 1080, 1920)
```
- `page(n, body, nxt=True, total=1, story=False, legal=True)`: fondo negro con brillo lima, header con la marca BASE y contador "n / total" (solo si total > 1). `nxt=True` agrega el botón "DESLIZÁ". La leyenda legal va sola abajo (`legal=True`).
- `tiles(items, top, ancho, alto, gap)`: recuadros GRISES con el producto. `pf(marca, precio)` = pie lima con marca y precio; `cf(texto)` = pie oscuro con categoría.
- Clases: `.eb` (etiqueta lima con raya), `.t` (título Montserrat 900 en mayúsculas) con `.box` (caja lima, texto negro) o `.hl` (texto lima), `.txt` (párrafo con `<em>` lima), `.panel` / `.panel.on` (tarjeta oscura; `.on` resaltada en lima), `.btn` / `.btn.ghost` (botón recto).
- Ejemplo completo: `ejemplo_quiz_combos.py` (carrusel de 3 slides).
- **Ejemplo VISUAL (estándar actual): `ejemplo_visual.py`** (carrusel de 4 slides: mito o verdad + recetas + venta). Usalo como referencia de estilo.

## Estilo visual obligatorio (pedido de Valentín, 10/11/2026)
Cada flyer tiene que ser **visual, con imágenes y emojis**, no solo texto:
- Emojis a color con `E('🔥', 120)` (Noto Color Emoji; clase `.e`). Usarlos como **ilustraciones grandes** (80–130 px) dentro de paneles o recuadros grises, y como íconos (40–60 px) en lugar de números en listas. Emojis chicos (22–30 px) en llamados a la acción: 👇 en "comentá", 👉 en "deslizá", 🛒 en el botón del catálogo, 💬 en WhatsApp, 📌 en "guardalo".
- Cada slide lleva al menos un elemento gráfico fuerte: foto de producto en tile, una "ecuación" visual (producto + 🔥 = ?), un antes/después con emojis (🥚 → 🍳), tarjetas con un ícono grande a la izquierda, chips de sabor sobre los productos (🍦 VAINILLA / 🍫 CHOCOLATE).
- El ícono tiene que representar EXACTAMENTE lo que dice el texto (ej.: "brownie en taza" no es una barra de chocolate 🍫). Si no hay un emoji que lo muestre bien, dibujá un SVG simple en estilo plano (como la taza con brownie de `ejemplo_visual.py`).
- Sin abusar: emojis con sentido, nunca tapando productos ni textos; en quizzes no usar colores que adelanten la respuesta.

## Identidad (obligatoria, igual que la web de BASE)
- Paleta: negro #0B0B0C, lima #C6F432 (oscuro #8FB31E) y blanco; paneles #111112 con borde #2a2a2d.
- Tipografías: Montserrat 900 para títulos (mayúsculas), Montserrat 500–800 para textos, Archivo Black para la palabra BASE y los precios.
- Esquinas rectas (sin bordes redondeados). Márgenes de 80 px.
- Marca: cuadrado lima con una barra negra abajo + "BASE" y "SUPLEMENTOS" en lima chico. No rediseñarla.

## Reglas de contenido
- Productos SIEMPRE en recuadros grises (`tiles`). Sin marca de agua del Instagram.
- NO usar la foto de la whey Gold (se ve mal; se puede nombrar en texto). Tampoco productos One Fit.
- Salud: no prometer resultados. Solo frases cautas o de tipo EFSA:
  - proteína: "contribuye a aumentar y mantener la masa muscular"
  - creatina: "aumenta el rendimiento físico en series sucesivas de ejercicios cortos de alta intensidad"
  - magnesio: "contribuye a disminuir el cansancio y la fatiga" y "al funcionamiento normal de los músculos"
- Leyenda legal en cada pieza: "SUPLEMENTA DIETAS INSUFICIENTES. CONSULTE A SU MÉDICO Y/O FARMACÉUTICO."
- No decir "más vendido" ni "en stock" sin datos. No inventar estudios ni cifras.
- Llamado a la acción principal: **ver el catálogo en la web ("link en la bio")**, tanto en el flyer como en el texto del post. WhatsApp 11 2178-9431 va como canal de consulta, **solo por mensaje** (no llamadas). Instagram @basesuplementos.ar.
- Precios: los de transferencia o efectivo (10% OFF vs. tarjeta).
- Español rioplatense con voseo. Los textos del post terminan con una pregunta.

## Productos (archivo en assets/ → producto · precio transferencia/efectivo, según la web de BASE)
| archivo | producto | precio |
|---|---|---|
| ena_prot_vain | ENA 100% Whey 907 g | $66.900 |
| ena_truemade_vainilla | ENA Truemade Whey 930 g | $90.900 |
| whey_star_2lb_vainilla | Star Whey Protein 2 lb | $81.900 |
| platinum1kg_vainilla | Star Platinum Whey 2 lb (pote) | $93.900 |
| on_gs_choc / on_gold_standard | ON 100% Whey Gold Standard ~310 g | $60.900 |
| mp_whey_brownie | MyProtein Impact Whey 1 kg | $78.900 |
| creatina_star_300g | Creatina Star doypack 300 g | $23.800 |
| creatina_gold_300g | Creatina Gold doypack 300 g | $22.900 |
| gold_creapure200 | Creatina Gold Creapure 200 g | $31.900 |
| ena_crea_neutra | Creatina ENA 300 g | $26.900 |
| pote300 / pote500 / star_crea1kg | Creatina Star pote 300 g / 500 g / 1 kg | $28.900 / $44.900 / $84.900 |
| gold_crea1kg | Creatina Gold 1 kg | $57.900 |
| on_creatine | ON Micronised Creatine 317 g | $28.900 |
| ena_creaelec_bluelemon | ENA Creatina + electrolitos 300 g | $28.900 |
| star_citratomg | Magnesio citrato Star 60 caps | $10.900 |
| ena_citratomg | Magnesio citrato ENA 60 caps | $12.900 |
| magnesio_glicinato_gold | Magnesio glicinato Gold 60 caps | $15.900 |
| ena_omega3 | Omega 3 ENA 60 caps | $27.900 |
| gold_omega3 | Omega 3 Gold 30 caps | $28.900 |
| collagen | Colágeno Star con resveratrol 210 g | $18.900 |
| tnt_dynamite_star | Pre-entreno TNT Dynamite Star 240 g | $24.900 |

Combos (transferencia o efectivo): Star (Whey 2 lb + Creatina 300 g) $99.900, ahorrás $5.800 · ENA (Proteína 907 g + Creatina 300 g) $85.900, ahorrás $7.900 · Gold (Whey 2 lb + Creatina 300 g) $88.900, ahorrás $6.900 · 2x Creatina Star 300 g $44.900, ahorrás $2.700.

Ver `historial.md` para no repetir temas.
