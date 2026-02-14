# J&R Rehabilitaciones · Web corporativa + mini CRM

Proyecto Next.js orientado a captación y gestión de leads para trabajos verticales y rehabilitación en la Comunidad de Madrid.

## Puesta en marcha
1. Instala dependencias:
   ```bash
   npm install
   ```
2. Configura variables:
   ```bash
   cp .env.example .env.local
   ```
3. Ejecuta migraciones SQL en Supabase con `sql/schema.sql`.
4. Arranca el proyecto:
   ```bash
   npm run dev
   ```

## Qué editar antes de publicar
- **Teléfono y WhatsApp**: `NEXT_PUBLIC_COMPANY_PHONE`, `NEXT_PUBLIC_COMPANY_WHATSAPP`.
- **Email de notificaciones de leads**: `COMPANY_NOTIFICATION_EMAIL`.
- **Textos legales**: páginas `/aviso-legal`, `/privacidad`, `/cookies`.
- **Dominio real**: actualizar URLs en `app/sitemap.ts` y `app/robots.ts`.
- **Email provider**: añadir `EMAIL_PROVIDER_KEY` (Resend/SendGrid compatible vía wrapper).
- **Contenido comercial**: revisar copies en landings y servicios según enfoque final.

## Funcionalidades incluidas
- Home de conversión con CTAs visibles y sección especial para administradores.
- Formulario multi-paso con subida de fotos (hasta 6) y guardado de UTMs/referrer/user-agent.
- Guardado de leads en Supabase + historial de estado + notas internas.
- Subida de adjuntos a Supabase Storage (`lead-photos`).
- Envío de email a empresa y confirmación automática al cliente.
- Panel `/admin` con login, filtros, pipeline y exportación CSV.
- SEO técnico base: metadata, OpenGraph, sitemap, robots y schema.org.

## Rutas principales
`/`, `/servicios`, `/comunidades`, `/administradores-fincas`, `/obra-publica`, `/proyectos`, `/contacto`, `/admin`.
