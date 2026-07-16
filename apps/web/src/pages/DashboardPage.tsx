import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Card } from '../components/ui/Card';
import { Badge } from '../components/ui/Badge';
import { Button } from '../components/ui/Button';

const GOALS = [10, 20, 30, 50];

export default function DashboardPage() {
  const { t } = useTranslation();
  const [me, setMe] = useState<any>(null);
  const [mot, setMot] = useState<any>(null);

  const loadMot = () => api.motivationOverview().then(setMot).catch(() => setMot(null));
  useEffect(() => { api.me().then(setMe).catch(() => setMe(null)); loadMot(); }, []);

  const level = me?.current_cefr_level ?? 'A1';
  const goal = mot?.daily_goal ?? 20;
  const today = mot?.today_count ?? 0;
  const pct = Math.min(100, Math.round((today / Math.max(1, goal)) * 100));

  const setGoal = async (g: number) => { await api.motivationSetGoal(g); loadMot(); };
  const toggleReminders = async () => { await api.motivationSetReminders(!mot?.reminders_enabled, mot?.reminder_hour ?? 19); loadMot(); };
  const setHour = async (h: number) => { await api.motivationSetReminders(mot?.reminders_enabled ?? false, h); loadMot(); };

  return (
    <div>
      <PageHeader title={t('dashboard.welcome')} />
      <div className="grid gap-4 md:grid-cols-3">
        <Card>
          <div className="text-sm text-slate-500">{t('dashboard.level')}</div>
          <div className="mt-2 text-3xl font-bold">{level}</div>
          <Badge tone="green">CEFR</Badge>
        </Card>
        <Card>
          <div className="text-sm text-slate-500">🔥 {t('mot.streak')}</div>
          <div className="mt-2 text-3xl font-bold">{mot?.current_streak ?? 0}</div>
          <span className="text-xs text-slate-400">{t('mot.longest')}: {mot?.longest_streak ?? 0}</span>
        </Card>
        <Card>
          <div className="text-sm text-slate-500">{t('mot.due')}</div>
          <div className="mt-2 text-3xl font-bold">{mot?.due ?? 0}</div>
          <Link to="/app/review"><Button variant="secondary" className="mt-1">{t('nav.review')}</Button></Link>
        </Card>
      </div>

      <Card className="mt-4">
        <div className="flex items-center justify-between">
          <div className="text-sm font-medium">{t('mot.dailyGoal')}</div>
          <span className="text-sm text-slate-500">{today} / {goal} {mot?.goal_met && '✅'}</span>
        </div>
        <div className="mt-2 h-2 rounded-full bg-slate-100"><div className="h-2 rounded-full bg-brand-500" style={{ width: `${pct}%` }} /></div>
        <div className="mt-3 flex flex-wrap items-center gap-2">
          <span className="text-xs text-slate-500">{t('mot.goalSize')}:</span>
          {GOALS.map((g) => (
            <button key={g} onClick={() => setGoal(g)} className={`rounded-lg border px-2.5 py-1 text-sm ${goal === g ? 'border-brand-400 bg-brand-50 text-brand-700' : 'border-slate-200'}`}>{g}</button>
          ))}
        </div>
      </Card>

      <Card className="mt-4">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <div className="text-sm font-medium">{t('mot.reminders')}</div>
            <p className="mt-1 text-xs text-slate-500">{t('mot.remindersHint')}</p>
          </div>
          <div className="flex items-center gap-2">
            <select className="rounded-lg border border-slate-200 px-2 py-1 text-sm" value={mot?.reminder_hour ?? 19} onChange={(e) => setHour(Number(e.target.value))}>
              {Array.from({ length: 24 }, (_, h) => <option key={h} value={h}>{String(h).padStart(2, '0')}:00</option>)}
            </select>
            <Button variant={mot?.reminders_enabled ? 'primary' : 'secondary'} onClick={toggleReminders}>
              {mot?.reminders_enabled ? t('mot.on') : t('mot.off')}
            </Button>
          </div>
        </div>
      </Card>

      <Card className="mt-4">
        <div className="flex items-center justify-between gap-4">
          <div>
            <div className="text-sm font-medium">{t('diag.title')}</div>
            <p className="mt-1 text-sm text-slate-500">{t('diag.subtitle')}</p>
          </div>
          <Link to="/app/diagnostic"><Button variant="secondary">{t('diag.submit')}</Button></Link>
        </div>
      </Card>
    </div>
  );
}
