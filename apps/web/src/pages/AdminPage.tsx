import { useState } from 'react';
import { PageHeader } from '../components/layout/PageHeader';
import { Badge } from '../components/ui/Badge';
import { Button } from '../components/ui/Button';
import { Card } from '../components/ui/Card';

const sections = ['Dashboard', 'Users', 'Payments', 'Usage & Costs', 'Jobs', 'Logs', 'System Health', 'Licenses'];

const metrics = [
  ['Users', '128', 'blue'],
  ['MRR', '646 €', 'green'],
  ['Active subscriptions', '34', 'green'],
  ['Failed payments', '3', 'rose'],
  ['AI cost today', '12.48 €', 'orange'],
  ['Failed jobs', '7', 'rose']
] as const;

const users = [
  ['demo@example.com', 'Pro', 'active', '4 920 AI req'],
  ['student.uk@example.com', 'Basic', 'active', '830 AI req'],
  ['free.user@example.com', 'Free', 'active', '97 AI req']
];

const jobs = [
  ['text_analyzer_agent', 'completed', '1 attempt'],
  ['transcription_agent', 'running', '1 attempt'],
  ['podcast_builder_agent', 'failed', '3 attempts'],
  ['image_lesson_agent', 'queued', '0 attempts']
];

export default function AdminPage() {
  const [active, setActive] = useState('Dashboard');

  return (
    <div>
      <PageHeader title="Admin / Developer Console" description="Пользователи, подписки, usage, фоновые задачи, логи, лицензии и состояние облачной инфраструктуры." />

      <div className="mb-6 flex flex-wrap gap-2">
        {sections.map((section) => (
          <Button key={section} variant={active === section ? 'primary' : 'secondary'} onClick={() => setActive(section)}>{section}</Button>
        ))}
      </div>

      {active === 'Dashboard' && (
        <>
          <div className="grid gap-5 md:grid-cols-3">
            {metrics.map(([title, value, tone]) => (
              <Card key={title}>
                <div className="flex items-center justify-between">
                  <p className="text-sm font-bold text-slate-500">{title}</p>
                  <Badge tone={tone}>{tone}</Badge>
                </div>
                <p className="mt-2 text-4xl font-black">{value}</p>
              </Card>
            ))}
          </div>
          <Card className="mt-6">
            <h3 className="text-xl font-black">SaaS control plane</h3>
            <p className="mt-2 text-sm leading-6 text-slate-600">Эта панель нужна для AWS SaaS: CloudWatch-style health, Stripe webhooks, AI costs, failed jobs, ручная выдача доступа и self-hosted лицензии.</p>
          </Card>
        </>
      )}

      {active === 'Users' && (
        <Card>
          <h3 className="text-xl font-black">Users</h3>
          <div className="mt-4 overflow-hidden rounded-2xl border border-slate-200">
            {users.map(([email, plan, status, usage]) => (
              <div key={email} className="grid grid-cols-4 gap-3 border-b border-slate-100 p-4 text-sm last:border-0">
                <span className="font-bold">{email}</span><Badge tone="blue">{plan}</Badge><Badge tone="green">{status}</Badge><span>{usage}</span>
              </div>
            ))}
          </div>
          <Button className="mt-4" variant="secondary">Grant manual access</Button>
        </Card>
      )}

      {active === 'Payments' && (
        <Card>
          <h3 className="text-xl font-black">Stripe payments & webhooks</h3>
          <div className="mt-4 space-y-3">
            {['checkout.session.completed', 'invoice.paid', 'customer.subscription.updated', 'invoice.payment_failed'].map((event, index) => (
              <div key={event} className="flex items-center justify-between rounded-2xl bg-slate-50 p-4"><span className="font-bold">{event}</span><Badge tone={index === 3 ? 'rose' : 'green'}>{index === 3 ? 'needs attention' : 'processed'}</Badge></div>
            ))}
          </div>
        </Card>
      )}

      {active === 'Usage & Costs' && (
        <div className="grid gap-5 md:grid-cols-2">
          {['AI tokens: 1.2M', 'STT: 420 min', 'TTS: 88 min', 'Images: 312', 'Storage: 18 GB', 'Top user cost: 4.12 €'].map((item) => <Card key={item}><p className="text-2xl font-black">{item}</p></Card>)}
        </div>
      )}

      {active === 'Jobs' && (
        <Card>
          <h3 className="text-xl font-black">Worker queue</h3>
          <div className="mt-4 space-y-3">
            {jobs.map(([job, status, attempts]) => <div key={job} className="flex items-center justify-between rounded-2xl bg-slate-50 p-4"><div><p className="font-bold">{job}</p><p className="text-xs text-slate-500">{attempts}</p></div><Badge tone={status === 'failed' ? 'rose' : status === 'completed' ? 'green' : 'orange'}>{status}</Badge></div>)}
          </div>
        </Card>
      )}

      {active === 'Logs' && (
        <Card>
          <h3 className="text-xl font-black">Logs</h3>
          <div className="mt-4 space-y-3 font-mono text-xs">
            {['INFO api request_id=abc123 path=/api/billing/plans', 'WARN stripe webhook invoice.payment_failed', 'ERROR worker podcast_builder_agent failed file_id=up_91', 'INFO admin manual_access_granted user=demo@example.com'].map((line) => <div key={line} className="rounded-2xl bg-slate-950 p-3 text-slate-100">{line}</div>)}
          </div>
        </Card>
      )}

      {active === 'System Health' && (
        <div className="grid gap-5 md:grid-cols-3">
          {['API', 'PostgreSQL/RDS', 'Redis/ElastiCache', 'S3/MinIO', 'Workers', 'Stripe webhook'].map((svc) => <Card key={svc}><p className="font-black">{svc}</p><Badge tone="green">ok</Badge></Card>)}
        </div>
      )}

      {active === 'Licenses' && (
        <Card>
          <h3 className="text-xl font-black">Self-hosted licenses</h3>
          <div className="mt-4 space-y-3">
            {['School Basic — 50 users — active', 'Enterprise Hybrid — 500 users — active', 'Demo VPS — 10 users — expires soon'].map((license) => <div key={license} className="rounded-2xl bg-slate-50 p-4 font-bold">{license}</div>)}
          </div>
        </Card>
      )}
    </div>
  );
}
