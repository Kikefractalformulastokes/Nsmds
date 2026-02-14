import './globals.css';
import type { Metadata } from 'next';
import { Header } from '@/components/Header';
import { Footer } from '@/components/Footer';
import { MobileStickyCTA } from '@/components/MobileStickyCTA';
import { company } from '@/lib/site';

export const metadata: Metadata = {
  title: `${company.name} | Trabajos verticales y rehabilitación en Madrid`,
  description: 'Empresa de trabajos verticales, fachadas, cubiertas e impermeabilizaciones en la Comunidad de Madrid. Presupuesto claro y sin compromiso.',
  openGraph: {
    title: company.name,
    description: 'Intervenciones seguras, rápidas y con informe fotográfico.',
    locale: 'es_ES',
    type: 'website',
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  const schema = {
    '@context': 'https://schema.org',
    '@type': 'ConstructionCompany',
    name: company.name,
    areaServed: company.area,
    serviceType: ['trabajos verticales', 'rehabilitación de fachadas', 'cubiertas y tejados', 'impermeabilizaciones', 'mantenimiento'],
  };

  return (
    <html lang="es">
      <body>
        <Header />
        {children}
        <Footer />
        <MobileStickyCTA />
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }} />
      </body>
    </html>
  );
}
