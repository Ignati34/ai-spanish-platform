import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { Card } from './ui/Card';
import { Button } from './ui/Button';

export interface Exercise {
  exercise_type?: string;
  prompt: string;
  options?: string[] | null;
  correct_answer?: string;
  explanation?: string;
}

// Strip a leading option label like "A. ", "b) ", "3 - " and normalize for comparison.
const norm = (s: string) =>
  (s || '').replace(/^\s*[A-Za-z0-9][.)\-]\s*/, '').trim().toLowerCase().replace(/[.!?]+$/, '');

function resolveCorrect(ex: Exercise): string {
  const ca = (ex.correct_answer || '').trim();
  const opts = ex.options || [];
  // correct_answer is a bare letter (A/B/C/D) -> map to option by index
  if (/^[A-Da-d]$/.test(ca) && opts.length) {
    const idx = ca.toUpperCase().charCodeAt(0) - 65;
    if (opts[idx]) return norm(opts[idx]);
  }
  return norm(ca);
}

export function ExerciseCard({ ex, onAnswer }: { ex: Exercise; onAnswer?: (correct: boolean) => void }) {
  const { t } = useTranslation();
  const [picked, setPicked] = useState<string | null>(null);
  const [typed, setTyped] = useState('');
  const [checked, setChecked] = useState(false);
  const hasOptions = Array.isArray(ex.options) && ex.options.length > 0;
  const correct = resolveCorrect(ex);

  const answerValue = hasOptions ? (picked ?? '') : typed;
  const isCorrect = norm(answerValue) === correct && !!correct;

  const submit = (value: string) => {
    if (checked) return;
    if (hasOptions) setPicked(value); else setTyped(value);
    setChecked(true);
    onAnswer?.(norm(value) === correct);
  };

  const optionClass = (opt: string) => {
    if (!checked) return 'border-slate-200 hover:bg-slate-50';
    if (norm(opt) === correct) return 'border-emerald-400 bg-emerald-50 text-emerald-700';
    if (opt === picked) return 'border-rose-400 bg-rose-50 text-rose-700';
    return 'border-slate-200 opacity-60';
  };

  return (
    <Card>
      <div className="text-sm font-medium">{ex.prompt}</div>

      {hasOptions ? (
        <div className="mt-2 flex flex-wrap gap-2">
          {ex.options!.map((opt, j) => (
            <button key={j} disabled={checked} onClick={() => submit(opt)}
              className={`rounded-lg border px-3 py-1.5 text-sm transition ${optionClass(opt)}`}>
              {opt}
            </button>
          ))}
        </div>
      ) : (
        <div className="mt-2 flex items-center gap-2">
          <input className="flex-1 rounded-lg border border-slate-200 px-3 py-1.5 text-sm" value={typed}
            disabled={checked} placeholder={t('ex.type')} onChange={(e) => setTyped(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && typed.trim() && submit(typed)} />
          {!checked && <Button onClick={() => typed.trim() && submit(typed)}>{t('ex.check')}</Button>}
        </div>
      )}

      {checked && (
        <div className="mt-3 text-sm">
          {isCorrect
            ? <div className="font-medium text-emerald-600">✓ {t('ex.correct')}</div>
            : <div className="font-medium text-rose-600">✗ {t('ex.wrong')} <span className="text-slate-500">— {ex.correct_answer}</span></div>}
          {ex.explanation && <div className="mt-1 text-slate-500">{ex.explanation}</div>}
        </div>
      )}
    </Card>
  );
}
