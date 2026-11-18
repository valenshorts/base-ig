// Aviso de Mercado Pago cuando cambia un pago. Lo consulta a la API (no confía en el aviso)
// y deja el detalle en el registro de la función en Netlify (Logs → Functions → mp-webhook).
export default async (req) => {
  const url = new URL(req.url);
  let id = url.searchParams.get('data.id') || url.searchParams.get('id');
  let tipo = url.searchParams.get('type') || url.searchParams.get('topic');
  if (req.method === 'POST') {
    try { const b = await req.json(); id = b?.data?.id || id; tipo = b?.type || tipo; } catch {}
  }
  if (tipo !== 'payment' || !id || !process.env.MP_ACCESS_TOKEN) return new Response('ok');
  const res = await fetch(`https://api.mercadopago.com/v1/payments/${encodeURIComponent(id)}`, {
    headers: { Authorization: `Bearer ${process.env.MP_ACCESS_TOKEN}` },
  });
  const p = await res.json().catch(() => ({}));
  console.log('PAGO', JSON.stringify({
    id: p.id, estado: p.status, detalle: p.status_detail, total: p.transaction_amount,
    neto: p.transaction_details?.net_received_amount, referencia: p.external_reference,
    comprador: p.metadata?.nombre, whatsapp: p.metadata?.whatsapp, localidad: p.metadata?.localidad,
    origen: p.metadata?.origen, envio: p.metadata?.envio, items: (p.additional_info?.items || []).map(i => `${i.quantity}x ${i.title}`),
  }));
  return new Response('ok');
};
