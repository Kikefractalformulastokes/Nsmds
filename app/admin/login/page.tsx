'use client';
import { useState } from 'react';
import { createClient } from '@supabase/supabase-js';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    const supabase = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL || process.env.SUPABASE_URL!, process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || process.env.SUPABASE_ANON_KEY!);
    const { error } = await supabase.auth.signInWithPassword({ email, password });
    if (error) return setError(error.message);
    window.location.href = '/admin';
  }

  return <main className="container-page py-20"><form className="card mx-auto max-w-md space-y-3" onSubmit={submit}><h1 className="text-2xl font-bold">Acceso admin</h1><input className="w-full rounded border p-3" placeholder="Email" onChange={(e)=>setEmail(e.target.value)} /><input className="w-full rounded border p-3" placeholder="Contraseña" type="password" onChange={(e)=>setPassword(e.target.value)} /><button className="btn-primary w-full">Entrar</button>{error && <p className="text-red-500">{error}</p>}</form></main>;
}
