import Link from 'next/link';
import { company } from '@/lib/site';

export function Header() {
  return (
    <header className="sticky top-0 z-40 border-b bg-white/95 backdrop-blur">
      <div className="container-page flex h-16 items-center justify-between">
        <Link href="/" className="font-bold text-brand">{company.name}</Link>
        <nav className="hidden gap-4 md:flex">
          <Link href="/servicios">Servicios</Link>
          <Link href="/comunidades">Comunidades</Link>
          <Link href="/administradores-fincas">Administradores</Link>
          <Link href="/proyectos">Proyectos</Link>
          <Link href="/contacto">Contacto</Link>
        </nav>
        <Link className="btn-primary hidden md:inline-flex" href="/contacto">Pedir presupuesto</Link>
      </div>
    </header>
  );
}
