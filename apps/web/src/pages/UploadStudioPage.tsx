import { useEffect, useRef, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { Link } from 'react-router-dom';
import { ExerciseCard } from '../components/ExerciseCard';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

const LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];

const statusTone: Record<string, string> = {
  uploaded: 'slate', extracted: 'blue', transcribed: 'amber', lesson_ready: 'green'
};

export default function UploadStudioPage() {
  const { t, i18n } = useTranslation();
  const [tab, setTab] = useState<'text' | 'file' | 'url'>('text');
  const [text, setText] = useState('Ayer fui al supermercado y compré frutas porque quería preparar una cena para mis amigos.');
  const [url, setUrl] = useState('');
  const [cefr, setCefr] = useState('A1');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [lesson, setLesson] = useState<any>(null);
  const [history, setHistory] = useState<any[]>([]);
  const fileRef = useRef<HTMLInputElement>(null);

  const loadHistory = () => api.listUploads().then((r) => setHistory(r || [])).catch(() => setHistory([]));
  useEffect(() => { loadHistory(); }, []);

  const run = async (fn: () => Promise<any>) => {
    setLoading(true); setError(null); setLesson(null);
    try {
      const result = await fn();
      setLesson(result);
      loadHistory();
    } catch (e: any) { setError(String(e.message || e)); }
    finally { setLoading(false); }
  };

  const buildText = () => run(() => api.uploadText(text, i18n.language, cefr));
  const buildFile = () => {
    const f = fileRef.current?.files?.[0];
    if (!f) return;
    return run(() => api.uploadFile(f, i18n.language, cefr));
  };
  const buildUrl = () => {
    if (!url.trim()) return;
    return run(() => api.uploadUrl(url.trim(), i18n.language, cefr));
  };

  const fmtDate = (s?: string) => {
    if (!s) return '';
    const d = new Date(s);
    return isNaN(d.getTime()) ? '' : d.toLocaleDateString();
  };

  return (
    <div>
      <PageHeader title={t('upload.title')} description={t('upload.subtitle')} />

      <Card>
        <div className="mb-4 flex gap-2">
          <Button variant={tab === 'text' ? 'primary' : 'secondary'} onClick={() => setTab('text')}>{t('upload.paste')}</Button>
          <Button variant={tab === 'file' ? 'primary' : 'secondary'} onClick={() => setTab('file')}>{t('upload.file')}</Button>
          <Button variant={tab === 'url' ? 'primary' : 'secondary'} onClick={() => setTab('url')}>{t('upload.url')}</Button>
          <div className="ms-auto flex items-center gap-2">
            <span className="text-xs text-slate-500">{t('upload.level')}</span>
            <select className="rounded-lg border border-slate-200 px-2 py-1 text-sm" value={cefr} onChange={(e) => setCefr(e.target.value)}>
              {LEVELS.map((l) => <option key={l} value={l}>{l}</option>)}
            </select>
          </div>
        </div>

        {tab === 'text' && (
          <>
            <textarea className="h-40 w-full rounded-lg border border-slate-200 p-3 text-sm" value={text}
              placeholder={t('upload.placeholder')} onChange={(e) => setText(e.target.value)} />
            <Button className="mt-3" onClick={buildText} disabled={loading}>{loading ? t('upload.building') : t('upload.build')}</Button>
          </>
        )}
        {tab === 'file' && (
          <>
            <input ref={fileRef} type="file" accept=".txt,.md,.pdf,.docx,.html,.mp3,.wav,.m4a,.ogg" className="block w-full text-sm" />
            <p className="mt-1 text-xs text-slate-400">{t('upload.drop')}</p>
            <Button className="mt-3" onClick={buildFile} disabled={loading}>{loading ? t('upload.building') : t('upload.build')}</Button>
          </>
        )}
        {tab === 'url' && (
          <>
            <input type="url" value={url} onChange={(e) => setUrl(e.target.value)}
              placeholder={t('upload.urlPlaceholder')}
              className="block w-full rounded-lg border border-slate-200 px-3 py-2 text-sm" />
            <p className="mt-1 text-xs text-slate-400">{t('upload.urlHint')}</p>
            <Button className="mt-3" onClick={buildUrl} disabled={loading || !url.trim()}>{loading ? t('upload.building') : t('upload.build')}</Button>
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
            {(lesson.lesson_id || lesson.deck_id) && (
              <div className="mt-3 flex flex-wrap items-center gap-3 border-t border-slate-100 pt-3">
                <span className="text-sm text-emerald-700">✓ {t('upload.saved')}</span>
                <Link to="/app/course" className="text-sm font-medium text-brand-700 hover:underline">{t('upload.openCourse')}</Link>
                <Link to="/app/review" className="text-sm font-medium text-brand-700 hover:underline">{t('upload.openReview')}</Link>
              </div>
            )}
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

      <div className="mt-8">
        <div className="mb-3 text-sm font-medium text-slate-700">{t('upload.history')}</div>
        {history.length === 0 ? (
          <Card className="text-center text-sm text-slate-500">{t('upload.empty')}</Card>
        ) : (
          <div className="space-y-2">
            {history.map((h) => (
              <Card key={h.id} className="flex items-center justify-between gap-3 py-3">
                <div className="min-w-0">
                  <div className="truncate text-sm font-medium text-slate-800">{h.filename}</div>
                  <div className="text-xs text-slate-400">{(h.file_type || '').toUpperCase()} · {fmtDate(h.created_at)}</div>
                </div>
                <Badge tone={statusTone[h.status] ?? 'slate'}>{t(`upload.status_${h.status}`, { defaultValue: h.status }) as string}</Badge>
              </Card>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
