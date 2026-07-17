import { useRef, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { ExerciseCard } from '../components/ExerciseCard';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

const LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];

function fmt(t: number) {
  const s = Math.floor(t || 0);
  return `${String(Math.floor(s / 60)).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`;
}

export default function PodcastStudioPage() {
  const { t, i18n } = useTranslation();
  const [cefr, setCefr] = useState('A1');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [data, setData] = useState<any>(null);
  const fileRef = useRef<HTMLInputElement>(null);

  const build = async () => {
    const f = fileRef.current?.files?.[0];
    if (!f) return;
    setLoading(true); setError(null); setData(null);
    try { setData(await api.podcastCreate(f, i18n.language, cefr, f.name)); }
    catch (e: any) { setError(String(e.message || e)); }
    finally { setLoading(false); }
  };

  const lesson = data?.lesson;

  return (
    <div>
      <PageHeader title={t('podcast.title')} description={t('podcast.subtitle')} />

      <Card>
        <input ref={fileRef} type="file" accept=".mp3,.wav,.m4a,.ogg,.webm" className="block w-full text-sm" />
        <div className="mt-3 flex items-center gap-3">
          <span className="text-xs text-slate-500">{t('podcast.level')}</span>
          <select className="rounded-lg border border-slate-200 px-2 py-1 text-sm" value={cefr} onChange={(e) => setCefr(e.target.value)}>
            {LEVELS.map((l) => <option key={l} value={l}>{l}</option>)}
          </select>
          <Button onClick={build} disabled={loading}>{loading ? t('podcast.building') : t('podcast.build')}</Button>
        </div>
        {error && <p className="mt-3 text-sm text-rose-600">{error}</p>}
      </Card>

      {data && (
        <div className="mt-6 space-y-5">
          <Card>
            <div className="flex items-center justify-between">
              <h2 className="text-xl font-semibold">{data.title}</h2>
              <div className="flex gap-2">
                {data.duration_seconds > 0 && <Badge tone="slate">{fmt(data.duration_seconds)}</Badge>}
                <Badge tone="blue">{data.segments.length} {t('podcast.segments')}</Badge>
              </div>
            </div>
            {lesson?.summary && <p className="mt-2 text-sm text-slate-600">{lesson.summary}</p>}
          </Card>

          <div>
            <div className="mb-3 text-sm font-medium text-slate-700">{t('podcast.segments')}</div>
            <div className="space-y-2">
              {data.segments.map((s: any, i: number) => (
                <Card key={i}>
                  <div className="flex gap-3">
                    <Badge tone="amber">{s.start > 0 || s.end > 0 ? `${fmt(s.start)}` : s.title}</Badge>
                    <div className="text-sm text-slate-700">{s.text}</div>
                  </div>
                </Card>
              ))}
            </div>
          </div>

          {!!(lesson?.cards?.length) && (
            <div>
              <div className="mb-3 text-sm font-medium text-slate-700">{t('podcast.cards')}</div>
              <div className="grid gap-4 md:grid-cols-3">
                {lesson.cards.map((c: any, i: number) => (
                  <Card key={i}><div className="text-lg font-medium">{c.front}</div><div className="mt-1 text-slate-500">{c.back}</div></Card>
                ))}
              </div>
            </div>
          )}

          {!!(lesson?.exercises?.length) && (
            <div>
              <div className="mb-3 text-sm font-medium text-slate-700">{t('podcast.exercises')}</div>
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
