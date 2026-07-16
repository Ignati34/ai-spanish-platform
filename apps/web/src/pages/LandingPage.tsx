import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { LanguageSwitcher } from '../components/layout/LanguageSwitcher';
import { Button } from '../components/ui/Button';

export default function LandingPage() {
  const { t } = useTranslation();
  return (
    <div className="min-h-full">
      <header className="flex items-center justify-between px-6 py-4">
        <div className="text-lg font-semibold text-brand-700">🇪🇸 {t('app')}</div>
        <div className="flex items-center gap-3">
          <LanguageSwitcher />
          <Link to="/login"><Button variant="secondary">{t('login.submit')}</Button></Link>
        </div>
      </header>
      <section className="mx-auto max-w-3xl px-6 py-20 text-center">
        <h1 className="text-4xl font-bold text-slate-900">A1 → C2</h1>
        <p className="mt-4 text-lg text-slate-600">
          Sube cualquier texto, audio o vídeo y recibe una lección personalizada de español:
          gramática en tu idioma, tarjetas, ejercicios, práctica de voz y corrección de errores.
        </p>
        <div className="mt-8 flex justify-center gap-3">
          <Link to="/login"><Button>{t('login.register')}</Button></Link>
        </div>
        <p className="mt-6 text-sm text-slate-400">RU · UK · AR · FR · ES · EN — Web + Telegram Mini App</p>
      </section>
    </div>
  );
}
