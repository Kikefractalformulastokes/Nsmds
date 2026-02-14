import { notFound, redirect } from 'next/navigation';
import { createSupabaseServerClient } from '@/lib/supabase';
import { pipelineStates } from '@/lib/site';

export default async function LeadDetail({ params }: { params: { id: string } }) {
  const supabase = createSupabaseServerClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect('/admin/login');

  const { data: lead } = await supabase.from('leads').select('*').eq('id', params.id).single();
  if (!lead) notFound();
  const { data: history } = await supabase.from('lead_history').select('*').eq('lead_id', params.id).order('created_at', { ascending: false });

  return <main className="container-page py-10"><h1 className="text-3xl font-bold">Lead: {lead.name}</h1><div className="mt-4 grid gap-4 md:grid-cols-2"><div className="card space-y-2"><p><strong>Tel:</strong> <a href={`tel:${lead.phone}`} className="underline">{lead.phone}</a></p><p><strong>Email:</strong> <a href={`mailto:${lead.email}`} className="underline">{lead.email}</a></p><p><strong>WhatsApp:</strong> <a className="underline" href={`https://wa.me/${String(lead.phone).replace('+','')}`} target="_blank">Abrir chat</a></p><p><strong>Servicio:</strong> {lead.service}</p><p><strong>Tipo:</strong> {lead.client_type}</p><p><strong>Zona:</strong> {lead.location}</p><p><strong>Urgencia:</strong> {lead.urgency}</p><p><strong>Descripción:</strong> {lead.description}</p><p><strong>UTMs:</strong> {lead.utm_source} / {lead.utm_medium} / {lead.utm_campaign}</p></div><form className="card" action={`/api/admin/leads/${params.id}`} method="post"><label>Estado</label><select name="state" defaultValue={lead.state} className="mb-3 mt-1 w-full rounded border p-2">{pipelineStates.map((s)=><option key={s}>{s}</option>)}</select><label>Notas internas</label><textarea name="notes" defaultValue={lead.notes || ''} className="mt-1 w-full rounded border p-2" rows={6}/><button className="btn-primary mt-3">Guardar cambios</button></form></div><section className="mt-6"><h2 className="text-xl font-bold">Historial</h2><ul className="mt-2 space-y-2">{history?.map((h:any)=><li key={h.id} className="card text-sm">{new Date(h.created_at).toLocaleString('es-ES')} · {h.state} · {h.note || 'Sin nota'}</li>)}</ul></section></main>;
}
