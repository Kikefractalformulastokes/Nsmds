import { LeadForm } from '@/components/LeadForm';
import { company } from '@/lib/site';

export default function Page(){return <main className="container-page py-12"><h1 className="text-4xl font-bold">Contacto y presupuesto</h1><p className="mt-4">Zona de servicio: Comunidad de Madrid (Madrid, Alcobendas, San Sebastián de los Reyes, Getafe, Leganés, Alcorcón, Móstoles, Pozuelo, Majadahonda, Las Rozas, Rivas, Coslada).</p><p className="mt-2">Tel: <a href={`tel:${company.phone}`} className="text-brand">{company.phone}</a> · WhatsApp: <a href={`https://wa.me/${company.whatsapp.replace('+','')}`} className="text-brand">{company.whatsapp}</a></p><section className="mt-6"><LeadForm/></section></main>}
