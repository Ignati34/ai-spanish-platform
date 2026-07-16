import { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

export default function ProgressPage() {
  const { t } = useTranslation();
  const [data, setData] = useState<any>(null);
  const [exercises, setExercises] = useState<any[]>([]);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api.progressOverview().then(setData).catch((e) => setError(String(e.message || e)));
  }, []);

  const maxCount = Math.max(1, ...((data?.weak_spots || []).map((s: any) => s.count)));

  const practice = async () => {
    setBusy(true); setError(null);
    try { const r = await api.progressPractice(); setExercises(r.exercises || []); }
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

      {exercises.length > 0 && (
        <div className="mt-6">
          <div className="mb-3 text-sm font-medium text-slate-700">{t('progress.targeted')}</div>
          <div className="space-y-3">
            {exercises.map((ex: any, i: number) => (
              <Card key={i}>
                <div className="text-sm font-medium">{ex.prompt}</div>
                {ex.options && <div className="mt-2 flex flex-wrap gap-2">{ex.options.map((o: string, j: number) => <Badge key={j} tone={o === ex.correct_answer ? 'green' : 'slate'}>{o}</Badge>)}</div>}
                {ex.explanation && <div className="mt-2 text-xs text-slate-500">{ex.explanation}</div>}
              </Card>
            ))}
          </div>
        </div>
      )}

      {data?.recent?.length > 0 && (
        <Card className="mt-6">
          <div className="mb-3 text-sm font-medium">{t('progress.recent')}</div>
          <div className="space-y-2">
            {data.recent.map((m: any, i: number) => (
              <div key={i} className="text-sm">
                <span className="text-slate-400">[{m.type}]</span>{' '}
                {m.topic && <Badge tone="amber">{m.topic}</Badge>}{' '}
                {m.explanation && <span className="text-slate-600">— {m.explanation}</span>}
              </div>
            ))}
          </div>
        </Card>
      )}
    </div>
  );
}
