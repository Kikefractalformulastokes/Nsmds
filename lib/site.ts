export const company = {
  name: 'J&R Rehabilitaciones',
  area: 'Comunidad de Madrid',
  phone: process.env.NEXT_PUBLIC_COMPANY_PHONE || '+34000000000',
  whatsapp: process.env.NEXT_PUBLIC_COMPANY_WHATSAPP || '+34000000000',
};

export const services = [
  { slug: 'trabajos-verticales', title: 'Trabajos verticales' },
  { slug: 'rehabilitacion-fachadas', title: 'Rehabilitación de fachadas' },
  { slug: 'cubiertas-tejados', title: 'Cubiertas y tejados' },
  { slug: 'impermeabilizaciones', title: 'Impermeabilizaciones' },
  { slug: 'patios-medianeras-bajantes', title: 'Patios, medianeras y bajantes' },
  { slug: 'mantenimiento-urgencias', title: 'Mantenimiento y urgencias' },
];

export const pipelineStates = ['Nuevo', 'Contactado', 'Visitado', 'Presupuesto enviado', 'Ganado', 'Perdido'];
