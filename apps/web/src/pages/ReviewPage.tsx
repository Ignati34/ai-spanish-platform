import { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

const GRADES: { key: 'again' | 'hard' | 'good' | 'easy'; tone: string }[] = [
  { key: 'again', tone: 'red' }, { key: 'hard', tone: 'amber' },
  { key: 'good', tone: 'blue' }, { key: 'easy', tone: 'green' }
];

export default function ReviewPage() {
  const { t } = useTranslation();
  const [queue, setQueue] = useState<any[]>([]);
  const [stats, setStats] = useState<any>(null);
  const [idx, setIdx] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const load = async () => {
    setLoading(true); setError(null); setIdx(0); setRevealed(false);
    try {
      const r = await api.srsDue(20);
      setQueue(r.cards || []); setStats(r.stats || null);
    } catch (e: any) { setError(String(e.message || e)); }
    finally { setLoading(false); }
  };
  useEffect(() => { load(); }, []);

  const card = queue[idx];

  const grade = async (g: 'again' | 'hard' | 'good' | 'easy') => {
    if (!card) return;
    try { await api.srsReview(card.id, g); } catch (e: any) { setError(String(e.message || e)); }
    if (idx + 1 < queue.length) { setIdx(idx + 1); setRevealed(false); }
    else { setQueue([]); setStats((s: any) => s ? { ...s, due: Math.max(0, (s.due || 0) - 1) } : s); }
  };

  return (
    <div>
      <PageHeader title={t('review.title')} description={t('review.subtitle')} />

      {stats && (
        <div className="mb-4 flex flex-wrap gap-2">
          <Badge tone="blue">{t('review.due')}: {stats.due}</Badge>
          <Badge tone="slate">{t('review.new')}: {stats.new}</Badge>
          <Badge tone="amber">{t('review.learning')}: {stats.learning}</Badge>
          <Badge tone="green">{t('review.mastered')}: {stats.mastered}</Badge>
        </div>
      )}

      {error && <p className="mb-3 text-sm text-rose-600">{error}</p>}

      {loading ? (
        <Card>…</Card>
      ) : !card ? (
        <Card>
          <div className="text-center">
            <div className="text-lg font-medium">🎉 {t('review.done')}</div>
            <p className="mt-1 text-sm text-slate-500">{t('review.doneHint')}</p>
            <Button className="mt-4" variant="secondary" onClick={load}>{t('review.reload')}</Button>
          </div>
        </Card>
      ) : (
        <>
          <Card className="min-h-[180px]">
            <div className="flex items-center justify-between">
              <Badge tone={card.status === 'new' ? 'slate' : 'blue'}>{card.status}</Badge>
              <span className="text-xs text-slate-400">{idx + 1} / {queue.length}</span>
            </div>
            <div className="mt-6 text-center text-2xl font-semibold">{card.front}</div>
            {revealed && (
              <div className="mt-4 border-t border-slate-100 pt-4 text-center">
                <div className="text-lg text-slate-700">{card.back}</div>
                {card.example_sentence && <div className="mt-2 text-sm text-slate-400">{card.example_sentence}</div>}
              </div>
            )}
          </Card>

          {!revealed ? (
            <Button className="mt-4 w-full" onClick={() => setRevealed(true)}>{t('review.show')}</Button>
          ) : (
            <div className="mt-4 grid grid-cols-4 gap-2">
              {GRADES.map((g) => (
                <button key={g.key} onClick={() => grade(g.key)}
                  className="rounded-xl border border-slate-200 py-2 text-sm font-medium hover:bg-slate-50">
                  {t(`review.${g.key}`)}
                </button>
              ))}
            </div>
          )}
        </>
      )}
    </div>
  );
}
