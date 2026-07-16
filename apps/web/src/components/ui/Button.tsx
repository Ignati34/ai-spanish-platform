import { ButtonHTMLAttributes } from 'react';
interface Props extends ButtonHTMLAttributes<HTMLButtonElement> { variant?: 'primary' | 'secondary'; }
export function Button({ variant = 'primary', className = '', ...rest }: Props) {
  const styles = variant === 'primary'
    ? 'bg-brand-600 text-white hover:bg-brand-700'
    : 'bg-slate-100 text-slate-800 hover:bg-slate-200';
  return <button className={`rounded-xl px-4 py-2 text-sm font-medium transition disabled:opacity-50 ${styles} ${className}`} {...rest} />;
}
