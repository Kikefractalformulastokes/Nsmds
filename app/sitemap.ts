import { MetadataRoute } from 'next';

export default function sitemap(): MetadataRoute.Sitemap {
  const routes = ['','/servicios','/servicios/trabajos-verticales','/servicios/rehabilitacion-fachadas','/servicios/cubiertas-tejados','/servicios/impermeabilizaciones','/servicios/patios-medianeras-bajantes','/servicios/mantenimiento-urgencias','/comunidades','/administradores-fincas','/obra-publica','/proyectos','/contacto','/aviso-legal','/privacidad','/cookies'];
  return routes.map((r) => ({ url: `https://jrrehabilitaciones.es${r}`, lastModified: new Date() }));
}
