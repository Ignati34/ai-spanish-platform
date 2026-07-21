// Minimal mock API so the UI can run without a backend (VITE_USE_MOCK=true).
export const mockApi = {
  async request<T>(path: string, _options: RequestInit = {}): Promise<T> {
    const bare = path.split('?')[0];
    const data: Record<string, unknown> = {
      '/api/billing/plans': [{ code: 'pro', name: 'Pro', price_monthly: 14.99, currency: 'eur' }],
      '/api/billing/providers': { country: 'ES', providers: [{ code: 'stripe', configured: false, methods: [{ code: 'bizum', label: 'Bizum (Spain)', recommended: true }, { code: 'card', label: 'Card' }] }] },
      '/api/analyze/text': {
        cefr_estimate: 'A2',
        translation: 'Вчера я пошёл в супермаркет и купил фрукты, потому что хотел приготовить ужин.',
        verbs: [
          { word: 'ir', tense: 'pretérito indefinido', translation: 'идти, ехать' },
          { word: 'comprar', tense: 'pretérito indefinido', translation: 'покупать' },
          { word: 'querer', tense: 'pretérito imperfecto', translation: 'хотеть' }
        ],
        tenses: ['pretérito indefinido', 'pretérito imperfecto'],
        nouns: [{ word: 'supermercado', translation: 'супермаркет' }, { word: 'frutas', translation: 'фрукты' }, { word: 'cena', translation: 'ужин' }],
        adjectives: [],
        adverbs: [{ word: 'ayer', translation: 'вчера' }],
        conjunctions: ['porque'],
        vocabulary: [{ word: 'preparar', translation: 'готовить', cefr: 'A2' }],
        grammar_topics: ['pretérito indefinido', 'pretérito imperfecto'],
        summary: 'Короткий рассказ о походе в супермаркет.'
      },
      '/api/analyze/file': {
        cefr_estimate: 'B1', source_text: '(демо) Расшифрованный/извлечённый текст появится здесь.',
        translation: '(демо) перевод текста.', verbs: [{ word: 'llegar', tense: 'presente', translation: 'прибывать' }],
        tenses: ['presente'], nouns: [], adjectives: [], adverbs: [], conjunctions: [], vocabulary: [],
        grammar_topics: ['presente'], summary: 'Демо-анализ файла.'
      },
      '/api/analyze/url': {
        cefr_estimate: 'B1', source_text: '(демо) Текст, извлечённый со страницы, появится здесь.',
        translation: '(демо) перевод текста.', verbs: [{ word: 'informar', tense: 'presente', translation: 'сообщать' }],
        tenses: ['presente'], nouns: [], adjectives: [], adverbs: [], conjunctions: [], vocabulary: [],
        grammar_topics: ['presente'], summary: 'Демо-анализ страницы.'
      },
      '/api/uploads': [
        { id: 'u1', filename: 'entrevista.mp3', file_type: 'mp3', status: 'lesson_ready', size: 812000, created_at: new Date(Date.now() - 86400000).toISOString() },
        { id: 'u2', filename: 'articulo.pdf', file_type: 'pdf', status: 'extracted', size: 45000, created_at: new Date(Date.now() - 2 * 86400000).toISOString() }
      ],
      '/api/uploads/text': {
        lesson_id: 'mock-lesson', deck_id: 'mock-deck', title: 'Lección desde texto',
        cefr_estimate: 'A2', summary: 'Un texto sobre una cena con amigos.',
        analysis: { vocabulary: [{ word: 'compré', translation: 'я купил' }, { word: 'cena', translation: 'ужин' }] },
        cards: [{ front: 'comprar', back: 'покупать', example_sentence: 'Compré frutas.' }],
        exercises: [{ section: 'Práctica', exercise_type: 'multiple_choice', prompt: 'Ayer ___ frutas.', options: ['compré', 'compro', 'compraré'], correct_answer: 'compré', translation: 'Вчера я купил фрукты.' }],
        source: 'raw_text'
      },
      '/api/simulations/scenarios': { levels: ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], scenarios: [
        { id: 'a1_cafe', level: 'A1', title: 'Заказ в кафе', role: 'camarero de una cafetería', goal: 'Заказать кофе и что-нибудь поесть', setup: 'Entras en una cafetería.', hints: ['Buenos días, ¿me pone un café?'] },
        { id: 'a1_tienda', level: 'A1', title: 'В магазине', role: 'dependiente', goal: 'Купить фрукты и хлеб', setup: 'Vas a la tienda.', hints: ['¿Tiene manzanas?'] }
      ] },
      '/api/voice/scenarios': { levels: ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], scenarios: [
        { id: 'a1_cafe', level: 'A1', label: 'В кафе', prompt: 'Eres camarero en una cafetería.' },
        { id: 'a1_presentarse', level: 'A1', label: 'Знакомство', prompt: 'Preséntate y pregunta su nombre.' },
        { id: 'a1_tienda', level: 'A1', label: 'В магазине', prompt: 'Eres dependiente de una tienda.' },
        { id: 'a1_direcciones', level: 'A1', label: 'Спросить дорогу', prompt: 'El estudiante pregunta cómo llegar a la estación.' }
      ] },
      '/api/reading': { levels: ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], resources: [
        { id: 'r1', kind: 'text', level: 'A1', title: 'Mi familia', excerpt: 'Me llamo Ana. Tengo veinte años y vivo en Madrid…', downloadable: true },
        { id: 'r2', kind: 'link', level: 'A1', title: 'SpanishDict', url: 'https://www.spanishdict.com', category: 'course', description: 'Diccionario, conjugador y lecciones.' }
      ] },
      '/api/reading/r1': { id: 'r1', kind: 'text', level: 'A1', title: 'Mi familia', downloadable: true,
        body: 'Me llamo Ana. Tengo veinte años y vivo en Madrid. Mi familia es pequeña. Tengo un hermano y una hermana.' },
      '/api/uploads/url': {
        lesson_id: 'mock-lesson-url', deck_id: 'mock-deck-url', title: 'Lección desde un enlace',
        cefr_estimate: 'B1', summary: 'Texto extraído de una página web.',
        analysis: { vocabulary: [{ word: 'noticia', translation: 'новость' }] },
        cards: [{ front: 'según', back: 'согласно', example_sentence: 'Según el artículo…' }],
        exercises: [{ section: 'Práctica', exercise_type: 'translation', prompt: 'Переведите: «согласно статье»', options: null, correct_answer: 'según el artículo', translation: 'según el artículo' }],
        source: 'url'
      },
      '/api/dialogues': { levels: ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], dialogues: [
        { id: 'a1_cafe', level: 'A1', title: 'В кафе', lines: [
          { speaker: 'Camarero', es: 'Buenos días, ¿qué desea?', translation: 'Доброе утро, что желаете?' },
          { speaker: 'Cliente', es: 'Un café con leche, por favor.', translation: 'Кофе с молоком, пожалуйста.' }
        ] }
      ] },
      '/api/dialogues/generate': { title: 'En el aeropuerto', level: 'A2', topic: 'aeropuerto', stub: true, lines: [
        { speaker: 'A', es: '¿Dónde está la puerta de embarque?', translation: 'Где выход на посадку?' },
        { speaker: 'B', es: 'Al fondo, a la derecha.', translation: 'В глубине, справа.' }
      ] },
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
      ] },
      '/api/admin/usage-costs': (() => {
        const days = 30;
        const today = new Date();
        const daily = Array.from({ length: days }, (_, i) => {
          const d = new Date(today); d.setDate(today.getDate() - (days - 1 - i));
          const cost = Math.max(0, 0.02 + 0.03 * Math.sin(i / 3) + (i % 7 === 0 ? 0.05 : 0));
          return { date: d.toISOString().slice(0, 10), cost: Number(cost.toFixed(4)), requests: Math.round(cost * 400), input_tokens: Math.round(cost * 90000), output_tokens: Math.round(cost * 30000) };
        });
        const cost = daily.reduce((a, b) => a + b.cost, 0);
        return {
          window_days: days,
          totals: { cost: Number(cost.toFixed(4)), requests: daily.reduce((a, b) => a + b.requests, 0), input_tokens: daily.reduce((a, b) => a + b.input_tokens, 0), output_tokens: daily.reduce((a, b) => a + b.output_tokens, 0), audio_seconds: 1240.5 },
          today_cost: daily[daily.length - 1].cost,
          daily,
          by_agent: [ { agent: 'chat', cost: Number((cost * 0.6).toFixed(4)), requests: 800 }, { agent: 'transcription', cost: Number((cost * 0.25).toFixed(4)), requests: 210 }, { agent: 'tts', cost: Number((cost * 0.15).toFixed(4)), requests: 190 } ],
          by_model: [ { model: 'gpt-4o-mini', cost: Number((cost * 0.6).toFixed(4)), requests: 800 }, { model: 'gpt-4o-mini-transcribe', cost: Number((cost * 0.25).toFixed(4)), requests: 210 }, { model: 'gpt-4o-mini-tts', cost: Number((cost * 0.15).toFixed(4)), requests: 190 } ],
          note: 'Costs are estimates based on configurable per-model rates.'
        };
      })()
    };
    // Try exact path first, then fall back to the path without query string.
    return ((data[path] ?? data[bare]) ?? {}) as T;
  }
};
