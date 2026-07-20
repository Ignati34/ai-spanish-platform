import { useEffect, useRef, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

const LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];
const MAX_TOPIC = 500;

function DialogueLines({ lines }: { lines: any[] }) {
  return (
    <div className="space-y-2">
      {lines.map((ln, i) => (
        <div key={i} className="rounded-lg bg-slate-50 px-3 py-2">
          <div className="text-sm">
            <span className="font-semibold text-brand-700">{ln.speaker}: </span>
            <span dir="ltr" lang="es" className="text-slate-800">{ln.es}</span>
          </div>
          {ln.translation && <div className="text-xs text-slate-500">{ln.translation}</div>}
        </div>
      ))}
    </div>
  );
}

export default function DialoguesPage() {
  const { t, i18n } = useTranslation();
  const [level, setLevel] = useState('A1');
  const [items, setItems] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [topic, setTopic] = useState('');
  const [gen, setGen] = useState<any>(null);
  const [genLoading, setGenLoading] = useState(false);
  const reqId = useRef(0);

  useEffect(() => {
    const id = ++reqId.current;
    setLoading(true);
    api.listDialogues(level, i18n.language)
      .then((r) => { if (id === reqId.current) setItems(r?.dialogues || []); })
      .catch(() => { if (id === reqId.current) setItems([]); })
      .finally(() => { if (id === reqId.current) setLoading(false); });
  }, [level, i18n.language]);

  const generate = async () => {
    if (!topic.trim()) return;
    setGenLoading(true); setGen(null);
    try { setGen(await api.generateDialogue(topic.trim(), level, i18n.language)); }
    catch { setGen(null); }
    finally { setGenLoading(false); }
  };

  const left = MAX_TOPIC - topic.length;

  return (
    <div>
      <PageHeader title={t('dialogues.title')} description={t('dialogues.subtitle')} />

      <div className="mb-4 flex flex-wrap items-center gap-2">
        <span className="text-sm text-slate-500">{t('dialogues.level')}</span>
        {LEVELS.map((l) => (
          <Button key={l} variant={level === l ? 'primary' : 'secondary'} onClick={() => setLevel(l)}>{l}</Button>
        ))}
      </div>

      {/* Custom generator */}
      <Card className="mb-6">
        <div className="mb-2 text-sm font-medium">{t('dialogues.generateTitle')}</div>
        <textarea
          className="h-20 w-full rounded-lg border border-slate-200 p-3 text-sm"
          maxLength={MAX_TOPIC}
          value={topic}
          placeholder={t('dialogues.topicPlaceholder')}
          onChange={(e) => setTopic(e.target.value.slice(0, MAX_TOPIC))}
        />
        <div className="mt-2 flex items-center justify-between">
          <span className={`text-xs ${left < 50 ? 'text-amber-600' : 'text-slate-400'}`}>{t('dialogues.charsLeft', { n: left })}</span>
          <Button onClick={generate} disabled={genLoading || !topic.trim()}>{genLoading ? t('dialogues.generating') : t('dialogues.generate')}</Button>
        </div>
        {gen && (
          <div className="mt-4 border-t border-slate-100 pt-4">
            <div className="mb-2 flex items-center justify-between">
              <div className="font-semibold text-slate-800" dir="ltr" lang="es">{gen.title}</div>
              <Badge tone="amber">{gen.level}</Badge>
            </div>
            <DialogueLines lines={gen.lines || []} />
            {gen.stub && <p className="mt-2 text-xs text-amber-600">{t('dialogues.stubNote')}</p>}
          </div>
        )}
      </Card>

      {/* Built-in, graded dialogues */}
      <div className="mb-3 text-sm font-medium text-slate-700">{t('dialogues.builtin')} · {level}</div>
      {loading ? (
        <p className="text-sm text-slate-400">{t('dialogues.loading')}</p>
      ) : items.length === 0 ? (
        <Card className="text-center text-sm text-slate-500">{t('dialogues.empty')}</Card>
      ) : (
        <div className="space-y-4">
          {items.map((d) => (
            <Card key={d.id}>
              <div className="mb-3 flex items-center justify-between">
                <div className="font-semibold text-slate-800">{d.title}</div>
                <Badge tone="slate">{d.level}</Badge>
              </div>
              <DialogueLines lines={d.lines || []} />
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}
