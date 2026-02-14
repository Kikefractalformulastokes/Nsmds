create table if not exists public.leads (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  service text,
  client_type text,
  location text,
  urgency text,
  description text,
  name text,
  phone text,
  email text,
  consent boolean default false,
  state text default 'Nuevo',
  notes text,
  photo_paths text[],
  utm_source text,
  utm_medium text,
  utm_campaign text,
  utm_content text,
  utm_term text,
  referrer text,
  source_page text,
  user_agent text
);

create table if not exists public.lead_history (
  id bigint generated always as identity primary key,
  lead_id uuid references public.leads(id) on delete cascade,
  state text,
  note text,
  created_at timestamptz default now()
);

alter table public.leads enable row level security;
alter table public.lead_history enable row level security;

create policy "Allow authenticated read leads" on public.leads for select to authenticated using (true);
create policy "Allow authenticated update leads" on public.leads for update to authenticated using (true);
create policy "Allow service insert leads" on public.leads for insert to anon, authenticated with check (true);
create policy "Allow authenticated read history" on public.lead_history for select to authenticated using (true);
create policy "Allow service insert history" on public.lead_history for insert to anon, authenticated with check (true);

insert into storage.buckets (id, name, public) values ('lead-photos', 'lead-photos', false) on conflict (id) do nothing;
