import { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Badge } from '../components/ui/Badge';
import { ExerciseCard } from '../components/ExerciseCard';

const LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];
const THEORY_LANGS: { code: string; label: string }[] = [
  { code: 'ru', label: 'Русский' },
  { code: 'uk', label: 'Українська' },
  { code: 'ar', label: 'العربية' },
  { code: 'fr', label: 'Français' },
  { code: 'es', label: 'Español' },
  { code: 'en', label: 'English' }
];

export default function CoursePage() {
  const { t, i18n } = useTranslation();
  const [lessons, setLessons] = useState<any[]>([]);
  const [openLevel, setOpenLevel] = useState<string | null>('A1');
  const [openLesson, setOpenLesson] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [theoryLang, setTheoryLang] = useState<string>((i18n.language || 'ru').slice(0, 2));
  const [theoryLoading, setTheoryLoading] = useState(false);

  useEffect(() => {
    api.lessons().then((r) => setLessons(Array.isArray(r) ? r : [])).catch(() => setLessons([])).finally(() => setLoading(false));
  }, []);

  const byLevel = (lvl: string) => lessons.filter((l) => (l.cefr_level || 'A1') === lvl);

  const openDetail = async (id: string, lang = theoryLang) => {
    setOpenLesson({ loading: true });
    try { setOpenLesson(await api.courseLesson(id, lang)); } catch { setOpenLesson(null); }
  };

  const changeTheoryLang = async (lang: string) => {
    setTheoryLang(lang);
    if (!openLesson?.id) return;
    setTheoryLoading(true);
    try {
      const fresh = await api.courseLesson(openLesson.id, lang);
      setOpenLesson(fresh);
    } catch { /* keep current theory on failure */ }
    finally { setTheoryLoading(false); }
  };

  if (openLesson && !openLesson.loading) {
    return (
      <div>
        <PageHeader title={openLesson.title} />
        <button className="mb-4 text-sm text-brand-600" onClick={() => setOpenLesson(null)}>← {t('course.back')}</button>
        {openLesson.theory && (
          <Card className="mb-4">
            <div className="mb-2 flex items-center justify-between gap-2">
              <div className="text-sm font-medium">{t('course.theory')}</div>
              <div className="flex items-center gap-2">
                {theoryLoading && <span className="text-xs text-slate-400">{t('course.translating')}</span>}
                <select
                  className="rounded-lg border border-slate-200 px-2 py-1 text-xs"
                  value={theoryLang}
                  onChange={(e) => changeTheoryLang(e.target.value)}
                  title={t('course.theoryLang')}
                  disabled={theoryLoading}
                >
                  {THEORY_LANGS.map((l) => <option key={l.code} value={l.code}>{l.label}</option>)}
                </select>
              </div>
            </div>
            <p className={`whitespace-pre-line text-sm leading-6 text-slate-600 ${theoryLoading ? 'opacity-50' : ''}`}>{openLesson.theory}</p>
          </Card>
        )}
        {!openLesson.theory && openLesson.summary && <Card className="mb-4"><p className="text-sm text-slate-600">{openLesson.summary}</p></Card>}
        {!!(openLesson.cards?.length) && (
          <div className="mb-4">
            <div className="mb-2 text-sm font-medium">{t('course.words')}</div>
            <div className="grid gap-3 md:grid-cols-3">
              {openLesson.cards.map((c: any, i: number) => (
                <Card key={i}><div className="font-medium">{c.front}</div><div className="text-sm text-slate-500">{c.back}</div>
                  {c.example_sentence && <div className="mt-1 text-xs text-slate-400">{c.example_sentence}</div>}</Card>
              ))}
            </div>
          </div>
        )}
        {!!(openLesson.exercises?.length) && (
          <div>
            <div className="mb-2 text-sm font-medium">{t('course.exercises')}</div>
            <div className="space-y-3">
              {openLesson.exercises.map((ex: any, i: number) => (
                <div key={i}>
                  {ex.section && ex.section !== openLesson.exercises[i - 1]?.section && (
                    <div className="mb-2 mt-4 text-sm font-semibold text-slate-700">{ex.section}</div>
                  )}
                  <ExerciseCard ex={ex} />
                </div>
              ))}
            </div>
          </div>
        )}
        {!openLesson.cards?.length && !openLesson.exercises?.length && <Card><p className="text-sm text-slate-400">{t('course.empty')}</p></Card>}
      </div>
    );
  }

  return (
    <div>
      <PageHeader title={t('nav.course')} description={t('course.subtitle')} />
      {loading ? <Card>…</Card> : (
        <div className="space-y-3">
          {LEVELS.map((lvl) => {
            const ls = byLevel(lvl);
            const isOpen = openLevel === lvl;
            return (
              <Card key={lvl}>
                <button className="flex w-full items-center justify-between" onClick={() => setOpenLevel(isOpen ? null : lvl)}>
                  <span className="text-xl font-semibold">{lvl}</span>
                  <Badge tone={ls.length ? 'green' : 'slate'}>{ls.length ? `${ls.length} ${t('course.lessons')}` : t('course.none')}</Badge>
                </button>
                {isOpen && ls.length > 0 && (
                  <div className="mt-3 space-y-2 border-t border-slate-100 pt-3">
                    {ls.map((l) => (
                      <button key={l.id} onClick={() => openDetail(l.id)} className="block w-full rounded-lg border border-slate-200 px-3 py-2 text-left text-sm hover:bg-slate-50">
                        {l.title}
                      </button>
                    ))}
                  </div>
                )}
                {isOpen && ls.length === 0 && (
                  <div className="mt-3 border-t border-slate-100 pt-3 text-sm text-slate-400">{t('course.buildHint')}</div>
                )}
              </Card>
            );
          })}
        </div>
      )}
    </div>
  );
}
