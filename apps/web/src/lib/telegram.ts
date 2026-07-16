// Telegram Mini App bootstrap. When running inside Telegram, we expand the
// viewport, apply the theme, and expose initData for backend authentication.
export interface TG {
  initData: string;
  initDataUnsafe: any;
  expand: () => void;
  ready: () => void;
  colorScheme: string;
  themeParams: any;
  openInvoice?: (url: string, cb: (status: string) => void) => void;
}

export function getTelegram(): TG | null {
  return (window as any).Telegram?.WebApp ?? null;
}

export function isTelegram(): boolean {
  const tg = getTelegram();
  return !!(tg && tg.initData);
}

export function initTelegram() {
  const tg = getTelegram();
  if (!tg) return;
  try { tg.ready(); tg.expand(); } catch { /* noop */ }
}
