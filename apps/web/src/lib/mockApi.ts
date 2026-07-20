// Minimal mock API so the UI can run without a backend (VITE_USE_MOCK=true).
export const mockApi = {
  async request<T>(path: string, _options: RequestInit = {}): Promise<T> {
    const bare = path.split('?')[0];
    const data: Record<string, unknown> = {
      '/api/billing/plans': [{ code: 'pro', name: 'Pro', price_monthly: 14.99, currency: 'eur' }],
      '/api/billing/providers': { country: 'ES', providers: [{ code: 'stripe', configured: false, methods: [{ code: 'bizum', label: 'Bizum (Spain)', recommended: true }, { code: 'card', label: 'Card' }] }] },
      '/api/analyze/text': { cefr_estimate: 'A1', verbs: [], nouns: [], tenses: ['presente'], grammar_topics: ['ser/estar'] },
      '/api/vocab-bank/stats': { counts: { verbs: 387, collocations: 512, examples: 640, phrases: 2177 } },
      '/api/vocab-bank/search': { items: [
        { es: 'echar de menos', ru: 'скучать по', kind: 'phrases' },
        { es: 'dar con', ru: 'найти, наткнуться', kind: 'verbs' },
        { es: 'tener ganas de', ru: 'хотеть, не терпится', kind: 'phrases' },
        { es: 'Me da igual', ru: 'мне всё равно', kind: 'examples' },
        { es: 'a lo mejor', ru: 'может быть', kind: 'collocations' }
      ] },
      '/api/vocab-bank/sample': { items: [
        { es: 'valer la pena', ru: 'стоить того' },
        { es: 'meter la pata', ru: 'сесть в лужу' },
        { es: 'tomar el pelo', ru: 'разыгрывать' }
      ] }
    };
    // Try exact path first, then fall back to the path without query string.
    return ((data[path] ?? data[bare]) ?? {}) as T;
  }
};
