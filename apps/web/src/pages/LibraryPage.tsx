import { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

const LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];
const levelTone: Record<string, string> = { A1: 'green', A2: 'green', B1: 'blue', B2: 'blue', C1: 'amber', C2: 'amber' };

function downloadTxt(title: string, body: string) {
  const blob = new Blob([body], { type: 'text/plain;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${title.replace(/[^\w\-]+/g, '_')}.txt`;
  document.body.appendChild(a); a.click(); a.remove();
  URL.revokeObjectURL(url);
}

export default function LibraryPage() {
  const { t } = useTranslation();
  const [tab, setTab] = useState<'text' | 'link'>('text');
  const [level, setLevel] = useState<string>('');
  const [items, setItems] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [open, setOpen] = useState<any>(null); // full text being read

  useEffect(() => {
    setLoading(true); setOpen(null);
    api.listReading(tab, level || undefined)
      .then((r) => setItems(r?.resources || []))
      .catch(() => setItems([]))
      .finally(() => setLoading(false));
  }, [tab, level]);

  const read = async (id: string) => {
    try { setOpen(await api.getReading(id)); window.scrollTo({ top: 0, behavior: 'smooth' }); }
    catch { setOpen(null); }
  };

  return (
    <div>
      <PageHeader title={t('library.title')} description={t('library.subtitle')} />

      <div className="mb-4 flex flex-wrap items-center gap-2">
        <Button variant={tab === 'text' ? 'primary' : 'secondary'} onClick={() => { setTab('text'); }}>{t('library.reading')}</Button>
        <Button variant={tab === 'link' ? 'primary' : 'secondary'} onClick={() => { setTab('link'); }}>{t('library.online')}</Button>
        <span className="mx-1 h-5 w-px bg-slate-200" />
        <button onClick={() => setLevel('')} className={`rounded-lg px-2 py-1 text-xs ${level === '' ? 'bg-brand-100 text-brand-700' : 'text-slate-500 hover:bg-slate-100'}`}>{t('library.allLevels')}</button>
        {LEVELS.map((l) => (
          <button key={l} onClick={() => setLevel(l)} className={`rounded-lg px-2 py-1 text-xs ${level === l ? 'bg-brand-100 text-brand-700' : 'text-slate-500 hover:bg-slate-100'}`}>{l}</button>
        ))}
      </div>

      {/* Inline reader */}
      {open && tab === 'text' && (
        <Card className="mb-5">
          <div className="mb-2 flex items-center justify-between">
            <div className="flex items-center gap-2">
              {open.level && <Badge tone={levelTone[open.level] || 'slate'}>{open.level}</Badge>}
              <h2 className="text-lg font-semibold">{open.title}</h2>
            </div>
            <div className="flex gap-2">
              <Button variant="secondary" onClick={() => downloadTxt(open.title, open.body || '')}>{t('library.download')}</Button>
              <Button variant="secondary" onClick={() => setOpen(null)}>{t('library.close')}</Button>
            </div>
          </div>
          <p className="whitespace-pre-line text-[15px] leading-7 text-slate-700" dir="ltr" lang="es">{open.body}</p>
        </Card>
      )}

      {loading ? (
        <p className="text-sm text-slate-400">{t('library.loading')}</p>
      ) : items.length === 0 ? (
        <Card className="text-center text-sm text-slate-500">{t('library.empty')}</Card>
      ) : tab === 'text' ? (
        <div className="grid gap-4 md:grid-cols-2">
          {items.map((r) => (
            <Card key={r.id} className="flex flex-col">
              <div className="mb-1 flex items-center gap-2">
                {r.level && <Badge tone={levelTone[r.level] || 'slate'}>{r.level}</Badge>}
                <div className="font-semibold text-slate-800">{r.title}</div>
              </div>
              {r.excerpt && <p className="mb-3 text-sm text-slate-500" dir="ltr" lang="es">{r.excerpt}</p>}
              <div className="mt-auto flex gap-2">
                <Button onClick={() => read(r.id)}>{t('library.read')}</Button>
              </div>
            </Card>
          ))}
        </div>
      ) : (
        <div className="grid gap-3 md:grid-cols-2">
          {items.map((r) => (
            <Card key={r.id} className="flex items-start justify-between gap-3">
              <div className="min-w-0">
                <div className="flex items-center gap-2">
                  {r.level ? <Badge tone={levelTone[r.level] || 'slate'}>{r.level}</Badge> : <Badge tone="slate">{r.category || '—'}</Badge>}
                  <div className="truncate font-semibold text-slate-800">{r.title}</div>
                </div>
                {r.description && <p className="mt-1 text-sm text-slate-500">{r.description}</p>}
              </div>
              <a href={r.url} target="_blank" rel="noopener noreferrer"
                 className="shrink-0 rounded-lg bg-brand-600 px-3 py-1.5 text-sm font-medium text-white hover:bg-brand-700">
                {t('library.open')}
              </a>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}
