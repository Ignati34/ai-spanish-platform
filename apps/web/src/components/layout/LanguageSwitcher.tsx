import { useTranslation } from 'react-i18next';
const LANGS = [
  { code: 'ru', label: 'Русский' }, { code: 'uk', label: 'Українська' },
  { code: 'ar', label: 'العربية' }, { code: 'fr', label: 'Français' },
  { code: 'es', label: 'Español' }, { code: 'en', label: 'English' }
];
export function LanguageSwitcher() {
  const { i18n } = useTranslation();
  return (
    <select
      value={i18n.language}
      onChange={(e) => i18n.changeLanguage(e.target.value)}
      className="rounded-lg border border-slate-200 bg-white px-2 py-1 text-sm"
      aria-label="language"
    >
      {LANGS.map((l) => <option key={l.code} value={l.code}>{l.label}</option>)}
    </select>
  );
}
