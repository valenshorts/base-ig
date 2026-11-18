// Link de la bio de Instagram: basesuplementos.netlify.app/ig
// Cuenta el clic (por día) y lleva a la web marcando que la visita vino de la bio.
import { getStore } from '@netlify/blobs';

export default async () => {
  const hoy = new Date(Date.now() - 3 * 3600e3).toISOString().slice(0, 10); // fecha en hora Argentina
  try {
    const store = getStore('clics');
    const actual = Number(await store.get(`bio/${hoy}`)) || 0;
    await store.set(`bio/${hoy}`, String(actual + 1));
  } catch (e) { console.error('No se pudo contar el clic', e); }
  return new Response(null, { status: 302, headers: { Location: '/?utm_source=instagram&utm_medium=bio', 'Cache-Control': 'no-store' } });
};
export const config = { path: '/ig' };
