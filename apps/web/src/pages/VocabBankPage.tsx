import { useEffect, useMemo, useRef, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';
import { api, VocabItem } from '../lib/api';

type Kind = 'all' | 'verbs' | 'collocations' | 'examples' | 'phrases';
const KINDS: Kind[] = ['all', 'verbs', 'collocations', 'examples', 'phrases'];
const kindTone: Record<string, string> = {
  verbs: 'blue', collocations: 'green', examples: 'amber', phrases: 'slate'
};

export default function VocabBankPage() {
  const { t } = useTranslation();
  const [counts, setCounts] = useState<Record<string, number>>({});
  const [kind, setKind] = useState<Kind>('all');
  const [query, setQuery] = useState('');
  const [items, setItems] = useState<VocabItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [randomMode, setRandomMode] = useState(false);
  const reqId = useRef(0);

  // Load counts once.
  useEffect(() => {
    api.vocabStats()
      .then((r) => setCounts(r?.counts ?? {}))
      .catch(() => setCounts({}));
  }, []);

  // Debounced search whenever kind or query changes (cancels random mode).
  useEffect(() => {
    setRandomMode(false);
    const id = ++reqId.current;
    setLoading(true);
    const handle = setTimeout(() => {
      api.vocabSearch(query.trim(), kind === 'all' ? undefined : kind, 60)
        .then((r) => { if (id === reqId.current) setItems(r?.items ?? []); })
        .catch(() => { if (id === reqId.current) setItems([]); })
        .finally(() => { if (id === reqId.current) setLoading(false); });
    }, 300);
    return () => clearTimeout(handle);
  }, [kind, query]);

  const total = useMemo(
    () => Object.values(counts).reduce((a, b) => a + (b || 0), 0),
    [counts]
  );

  function countFor(k: Kind) {
    return k === 'all' ? total : (counts[k] ?? 0);
  }

  async function drawRandom() {
    const id = ++reqId.current;
    setLoading(true);
    setRandomMode(true);
    try {
      const sampleKind = kind === 'all' ? 'phrases' : kind;
      const r = await api.vocabSample(sampleKind, 12);
      if (id === reqId.current) setItems(r?.items ?? []);
    } catch {
      if (id === reqId.current) setItems([]);
    } finally {
      if (id === reqId.current) setLoading(false);
    }
  }

  return (
    <div>
      <PageHeader title={t('vocab.title')} description={t('vocab.subtitle')} />

      {/* Kind tabs with counts */}
      <div className="mb-4 flex flex-wrap gap-2">
        {KINDS.map((k) => {
          const active = k === kind;
          return (
            <button
              key={k}
              onClick={() => setKind(k)}
              className={`inline-flex items-center gap-2 rounded-xl border px-3 py-1.5 text-sm transition ${
                active
                  ? 'border-brand-300 bg-brand-50 text-brand-700 font-medium'
                  : 'border-slate-200 bg-white text-slate-600 hover:bg-slate-50'
              }`}
            >
              <span>{t(`vocab.${k}`)}</span>
              <span className={`rounded-full px-1.5 text-xs ${active ? 'bg-brand-100 text-brand-700' : 'bg-slate-100 text-slate-500'}`}>
                {countFor(k)}
              </span>
            </button>
          );
        })}
      </div>

      {/* Search + random */}
      <div className="mb-5 flex flex-col gap-3 sm:flex-row sm:items-center">
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder={t('vocab.search')}
          className="w-full rounded-xl border border-slate-200 px-4 py-2 text-sm outline-none focus:border-brand-400 sm:max-w-md"
        />
        <Button variant="secondary" onClick={drawRandom}>{t('vocab.random')}</Button>
      </div>

      {/* Results */}
      {loading ? (
        <p className="text-sm text-slate-400">{t('vocab.loading')}</p>
      ) : items.length === 0 ? (
        <Card className="text-center text-sm text-slate-500">{t('vocab.empty')}</Card>
      ) : (
        <>
          <p className="mb-3 text-xs text-slate-400">
            {randomMode ? t('vocab.randomHint') : t('vocab.count', { n: items.length })}
          </p>
          <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
            {items.map((it, i) => (
              <Card key={`${it.es}-${i}`} className="flex flex-col gap-1">
                <div className="flex items-start justify-between gap-2">
                  <span className="font-medium text-slate-900" dir="ltr" lang="es">{it.es}</span>
                  {kind === 'all' && it.kind && (
                    <Badge tone={kindTone[it.kind] ?? 'slate'}>{t(`vocab.${it.kind}`)}</Badge>
                  )}
                </div>
                <span className="text-sm text-slate-500" dir="ltr" lang="ru">{it.ru}</span>
              </Card>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
