import { NextRequest, NextResponse } from 'next/server';
import { createSupabaseAdmin } from '@/lib/supabase';

export async function POST(req: NextRequest, { params }: { params: { id: string } }) {
  const fd = await req.formData();
  const state = String(fd.get('state') || 'Nuevo');
  const notes = String(fd.get('notes') || '');
  const supabase = createSupabaseAdmin();
  await supabase.from('leads').update({ state, notes }).eq('id', params.id);
  await supabase.from('lead_history').insert({ lead_id: params.id, state, note: notes ? 'Actualización manual' : '' });
  return NextResponse.redirect(new URL(`/admin/leads/${params.id}`, req.url));
}
