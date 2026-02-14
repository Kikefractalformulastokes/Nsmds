import Link from 'next/link';
import Image from 'next/image';
import { services } from '@/lib/site';

export function ServicesGrid() {
  return <section className="container-page py-12"><h2 className="mb-6 text-3xl font-bold">Servicios</h2><div className="grid gap-4 md:grid-cols-3">{services.map((s)=><Link key={s.slug} className="card hover:border-brand" href={`/servicios/${s.slug}`}>{s.title}</Link>)}</div></section>;
}

export function ProjectsSection() {
  const cards = ['Fachada','Tejado','Verticales','Impermeabilización','Fachada','Verticales'];
  return <section className="container-page py-12"><h2 className="mb-6 text-3xl font-bold">Proyectos destacados</h2><div className="grid gap-4 md:grid-cols-3">{cards.map((c,i)=><article key={i} className="card"><Image src={`https://images.unsplash.com/photo-1487958449943-2429e8be8625?auto=format&fit=crop&w=900&q=80&v=${i}`} alt={c} width={600} height={340} className="mb-3 h-40 w-full rounded-xl object-cover"/><span className="text-xs font-semibold text-brand">{c}</span><p className="text-sm">Intervención planificada con seguridad y coordinación de vecinos.</p></article>)}</div></section>;
}
