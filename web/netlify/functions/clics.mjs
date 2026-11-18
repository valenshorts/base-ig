// Clics del link de la bio por día: basesuplementos.netlify.app/clics (JSON).
import { getStore } from '@netlify/blobs';

export default async () => {
  const store = getStore('clics');
  const { blobs } = await store.list({ prefix: 'bio/' });
  const dias = {};
  for (const b of blobs) dias[b.key.slice(4)] = Number(await store.get(b.key)) || 0;
  const total = Object.values(dias).reduce((a, b) => a + b, 0);
  return new Response(JSON.stringify({ total, dias }, null, 1), { headers: { 'content-type': 'application/json', 'Cache-Control': 'no-store' } });
};
export const config = { path: '/clics' };
