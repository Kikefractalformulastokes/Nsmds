import Link from 'next/link';
import { company } from '@/lib/site';

export function Footer() {
  return (
    <footer className="mt-16 border-t bg-white">
      <div className="container-page py-10 text-sm text-slate-600">
        <p className="font-semibold text-slate-800">{company.name} · Zona de servicio: {company.area}</p>
        <div className="mt-4 flex flex-wrap gap-4">
          <Link href="/aviso-legal">Aviso legal</Link>
          <Link href="/privacidad">Privacidad</Link>
          <Link href="/cookies">Cookies</Link>
          <Link href="/admin">/admin</Link>
        </div>
      </div>
    </footer>
  );
}
