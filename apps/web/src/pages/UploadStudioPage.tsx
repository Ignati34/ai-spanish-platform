import { useRef, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { ExerciseCard } from '../components/ExerciseCard';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

const LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];

export default function UploadStudioPage() {
  const { t, i18n } = useTranslation();
  const [tab, setTab] = useState<'text' | 'file'>('text');
  const [text, setText] = useState('Ayer fui al supermercado y compré frutas porque quería preparar una cena para mis amigos.');
  const [cefr, setCefr] = useState('A1');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [lesson, setLesson] = useState<any>(null);
  const fileRef = useRef<HTMLInputElement>(null);

  const run = async (fn: () => Promise<any>) => {
    setLoading(true); setError(null); setLesson(null);
    try { setLesson(await fn()); }
    catch (e: any) { setError(String(e.message || e)); }
    finally { setLoading(false); }
  };

  const buildText = () => run(() => api.uploadText(text, i18n.language, cefr));
  const buildFile = () => {
    const f = fileRef.current?.files?.[0];
    if (!f) return;
    return run(() => api.uploadFile(f, i18n.language, cefr));
  };

  return (
    <div>
      <PageHeader title={t('upload.title')} description="файл/текст → урок: анализ, карточки, упражнения" />

      <Card>
        <div className="mb-4 flex gap-2">
          <Button variant={tab === 'text' ? 'primary' : 'secondary'} onClick={() => setTab('text')}>{t('upload.paste')}</Button>
          <Button variant={tab === 'file' ? 'primary' : 'secondary'} onClick={() => setTab('file')}>{t('upload.file')}</Button>
          <div className="ms-auto flex items-center gap-2">
            <span className="text-xs text-slate-500">{t('upload.level')}</span>
            <select className="rounded-lg border border-slate-200 px-2 py-1 text-sm" value={cefr} onChange={(e) => setCefr(e.target.value)}>
              {LEVELS.map((l) => <option key={l} value={l}>{l}</option>)}
            </select>
          </div>
        </div>

        {tab === 'text' ? (
          <>
            <textarea className="h-40 w-full rounded-lg border border-slate-200 p-3 text-sm" value={text}
              placeholder={t('upload.placeholder')} onChange={(e) => setText(e.target.value)} />
            <Button className="mt-3" onClick={buildText} disabled={loading}>{loading ? t('upload.building') : t('upload.build')}</Button>
          </>
        ) : (
          <>
            <input ref={fileRef} type="file" accept=".txt,.md,.pdf,.docx,.html,.mp3,.wav,.m4a,.ogg" className="block w-full text-sm" />
            <p className="mt-1 text-xs text-slate-400">{t('upload.drop')}</p>
            <Button className="mt-3" onClick={buildFile} disabled={loading}>{loading ? t('upload.building') : t('upload.build')}</Button>
          </>
        )}
        {error && <p className="mt-3 text-sm text-rose-600">{error}</p>}
      </Card>

      {lesson && (
        <div className="mt-6 space-y-5">
          <Card>
            <div className="flex items-center justify-between">
              <h2 className="text-xl font-semibold">{lesson.title}</h2>
              <Badge tone="amber">CEFR {lesson.cefr_estimate}</Badge>
            </div>
            {lesson.summary && <p className="mt-2 text-sm text-slate-600">{lesson.summary}</p>}
          </Card>

          {lesson.transcript && (
            <Card>
              <div className="mb-2 text-sm font-medium">{t('upload.transcript')}</div>
              <p className="text-sm leading-6 text-slate-600">{lesson.transcript}</p>
            </Card>
          )}

          {!!(lesson.analysis?.vocabulary?.length) && (
            <Card>
              <div className="mb-3 text-sm font-medium">{t('upload.vocabulary')}</div>
              <div className="flex flex-wrap gap-2">
                {lesson.analysis.vocabulary.map((v: any, i: number) => (
                  <Badge key={i} tone="slate">{v.word} → {v.translation}</Badge>
                ))}
              </div>
            </Card>
          )}

          {!!(lesson.cards?.length) && (
            <div>
              <div className="mb-3 text-sm font-medium text-slate-700">{t('upload.cards')}</div>
              <div className="grid gap-4 md:grid-cols-3">
                {lesson.cards.map((c: any, i: number) => (
                  <Card key={i}>
                    <div className="text-lg font-medium">{c.front}</div>
                    <div className="mt-1 text-slate-500">{c.back}</div>
                    {c.example_sentence && <div className="mt-2 text-xs text-slate-400">{c.example_sentence}</div>}
                  </Card>
                ))}
              </div>
            </div>
          )}

          {!!(lesson.exercises?.length) && (
            <div>
              <div className="mb-3 text-sm font-medium text-slate-700">{t('upload.exercises')}</div>
              <div className="space-y-3">
                {lesson.exercises.map((ex: any, i: number) => <ExerciseCard key={i} ex={ex} />)}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
