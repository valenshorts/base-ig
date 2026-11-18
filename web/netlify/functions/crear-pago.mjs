// Crea el pago de Mercado Pago (Checkout Pro) para el carrito o un producto suelto.
// Cobra precio de lista (sin el 10% OFF, que queda para transferencia o efectivo por WhatsApp).
// El navegador solo manda ids, sabores y cantidades: los precios salen de catalogo.json,
// que se genera desde index.html en cada deploy. La clave de Mercado Pago vive en la
// variable de entorno MP_ACCESS_TOKEN de Netlify (nunca en el código).
import catalogo from './catalogo.json';

const SITIO = process.env.URL || 'https://basesuplementos.netlify.app';
const r = (status, body) => new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } });
const limpiar = (s, n = 80) => String(s ?? '').replace(/[\u0000-\u001f<>]/g, '').trim().slice(0, n);

// MP_MODO: "produccion" muestra el pago a todos. Cualquier otro valor (o vacío) = modo prueba:
// el botón solo aparece entrando a la web con ?prueba-mp, así ningún cliente paga a la cuenta de prueba.
const MODO = () => (process.env.MP_MODO === 'produccion' ? 'produccion' : 'prueba');

export default async (req) => {
  if (req.method === 'GET') return r(200, { activo: !!process.env.MP_ACCESS_TOKEN, modo: MODO() });
  if (req.method !== 'POST') return r(405, { error: 'Usá POST' });
  const token = process.env.MP_ACCESS_TOKEN;
  if (!token) return r(503, { error: 'El pago online todavía no está configurado. Escribinos por WhatsApp.' });

  let datos;
  try { datos = await req.json(); } catch { return r(400, { error: 'Pedido inválido' }); }
  const items = [];
  for (const it of (datos.items || []).slice(0, 40)) {
    const p = catalogo.productos[String(it.id)];
    const qty = Math.trunc(Number(it.qty));
    if (!p || !(qty >= 1 && qty <= 20)) return r(400, { error: 'Hay un producto que no existe o una cantidad inválida.' });
    const sabor = it.sabor && p.sabores.includes(it.sabor) ? it.sabor : '';
    items.push({ id: String(it.id), title: limpiar(p.titulo + (sabor ? ` (${sabor})` : ''), 250), quantity: qty, unit_price: p.precio, currency_id: 'ARS' });
  }
  for (const id of (datos.combos || []).slice(0, 10)) {
    const c = catalogo.combos[String(id)];
    if (!c) return r(400, { error: 'Hay un combo que no existe.' });
    items.push({ id: String(id), title: limpiar(c.titulo, 250), quantity: 1, unit_price: c.precio, currency_id: 'ARS' });
  }
  if (!items.length) return r(400, { error: 'El carrito está vacío.' });

  const comprador = datos.comprador || {};
  const nombre = limpiar(comprador.nombre, 60);
  const whatsapp = limpiar(comprador.whatsapp, 30).replace(/[^\d+ ]/g, '');
  const localidad = limpiar(comprador.localidad, 80);
  if (!nombre || whatsapp.replace(/\D/g, '').length < 8 || !localidad) return r(400, { error: 'Completá nombre, WhatsApp y localidad.' });

  const referencia = `BASE-${Date.now().toString(36).toUpperCase()}-${Math.random().toString(36).slice(2, 6).toUpperCase()}`;
  const preferencia = {
    items,
    payer: { name: nombre, ...(comprador.email ? { email: limpiar(comprador.email, 120) } : {}) },
    external_reference: referencia,
    statement_descriptor: 'BASE SUPLEMENTOS',
    back_urls: {
      success: `${SITIO}/pago.html?r=ok`,
      pending: `${SITIO}/pago.html?r=pendiente`,
      failure: `${SITIO}/pago.html?r=error`,
    },
    auto_return: 'approved',
    notification_url: `${SITIO}/.netlify/functions/mp-webhook`,
    metadata: {
      whatsapp, localidad, nombre,
      notas: limpiar(comprador.notas, 300),
      origen: limpiar(datos.origen, 40) || 'web',
    },
  };
  const res = await fetch('https://api.mercadopago.com/checkout/preferences', {
    method: 'POST',
    headers: { Authorization: `Bearer ${token}`, 'content-type': 'application/json', 'X-Idempotency-Key': referencia },
    body: JSON.stringify(preferencia),
  });
  const j = await res.json().catch(() => ({}));
  if (!res.ok) {
    console.error('Mercado Pago rechazó la preferencia', res.status, JSON.stringify(j).slice(0, 500));
    return r(502, { error: 'Mercado Pago no respondió bien. Probá de nuevo o escribinos por WhatsApp.' });
  }
  return r(200, { url: j.init_point, referencia, prueba: MODO() === 'prueba' });
};
