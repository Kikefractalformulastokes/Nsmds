'use client';

import { useState } from 'react';

const services = ['Fachada', 'Tejado-Cubierta', 'Impermeabilización', 'Verticales', 'Patios-Medianeras-Bajantes', 'Mantenimiento', 'Urgencia'];
const clients = ['Comunidad', 'Administrador', 'Empresa', 'Particular', 'Obra pública'];

export function LeadForm() {
  const [step, setStep] = useState(1);
  const [loading, setLoading] = useState(false);
  const [form, setForm] = useState<any>({ urgency: 'Esta semana', consent: false });

  const set = (k: string, v: string | boolean) => setForm((s: any) => ({ ...s, [k]: v }));

  async function submit() {
    setLoading(true);
    const fd = new FormData();
    Object.entries(form).forEach(([k, v]) => {
      if (k !== 'photos') fd.append(k, String(v));
    });
    if (form.photos) Array.from(form.photos as FileList).slice(0, 6).forEach((f: any) => fd.append('photos', f));
    const params = new URLSearchParams(window.location.search);
    ['utm_source','utm_medium','utm_campaign','utm_content','utm_term'].forEach((k)=>fd.append(k, params.get(k) || ''));
    fd.append('referrer', document.referrer || '');
    fd.append('source_page', window.location.pathname);

    const res = await fetch('/api/leads', { method: 'POST', body: fd });
    setLoading(false);
    if (res.ok) window.location.href = '/gracias';
    else alert('No se pudo enviar. Inténtalo de nuevo.');
  }

  return (
    <div className="card">
      <p className="mb-4 text-sm text-slate-500">Paso {step} de 4</p>
      {step === 1 && <div className="space-y-3">{services.map((s)=><button key={s} onClick={()=>{set('service',s);setStep(2);}} className="w-full rounded-lg border p-3 text-left hover:border-brand">{s}</button>)}</div>}
      {step === 2 && <div className="space-y-3">{clients.map((s)=><button key={s} onClick={()=>{set('client_type',s);setStep(3);}} className="w-full rounded-lg border p-3 text-left hover:border-brand">{s}</button>)}<button className="text-sm" onClick={()=>setStep(1)}>Atrás</button></div>}
      {step === 3 && <div className="space-y-3">
        <input className="w-full rounded-lg border p-3" placeholder="Municipio/Zona" onChange={(e)=>set('location',e.target.value)} />
        <select className="w-full rounded-lg border p-3" onChange={(e)=>set('urgency',e.target.value)} defaultValue="Esta semana"><option>Hoy</option><option>Esta semana</option><option>Este mes</option></select>
        <textarea className="w-full rounded-lg border p-3" placeholder="Breve descripción" onChange={(e)=>set('description',e.target.value)} />
        <input type="file" multiple accept="image/*" onChange={(e)=>set('photos', e.target.files || '')} />
        <button className="btn-primary" onClick={()=>setStep(4)}>Continuar</button>
      </div>}
      {step === 4 && <div className="space-y-3">
        <input className="w-full rounded-lg border p-3" placeholder="Nombre" onChange={(e)=>set('name',e.target.value)} />
        <input className="w-full rounded-lg border p-3" placeholder="Teléfono" onChange={(e)=>set('phone',e.target.value)} />
        <input className="w-full rounded-lg border p-3" placeholder="Email" onChange={(e)=>set('email',e.target.value)} />
        <label className="flex gap-2 text-sm"><input type="checkbox" onChange={(e)=>set('consent',e.target.checked)} /> Acepto la política de privacidad y el tratamiento de datos.</label>
        <button disabled={loading || !form.consent} className="btn-primary" onClick={submit}>{loading ? 'Enviando...' : 'Enviar solicitud'}</button>
      </div>}
    </div>
  );
}
