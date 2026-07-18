import { config } from './config';
import { mockApi } from './mockApi';

class ApiClient {
  private token: string | null = localStorage.getItem('access_token');

  setToken(token: string | null) {
    this.token = token;
    if (token) localStorage.setItem('access_token', token);
    else localStorage.removeItem('access_token');
  }

  async request<T>(path: string, options: RequestInit = {}): Promise<T> {
    if (config.useMock) return mockApi.request<T>(path, options);
    const response = await fetch(`${config.apiUrl}${path}`, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...(this.token ? { Authorization: `Bearer ${this.token}` } : {}),
        ...(options.headers ?? {})
      }
    });
    this.handleAuth(response);
    if (!response.ok) throw new Error((await response.text()) || `Request failed: ${response.status}`);
    return response.json() as Promise<T>;
  }

  private handleAuth(response: Response) {
    if (response.status === 401) {
      this.setToken(null);
      if (typeof window !== 'undefined' && window.location.pathname !== '/login') {
        window.location.href = '/login';
      }
      throw new Error('Session expired — please sign in again.');
    }
  }

  // --- Auth ---
  login(email: string, password: string) {
    return this.request<{ access_token: string }>('/api/auth/login', { method: 'POST', body: JSON.stringify({ email, password }) });
  }
  register(payload: { email: string; password: string; native_language?: string }) {
    return this.request<{ access_token: string }>('/api/auth/register', { method: 'POST', body: JSON.stringify(payload) });
  }
  telegramAuth(init_data: string, native_language?: string) {
    return this.request<{ access_token: string; user: any }>('/api/telegram/auth', { method: 'POST', body: JSON.stringify({ init_data, native_language }) });
  }
  updateMe(payload: { native_language?: string; interface_language?: string }) {
    return this.request<any>('/api/users/me', { method: 'PATCH', body: JSON.stringify(payload) });
  }
  me() { return this.request('/api/users/me'); }

  // --- Learning ---
  lessons() { return this.request<any[]>('/api/course/lessons'); }
  courseLesson(id: string) { return this.request<any>(`/api/course/lessons/${id}`); }
  analyzeText(text: string, native_language = 'ru') {
    return this.request('/api/analyze/text', { method: 'POST', body: JSON.stringify({ text, native_language }) });
  }
  generateFlashcards(text: string, opts: { native_language?: string; cefr_level?: string; source_language?: string } = {}) {
    return this.request<any>('/api/flashcards/generate', { method: 'POST', body: JSON.stringify({ text, ...opts }) });
  }
  flashcardsFromFile(file: File, opts: { native_language?: string; cefr_level?: string; source_language?: string } = {}) {
    const form = new FormData();
    form.append('file', file);
    if (opts.native_language) form.append('native_language', opts.native_language);
    if (opts.cefr_level) form.append('cefr_level', opts.cefr_level);
    if (opts.source_language) form.append('source_language', opts.source_language);
    return this.postForm<any>('/api/flashcards/from-file', form);
  }

  // --- Upload Studio (file/text -> lesson) ---
  uploadText(text: string, native_language = 'ru', cefr_level = 'A1') {
    return this.request<any>('/api/uploads/text', {
      method: 'POST',
      body: JSON.stringify({ text, native_language, cefr_level })
    });
  }
  async uploadFile(file: File, native_language = 'ru', cefr_level = 'A1') {
    const form = new FormData();
    form.append('file', file);
    form.append('native_language', native_language);
    form.append('cefr_level', cefr_level);
    // NOTE: do not set Content-Type; the browser adds the multipart boundary.
    const res = await fetch(`${config.apiUrl}/api/uploads/file`, {
      method: 'POST',
      headers: { ...(this.token ? { Authorization: `Bearer ${this.token}` } : {}) },
      body: form
    });
    this.handleAuth(res);
    if (!res.ok) throw new Error((await res.text()) || `Upload failed: ${res.status}`);
    return res.json();
  }

  private async postForm<T>(path: string, form: FormData): Promise<T> {
    const res = await fetch(`${config.apiUrl}${path}`, {
      method: 'POST',
      headers: { ...(this.token ? { Authorization: `Bearer ${this.token}` } : {}) },
      body: form
    });
    this.handleAuth(res);
    if (!res.ok) throw new Error((await res.text()) || `Request failed: ${res.status}`);
    return res.json() as Promise<T>;
  }

  // --- Voice Tutor ---
  voiceCreateSession(scenario: string, cefr_level = 'A1', native_language = 'ru') {
    return this.request<any>('/api/voice/sessions', {
      method: 'POST',
      body: JSON.stringify({ scenario, cefr_level, native_language })
    });
  }
  voiceSendText(sessionId: string, text: string) {
    const form = new FormData();
    form.append('text', text);
    return this.postForm<any>(`/api/voice/sessions/${sessionId}/message`, form);
  }
  voiceSendAudio(sessionId: string, blob: Blob) {
    const form = new FormData();
    form.append('audio', blob, 'clip.webm');
    return this.postForm<any>(`/api/voice/sessions/${sessionId}/message`, form);
  }
  transcribe(blob: Blob, language = 'es') {
    const form = new FormData();
    form.append('file', blob, 'clip.webm');
    form.append('language', language);
    return this.postForm<any>('/api/voice/transcribe', form);
  }

  // --- Podcast Studio ---
  podcastCreate(file: File, native_language = 'ru', cefr_level = 'A1', title?: string) {
    const form = new FormData();
    form.append('file', file);
    form.append('native_language', native_language);
    form.append('cefr_level', cefr_level);
    if (title) form.append('title', title);
    return this.postForm<any>('/api/podcasts', form);
  }

  // --- Role-play simulations ---
  simScenarios(native_language = 'ru') {
    return this.request<any>(`/api/simulations/scenarios?native_language=${encodeURIComponent(native_language)}`);
  }
  simStart(scenario_id: string, cefr_level = 'A1', native_language = 'ru') {
    return this.request<any>('/api/simulations/start', { method: 'POST', body: JSON.stringify({ scenario_id, cefr_level, native_language }) });
  }
  simSendText(sessionId: string, text: string) {
    const form = new FormData();
    form.append('text', text);
    return this.postForm<any>(`/api/simulations/${sessionId}/message`, form);
  }
  simSendAudio(sessionId: string, blob: Blob) {
    const form = new FormData();
    form.append('audio', blob, 'clip.webm');
    return this.postForm<any>(`/api/simulations/${sessionId}/message`, form);
  }

  // --- Diagnostic ---
  diagnosticQuestions(native_language = 'ru') {
    return this.request<any>(`/api/diagnostic/questions?native_language=${encodeURIComponent(native_language)}`);
  }
  diagnosticSubmit(payload: { answers: { id: string; answer: number | null }[]; writing_sample: string; speaking_sample?: string; native_language: string }) {
    return this.request<any>('/api/diagnostic/submit', { method: 'POST', body: JSON.stringify(payload) });
  }

  // --- Admin: curriculum ---
  adminCurriculumStatus() { return this.request<any>('/api/admin/curriculum/status'); }
  adminSecurityStatus() { return this.request<any>('/api/admin/security/status'); }
  adminAuditDependencies() { return this.request<any>('/api/admin/security/audit-dependencies', { method: 'POST', body: '{}' }); }
  adminCurriculumGenerate(count = 5, native = 'ru') {
    return this.request<any>(`/api/admin/curriculum/generate?count=${count}&native=${native}`, { method: 'POST', body: '{}' });
  }

  // --- Progress / My mistakes ---
  progressOverview() { return this.request<any>('/api/progress/overview'); }
  progressPractice() { return this.request<any>('/api/progress/practice', { method: 'POST', body: '{}' }); }
  progressRecord(payload: { topic?: string; original?: string; corrected?: string; explanation?: string }) {
    return this.request<any>('/api/progress/record', { method: 'POST', body: JSON.stringify(payload) });
  }

  // --- Spaced repetition ---
  srsDue(limit = 20) { return this.request<any>(`/api/srs/due?limit=${limit}`); }
  srsReview(card_id: string, grade: 'again' | 'hard' | 'good' | 'easy') {
    return this.request<any>('/api/srs/review', { method: 'POST', body: JSON.stringify({ card_id, grade }) });
  }

  // --- Motivation ---
  motivationOverview() { return this.request<any>('/api/motivation/overview'); }
  motivationSetGoal(daily_goal: number) {
    return this.request<any>('/api/motivation/goal', { method: 'POST', body: JSON.stringify({ daily_goal }) });
  }
  motivationSetReminders(enabled: boolean, hour?: number) {
    return this.request<any>('/api/motivation/reminders', { method: 'POST', body: JSON.stringify({ enabled, hour }) });
  }

  // --- Billing (multi-provider) ---
  billingPlans() { return this.request('/api/billing/plans'); }
  billingProviders(country?: string) {
    const q = country ? `?country=${encodeURIComponent(country)}` : '';
    return this.request<{ country: string | null; providers: any[] }>(`/api/billing/providers${q}`);
  }
  billingSubscription() { return this.request('/api/billing/subscription'); }
  billingUsage() { return this.request('/api/billing/usage'); }
  checkout(provider: string, plan_code: string, billing_interval = 'monthly') {
    return this.request<{ provider: string; checkout_url?: string; invoice_payload?: string; mode?: string }>(
      '/api/billing/checkout', { method: 'POST', body: JSON.stringify({ provider, plan_code, billing_interval }) });
  }

  // --- Admin ---
  adminDashboard() { return this.request<any>('/api/admin/dashboard'); }
  adminUsers() { return this.request<any[]>('/api/admin/users'); }
  adminPayments() { return this.request<any>('/api/admin/payments'); }
  adminJobs() { return this.request<any[]>('/api/admin/jobs'); }
  adminRetryJob(id: string) { return this.request<any>(`/api/admin/jobs/${id}/retry`, { method: 'POST', body: '{}' }); }
  adminLogs() { return this.request<any>('/api/admin/logs'); }
  adminSystemHealth() { return this.request<any>('/api/admin/system-health'); }
  adminLicenses() { return this.request<any[]>('/api/admin/licenses'); }
}

export const api = new ApiClient();
