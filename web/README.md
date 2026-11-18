# Web de BASE (basesuplementos.netlify.app)

- `public/index.html`: la tienda. `public/pago.html`: resultado del pago.
- `netlify/functions/crear-pago.mjs`: arma el pago de Mercado Pago (Checkout Pro). Cobra el precio de
  de lista (`precio_normal`; combos = precio combo ÷ 0,9 redondeado a …900); el 10% OFF es solo por WhatsApp; el navegador solo manda ids y cantidades.
- `netlify/functions/mp-webhook.mjs`: aviso de Mercado Pago; deja cada pago en los logs de la función.
- `netlify/functions/ig.mjs`: link de la bio `/ig` (cuenta clics y lleva a la web con `utm_source=instagram`).
- `netlify/functions/clics.mjs`: `/clics` muestra los clics de la bio por día.
- `tools/extraer_catalogo.py`: corre en cada deploy y genera `catalogo.json` desde `index.html`.

## Netlify
Sitio vinculado a este repo con **base directory `web`**. Solo publica cuando cambia algo de `web/`.
Variables de entorno (Project configuration → Environment variables):
- `MP_ACCESS_TOKEN`: Access Token de la app «BASE web» de Mercado Pago. Hoy tiene el de **prueba**.
- `MP_MODO`: sin cargar = modo prueba (el pago online solo se ve entrando con `?prueba-mp`).
  Para salir a producción: cambiar `MP_ACCESS_TOKEN` por el de producción y crear `MP_MODO=produccion`.
Nunca pegar la clave en el código ni en un chat.

## Cambiar la tienda
Editar `public/index.html` (productos, precios, textos) y pushear a `main`: Netlify publica solo y
los precios de Mercado Pago se actualizan con el mismo deploy.
