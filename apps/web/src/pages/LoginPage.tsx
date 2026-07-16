import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { useAuth } from '../store/auth';
import { getTelegram, isTelegram } from '../lib/telegram';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { LanguageSwitcher } from '../components/layout/LanguageSwitcher';

export default function LoginPage() {
  const { t, i18n } = useTranslation();
  const navigate = useNavigate();
  const { setToken } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [mode, setMode] = useState<'login' | 'register'>('login');
  const [error, setError] = useState<string | null>(null);

  // Auto sign-in inside Telegram Mini App using signed initData.
  useEffect(() => {
    if (!isTelegram()) return;
    const tg = getTelegram()!;
    api.telegramAuth(tg.initData, i18n.language)
      .then((r) => { setToken(r.access_token); navigate('/app'); })
      .catch((e) => setError(String(e.message || e)));
  }, []);

  const submit = async () => {
    setError(null);
    try {
      const r = mode === 'login'
        ? await api.login(email, password)
        : await api.register({ email, password, native_language: i18n.language });
      setToken(r.access_token);
      navigate('/app');
    } catch (e: any) { setError(String(e.message || e)); }
  };

  return (
    <div className="flex min-h-full items-center justify-center p-6">
      <Card className="w-full max-w-sm">
        <div className="mb-4 flex items-center justify-between">
          <h1 className="text-xl font-semibold">{mode === 'login' ? t('login.title') : t('login.register')}</h1>
          <LanguageSwitcher />
        </div>
        <label className="block text-sm text-slate-600">{t('login.email')}</label>
        <input className="mb-3 mt-1 w-full rounded-lg border border-slate-200 px-3 py-2 text-sm" value={email} onChange={(e) => setEmail(e.target.value)} />
        <label className="block text-sm text-slate-600">{t('login.password')}</label>
        <input type="password" className="mb-4 mt-1 w-full rounded-lg border border-slate-200 px-3 py-2 text-sm" value={password} onChange={(e) => setPassword(e.target.value)} />
        {error && <p className="mb-3 text-sm text-rose-600">{error}</p>}
        <Button className="w-full" onClick={submit}>{mode === 'login' ? t('login.submit') : t('login.register')}</Button>
        <button className="mt-3 w-full text-sm text-slate-500" onClick={() => setMode(mode === 'login' ? 'register' : 'login')}>
          {mode === 'login' ? t('login.register') : t('login.title')}
        </button>
      </Card>
    </div>
  );
}
