import { Resend } from 'resend';

const resend = process.env.EMAIL_PROVIDER_KEY ? new Resend(process.env.EMAIL_PROVIDER_KEY) : null;

export async function sendEmail(to: string, subject: string, html: string) {
  if (!resend) return;
  await resend.emails.send({
    from: 'J&R Rehabilitaciones <no-reply@jrrehabilitaciones.es>',
    to,
    subject,
    html,
  });
}
