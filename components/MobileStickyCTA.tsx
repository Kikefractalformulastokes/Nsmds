import Link from 'next/link';
import { company } from '@/lib/site';

export function MobileStickyCTA() {
  const wa = `https://wa.me/${company.whatsapp.replace('+', '')}`;
  return (
    <div className="fixed bottom-0 left-0 right-0 z-50 border-t bg-white p-2 md:hidden">
      <div className="grid grid-cols-3 gap-2 text-center text-sm font-semibold">
        <a className="rounded-lg bg-brand p-2 text-white" href={`tel:${company.phone}`}>Llamar</a>
        <a className="rounded-lg bg-emerald-600 p-2 text-white" href={wa} target="_blank">WhatsApp</a>
        <Link className="rounded-lg bg-accent p-2 text-white" href="/contacto">Presupuesto</Link>
      </div>
    </div>
  );
}
