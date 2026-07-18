import { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { ExerciseCard } from '../components/ExerciseCard';
import { Badge } from '../components/ui/Badge';

export default function ProgressPage() {
  const { t } = useTranslation();
  const [data, setData] = useState<any>(null);
  const [exercises, setExercises] = useState<any[]>([]);
  const [vocab, setVocab] = useState<any[]>([]);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api.progressOverview().then(setData).catch((e) => setError(String(e.message || e)));
  }, []);

  const maxCount = Math.max(1, ...((data?.weak_spots || []).map((s: any) => s.count)));

  const [autoPracticed, setAutoPracticed] = useState(false);
  useEffect(() => {
    if (!autoPracticed && (data?.weak_spots || []).length > 0) {
      setAutoPracticed(true);
      api.progressPractice().then((r) => { setVocab(r.vocabulary || []); setExercises(r.exercises || []); }).catch(() => {});
    }
  }, [data, autoPracticed]);

  const practice = async () => {
    setBusy(true); setError(null);
    try { const r = await api.progressPractice(); setExercises(r.exercises || []); setVocab(r.vocabulary || []); }
    catch (e: any) { setError(String(e.message || e)); }
    finally { setBusy(false); }
  };

  return (
    <div>
      <PageHeader title={t('progress.title')} description={t('progress.subtitle')} />
      {error && <p className="mb-3 text-sm text-rose-600">{error}</p>}

      <div className="grid gap-4 md:grid-cols-3">
        <Card><div className="text-sm text-slate-500">{t('progress.level')}</div><div className="mt-2 text-3xl font-bold">{data?.level ?? '—'}</div></Card>
        <Card><div className="text-sm text-slate-500">{t('progress.mistakes')}</div><div className="mt-2 text-3xl font-bold">{data?.total_mistakes ?? 0}</div></Card>
        <Card className="md:col-span-1">
          <div className="text-sm text-slate-500">{t('progress.practice')}</div>
          <Button className="mt-2" onClick={practice} disabled={busy}>{busy ? '…' : t('progress.practiceBtn')}</Button>
        </Card>
      </div>

      <div className="mt-4 grid gap-4 md:grid-cols-2">
        <Card>
          <div className="mb-3 text-sm font-medium">{t('progress.weakSpots')}</div>
          {(data?.weak_spots || []).length === 0 && <p className="text-sm text-slate-400">{t('progress.empty')}</p>}
          <div className="space-y-2">
            {(data?.weak_spots || []).map((s: any, i: number) => (
              <div key={i}>
                <div className="flex justify-between text-sm"><span>{s.topic}</span><span className="text-slate-400">{s.count}×</span></div>
                <div className="mt-1 h-2 rounded-full bg-slate-100"><div className="h-2 rounded-full bg-brand-500" style={{ width: `${(s.count / maxCount) * 100}%` }} /></div>
              </div>
            ))}
          </div>
        </Card>

        <Card>
          <div className="mb-3 text-sm font-medium">{t('progress.plan')}</div>
          <ol className="list-decimal space-y-1 ps-5 text-sm text-slate-600">
            {(data?.study_plan || []).map((s: string, i: number) => <li key={i}>{s}</li>)}
          </ol>
        </Card>
      </div>

      {vocab.length > 0 && (
        <div className="mt-6">
          <div className="mb-3 text-sm font-medium text-slate-700">{t('progress.words')}</div>
          <div className="grid gap-3 md:grid-cols-2">
            {vocab.map((v: any, i: number) => (
              <Card key={i}>
                <div className="flex items-baseline justify-between">
                  <span className="text-lg font-medium">{v.word}</span>
                  <span className="text-sm text-slate-500">{v.translation}</span>
                </div>
                {v.example && <div className="mt-1 text-sm text-slate-400">“{v.example}”</div>}
              </Card>
            ))}
          </div>
        </div>
      )}

      {exercises.length > 0 && (
        <div className="mt-6">
          <div className="mb-3 text-sm font-medium text-slate-700">{t('progress.targeted')}</div>
          <div className="space-y-3">
            {exercises.map((ex: any, i: number) => (
              <ExerciseCard key={i} ex={ex} onAnswer={(correct) => {
                if (!correct) api.progressRecord({ original: ex.prompt, corrected: ex.correct_answer, explanation: ex.explanation }).then(() => api.progressOverview().then(setData)).catch(() => {});
              }} />
            ))}
          </div>
        </div>
      )}

      {data?.recent?.length > 0 && (
        <Card className="mt-6">
          <div className="mb-3 text-sm font-medium">{t('progress.recent')}</div>
          <div className="space-y-2">
            {data.recent.map((m: any, i: number) => {
              const hasCorrection = m.original && m.corrected && m.original !== m.corrected && m.corrected !== '-' && m.original !== '-';
              return (
                <div key={i} className="rounded-lg border border-slate-100 px-3 py-2 text-sm">
                  {m.topic && <Badge tone="amber">{m.topic}</Badge>}
                  {hasCorrection && (
                    <div className="mt-1"><span className="text-rose-500 line-through">{m.original}</span>{' → '}<span className="text-emerald-600">{m.corrected}</span></div>
                  )}
                  {m.explanation && <div className="mt-1 text-slate-500">{m.explanation}</div>}
                </div>
              );
            })}
          </div>
        </Card>
      )}
    </div>
  );
}
