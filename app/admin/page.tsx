import { redirect } from 'next/navigation';
import { createSupabaseServerClient } from '@/lib/supabase';
import Link from 'next/link';
import { pipelineStates } from '@/lib/site';

export default async function AdminPage({ searchParams }: { searchParams: Record<string, string | undefined> }) {
  const supabase = createSupabaseServerClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect('/admin/login');

  let query = supabase.from('leads').select('*').order('created_at', { ascending: false });
  ['service','client_type','location','urgency','state'].forEach((k) => {
    const v = searchParams[k];
    if (v) query = query.eq(k, v);
  });
  const { data: leads } = await query;

  return <main className="container-page py-10"><h1 className="text-3xl font-bold">Panel de leads</h1><div className="mt-3 flex gap-2 text-sm">{pipelineStates.map((s)=><Link key={s} href={`/admin?state=${encodeURIComponent(s)}`} className="rounded border px-2 py-1">{s}</Link>)}</div><div className="mt-4 overflow-x-auto"><table className="w-full text-sm"><thead><tr className="text-left"><th>Fecha</th><th>Nombre</th><th>Servicio</th><th>Tipo</th><th>Zona</th><th>Urgencia</th><th>Estado</th></tr></thead><tbody>{leads?.map((l:any)=><tr key={l.id} className="border-t"><td>{new Date(l.created_at).toLocaleString('es-ES')}</td><td><Link className="text-brand underline" href={`/admin/leads/${l.id}`}>{l.name}</Link></td><td>{l.service}</td><td>{l.client_type}</td><td>{l.location}</td><td>{l.urgency}</td><td>{l.state}</td></tr>)}</tbody></table></div><a href="/api/admin/export" className="btn-secondary mt-4">Exportar CSV</a></main>;
}
