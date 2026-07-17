import { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Badge } from '../components/ui/Badge';

const LANGS: { code: string; label: string }[] = [
  { code: 'ru', label: 'Русский' },
  { code: 'uk', label: 'Українська' },
  { code: 'ar', label: 'العربية' },
  { code: 'fr', label: 'Français' },
  { code: 'es', label: 'Español' },
  { code: 'en', label: 'English' }
];

export default function SettingsPage() {
  const { t, i18n } = useTranslation();
  const [me, setMe] = useState<any>(null);
  const [saving, setSaving] = useState('');
  const [saved, setSaved] = useState('');

  useEffect(() => { api.me().then(setMe).catch(() => setMe(null)); }, []);

  const setNative = async (lang: string) => {
    setSaving('native'); setSaved('');
    try { const r = await api.updateMe({ native_language: lang }); setMe(r); setSaved('native'); }
    finally { setSaving(''); setTimeout(() => setSaved(''), 2000); }
  };

  const setInterface = async (lang: string) => {
    setSaving('interface');
    try {
      const r = await api.updateMe({ interface_language: lang });
      setMe(r);
      i18n.changeLanguage(lang);
      document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
      setSaved('interface');
    } finally { setSaving(''); setTimeout(() => setSaved(''), 2000); }
  };

  return (
    <div>
      <PageHeader title={t('settings.title')} description={t('settings.subtitle')} />

      <Card className="mb-4">
        <div className="text-sm text-slate-500">{t('settings.account')}</div>
        <div className="mt-1 text-sm">{me?.email ?? '—'}</div>
        <div className="mt-2 flex gap-2">
          <Badge tone="green">CEFR {me?.current_cefr_level ?? 'A1'}</Badge>
          <Badge tone="slate">{me?.role ?? 'student'}</Badge>
        </div>
      </Card>

      <Card className="mb-4">
        <div className="text-sm font-medium">{t('settings.nativeLang')}</div>
        <p className="mt-1 text-xs text-slate-500">{t('settings.nativeHint')}</p>
        <div className="mt-3 flex flex-wrap gap-2">
          {LANGS.map((l) => (
            <button key={l.code} onClick={() => setNative(l.code)} disabled={saving === 'native'}
              className={`rounded-lg border px-3 py-1.5 text-sm ${me?.native_language === l.code ? 'border-brand-400 bg-brand-50 text-brand-700' : 'border-slate-200'}`}>
              {l.label}
            </button>
          ))}
        </div>
        {saved === 'native' && <div className="mt-2 text-xs text-emerald-600">✓ {t('settings.saved')}</div>}
      </Card>

      <Card>
        <div className="text-sm font-medium">{t('settings.interfaceLang')}</div>
        <p className="mt-1 text-xs text-slate-500">{t('settings.interfaceHint')}</p>
        <div className="mt-3 flex flex-wrap gap-2">
          {LANGS.map((l) => (
            <button key={l.code} onClick={() => setInterface(l.code)} disabled={saving === 'interface'}
              className={`rounded-lg border px-3 py-1.5 text-sm ${me?.interface_language === l.code ? 'border-brand-400 bg-brand-50 text-brand-700' : 'border-slate-200'}`}>
              {l.label}
            </button>
          ))}
        </div>
        {saved === 'interface' && <div className="mt-2 text-xs text-emerald-600">✓ {t('settings.saved')}</div>}
      </Card>
    </div>
  );
}
