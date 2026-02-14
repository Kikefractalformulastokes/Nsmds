import Image from 'next/image';
import { PageLeadCTA } from '@/components/PageLeadCTA';

const items = [
  ['Fachadas', 'Reparación de revestimiento y protección superficial'],
  ['Cubiertas', 'Sellado de puntos críticos y mejora de evacuación'],
  ['Verticales', 'Intervención en altura sin andamio en zonas puntuales'],
  ['Impermeabilización', 'Tratamiento integral frente a filtraciones'],
];

export default function Page(){return <main className="container-page py-12"><h1 className="text-4xl font-bold">Proyectos y casos</h1><p className="mt-3">Filtra por tipología: Fachadas / Cubiertas / Verticales / Impermeabilización.</p><div className="mt-6 grid gap-4 md:grid-cols-2">{items.map((x,i)=><article key={i} className="card"><Image src={`https://images.unsplash.com/photo-1429497419816-9ca5cfb4571a?auto=format&fit=crop&w=1200&q=80&v=${i}`} alt={x[0]} width={600} height={300} className="h-44 w-full rounded-lg object-cover"/><h2 className="mt-3 text-xl font-bold">{x[0]} · Madrid</h2><p className="text-sm"><strong>Problema:</strong> deterioro y riesgo de filtraciones.</p><p className="text-sm"><strong>Solución:</strong> {x[1]}.</p><p className="text-sm"><strong>Resultado:</strong> recuperación funcional y estética con seguimiento documentado.</p></article>)}</div><PageLeadCTA/></main>}
