import Link from 'next/link';
import { LeadForm } from '@/components/LeadForm';
import { ProjectsSection, ServicesGrid } from '@/components/Sections';

export default function HomePage() {
  return (
    <main>
      <section className="container-page py-14">
        <h1 className="text-4xl font-bold">Trabajos verticales y rehabilitación de edificios en la Comunidad de Madrid</h1>
        <p className="mt-4 max-w-3xl text-lg">Especialistas en comunidades de vecinos, administradores de fincas y actuaciones de obra pública. Intervenciones seguras, rápidas y con informe fotográfico.</p>
        <div className="mt-6 flex flex-wrap gap-3">
          <Link className="btn-primary" href="/contacto">Pedir presupuesto</Link>
          <Link className="btn-secondary" href="/servicios">Ver servicios</Link>
        </div>
        <p className="mt-3 text-sm text-slate-600">Respuesta rápida · Coordinación con vecinos · Seguridad y PRL</p>
      </section>

      <section className="container-page"><div className="card bg-brand text-white"><h2 className="text-2xl font-bold">Para administradores de fincas: incidencias resueltas sin dolores de cabeza</h2><ul className="mt-3 list-disc space-y-2 pl-5"><li>Visita e inspección con reporte</li><li>Planificación por portales y horarios</li><li>Fotos antes/después para actas y juntas</li><li>Presupuesto claro por partidas</li></ul><Link href="/contacto" className="mt-5 inline-block rounded-xl bg-white px-5 py-3 font-semibold text-brand">Solicitar visita</Link></div></section>

      <ServicesGrid />

      <section className="container-page py-12"><h2 className="mb-6 text-3xl font-bold">Proceso de trabajo</h2><div className="grid gap-4 md:grid-cols-4">{['1. Inspección y diagnóstico','2. Propuesta y planificación','3. Ejecución segura','4. Entrega con informe y seguimiento'].map((s)=><div key={s} className="card">{s}</div>)}</div></section>

      <section className="container-page py-12"><h2 className="mb-6 text-3xl font-bold">Opiniones</h2><div className="grid gap-4 md:grid-cols-3">{['M. R.','A. G.','P. L.'].map((i)=><div key={i} className="card"><p className="italic">"Servicio rápido, limpio y bien coordinado con la comunidad."</p><p className="mt-3 text-sm font-semibold">{i}</p></div>)}</div><p className="mt-4 text-sm text-slate-500">Casos reales varían según obra; te damos una propuesta adaptada.</p></section>

      <ProjectsSection />

      <section className="container-page py-12"><h2 className="mb-6 text-3xl font-bold">Preguntas frecuentes</h2><div className="grid gap-3">{['¿Cuánto tarda un presupuesto?','¿Hacéis trabajos sin andamio?','¿Cómo coordináis con vecinos?','¿Incluís informe fotográfico?','¿Atendéis urgencias por filtraciones?','¿Trabajáis toda la Comunidad de Madrid?','¿Qué datos necesitáis para estimar precio?','¿Podéis planificar por fases para minimizar molestias?'].map((q)=><details key={q} className="card"><summary className="cursor-pointer font-semibold">{q}</summary><p className="mt-2 text-sm">Analizamos el caso y planteamos una propuesta clara, priorizando seguridad, planificación y mínima molestia.</p></details>)}</div></section>

      <section className="container-page py-12"><div className="grid gap-6 md:grid-cols-2"><div><h2 className="text-3xl font-bold">Pedir presupuesto en 1 minuto</h2><p className="mt-3">Llámanos, escríbenos por WhatsApp o completa este formulario.</p></div><LeadForm /></div></section>
    </main>
  );
}
