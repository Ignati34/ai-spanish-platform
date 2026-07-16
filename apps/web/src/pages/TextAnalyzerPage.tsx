import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

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
        <Button className="mt-3" onClick={run} disabled={loading}>{t('analyzer.run')}</Button>
      </Card>
      {result && (
        <div className="mt-5 grid gap-4 md:grid-cols-2">
          <Card><div className="mb-2 text-sm font-medium">CEFR</div><Badge tone="amber">{result.cefr_estimate}</Badge></Card>
          <Card><div className="mb-2 text-sm font-medium">{t('analyzer.topics')}</div>
            <div className="flex flex-wrap gap-2">{(result.grammar_topics || []).map((g: string) => <Badge key={g} tone="slate">{g}</Badge>)}</div>
          </Card>
          <Card><div className="mb-2 text-sm font-medium">{t('analyzer.verbs')}</div>
            <div className="flex flex-wrap gap-2">{(result.verbs || []).map((v: any, i: number) => <Badge key={i} tone="blue">{v.word || v}</Badge>)}</div>
          </Card>
          <Card><div className="mb-2 text-sm font-medium">{t('analyzer.tenses')}</div>
            <div className="flex flex-wrap gap-2">{(result.tenses || []).map((x: string) => <Badge key={x} tone="green">{x}</Badge>)}</div>
          </Card>
        </div>
      )}
    </div>
  );
}
