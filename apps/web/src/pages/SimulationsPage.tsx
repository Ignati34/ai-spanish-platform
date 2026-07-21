import { useEffect, useRef, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

const LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];

interface Turn { role: 'user' | 'assistant'; text: string; correction?: string; score?: number; }

function playB64(b64?: string, mime?: string) {
  if (!b64) return;
  new Audio(`data:${mime || 'audio/mpeg'};base64,${b64}`).play().catch(() => {});
}

export default function SimulationsPage() {
  const { t, i18n } = useTranslation();
  const [scenarios, setScenarios] = useState<any[]>([]);
  const [cefr, setCefr] = useState('A1');
  const [session, setSession] = useState<any>(null);
  const [turns, setTurns] = useState<Turn[]>([]);
  const [hints, setHints] = useState<string[]>([]);
  const [goal, setGoal] = useState('');
  const [completed, setCompleted] = useState(false);
  const [text, setText] = useState('');
  const [busy, setBusy] = useState(false);
  const [recording, setRecording] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const recRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);

  useEffect(() => { api.simScenarios(i18n.language, cefr).then((r) => setScenarios(r.scenarios || [])).catch((e) => setError(String(e.message || e))); }, [i18n.language, cefr]);

  const start = async (scenarioId: string) => {
    setBusy(true); setError(null); setTurns([]); setCompleted(false);
    try {
      const r = await api.simStart(scenarioId, cefr, i18n.language);
      setSession(r); setGoal(r.goal); setHints(r.hints || []);
      setTurns([{ role: 'assistant', text: r.reply_es }]);
      playB64(r.audio_b64, r.audio_mime);
    } catch (e: any) { setError(String(e.message || e)); }
    finally { setBusy(false); }
  };

  const applyReply = (r: any, userText?: string) => {
    setTurns((prev) => [
      ...prev,
      ...(userText ? [{ role: 'user' as const, text: userText }] : []),
      { role: 'assistant', text: r.reply_es, correction: r.correction, score: r.score }
    ]);
    if (r.hint) setHints([r.hint]);
    if (r.goal_met || r.status === 'completed') setCompleted(true);
    playB64(r.audio_b64, r.audio_mime);
  };

  const sendText = async () => {
    if (!session || !text.trim()) return;
    const msg = text.trim(); setText(''); setBusy(true); setError(null);
    try { applyReply(await api.simSendText(session.session_id, msg), msg); }
    catch (e: any) { setError(String(e.message || e)); }
    finally { setBusy(false); }
  };

  const toggleRecord = async () => {
    if (recording) { recRef.current?.stop(); return; }
    if (!session) return;
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const rec = new MediaRecorder(stream); chunksRef.current = [];
      rec.ondataavailable = (e) => chunksRef.current.push(e.data);
      rec.onstop = async () => {
        stream.getTracks().forEach((tr) => tr.stop()); setBusy(true);
        try { applyReply(await api.simSendAudio(session.session_id, new Blob(chunksRef.current, { type: 'audio/webm' })), '🎙'); }
        catch (e: any) { setError(String(e.message || e)); }
        finally { setBusy(false); setRecording(false); }
      };
      recRef.current = rec; rec.start(); setRecording(true);
    } catch (e: any) { setError('Microphone unavailable: ' + String(e.message || e)); }
  };

  if (!session) {
    return (
      <div>
        <PageHeader title={t('sim.title')} description={t('sim.subtitle')} />
        <div className="mb-4 flex items-center gap-2">
          <span className="text-xs text-slate-500">{t('sim.level')}</span>
          <select className="rounded-lg border border-slate-200 px-2 py-1 text-sm" value={cefr} onChange={(e) => setCefr(e.target.value)}>
            {LEVELS.map((l) => <option key={l} value={l}>{l}</option>)}
          </select>
        </div>
        {error && <p className="mb-3 text-sm text-rose-600">{error}</p>}
        <div className="grid gap-4 md:grid-cols-2">
          {scenarios.map((s) => (
            <Card key={s.id}>
              <div className="text-lg font-semibold">{s.title}</div>
              <div className="mt-1 text-xs text-slate-400">{s.role}</div>
              <div className="mt-2 text-sm text-slate-600">🎯 {s.goal}</div>
              <Button className="mt-3" onClick={() => start(s.id)} disabled={busy}>{t('sim.start')}</Button>
            </Card>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div>
      <PageHeader title={session.title} />
      <Card className="mb-4 border-brand-200 bg-brand-50">
        <div className="text-sm"><span className="font-medium">🎯 {t('sim.goal')}:</span> {goal}</div>
        {completed && <div className="mt-2"><Badge tone="green">✅ {t('sim.completed')}</Badge></div>}
      </Card>

      <div className="space-y-3">
        {turns.map((turn, i) => (
          <div key={i} className={turn.role === 'user' ? 'flex justify-end' : 'flex justify-start'}>
            <Card className={turn.role === 'user' ? 'max-w-[80%] bg-brand-50' : 'max-w-[80%]'}>
              <div className="mb-1 text-xs text-slate-400">{turn.role === 'user' ? t('sim.you') : session.role}</div>
              <div className="text-sm">{turn.text}</div>
              {turn.correction ? <div className="mt-2 text-xs text-rose-600">✎ {turn.correction}</div> : null}
              {typeof turn.score === 'number' ? <div className="mt-2"><Badge tone={turn.score >= 0.7 ? 'green' : 'amber'}>{Math.round(turn.score * 100)}%</Badge></div> : null}
            </Card>
          </div>
        ))}
      </div>

      {hints.length > 0 && !completed && (
        <div className="mt-3 flex flex-wrap gap-2">
          {hints.map((h, i) => (
            <button key={i} onClick={() => setText(h)} className="rounded-full border border-slate-200 px-3 py-1 text-xs text-slate-500 hover:bg-slate-50">💡 {h}</button>
          ))}
        </div>
      )}

      {error && <p className="mt-3 text-sm text-rose-600">{error}</p>}

      {completed ? (
        <Button className="mt-4" variant="secondary" onClick={() => { setSession(null); setTurns([]); }}>{t('sim.again')}</Button>
      ) : (
        <Card className="mt-4">
          <div className="flex items-center gap-2">
            <Button variant={recording ? 'primary' : 'secondary'} onClick={toggleRecord} disabled={busy}>
              {recording ? `⏹ ${t('sim.stop')}` : `🎙 ${t('sim.record')}`}
            </Button>
            <input className="flex-1 rounded-lg border border-slate-200 px-3 py-2 text-sm" value={text}
              placeholder={t('sim.type')} onChange={(e) => setText(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && sendText()} />
            <Button onClick={sendText} disabled={busy || !text.trim()}>{t('sim.send')}</Button>
          </div>
        </Card>
      )}
    </div>
  );
}
