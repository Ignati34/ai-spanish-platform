import { useEffect, useState } from 'react';
import { api } from '../lib/api';
import { PageHeader } from '../components/layout/PageHeader';
import { Badge } from '../components/ui/Badge';
import { Button } from '../components/ui/Button';
import { Card } from '../components/ui/Card';

const sections = ['Dashboard', 'Usage & Costs', 'Curriculum', 'Security', 'Users', 'Payments', 'Jobs', 'Logs', 'System Health', 'Licenses'] as const;
type Section = (typeof sections)[number];

const toneFor = (raw?: string): any => {
  const s = (raw || '').toLowerCase();
  if (['ok', 'green', 'active', 'trialing', 'completed', 'processed', 'paid', 'operational', 'succeeded'].includes(s)) return 'green';
  if (['failed', 'error', 'rose', 'uncollectible', 'void', 'needs_attention'].includes(s)) return 'rose';
  if (['running', 'queued', 'pending', 'open', 'orange', 'blue', 'amber'].includes(s)) return 'amber';
  return 'slate';
};

function Empty({ text }: { text: string }) {
  return <p className="text-sm text-slate-400">{text}</p>;
}

export default function AdminPage() {
  const [active, setActive] = useState<Section>('Dashboard');

  const [dash, setDash] = useState<any>(null);
  const [users, setUsers] = useState<any[] | null>(null);
  const [pays, setPays] = useState<any>(null);
  const [jobs, setJobs] = useState<any[] | null>(null);
  const [logs, setLogs] = useState<any>(null);
  const [health, setHealth] = useState<any>(null);
  const [licenses, setLicenses] = useState<any[] | null>(null);
  const [usage, setUsage] = useState<any>(null);
  const [usageDays, setUsageDays] = useState(30);
  const [err, setErr] = useState('');

  const [curr, setCurr] = useState<any>(null);
  const [genBusy, setGenBusy] = useState(false);
  const [genMsg, setGenMsg] = useState('');
  const loadCurr = () => api.adminCurriculumStatus().then(setCurr).catch(() => setCurr(null));
  const generate = async (n: number) => {
    setGenBusy(true); setGenMsg('');
    try { const r = await api.adminCurriculumGenerate(n, 'ru'); setGenMsg(`Создано: ${r.created}. Всего: ${r.generated_total}/${r.total}`); loadCurr(); }
    catch (e: any) { setGenMsg('Ошибка: ' + String(e.message || e)); }
    finally { setGenBusy(false); }
  };

  const [sec, setSec] = useState<any>(null);
  const loadSec = () => api.adminSecurityStatus().then(setSec).catch(() => setSec(null));
  const [audit, setAudit] = useState<any>(null);
  const [auditBusy, setAuditBusy] = useState(false);
  const runAudit = async () => {
    setAuditBusy(true); setAudit(null);
    try { setAudit(await api.adminAuditDependencies()); }
    catch (e: any) { setAudit({ ok: false, error: String(e.message || e) }); }
    finally { setAuditBusy(false); }
  };

  useEffect(() => {
    setErr('');
    const fail = (e: any) => setErr(String(e?.message || e));
    if (active === 'Dashboard') api.adminDashboard().then(setDash).catch(fail);
    if (active === 'Usage & Costs') { setUsage(null); api.adminUsageCosts(usageDays).then(setUsage).catch(fail); }
    if (active === 'Curriculum') loadCurr();
    if (active === 'Security') loadSec();
    if (active === 'Users') api.adminUsers().then(setUsers).catch(fail);
    if (active === 'Payments') api.adminPayments().then(setPays).catch(fail);
    if (active === 'Jobs') api.adminJobs().then(setJobs).catch(fail);
    if (active === 'Logs') api.adminLogs().then(setLogs).catch(fail);
    if (active === 'System Health') api.adminSystemHealth().then(setHealth).catch(fail);
    if (active === 'Licenses') api.adminLicenses().then(setLicenses).catch(fail);
  }, [active, usageDays]);

  const retry = async (id: string) => {
    try { await api.adminRetryJob(id); setJobs(await api.adminJobs()); } catch (e: any) { setErr(String(e.message || e)); }
  };

  return (
    <div>
      <PageHeader title="Admin / Developer Console" description="Реальные данные: пользователи, подписки, платежи, фоновые задачи, логи, лицензии, безопасность и курс." />

      <div className="mb-6 flex flex-wrap gap-2">
        {sections.map((section) => (
          <Button key={section} variant={active === section ? 'primary' : 'secondary'} onClick={() => setActive(section)}>{section}</Button>
        ))}
      </div>

      {err && <Card className="mb-4"><p className="text-sm text-rose-600">{err}</p></Card>}

      {active === 'Dashboard' && (
        <div className="grid gap-5 md:grid-cols-3">
          {dash ? (dash.metrics || []).map((m: any) => (
            <Card key={m.label}>
              <div className="flex items-center justify-between">
                <p className="text-sm font-bold text-slate-500">{m.label}</p>
                <Badge tone={toneFor(m.tone)}>{m.tone}</Badge>
              </div>
              <p className="mt-2 text-4xl font-black">{m.value}</p>
            </Card>
          )) : <Empty text="Загрузка…" />}
        </div>
      )}

      {active === 'Usage & Costs' && (
        usage ? (() => {
          const daily: any[] = usage.daily || [];
          const maxCost = Math.max(1e-9, ...daily.map((d) => d.cost || 0));
          const money = (v: number) => `$${(v || 0).toFixed(v && v < 1 ? 4 : 2)}`;
          const t = usage.totals || {};
          const maxAgent = Math.max(1e-9, ...(usage.by_agent || []).map((x: any) => x.cost || 0));
          const maxModel = Math.max(1e-9, ...(usage.by_model || []).map((x: any) => x.cost || 0));
          return (
            <div className="space-y-5">
              <div className="flex flex-wrap items-center gap-2">
                <span className="text-sm text-slate-500">Окно:</span>
                {[7, 30, 90].map((d) => (
                  <Button key={d} variant={usageDays === d ? 'primary' : 'secondary'} onClick={() => setUsageDays(d)}>{d} дн.</Button>
                ))}
              </div>

              <div className="grid gap-5 md:grid-cols-4">
                <Card><p className="text-sm font-bold text-slate-500">Стоимость ИИ (окно)</p><p className="mt-2 text-3xl font-black">{money(t.cost)}</p></Card>
                <Card><p className="text-sm font-bold text-slate-500">Сегодня</p><p className="mt-2 text-3xl font-black">{money(usage.today_cost)}</p></Card>
                <Card><p className="text-sm font-bold text-slate-500">Запросов</p><p className="mt-2 text-3xl font-black">{t.requests ?? 0}</p></Card>
                <Card><p className="text-sm font-bold text-slate-500">Токены (вход/выход)</p><p className="mt-2 text-xl font-black">{(t.input_tokens ?? 0).toLocaleString()} / {(t.output_tokens ?? 0).toLocaleString()}</p></Card>
              </div>

              <Card>
                <div className="mb-3 flex items-center justify-between">
                  <div className="text-lg font-semibold">Стоимость по дням</div>
                  <span className="text-xs text-slate-400">макс. {money(maxCost)}/день</span>
                </div>
                {t.requests ? (
                  <div className="flex h-40 items-end gap-1">
                    {daily.map((d) => (
                      <div key={d.date} className="group relative flex-1"
                        title={`${d.date}: ${money(d.cost)} · ${d.requests} запр.`}>
                        <div className="w-full rounded-t bg-brand-400 transition group-hover:bg-brand-600"
                          style={{ height: `${Math.max(2, Math.round((d.cost / maxCost) * 152))}px` }} />
                      </div>
                    ))}
                  </div>
                ) : <Empty text="Пока нет данных об использовании ИИ. Появятся после первых запросов к провайдеру." />}
                {daily.length > 0 && (
                  <div className="mt-1 flex justify-between text-[10px] text-slate-400">
                    <span>{daily[0]?.date?.slice(5)}</span>
                    <span>{daily[daily.length - 1]?.date?.slice(5)}</span>
                  </div>
                )}
              </Card>

              <div className="grid gap-5 md:grid-cols-2">
                <Card>
                  <div className="mb-3 text-lg font-semibold">По типам вызовов</div>
                  {(usage.by_agent || []).length ? (usage.by_agent).map((a: any) => (
                    <div key={a.agent} className="mb-2">
                      <div className="flex justify-between text-sm"><span className="text-slate-700">{a.agent}</span><span className="text-slate-500">{money(a.cost)} · {a.requests}</span></div>
                      <div className="mt-1 h-2 rounded-full bg-slate-100"><div className="h-2 rounded-full bg-brand-500" style={{ width: `${Math.round((a.cost / maxAgent) * 100)}%` }} /></div>
                    </div>
                  )) : <Empty text="Нет данных." />}
                </Card>
                <Card>
                  <div className="mb-3 text-lg font-semibold">По моделям</div>
                  {(usage.by_model || []).length ? (usage.by_model).map((m: any) => (
                    <div key={m.model} className="mb-2">
                      <div className="flex justify-between text-sm"><span className="text-slate-700">{m.model}</span><span className="text-slate-500">{money(m.cost)} · {m.requests}</span></div>
                      <div className="mt-1 h-2 rounded-full bg-slate-100"><div className="h-2 rounded-full bg-emerald-500" style={{ width: `${Math.round((m.cost / maxModel) * 100)}%` }} /></div>
                    </div>
                  )) : <Empty text="Нет данных." />}
                </Card>
              </div>
              <p className="text-xs text-slate-400">{usage.note} Аудио за окно: {t.audio_seconds ?? 0} с.</p>
            </div>
          );
        })() : <Empty text="Загрузка…" />
      )}

      {active === 'Curriculum' && (
        <Card>
          <div className="text-lg font-semibold">Учебный курс (генерация ИИ)</div>
          <p className="mt-1 text-sm text-slate-500">Полный урок (теория + упражнения) генерируется по силлабусу через ИИ, оригинальными формулировками. Генерация расходует AI-запросы вашего провайдера.</p>
          {curr ? (
            <div className="mt-3">
              <div className="mb-2 flex flex-wrap gap-2">
                <Badge tone="green">Готово: {curr.generated}</Badge>
                <Badge tone="slate">Всего: {curr.total}</Badge>
                <Badge tone="amber">Осталось: {curr.remaining}</Badge>
              </div>
              <div className="h-2 rounded-full bg-slate-100">
                <div className="h-2 rounded-full bg-brand-500" style={{ width: `${Math.round((curr.generated / Math.max(1, curr.total)) * 100)}%` }} />
              </div>
            </div>
          ) : <p className="mt-2 text-sm text-slate-400">Загрузка…</p>}
          <div className="mt-4 flex flex-wrap items-center gap-2">
            <Button onClick={() => generate(5)} disabled={genBusy}>{genBusy ? 'Генерация…' : 'Сгенерировать 5'}</Button>
            <Button variant="secondary" onClick={() => generate(20)} disabled={genBusy}>Сгенерировать 20</Button>
            {genMsg && <span className="text-sm text-slate-600">{genMsg}</span>}
          </div>
          <p className="mt-3 text-xs text-slate-400">Пакетно из контейнера: <code>python scripts/generate_curriculum.py --limit 20 --native ru</code></p>
          <p className="mt-1 text-xs text-slate-400">Прогрев переводов теории (UK/AR/FR/EN): <code>python scripts/prewarm_translations.py --langs uk,ar,fr,en</code></p>
        </Card>
      )}

      {active === 'Security' && (
        <Card>
          <div className="text-lg font-semibold">Безопасность</div>
          {sec ? (
            <div className="mt-3 space-y-4">
              <div>
                <div className="mb-1 text-sm font-medium">Антивирус загрузок</div>
                <div className="flex flex-wrap gap-2">
                  <Badge tone={sec.malware_scan?.enabled ? 'green' : 'slate'}>{sec.malware_scan?.enabled ? 'Включено' : 'Выключено'}</Badge>
                  <Badge tone={sec.malware_scan?.reachable ? 'green' : 'rose'}>{sec.malware_scan?.reachable ? 'Сканер доступен' : 'Сканер недоступен'}</Badge>
                  {sec.malware_scan?.version && <Badge tone="slate">{String(sec.malware_scan.version).slice(0, 40)}</Badge>}
                </div>
              </div>
              <div>
                <div className="mb-1 text-sm font-medium">Заголовки безопасности</div>
                <div className="flex flex-wrap gap-2">
                  <Badge tone={sec.headers?.enabled ? 'green' : 'rose'}>{sec.headers?.enabled ? 'Активны' : 'Выключены'}</Badge>
                  <Badge tone={sec.headers?.hsts ? 'green' : 'slate'}>HSTS: {sec.headers?.hsts ? 'вкл' : 'выкл (HTTP)'}</Badge>
                  {(sec.headers?.list || []).map((h: string) => <Badge key={h} tone="slate">{h}</Badge>)}
                </div>
              </div>
              <div>
                <div className="mb-1 text-sm font-medium">Ограничение частоты запросов</div>
                <div className="flex flex-wrap gap-2">
                  <Badge tone={sec.rate_limit?.enabled ? 'green' : 'rose'}>{sec.rate_limit?.enabled ? 'Включено' : 'Выключено'}</Badge>
                  <Badge tone="slate">API: {sec.rate_limit?.api_per_min}/мин на IP</Badge>
                  <Badge tone="slate">Вход: {sec.rate_limit?.login_max} за {Math.round((sec.rate_limit?.login_window_seconds || 0) / 60)} мин</Badge>
                </div>
              </div>
            </div>
          ) : <p className="mt-2 text-sm text-slate-400">Загрузка…</p>}

          <div className="mt-5 border-t border-slate-100 pt-4">
            <div className="text-sm font-medium">Аудит зависимостей (pip-audit)</div>
            <p className="mt-1 text-xs text-slate-500">Проверка Python-пакетов на известные уязвимости по базе OSV. Может занять до ~2 минут и требует доступа в интернет.</p>
            <div className="mt-2 flex items-center gap-2">
              <Button onClick={runAudit} disabled={auditBusy}>{auditBusy ? 'Проверка…' : 'Проверить зависимости'}</Button>
            </div>
            {audit && (audit.ok ? (
              <div className="mt-3">
                <Badge tone={audit.vulnerability_count ? 'rose' : 'green'}>{audit.vulnerability_count ? `Найдено уязвимостей: ${audit.vulnerability_count}` : 'Уязвимостей не найдено'}</Badge>
                <span className="ml-2 text-xs text-slate-400">Проверено пакетов: {audit.packages_checked}</span>
                {audit.vulnerability_count > 0 && (
                  <div className="mt-2 space-y-1">
                    {audit.vulnerabilities.map((v: any, i: number) => (
                      <div key={i} className="rounded border border-rose-100 bg-rose-50 px-2 py-1 text-xs text-slate-700"><b>{v.package} {v.version}</b> — {v.id}{v.fix_versions?.length ? ` · фикс: ${v.fix_versions.join(', ')}` : ''}</div>
                    ))}
                  </div>
                )}
              </div>
            ) : <div className="mt-3 text-sm text-rose-600">Ошибка: {audit.error}</div>)}
          </div>
          <p className="mt-4 text-xs text-slate-400">ClamAV при первом старте грузит базу сигнатур 1–2 мин. Проверка антивируса: загрузите тестовую строку EICAR — будет отклонена.</p>
        </Card>
      )}

      {active === 'Users' && (
        <Card>
          <div className="mb-3 text-lg font-semibold">Пользователи</div>
          {users ? (users.length ? (
            <div className="divide-y divide-slate-100">
              {users.map((u) => (
                <div key={u.id} className="flex items-center justify-between py-2 text-sm">
                  <div><div className="font-medium">{u.email}</div><div className="text-xs text-slate-400">{u.native_language} · {u.role}</div></div>
                  <div className="flex gap-2"><Badge tone="slate">{u.plan_code}</Badge><Badge tone={toneFor(u.status)}>{u.status}</Badge></div>
                </div>
              ))}
            </div>
          ) : <Empty text="Пока нет пользователей." />) : <Empty text="Загрузка…" />}
        </Card>
      )}

      {active === 'Payments' && (
        <Card>
          <div className="mb-3 text-lg font-semibold">Платежи и вебхуки Stripe</div>
          {pays ? (
            <>
              <div className="mb-2 text-sm font-medium text-slate-600">Счета</div>
              {pays.invoices?.length ? pays.invoices.map((i: any) => (
                <div key={i.id} className="flex items-center justify-between border-b border-slate-100 py-2 text-sm">
                  <span>{(i.amount_paid ?? 0) / 100} {String(i.currency || '').toUpperCase()}</span>
                  <Badge tone={toneFor(i.status)}>{i.status}</Badge>
                </div>
              )) : <Empty text="Счетов пока нет." />}
              <div className="mb-2 mt-4 text-sm font-medium text-slate-600">События вебхуков</div>
              {pays.events?.length ? pays.events.map((e: any, idx: number) => (
                <div key={idx} className="flex items-center justify-between border-b border-slate-100 py-2 text-sm">
                  <span className="font-mono text-xs">{e.event_type}</span>
                  <Badge tone={toneFor(e.processing_status)}>{e.processing_status}</Badge>
                </div>
              )) : <Empty text="Событий вебхуков пока нет." />}
            </>
          ) : <Empty text="Загрузка…" />}
        </Card>
      )}

      {active === 'Jobs' && (
        <Card>
          <div className="mb-3 text-lg font-semibold">Очередь фоновых задач</div>
          {jobs ? (jobs.length ? jobs.map((j) => (
            <div key={j.id} className="flex items-center justify-between border-b border-slate-100 py-3 text-sm">
              <div><div className="font-medium">{j.job_type}</div><div className="text-xs text-slate-400">{j.attempts} attempts{j.error_message ? ` · ${j.error_message}` : ''}</div></div>
              <div className="flex items-center gap-2">
                <Badge tone={toneFor(j.status)}>{j.status}</Badge>
                {j.status === 'failed' && <Button variant="secondary" onClick={() => retry(j.id)}>Повторить</Button>}
              </div>
            </div>
          )) : <Empty text="Очередь пуста." />) : <Empty text="Загрузка…" />}
        </Card>
      )}

      {active === 'Logs' && (
        <Card>
          <div className="mb-3 text-lg font-semibold">Логи</div>
          {logs ? (
            <>
              <div className="mb-2 text-sm font-medium text-slate-600">Системные события</div>
              {logs.system_events?.length ? logs.system_events.map((e: any, i: number) => (
                <div key={i} className="mb-1 rounded bg-slate-900 px-3 py-2 font-mono text-xs text-slate-100">{String(e.severity || 'INFO').toUpperCase()} {e.source} {e.event_type} — {e.message}</div>
              )) : <Empty text="Событий пока нет." />}
              <div className="mb-2 mt-4 text-sm font-medium text-slate-600">Аудит действий админа</div>
              {logs.admin_audit_logs?.length ? logs.admin_audit_logs.map((a: any, i: number) => (
                <div key={i} className="mb-1 rounded bg-slate-900 px-3 py-2 font-mono text-xs text-slate-100">{a.action} {a.target_type || ''} {a.target_id || ''}</div>
              )) : <Empty text="Записей аудита пока нет." />}
            </>
          ) : <Empty text="Загрузка…" />}
        </Card>
      )}

      {active === 'System Health' && (
        <Card>
          <div className="mb-3 text-lg font-semibold">Состояние системы</div>
          {health ? (
            <div className="grid gap-3 md:grid-cols-2">
              {Object.entries(health).map(([k, v]) => (
                <div key={k} className="flex items-center justify-between rounded-lg border border-slate-100 px-3 py-2 text-sm">
                  <span className="text-slate-600">{k}</span>
                  <Badge tone={toneFor(String(v))}>{String(v)}</Badge>
                </div>
              ))}
            </div>
          ) : <Empty text="Загрузка…" />}
        </Card>
      )}

      {active === 'Licenses' && (
        <Card>
          <div className="mb-3 text-lg font-semibold">Лицензии (self-hosted)</div>
          {licenses ? (licenses.length ? licenses.map((l) => (
            <div key={l.id} className="flex items-center justify-between border-b border-slate-100 py-2 text-sm">
              <div><div className="font-medium">{l.edition}</div><div className="text-xs text-slate-400">до {l.valid_until || '—'} · {l.max_users || '∞'} польз.</div></div>
              <Badge tone={toneFor(l.status)}>{l.status}</Badge>
            </div>
          )) : <Empty text="Лицензий пока нет." />) : <Empty text="Загрузка…" />}
        </Card>
      )}
    </div>
  );
}
