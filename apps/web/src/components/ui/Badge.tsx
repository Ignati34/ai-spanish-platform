import { ReactNode } from 'react';
const tones: Record<string, string> = {
  slate: 'bg-slate-100 text-slate-700', green: 'bg-emerald-100 text-emerald-700',
  blue: 'bg-brand-100 text-brand-700', red: 'bg-rose-100 text-rose-700', amber: 'bg-amber-100 text-amber-700'
};
export function Badge({ children, tone = 'blue' }: { children: ReactNode; tone?: string }) {
  return <span className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${tones[tone] ?? tones.blue}`}>{children}</span>;
}
