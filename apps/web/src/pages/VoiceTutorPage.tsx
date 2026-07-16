import { useRef, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Badge } from '../components/ui/Badge';

const SCENARIOS = ['cafe', 'aeropuerto', 'médico', 'entrevista', 'banco', 'alquiler'];
const LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];

interface Turn { role: 'user' | 'assistant'; text: string; correction?: string; score?: number; }

function playB64(b64?: string, mime?: string) {
  if (!b64) return;
  const audio = new Audio(`data:${mime || 'audio/mpeg'};base64,${b64}`);
  audio.play().catch(() => {});
}

export default function VoiceTutorPage() {
  const { t, i18n } = useTranslation();
  const [scenario, setScenario] = useState('cafe');
  const [cefr, setCefr] = useState('A1');
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [turns, setTurns] = useState<Turn[]>([]);
  const [text, setText] = useState('');
  const [busy, setBusy] = useState(false);
  const [recording, setRecording] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const recRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);

  const start = async () => {
    setBusy(true); setError(null); setTurns([]);
    try {
      const r = await api.voiceCreateSession(scenario, cefr, i18n.language);
      setSessionId(r.session_id);
      setTurns([{ role: 'assistant', text: r.reply_es }]);
      playB64(r.audio_b64, r.audio_mime);
    } catch (e: any) { setError(String(e.message || e)); }
    finally { setBusy(false); }
  };

  const pushReply = (r: any, userText?: string) => {
    setTurns((prev) => [
      ...prev,
      ...(userText ? [{ role: 'user' as const, text: userText }] : []),
      { role: 'assistant', text: r.reply_es, correction: r.correction, score: r.score }
    ]);
    playB64(r.audio_b64, r.audio_mime);
  };

  const sendText = async () => {
    if (!sessionId || !text.trim()) return;
    const msg = text.trim(); setText(''); setBusy(true); setError(null);
    try { pushReply(await api.voiceSendText(sessionId, msg), msg); }
    catch (e: any) { setError(String(e.message || e)); }
    finally { setBusy(false); }
  };

  const toggleRecord = async () => {
    if (recording) { recRef.current?.stop(); return; }
    if (!sessionId) return;
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const rec = new MediaRecorder(stream);
      chunksRef.current = [];
      rec.ondataavailable = (e) => chunksRef.current.push(e.data);
      rec.onstop = async () => {
        stream.getTracks().forEach((tr) => tr.stop());
        setBusy(true);
        try {
          const blob = new Blob(chunksRef.current, { type: 'audio/webm' });
          const r = await api.voiceSendAudio(sessionId, blob);
          pushReply(r, r.user_text);
        } catch (e: any) { setError(String(e.message || e)); }
        finally { setBusy(false); setRecording(false); }
      };
      recRef.current = rec; rec.start(); setRecording(true);
    } catch (e: any) { setError('Microphone unavailable: ' + String(e.message || e)); }
  };

  return (
    <div>
      <PageHeader title={t('voice.title')} description="Диалог на испанском: говорите или пишите, репетитор отвечает и исправляет." />

      {!sessionId ? (
        <Card>
          <div className="flex flex-wrap items-end gap-4">
            <div>
              <label className="block text-xs text-slate-500">{t('voice.scenario')}</label>
              <select className="mt-1 rounded-lg border border-slate-200 px-3 py-2 text-sm" value={scenario} onChange={(e) => setScenario(e.target.value)}>
                {SCENARIOS.map((s) => <option key={s} value={s}>{s}</option>)}
              </select>
            </div>
            <div>
              <label className="block text-xs text-slate-500">{t('voice.level')}</label>
              <select className="mt-1 rounded-lg border border-slate-200 px-3 py-2 text-sm" value={cefr} onChange={(e) => setCefr(e.target.value)}>
                {LEVELS.map((l) => <option key={l} value={l}>{l}</option>)}
              </select>
            </div>
            <Button onClick={start} disabled={busy}>{busy ? '…' : t('voice.start')}</Button>
          </div>
        </Card>
      ) : (
        <>
          <div className="space-y-3">
            {turns.map((turn, i) => (
              <div key={i} className={turn.role === 'user' ? 'flex justify-end' : 'flex justify-start'}>
                <Card className={turn.role === 'user' ? 'max-w-[80%] bg-brand-50' : 'max-w-[80%]'}>
                  <div className="mb-1 text-xs text-slate-400">{turn.role === 'user' ? t('voice.you') : t('voice.tutor')}</div>
                  <div className="text-sm">{turn.text}</div>
                  {turn.correction ? <div className="mt-2 text-xs text-rose-600">✎ {turn.correction}</div> : null}
                  {typeof turn.score === 'number' ? <div className="mt-2"><Badge tone={turn.score >= 0.7 ? 'green' : 'amber'}>{t('voice.score')}: {Math.round(turn.score * 100)}%</Badge></div> : null}
                </Card>
              </div>
            ))}
          </div>

          {error && <p className="mt-3 text-sm text-rose-600">{error}</p>}

          <Card className="mt-4">
            <div className="flex items-center gap-2">
              <Button variant={recording ? 'primary' : 'secondary'} onClick={toggleRecord} disabled={busy}>
                {recording ? `⏹ ${t('voice.stop')}` : `🎙 ${t('voice.record')}`}
              </Button>
              <input className="flex-1 rounded-lg border border-slate-200 px-3 py-2 text-sm" value={text}
                placeholder={t('voice.type')} onChange={(e) => setText(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && sendText()} />
              <Button onClick={sendText} disabled={busy || !text.trim()}>{t('voice.send')}</Button>
            </div>
          </Card>
        </>
      )}
    </div>
  );
}
