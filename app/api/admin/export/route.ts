import { NextResponse } from 'next/server';
import { createSupabaseAdmin } from '@/lib/supabase';

export async function GET() {
  const supabase = createSupabaseAdmin();
  const { data } = await supabase.from('leads').select('*').order('created_at', { ascending: false });
  const headers = ['created_at','name','phone','email','service','client_type','location','urgency','state'];
  const rows = [headers.join(','), ...(data || []).map((l: any) => headers.map((h)=>`"${String(l[h]||'').replace(/"/g,'""')}"`).join(','))].join('\n');
  return new NextResponse(rows, { headers: { 'Content-Type': 'text/csv; charset=utf-8', 'Content-Disposition': 'attachment; filename="leads.csv"' } });
}
