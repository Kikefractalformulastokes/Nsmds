import { NextRequest, NextResponse } from 'next/server';
import { createSupabaseAdmin } from '@/lib/supabase';
import { sendEmail } from '@/lib/email';

export async function POST(req: NextRequest) {
  try {
    const supabase = createSupabaseAdmin();
    const fd = await req.formData();
    const payload: any = {
      service: fd.get('service'), client_type: fd.get('client_type'), location: fd.get('location'), urgency: fd.get('urgency'),
      description: fd.get('description'), name: fd.get('name'), phone: fd.get('phone'), email: fd.get('email'),
      consent: fd.get('consent') === 'true', utm_source: fd.get('utm_source'), utm_medium: fd.get('utm_medium'), utm_campaign: fd.get('utm_campaign'), utm_content: fd.get('utm_content'), utm_term: fd.get('utm_term'),
      referrer: fd.get('referrer'), source_page: fd.get('source_page'), user_agent: req.headers.get('user-agent'), state: 'Nuevo',
    };

    const { data: lead, error } = await supabase.from('leads').insert(payload).select('*').single();
    if (error) throw error;

    const files = fd.getAll('photos') as File[];
    const urls: string[] = [];
    for (const file of files.slice(0, 6)) {
      const path = `${lead.id}/${Date.now()}-${file.name}`;
      const bytes = Buffer.from(await file.arrayBuffer());
      const up = await supabase.storage.from('lead-photos').upload(path, bytes, { contentType: file.type });
      if (!up.error) urls.push(path);
    }
    if (urls.length) await supabase.from('leads').update({ photo_paths: urls }).eq('id', lead.id);

    const adminUrl = `${req.nextUrl.origin}/admin/leads/${lead.id}`;
    const companyEmail = process.env.COMPANY_NOTIFICATION_EMAIL || 'contacto@jrrehabilitaciones.es';
    await sendEmail(companyEmail, `Nuevo lead: ${lead.service} (${lead.name})`, `<p>Nuevo lead recibido.</p><p><b>${lead.name}</b> · ${lead.phone} · ${lead.email}</p><p>${lead.description || ''}</p><p><a href="tel:${lead.phone}">Llamar</a> · <a href="mailto:${lead.email}">Email</a> · <a href="https://wa.me/${String(lead.phone).replace('+','')}">WhatsApp</a></p><p><a href="${adminUrl}">Abrir lead en admin</a></p>`);
    if (lead.email) await sendEmail(lead.email, 'Hemos recibido tu solicitud de presupuesto', '<p>Gracias por contactar con J&R Rehabilitaciones. Hemos recibido tu solicitud y te contactaremos con los próximos pasos.</p>');

    await supabase.from('lead_history').insert({ lead_id: lead.id, state: 'Nuevo', note: 'Lead creado' });
    return NextResponse.json({ ok: true });
  } catch (e) {
    return NextResponse.json({ error: 'Error al registrar lead' }, { status: 500 });
  }
}
