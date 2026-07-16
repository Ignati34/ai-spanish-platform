// Minimal mock API so the UI can run without a backend (VITE_USE_MOCK=true).
export const mockApi = {
  async request<T>(path: string, _options: RequestInit = {}): Promise<T> {
    const data: Record<string, unknown> = {
      '/api/billing/plans': [{ code: 'pro', name: 'Pro', price_monthly: 14.99, currency: 'eur' }],
      '/api/billing/providers': { country: 'ES', providers: [{ code: 'stripe', configured: false, methods: [{ code: 'bizum', label: 'Bizum (Spain)', recommended: true }, { code: 'card', label: 'Card' }] }] },
      '/api/analyze/text': { cefr_estimate: 'A1', verbs: [], nouns: [], tenses: ['presente'], grammar_topics: ['ser/estar'] }
    };
    return (data[path] ?? {}) as T;
  }
};
