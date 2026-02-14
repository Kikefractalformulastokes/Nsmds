import Link from 'next/link';

export function PageLeadCTA({ title = '¿Tienes un caso similar? Pide presupuesto' }: { title?: string }) {
  return <aside className="card mt-8"><h3 className="text-xl font-bold">{title}</h3><div className="mt-4 flex gap-3"><Link className="btn-primary" href="/contacto">Pedir presupuesto</Link><Link className="btn-secondary" href="/contacto">Inspección gratuita</Link></div></aside>;
}
