# Web de BASE (basesuplementos.netlify.app)

- `public/index.html`: la tienda. `public/pago.html`: resultado del pago.
- `netlify/functions/crear-pago.mjs`: arma el pago de Mercado Pago (Checkout Pro). Cobra el precio de
  transferencia (10% OFF) que figura en `index.html`; el navegador solo manda ids y cantidades.
- `netlify/functions/mp-webhook.mjs`: aviso de Mercado Pago; deja cada pago en los logs de la función.
- `netlify/functions/ig.mjs`: link de la bio `/ig` (cuenta clics y lleva a la web con `utm_source=instagram`).
- `netlify/functions/clics.mjs`: `/clics` muestra los clics de la bio por día.
- `tools/extraer_catalogo.py`: corre en cada deploy y genera `catalogo.json` desde `index.html`.

## Netlify
Sitio vinculado a este repo con **base directory `web`**. Solo publica cuando cambia algo de `web/`.
Variable de entorno: `MP_ACCESS_TOKEN` (Site configuration → Environment variables).
- Modo prueba: el Access Token **de prueba** de Mercado Pago (empieza con `TEST-`).
- Producción: reemplazarlo por el Access Token de producción (`APP_USR-…`).
Nunca pegar la clave en el código ni en un chat.

## Cambiar la tienda
Editar `public/index.html` (productos, precios, textos) y pushear a `main`: Netlify publica solo y
los precios de Mercado Pago se actualizan con el mismo deploy.
