import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

type TenseInfo = { name: string; key: string; explanation: string; examples: string[] };

function TenseChip({ info }: { info: TenseInfo }) {
  const [pinned, setPinned] = useState(false);
  return (
    <span className="group relative inline-block">
      <button
        onClick={() => setPinned((p) => !p)}
        className="inline-flex items-center gap-1 rounded-full border border-emerald-200 bg-emerald-50 px-2.5 py-1 text-xs text-emerald-700 hover:bg-emerald-100"
      >
        <span aria-hidden>⏱</span>{info.name}
      </button>
      <span
        className={`absolute bottom-full left-0 z-20 mb-2 w-72 rounded-xl border border-slate-200 bg-white p-3 text-left shadow-lg ${pinned ? 'block' : 'hidden'} group-hover:block`}
      >
        <span className="block text-sm text-slate-700">{info.explanation}</span>
        {info.examples?.length > 0 && (
          <span className="mt-2 block space-y-1">
            {info.examples.map((ex, i) => (
              <span key={i} className="block text-xs text-slate-500" dir="ltr" lang="es">• {ex}</span>
            ))}
          </span>
        )}
      </span>
    </span>
  );
}

function WordList({ title, tone, items }: { title: string; tone: string; items: any[] }) {
  if (!items || items.length === 0) return null;
  return (
    <Card>
      <div className="mb-2 text-sm font-medium">{title}</div>
      <div className="flex flex-wrap gap-2">
        {items.map((it, i) => (
          <Badge key={i} tone={tone}>
            <span dir="ltr" lang="es">{it.word}</span>
            {it.translation ? <span className="text-slate-400"> → {it.translation}</span> : null}
            {it.tense ? <span className="ms-1 text-[10px] opacity-70">({it.tense})</span> : null}
          </Badge>
        ))}
      </div>
    </Card>
  );
}

export default function TextAnalyzerPage() {
  const { t, i18n } = useTranslation();
  const [text, setText] = useState('Ayer fui al supermercado y compré frutas porque quería preparar una cena.');
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const run = async () => {
    setLoading(true);
    try { setResult(await api.analyzeText(text, i18n.language)); }
    finally { setLoading(false); }
  };

  return (
    <div>
      <PageHeader title={t('analyzer.title')} />
      <Card>
        <textarea className="h-32 w-full rounded-lg border border-slate-200 p-3 text-sm" value={text}
          placeholder={t('analyzer.placeholder')} onChange={(e) => setText(e.target.value)} />
        <Button className="mt-3" onClick={run} disabled={loading}>{loading ? t('analyzer.running') : t('analyzer.run')}</Button>
      </Card>

      {result && (
        <div className="mt-5 space-y-4">
          <div className="grid gap-4 md:grid-cols-2">
            <Card><div className="mb-2 text-sm font-medium">CEFR</div><Badge tone="amber">{result.cefr_estimate}</Badge></Card>
            <Card><div className="mb-2 text-sm font-medium">{t('analyzer.topics')}</div>
              <div className="flex flex-wrap gap-2">{(result.grammar_topics || []).map((g: string) => <Badge key={g} tone="slate">{g}</Badge>)}</div>
            </Card>
          </div>

          {result.translation && (
            <Card>
              <div className="mb-2 text-sm font-medium">{t('analyzer.translation')}</div>
              <p className="text-sm leading-6 text-slate-700">{result.translation}</p>
            </Card>
          )}

          {(result.tense_info?.length > 0 || result.tenses?.length > 0) && (
            <Card>
              <div className="mb-2 text-sm font-medium">{t('analyzer.tenses')} <span className="text-xs font-normal text-slate-400">· {t('analyzer.tenseHint')}</span></div>
              <div className="flex flex-wrap gap-2">
                {(result.tense_info?.length ? result.tense_info : (result.tenses || []).map((n: string) => ({ name: n, key: n, explanation: '', examples: [] }))).map((ti: TenseInfo, i: number) => (
                  ti.explanation ? <TenseChip key={i} info={ti} /> : <Badge key={i} tone="green">{ti.name}</Badge>
                ))}
              </div>
            </Card>
          )}

          <WordList title={t('analyzer.verbs')} tone="blue" items={result.verbs} />
          <WordList title={t('analyzer.nouns')} tone="slate" items={result.nouns} />
          <WordList title={t('analyzer.adjectives')} tone="amber" items={result.adjectives} />
          <WordList title={t('analyzer.adverbs')} tone="green" items={result.adverbs} />

          {!!(result.vocabulary?.length) && (
            <Card>
              <div className="mb-2 text-sm font-medium">{t('analyzer.vocabulary')}</div>
              <div className="grid gap-2 sm:grid-cols-2">
                {result.vocabulary.map((v: any, i: number) => (
                  <div key={i} className="flex items-center justify-between rounded-lg bg-slate-50 px-3 py-1.5 text-sm">
                    <span dir="ltr" lang="es" className="font-medium text-slate-800">{v.word}</span>
                    <span className="text-slate-500">{v.translation}</span>
                  </div>
                ))}
              </div>
            </Card>
          )}

          {result.summary && (
            <Card>
              <div className="mb-2 text-sm font-medium">{t('analyzer.summary')}</div>
              <p className="text-sm leading-6 text-slate-600">{result.summary}</p>
            </Card>
          )}
        </div>
      )}
    </div>
  );
}
