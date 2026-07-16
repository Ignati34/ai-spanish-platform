import { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

export default function DiagnosticPage() {
  const { t, i18n } = useTranslation();
  const navigate = useNavigate();
  const [data, setData] = useState<any>(null);
  const [answers, setAnswers] = useState<Record<string, number>>({});
  const [writing, setWriting] = useState('');
  const [speaking, setSpeaking] = useState('');
  const [busy, setBusy] = useState(false);
  const [recording, setRecording] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);
  const recRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);

  useEffect(() => {
    api.diagnosticQuestions(i18n.language).then(setData).catch((e) => setError(String(e.message || e)));
  }, [i18n.language]);

  const toggleRecord = async () => {
    if (recording) { recRef.current?.stop(); return; }
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const rec = new MediaRecorder(stream); chunksRef.current = [];
      rec.ondataavailable = (e) => chunksRef.current.push(e.data);
      rec.onstop = async () => {
        stream.getTracks().forEach((tr) => tr.stop()); setBusy(true);
        try {
          const r = await api.transcribe(new Blob(chunksRef.current, { type: 'audio/webm' }));
          setSpeaking(r.text || '');
        } catch (e: any) { setError(String(e.message || e)); }
        finally { setBusy(false); setRecording(false); }
      };
      recRef.current = rec; rec.start(); setRecording(true);
    } catch (e: any) { setError('Microphone unavailable: ' + String(e.message || e)); }
  };

  const submit = async () => {
    setBusy(true); setError(null);
    try {
      const payload = {
        answers: (data?.questions || []).map((q: any) => ({ id: q.id, answer: answers[q.id] ?? null })),
        writing_sample: writing, speaking_sample: speaking, native_language: i18n.language
      };
      setResult(await api.diagnosticSubmit(payload));
    } catch (e: any) { setError(String(e.message || e)); }
    finally { setBusy(false); }
  };

  if (result) {
    return (
      <div>
        <PageHeader title={t('diag.title')} />
        <Card>
          <div className="flex items-center justify-between">
            <div>
              <div className="text-sm text-slate-500">{t('diag.level')}</div>
              <div className="text-4xl font-black text-brand-700">{result.recommended_level}</div>
            </div>
            <Badge tone="amber">{t('diag.mc')}: {result.mc_correct}/{result.mc_total}</Badge>
          </div>
          {result.summary && <p className="mt-3 text-sm text-slate-600">{result.summary}</p>}
        </Card>
        <div className="mt-4 grid gap-4 md:grid-cols-2">
          <Card>
            <div className="mb-2 text-sm font-medium">{t('diag.strengths')}</div>
            <ul className="space-y-1 text-sm text-slate-600">{(result.strengths || []).map((s: string, i: number) => <li key={i}>✓ {s}</li>)}</ul>
          </Card>
          <Card>
            <div className="mb-2 text-sm font-medium">{t('diag.gaps')}</div>
            <ul className="space-y-1 text-sm text-slate-600">{(result.gaps || []).map((s: string, i: number) => <li key={i}>• {s}</li>)}</ul>
          </Card>
        </div>
        <Card className="mt-4">
          <div className="mb-2 text-sm font-medium">{t('diag.plan')}</div>
          <ol className="list-decimal space-y-1 ps-5 text-sm text-slate-600">{(result.study_plan || []).map((s: string, i: number) => <li key={i}>{s}</li>)}</ol>
        </Card>
        <Button className="mt-5" onClick={() => navigate('/app')}>{t('diag.start')}</Button>
      </div>
    );
  }

  return (
    <div>
      <PageHeader title={t('diag.title')} description={t('diag.subtitle')} />
      {error && <p className="mb-3 text-sm text-rose-600">{error}</p>}
      {!data ? <Card>…</Card> : (
        <div className="space-y-4">
          {data.questions.map((q: any, idx: number) => (
            <Card key={q.id}>
              <div className="mb-2 text-sm font-medium">{idx + 1}. {q.prompt} <span className="text-xs text-slate-400">({q.level})</span></div>
              <div className="flex flex-wrap gap-2">
                {q.options.map((opt: string, oi: number) => (
                  <button key={oi} onClick={() => setAnswers((p) => ({ ...p, [q.id]: oi }))}
                    className={`rounded-lg border px-3 py-1.5 text-sm ${answers[q.id] === oi ? 'border-brand-400 bg-brand-50 text-brand-700' : 'border-slate-200'}`}>
                    {opt}
                  </button>
                ))}
              </div>
            </Card>
          ))}

          <Card>
            <div className="mb-2 text-sm font-medium">{data.writing_prompt}</div>
            <textarea className="h-28 w-full rounded-lg border border-slate-200 p-3 text-sm" value={writing} onChange={(e) => setWriting(e.target.value)} />
          </Card>

          <Card>
            <div className="mb-2 text-sm font-medium">{data.speaking_prompt}</div>
            <div className="flex items-center gap-2">
              <Button variant={recording ? 'primary' : 'secondary'} onClick={toggleRecord} disabled={busy}>
                {recording ? `⏹ ${t('diag.stop')}` : `🎙 ${t('diag.record')}`}
              </Button>
              {speaking && <span className="text-xs text-slate-500 line-clamp-1">“{speaking}”</span>}
            </div>
          </Card>

          <Button onClick={submit} disabled={busy}>{busy ? t('diag.evaluating') : t('diag.submit')}</Button>
        </div>
      )}
    </div>
  );
}
