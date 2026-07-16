import { useEffect, useState } from 'react';
import { PageHeader } from '../components/layout/PageHeader';
import { Badge } from '../components/ui/Badge';
import { Button } from '../components/ui/Button';
import { Card } from '../components/ui/Card';
import { plans } from '../lib/mockData';
import { api } from '../lib/api';
import { getTelegram, isTelegram } from '../lib/telegram';

const COUNTRIES = [
  { code: 'ES', label: 'España' }, { code: 'FR', label: 'France' },
  { code: 'RU', label: 'Россия' }, { code: 'UA', label: 'Україна' },
  { code: 'AE', label: 'الإمارات' }, { code: 'US', label: 'United States' }
];

export default function BillingPage() {
  const [loadingPlan, setLoadingPlan] = useState<string | null>(null);
  const [country, setCountry] = useState('ES');
  const [providers, setProviders] = useState<any[]>([]);
  const [provider, setProvider] = useState<string>(isTelegram() ? 'telegram' : 'stripe');

  useEffect(() => {
    api.billingProviders(country)
      .then((r) => setProviders(r.providers || []))
      .catch(() => setProviders([]));
  }, [country]);

  const startCheckout = async (planCode: string) => {
    setLoadingPlan(planCode);
    try {
      const res = await api.checkout(provider, planCode, 'monthly');
      if (provider === 'telegram' && res.checkout_url && isTelegram()) {
        getTelegram()!.openInvoice?.(res.checkout_url, () => {});
      } else if (res.checkout_url) {
        window.location.href = res.checkout_url;
      }
    } catch (e) {
      // In dev/mock mode there is no live PSP configured — no-op.
      console.warn(e);
    } finally {
      setLoadingPlan(null);
    }
  };

  const activeProvider = providers.find((p) => p.code === provider);

  return (
    <div>
      <PageHeader title="Suscripción y pago" description="Tarifas, límites y métodos de pago según tu país." />

      <Card className="mb-5">
        <div className="flex flex-wrap items-end gap-4">
          <div>
            <label className="block text-xs text-slate-500">País</label>
            <select className="mt-1 rounded-lg border border-slate-200 px-3 py-2 text-sm" value={country} onChange={(e) => setCountry(e.target.value)}>
              {COUNTRIES.map((c) => <option key={c.code} value={c.code}>{c.label}</option>)}
            </select>
          </div>
          <div>
            <label className="block text-xs text-slate-500">Proveedor de pago</label>
            <select className="mt-1 rounded-lg border border-slate-200 px-3 py-2 text-sm" value={provider} onChange={(e) => setProvider(e.target.value)}>
              {providers.map((p) => <option key={p.code} value={p.code}>{p.code}</option>)}
            </select>
          </div>
          <div className="flex flex-wrap gap-2">
            {(activeProvider?.methods || []).map((m: any) => (
              <Badge key={m.code} tone={m.recommended ? 'green' : 'slate'}>{m.label}{m.recommended ? ' ★' : ''}</Badge>
            ))}
          </div>
        </div>
        <p className="mt-3 text-xs text-slate-400">
          España: Bizum + SEPA + tarjeta (Stripe). Internacional: tarjeta / PayPal. Dentro de Telegram: Telegram Payments.
        </p>
      </Card>

      <div className="grid gap-5 md:grid-cols-3">
        {plans.map((plan) => (
          <Card key={plan.code} className={plan.highlighted ? 'border-brand-300 ring-2 ring-brand-100' : ''}>
            <div className="flex items-center justify-between">
              <h3 className="text-xl font-black">{plan.name}</h3>
              {plan.highlighted && <Badge>Popular</Badge>}
            </div>
            <p className="mt-4 text-4xl font-black">{plan.price}</p>
            <ul className="mt-6 space-y-3 text-sm text-slate-600">
              {plan.features.map((feature) => <li key={feature}>✓ {feature}</li>)}
            </ul>
            <Button className="mt-6 w-full" variant={plan.highlighted ? 'primary' : 'secondary'} onClick={() => startCheckout(plan.code)} disabled={!!loadingPlan}>
              {loadingPlan === plan.code ? 'Checkout…' : 'Elegir'}
            </Button>
          </Card>
        ))}
      </div>

      <Card className="mt-6">
        <h3 className="text-lg font-black">Cómo se concede el acceso</h3>
        <p className="mt-2 text-sm leading-6 text-slate-600">
          El acceso Pro se concede solo tras el webhook del proveedor (Stripe / PayPal / Telegram). La página de éxito no es la fuente de verdad: el backend verifica el evento de pago y actualiza subscription y user_entitlements.
        </p>
      </Card>
    </div>
  );
}
