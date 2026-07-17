import { useRef, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

const LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];

export default function FlashcardsPage() {
  const { t, i18n } = useTranslation();
  const native = i18n.language;
  const [text, setText] = useState('hola, gracias, por favor, buenos días, hasta luego');
  const [cards, setCards] = useState<any[]>([]);
  const [cefr, setCefr] = useState('A1');
  const [sourceEs, setSourceEs] = useState(true); // true: material is Spanish; false: material is native
  const [busy, setBusy] = useState(false);
  const [recording, setRecording] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [saved, setSaved] = useState(false);
  const fileRef = useRef<HTMLInputElement>(null);
  const recRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);

  const sourceLanguage = sourceEs ? 'es' : native;

  const show = (r: any) => { setCards(r.cards || []); setSaved(true); setTimeout(() => setSaved(false), 2500); };

  const generate = async () => {
    if (!text.trim()) return;
    setBusy(true); setError(null);
    try { show(await api.generateFlashcards(text, { native_language: native, cefr_level: cefr, source_language: sourceLanguage })); }
    catch (e: any) { setError(String(e.message || e)); }
    finally { setBusy(false); }
  };

  const onFile = async () => {
    const f = fileRef.current?.files?.[0];
    if (!f) return;
    setBusy(true); setError(null);
    try { show(await api.flashcardsFromFile(f, { native_language: native, cefr_level: cefr, source_language: sourceLanguage })); }
    catch (e: any) { setError(String(e.message || e)); }
    finally { setBusy(false); }
  };

  const toggleRecord = async () => {
    if (recording) { recRef.current?.stop(); return; }
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const rec = new MediaRecorder(stream); chunksRef.current = [];
      rec.ondataavailable = (e) => chunksRef.current.push(e.data);
      rec.onstop = async () => {
        stream.getTracks().forEach((tr) => tr.stop()); setBusy(true);
        try {
          const r = await api.transcribe(new Blob(chunksRef.current, { type: 'audio/webm' }), sourceLanguage);
          if (r.text) setText(r.text);
        } catch (e: any) { setError(String(e.message || e)); }
        finally { setBusy(false); setRecording(false); }
      };
      recRef.current = rec; rec.start(); setRecording(true);
    } catch (e: any) { setError('Microphone unavailable: ' + String(e.message || e)); }
  };

  return (
    <div>
      <PageHeader title={t('flashcards.title')} description={t('flashcards.subtitle')} />

      <Card>
        <div className="mb-3 flex flex-wrap items-center gap-3">
          <div className="inline-flex overflow-hidden rounded-lg border border-slate-200 text-sm">
            <button className={`px-3 py-1.5 ${sourceEs ? 'bg-brand-50 text-brand-700' : ''}`} onClick={() => setSourceEs(true)}>{t('flashcards.matEs')}</button>
            <button className={`px-3 py-1.5 ${!sourceEs ? 'bg-brand-50 text-brand-700' : ''}`} onClick={() => setSourceEs(false)}>{t('flashcards.matNative')}</button>
          </div>
          <select className="rounded-lg border border-slate-200 px-2 py-1.5 text-sm" value={cefr} onChange={(e) => setCefr(e.target.value)}>
            {LEVELS.map((l) => <option key={l} value={l}>{l}</option>)}
          </select>
        </div>

        <textarea className="h-24 w-full rounded-lg border border-slate-200 p-3 text-sm" value={text}
          placeholder={sourceEs ? t('flashcards.phEs') : t('flashcards.phNative')} onChange={(e) => setText(e.target.value)} />

        <div className="mt-3 flex flex-wrap items-center gap-2">
          <Button onClick={generate} disabled={busy}>{busy ? '…' : t('flashcards.generate')}</Button>
          <Button variant={recording ? 'primary' : 'secondary'} onClick={toggleRecord} disabled={busy}>
            {recording ? `⏹ ${t('flashcards.stop')}` : `🎙 ${t('flashcards.speak')}`}
          </Button>
          <label className="cursor-pointer rounded-lg border border-slate-200 px-3 py-2 text-sm hover:bg-slate-50">
            📎 {t('flashcards.file')}
            <input ref={fileRef} type="file" className="hidden"
              accept=".txt,.md,.html,.pdf,.docx,.jpg,.jpeg,.png,.webp,.mp3,.wav,.m4a,.ogg,.mp4,.mov,.mkv" onChange={onFile} />
          </label>
          <span className="text-xs text-slate-400">{t('flashcards.fileHint')}</span>
        </div>
        {saved && <div className="mt-2 text-xs text-emerald-600">✓ {t('flashcards.saved')}</div>}
        {error && <div className="mt-2 text-sm text-rose-600">{error}</div>}
      </Card>

      <div className="mt-5 grid gap-4 md:grid-cols-3">
        {cards.map((c, i) => (
          <Card key={i}>
            <div className="text-lg font-medium">{c.front}</div>
            <div className="mt-2 text-slate-500">{c.back}</div>
            {c.example_sentence && <div className="mt-1 text-xs text-slate-400">{c.example_sentence}</div>}
          </Card>
        ))}
      </div>
      {cards.length > 0 && <p className="mt-4 text-sm text-slate-400">{t('flashcards.review')}</p>}
    </div>
  );
}
