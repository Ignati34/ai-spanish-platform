import { ReactNode } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { LanguageSwitcher } from './LanguageSwitcher';
import { useAuth } from '../../store/auth';

const items = [
  { to: '/app', key: 'dashboard', end: true },
  { to: '/app/diagnostic', key: 'diagnostic' },
  { to: '/app/course', key: 'course' },
  { to: '/app/upload', key: 'upload' },
  { to: '/app/analyzer', key: 'analyzer' },
  { to: '/app/voice', key: 'voice' },
  { to: '/app/flashcards', key: 'flashcards' },
  { to: '/app/review', key: 'review' },
  { to: '/app/progress', key: 'progress' },
  { to: '/app/billing', key: 'billing' },
  { to: '/app/admin', key: 'admin' }
];

export function AppShell({ children }: { children: ReactNode }) {
  const { t } = useTranslation();
  const { logout } = useAuth();
  const navigate = useNavigate();
  return (
    <div className="min-h-full md:grid md:grid-cols-[240px_1fr]">
      <aside className="border-e border-slate-200 bg-white p-4 md:min-h-screen">
        <div className="mb-6 px-2 text-lg font-semibold text-brand-700">🇪🇸 {t('app')}</div>
        <nav className="space-y-1">
          {items.map((it) => (
            <NavLink key={it.key} to={it.to} end={it.end}
              className={({ isActive }) => `block rounded-lg px-3 py-2 text-sm ${isActive ? 'bg-brand-50 text-brand-700 font-medium' : 'text-slate-600 hover:bg-slate-50'}`}>
              {t(`nav.${it.key}`)}
            </NavLink>
          ))}
        </nav>
        <button onClick={() => { logout(); navigate('/login'); }} className="mt-6 w-full rounded-lg px-3 py-2 text-start text-sm text-slate-500 hover:bg-slate-50">
          {t('nav.logout')}
        </button>
      </aside>
      <div>
        <header className="flex items-center justify-end gap-3 border-b border-slate-200 bg-white px-6 py-3">
          <LanguageSwitcher />
        </header>
        <main className="p-6">{children}</main>
      </div>
    </div>
  );
}
