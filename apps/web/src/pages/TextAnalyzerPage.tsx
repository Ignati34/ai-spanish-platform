import { useRef, useState } from 'react';
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
  const [tab, setTab] = useState<'text' | 'file' | 'url'>('text');
  const [text, setText] = useState('Ayer fui al supermercado y compré frutas porque quería preparar una cena.');
  const [url, setUrl] = useState('');
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const fileRef = useRef<HTMLInputElement>(null);

  const run = async (fn: () => Promise<any>) => {
    setLoading(true); setError(null); setResult(null);
    try { setResult(await fn()); }
    catch (e: any) { setError(String(e?.message || e)); }
    finally { setLoading(false); }
  };
  const runText = () => run(() => api.analyzeText(text, i18n.language));
  const runUrl = () => { if (url.trim()) return run(() => api.analyzeUrl(url.trim(), i18n.language)); };
  const runFile = () => {
    const f = fileRef.current?.files?.[0];
    if (f) return run(() => api.analyzeFile(f, i18n.language));
  };

  return (
    <div>
      <PageHeader title={t('analyzer.title')} description={t('analyzer.subtitle')} />
      <Card>
        <div className="mb-4 flex flex-wrap gap-2">
          <Button variant={tab === 'text' ? 'primary' : 'secondary'} onClick={() => setTab('text')}>{t('analyzer.tabText')}</Button>
          <Button variant={tab === 'file' ? 'primary' : 'secondary'} onClick={() => setTab('file')}>{t('analyzer.tabFile')}</Button>
          <Button variant={tab === 'url' ? 'primary' : 'secondary'} onClick={() => setTab('url')}>{t('analyzer.tabUrl')}</Button>
        </div>

        {tab === 'text' && (
          <>
            <textarea className="h-32 w-full rounded-lg border border-slate-200 p-3 text-sm" value={text}
              placeholder={t('analyzer.placeholder')} onChange={(e) => setText(e.target.value)} />
            <Button className="mt-3" onClick={runText} disabled={loading}>{loading ? t('analyzer.running') : t('analyzer.run')}</Button>
          </>
        )}
        {tab === 'file' && (
          <>
            <input ref={fileRef} type="file" accept=".txt,.md,.pdf,.docx,.html,.mp3,.wav,.m4a,.ogg,.mp4,.mov,.webm" className="block w-full text-sm" />
            <p className="mt-1 text-xs text-slate-400">{t('analyzer.fileHint')}</p>
            <Button className="mt-3" onClick={runFile} disabled={loading}>{loading ? t('analyzer.running') : t('analyzer.run')}</Button>
          </>
        )}
        {tab === 'url' && (
          <>
            <input type="url" value={url} onChange={(e) => setUrl(e.target.value)}
              placeholder={t('analyzer.urlPlaceholder')}
              className="block w-full rounded-lg border border-slate-200 px-3 py-2 text-sm" />
            <p className="mt-1 text-xs text-slate-400">{t('analyzer.urlHint')}</p>
            <Button className="mt-3" onClick={runUrl} disabled={loading || !url.trim()}>{loading ? t('analyzer.running') : t('analyzer.run')}</Button>
          </>
        )}
        {error && <p className="mt-3 text-sm text-rose-600">{error}</p>}
      </Card>

      {result?.source_text && tab !== 'text' && (
        <Card className="mt-4">
          <div className="mb-2 text-sm font-medium">{t('analyzer.sourceText')}</div>
          <p className="max-h-48 overflow-auto whitespace-pre-line text-sm leading-6 text-slate-600" dir="ltr" lang="es">{result.source_text}</p>
        </Card>
      )}

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
