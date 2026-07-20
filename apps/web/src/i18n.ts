import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

// Native-language interface: RU / UK / AR (RTL) / FR, plus ES/EN.
const resources = {
  ru: { translation: {
    app: 'AI-репетитор испанского',
    nav: { dashboard: 'Главная', course: 'Курс', analyzer: 'Анализ текста', flashcards: 'Карточки', billing: 'Подписка', admin: 'Админка', logout: 'Выйти' },
    login: { title: 'Вход', email: 'Email', password: 'Пароль', submit: 'Войти', register: 'Регистрация', native: 'Родной язык' },
    dashboard: { welcome: 'С возвращением!', level: 'Ваш уровень', continue: 'Продолжить обучение', streak: 'Дней подряд' },
    analyzer: { title: 'Анализ текста', placeholder: 'Вставьте испанский текст…', run: 'Разобрать', verbs: 'Глаголы', nouns: 'Существительные', tenses: 'Времена', topics: 'Темы грамматики' },
    flashcards: { title: 'Карточки', generate: 'Сгенерировать из текста', front: 'Лицо', back: 'Оборот' },
    billing: { title: 'Подписка и оплата', choose: 'Выбрать', method: 'Способ оплаты', country: 'Страна' }
  }},
  uk: { translation: {
    app: 'AI-репетитор іспанської',
    nav: { dashboard: 'Головна', course: 'Курс', analyzer: 'Аналіз тексту', flashcards: 'Картки', billing: 'Підписка', admin: 'Адмінка', logout: 'Вийти' },
    login: { title: 'Вхід', email: 'Email', password: 'Пароль', submit: 'Увійти', register: 'Реєстрація', native: 'Рідна мова' },
    dashboard: { welcome: 'З поверненням!', level: 'Ваш рівень', continue: 'Продовжити навчання', streak: 'Днів поспіль' },
    analyzer: { title: 'Аналіз тексту', placeholder: 'Вставте іспанський текст…', run: 'Розібрати', verbs: 'Дієслова', nouns: 'Іменники', tenses: 'Часи', topics: 'Теми граматики' },
    flashcards: { title: 'Картки', generate: 'Згенерувати з тексту', front: 'Лице', back: 'Зворот' },
    billing: { title: 'Підписка та оплата', choose: 'Обрати', method: 'Спосіб оплати', country: 'Країна' }
  }},
  ar: { translation: {
    app: 'مدرّس الإسبانية بالذكاء الاصطناعي',
    nav: { dashboard: 'الرئيسية', course: 'الدورة', analyzer: 'تحليل النص', flashcards: 'البطاقات', billing: 'الاشتراك', admin: 'الإدارة', logout: 'خروج' },
    login: { title: 'تسجيل الدخول', email: 'البريد', password: 'كلمة المرور', submit: 'دخول', register: 'إنشاء حساب', native: 'اللغة الأم' },
    dashboard: { welcome: 'مرحبًا بعودتك!', level: 'مستواك', continue: 'متابعة التعلّم', streak: 'أيام متتالية' },
    analyzer: { title: 'تحليل النص', placeholder: 'ألصق نصًا إسبانيًا…', run: 'حلّل', verbs: 'الأفعال', nouns: 'الأسماء', tenses: 'الأزمنة', topics: 'قواعد' },
    flashcards: { title: 'البطاقات', generate: 'إنشاء من النص', front: 'الوجه', back: 'الخلف' },
    billing: { title: 'الاشتراك والدفع', choose: 'اختر', method: 'طريقة الدفع', country: 'الدولة' }
  }},
  fr: { translation: {
    app: "Tuteur d'espagnol IA",
    nav: { dashboard: 'Accueil', course: 'Cours', analyzer: 'Analyse de texte', flashcards: 'Cartes', billing: 'Abonnement', admin: 'Admin', logout: 'Déconnexion' },
    login: { title: 'Connexion', email: 'Email', password: 'Mot de passe', submit: 'Se connecter', register: "S'inscrire", native: 'Langue maternelle' },
    dashboard: { welcome: 'Bon retour !', level: 'Votre niveau', continue: "Continuer l'apprentissage", streak: 'Jours de suite' },
    analyzer: { title: 'Analyse de texte', placeholder: 'Collez un texte espagnol…', run: 'Analyser', verbs: 'Verbes', nouns: 'Noms', tenses: 'Temps', topics: 'Points de grammaire' },
    flashcards: { title: 'Cartes', generate: 'Générer depuis un texte', front: 'Recto', back: 'Verso' },
    billing: { title: 'Abonnement et paiement', choose: 'Choisir', method: 'Moyen de paiement', country: 'Pays' }
  }},
  es: { translation: {
    app: 'Tutor de español IA',
    nav: { dashboard: 'Inicio', course: 'Curso', analyzer: 'Análisis de texto', flashcards: 'Tarjetas', billing: 'Suscripción', admin: 'Admin', logout: 'Salir' },
    login: { title: 'Entrar', email: 'Email', password: 'Contraseña', submit: 'Entrar', register: 'Registrarse', native: 'Lengua materna' },
    dashboard: { welcome: '¡Bienvenido de nuevo!', level: 'Tu nivel', continue: 'Continuar aprendiendo', streak: 'Días seguidos' },
    analyzer: { title: 'Análisis de texto', placeholder: 'Pega un texto en español…', run: 'Analizar', verbs: 'Verbos', nouns: 'Sustantivos', tenses: 'Tiempos', topics: 'Gramática' },
    flashcards: { title: 'Tarjetas', generate: 'Generar desde texto', front: 'Anverso', back: 'Reverso' },
    billing: { title: 'Suscripción y pago', choose: 'Elegir', method: 'Método de pago', country: 'País' }
  }},
  en: { translation: {
    app: 'AI Spanish Tutor',
    nav: { dashboard: 'Home', course: 'Course', analyzer: 'Text analysis', flashcards: 'Flashcards', billing: 'Billing', admin: 'Admin', logout: 'Log out' },
    login: { title: 'Sign in', email: 'Email', password: 'Password', submit: 'Sign in', register: 'Register', native: 'Native language' },
    dashboard: { welcome: 'Welcome back!', level: 'Your level', continue: 'Continue learning', streak: 'Day streak' },
    analyzer: { title: 'Text analysis', placeholder: 'Paste Spanish text…', run: 'Analyze', verbs: 'Verbs', nouns: 'Nouns', tenses: 'Tenses', topics: 'Grammar topics' },
    flashcards: { title: 'Flashcards', generate: 'Generate from text', front: 'Front', back: 'Back' },
    billing: { title: 'Billing', choose: 'Choose', method: 'Payment method', country: 'Country' }
  }}
};

export const RTL_LOCALES = ['ar'];
const saved = localStorage.getItem('locale') || 'ru';

i18n.use(initReactI18next).init({
  resources,
  lng: saved,
  fallbackLng: 'en',
  interpolation: { escapeValue: false }
});

// Upload Studio strings, merged per locale (keeps the main block tidy).
const uploadStrings: Record<string, any> = {
  ru: { nav: { upload: 'Загрузки' }, upload: { title: 'Загрузки', paste: 'Вставить текст', file: 'Загрузить файл', build: 'Собрать урок', building: 'Собираем урок…', placeholder: 'Вставьте испанский текст…', drop: 'PDF, DOCX, TXT, MP3, WAV', level: 'Уровень', native: 'Родной язык', summary: 'Кратко', vocabulary: 'Слова', cards: 'Карточки', exercises: 'Упражнения', transcript: 'Транскрипт' } },
  uk: { nav: { upload: 'Завантаження' }, upload: { title: 'Завантаження', paste: 'Вставити текст', file: 'Завантажити файл', build: 'Зібрати урок', building: 'Збираємо урок…', placeholder: 'Вставте іспанський текст…', drop: 'PDF, DOCX, TXT, MP3, WAV', level: 'Рівень', native: 'Рідна мова', summary: 'Стисло', vocabulary: 'Слова', cards: 'Картки', exercises: 'Вправи', transcript: 'Транскрипт' } },
  ar: { nav: { upload: 'الملفات' }, upload: { title: 'استوديو الرفع', paste: 'لصق نص', file: 'رفع ملف', build: 'أنشئ الدرس', building: 'جارٍ إنشاء الدرس…', placeholder: 'ألصق نصًا إسبانيًا…', drop: 'PDF, DOCX, TXT, MP3, WAV', level: 'المستوى', native: 'اللغة الأم', summary: 'ملخّص', vocabulary: 'المفردات', cards: 'البطاقات', exercises: 'التمارين', transcript: 'النص المفرّغ' } },
  fr: { nav: { upload: 'Imports' }, upload: { title: 'Studio d\'import', paste: 'Coller un texte', file: 'Téléverser un fichier', build: 'Créer la leçon', building: 'Création de la leçon…', placeholder: 'Collez un texte espagnol…', drop: 'PDF, DOCX, TXT, MP3, WAV', level: 'Niveau', native: 'Langue maternelle', summary: 'Résumé', vocabulary: 'Vocabulaire', cards: 'Cartes', exercises: 'Exercices', transcript: 'Transcription' } },
  es: { nav: { upload: 'Subidas' }, upload: { title: 'Estudio de subida', paste: 'Pegar texto', file: 'Subir archivo', build: 'Crear lección', building: 'Creando la lección…', placeholder: 'Pega un texto en español…', drop: 'PDF, DOCX, TXT, MP3, WAV', level: 'Nivel', native: 'Lengua materna', summary: 'Resumen', vocabulary: 'Vocabulario', cards: 'Tarjetas', exercises: 'Ejercicios', transcript: 'Transcripción' } },
  en: { nav: { upload: 'Uploads' }, upload: { title: 'Upload Studio', paste: 'Paste text', file: 'Upload file', build: 'Build lesson', building: 'Building lesson…', placeholder: 'Paste Spanish text…', drop: 'PDF, DOCX, TXT, MP3, WAV', level: 'Level', native: 'Native language', summary: 'Summary', vocabulary: 'Vocabulary', cards: 'Flashcards', exercises: 'Exercises', transcript: 'Transcript' } }
};
Object.entries(uploadStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

const voiceStrings: Record<string, any> = {
  ru: { nav: { voice: 'Голос' }, voice: { title: 'Голосовой репетитор', start: 'Начать', scenario: 'Сценарий', level: 'Уровень', send: 'Отправить', record: 'Запись', stop: 'Стоп', you: 'Вы', tutor: 'Репетитор', correction: 'Исправление', score: 'Оценка', type: 'Напишите сообщение…' } },
  uk: { nav: { voice: 'Голос' }, voice: { title: 'Голосовий репетитор', start: 'Почати', scenario: 'Сценарій', level: 'Рівень', send: 'Надіслати', record: 'Запис', stop: 'Стоп', you: 'Ви', tutor: 'Репетитор', correction: 'Виправлення', score: 'Оцінка', type: 'Напишіть повідомлення…' } },
  ar: { nav: { voice: 'الصوت' }, voice: { title: 'مدرّس المحادثة', start: 'ابدأ', scenario: 'السيناريو', level: 'المستوى', send: 'إرسال', record: 'تسجيل', stop: 'إيقاف', you: 'أنت', tutor: 'المدرّس', correction: 'تصحيح', score: 'التقييم', type: 'اكتب رسالة…' } },
  fr: { nav: { voice: 'Voix' }, voice: { title: 'Tuteur vocal', start: 'Commencer', scenario: 'Scénario', level: 'Niveau', send: 'Envoyer', record: 'Enregistrer', stop: 'Stop', you: 'Vous', tutor: 'Tuteur', correction: 'Correction', score: 'Note', type: 'Écrivez un message…' } },
  es: { nav: { voice: 'Voz' }, voice: { title: 'Tutor de voz', start: 'Empezar', scenario: 'Escenario', level: 'Nivel', send: 'Enviar', record: 'Grabar', stop: 'Parar', you: 'Tú', tutor: 'Tutor', correction: 'Corrección', score: 'Puntuación', type: 'Escribe un mensaje…' } },
  en: { nav: { voice: 'Voice' }, voice: { title: 'Voice Tutor', start: 'Start', scenario: 'Scenario', level: 'Level', send: 'Send', record: 'Record', stop: 'Stop', you: 'You', tutor: 'Tutor', correction: 'Correction', score: 'Score', type: 'Type a message…' } }
};
Object.entries(voiceStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

const diagStrings: Record<string, any> = {
  ru: { nav: { diagnostic: 'Диагностика' }, diag: { title: 'Диагностика уровня', subtitle: 'Ответьте на вопросы и напишите пару фраз — определим ваш уровень.', level: 'Ваш уровень', mc: 'Тест', strengths: 'Сильные стороны', gaps: 'Пробелы', plan: 'План', start: 'Начать обучение', submit: 'Определить уровень', evaluating: 'Оцениваем…', record: 'Записать', stop: 'Стоп' } },
  uk: { nav: { diagnostic: 'Діагностика' }, diag: { title: 'Діагностика рівня', subtitle: 'Дайте відповіді та напишіть кілька фраз — визначимо ваш рівень.', level: 'Ваш рівень', mc: 'Тест', strengths: 'Сильні сторони', gaps: 'Прогалини', plan: 'План', start: 'Почати навчання', submit: 'Визначити рівень', evaluating: 'Оцінюємо…', record: 'Записати', stop: 'Стоп' } },
  ar: { nav: { diagnostic: 'التقييم' }, diag: { title: 'تقييم المستوى', subtitle: 'أجب عن الأسئلة واكتب بضع جمل — سنحدّد مستواك.', level: 'مستواك', mc: 'الاختبار', strengths: 'نقاط القوة', gaps: 'الثغرات', plan: 'الخطة', start: 'ابدأ التعلّم', submit: 'حدّد المستوى', evaluating: 'جارٍ التقييم…', record: 'تسجيل', stop: 'إيقاف' } },
  fr: { nav: { diagnostic: 'Diagnostic' }, diag: { title: 'Diagnostic de niveau', subtitle: 'Répondez et écrivez quelques phrases — nous évaluons votre niveau.', level: 'Votre niveau', mc: 'Test', strengths: 'Points forts', gaps: 'Lacunes', plan: 'Plan', start: "Commencer l'apprentissage", submit: 'Évaluer', evaluating: 'Évaluation…', record: 'Enregistrer', stop: 'Stop' } },
  es: { nav: { diagnostic: 'Diagnóstico' }, diag: { title: 'Diagnóstico de nivel', subtitle: 'Responde y escribe unas frases — estimamos tu nivel.', level: 'Tu nivel', mc: 'Test', strengths: 'Fortalezas', gaps: 'Carencias', plan: 'Plan', start: 'Empezar a aprender', submit: 'Evaluar', evaluating: 'Evaluando…', record: 'Grabar', stop: 'Parar' } },
  en: { nav: { diagnostic: 'Diagnostic' }, diag: { title: 'Level diagnostic', subtitle: 'Answer a few questions and write a couple of sentences — we estimate your level.', level: 'Your level', mc: 'Test', strengths: 'Strengths', gaps: 'Gaps', plan: 'Plan', start: 'Start learning', submit: 'Assess level', evaluating: 'Assessing…', record: 'Record', stop: 'Stop' } }
};
Object.entries(diagStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

const progressStrings: Record<string, any> = {
  ru: { nav: { progress: 'Мои ошибки' }, progress: { title: 'Мои ошибки и прогресс', subtitle: 'Слабые места копятся из диагностики, диалогов и упражнений.', level: 'Уровень', mistakes: 'Всего ошибок', weakSpots: 'Слабые места', plan: 'План', practice: 'Тренировка', practiceBtn: 'Проработать слабые места', targeted: 'Упражнения по вашим темам', recent: 'Недавние ошибки', empty: 'Пока пусто — пройдите диагностику или урок.' } },
  uk: { nav: { progress: 'Мої помилки' }, progress: { title: 'Мої помилки та прогрес', subtitle: 'Слабкі місця збираються з діагностики, діалогів і вправ.', level: 'Рівень', mistakes: 'Усього помилок', weakSpots: 'Слабкі місця', plan: 'План', practice: 'Тренування', practiceBtn: 'Опрацювати слабкі місця', targeted: 'Вправи за вашими темами', recent: 'Нещодавні помилки', empty: 'Поки порожньо — пройдіть діагностику або урок.' } },
  ar: { nav: { progress: 'أخطائي' }, progress: { title: 'أخطائي وتقدّمي', subtitle: 'تتجمّع نقاط الضعف من التقييم والحوارات والتمارين.', level: 'المستوى', mistakes: 'إجمالي الأخطاء', weakSpots: 'نقاط الضعف', plan: 'الخطة', practice: 'تدريب', practiceBtn: 'تدرّب على نقاط ضعفك', targeted: 'تمارين حسب مواضيعك', recent: 'أخطاء حديثة', empty: 'لا شيء بعد — ابدأ بالتقييم أو درس.' } },
  fr: { nav: { progress: 'Mes erreurs' }, progress: { title: 'Mes erreurs et progrès', subtitle: 'Les points faibles se cumulent depuis le diagnostic, les dialogues et les exercices.', level: 'Niveau', mistakes: 'Total des erreurs', weakSpots: 'Points faibles', plan: 'Plan', practice: 'Entraînement', practiceBtn: 'Travailler mes points faibles', targeted: 'Exercices sur vos thèmes', recent: 'Erreurs récentes', empty: 'Rien pour l’instant — fais le diagnostic ou une leçon.' } },
  es: { nav: { progress: 'Mis errores' }, progress: { title: 'Mis errores y progreso', subtitle: 'Los puntos débiles se acumulan del diagnóstico, los diálogos y los ejercicios.', level: 'Nivel', mistakes: 'Errores totales', weakSpots: 'Puntos débiles', plan: 'Plan', practice: 'Práctica', practiceBtn: 'Practicar puntos débiles', targeted: 'Ejercicios sobre tus temas', recent: 'Errores recientes', empty: 'Nada aún — haz el diagnóstico o una lección.' } },
  en: { nav: { progress: 'My mistakes' }, progress: { title: 'My mistakes & progress', subtitle: 'Weak spots accumulate from the diagnostic, dialogues and exercises.', level: 'Level', mistakes: 'Total mistakes', weakSpots: 'Weak spots', plan: 'Plan', practice: 'Practice', practiceBtn: 'Practice weak spots', targeted: 'Exercises on your topics', recent: 'Recent mistakes', empty: 'Nothing yet — take the diagnostic or a lesson.' } }
};
Object.entries(progressStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

const reviewStrings: Record<string, any> = {
  ru: { nav: { review: 'Повторение' }, review: { title: 'Повторение', subtitle: 'Интервальные повторения: система сама выбирает, что показать сегодня.', due: 'К повторению', new: 'Новые', learning: 'Изучается', mastered: 'Освоено', progress: 'Прогресс освоения', tapToFlip: 'нажмите, чтобы перевернуть', clear: 'Очистить мои карточки', clearConfirm: 'Удалить все ваши карточки? Это уберёт старые карточки (например, на другом языке). Действие необратимо.', done: 'На сегодня всё!', doneHint: 'Возвращайтесь завтра — карточки появятся по расписанию.', reload: 'Обновить', show: 'Показать ответ', again: 'Снова', hard: 'Трудно', good: 'Хорошо', easy: 'Легко' } },
  uk: { nav: { review: 'Повторення' }, review: { title: 'Повторення', subtitle: 'Інтервальні повторення: система сама обирає, що показати сьогодні.', due: 'До повторення', new: 'Нові', learning: 'Вивчається', mastered: 'Засвоєно', progress: 'Прогрес засвоєння', tapToFlip: 'натисніть, щоб перевернути', clear: 'Очистити мої картки', clearConfirm: 'Видалити всі ваші картки? Дію не можна скасувати.', done: 'На сьогодні все!', doneHint: 'Повертайтесь завтра — картки зʼявляться за розкладом.', reload: 'Оновити', show: 'Показати відповідь', again: 'Знову', hard: 'Важко', good: 'Добре', easy: 'Легко' } },
  ar: { nav: { review: 'المراجعة' }, review: { title: 'المراجعة', subtitle: 'تكرار متباعد: النظام يختار ما تراجعه اليوم.', due: 'للمراجعة', new: 'جديدة', learning: 'قيد التعلّم', mastered: 'مُتقنة', progress: 'تقدّم الإتقان', tapToFlip: 'اضغط للقلب', clear: 'مسح بطاقاتي', clearConfirm: 'حذف كل بطاقاتك؟ لا يمكن التراجع.', done: 'انتهيت لليوم!', doneHint: 'عُد غدًا — ستظهر البطاقات حسب الجدول.', reload: 'تحديث', show: 'أظهر الإجابة', again: 'مجددًا', hard: 'صعب', good: 'جيد', easy: 'سهل' } },
  fr: { nav: { review: 'Révision' }, review: { title: 'Révision', subtitle: 'Répétition espacée : le système choisit quoi réviser aujourd’hui.', due: 'À réviser', new: 'Nouvelles', learning: 'En cours', mastered: 'Maîtrisées', progress: 'Progression', tapToFlip: 'cliquez pour retourner', clear: 'Effacer mes cartes', clearConfirm: 'Supprimer toutes vos cartes ? Action irréversible.', done: 'Fini pour aujourd’hui !', doneHint: 'Revenez demain — les cartes reviendront selon le planning.', reload: 'Actualiser', show: 'Voir la réponse', again: 'Encore', hard: 'Difficile', good: 'Bien', easy: 'Facile' } },
  es: { nav: { review: 'Repaso' }, review: { title: 'Repaso', subtitle: 'Repetición espaciada: el sistema elige qué repasar hoy.', due: 'Para repasar', new: 'Nuevas', learning: 'Aprendiendo', mastered: 'Dominadas', progress: 'Progreso', tapToFlip: 'toca para girar', clear: 'Borrar mis tarjetas', clearConfirm: '¿Borrar todas tus tarjetas? Acción irreversible.', done: '¡Listo por hoy!', doneHint: 'Vuelve mañana — las tarjetas volverán según el calendario.', reload: 'Actualizar', show: 'Ver respuesta', again: 'Otra vez', hard: 'Difícil', good: 'Bien', easy: 'Fácil' } },
  en: { nav: { review: 'Review' }, review: { title: 'Review', subtitle: 'Spaced repetition: the system picks what to show you today.', due: 'Due', new: 'New', learning: 'Learning', mastered: 'Mastered', progress: 'Mastery progress', tapToFlip: 'tap to flip', clear: 'Clear my cards', clearConfirm: 'Delete all your cards? This removes old cards (e.g. in another language). This cannot be undone.', done: 'Done for today!', doneHint: 'Come back tomorrow — cards return on schedule.', reload: 'Refresh', show: 'Show answer', again: 'Again', hard: 'Hard', good: 'Good', easy: 'Easy' } }
};
Object.entries(reviewStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

const motStrings: Record<string, any> = {
  ru: { mot: { streak: 'Серия дней', longest: 'Рекорд', due: 'К повторению', dailyGoal: 'Дневная цель', goalSize: 'Цель', reminders: 'Напоминания в Telegram', remindersHint: 'Напомним, когда есть карточки к повторению.', on: 'Включены', off: 'Выключены' } },
  uk: { mot: { streak: 'Серія днів', longest: 'Рекорд', due: 'До повторення', dailyGoal: 'Денна ціль', goalSize: 'Ціль', reminders: 'Нагадування в Telegram', remindersHint: 'Нагадаємо, коли є картки до повторення.', on: 'Увімкнені', off: 'Вимкнені' } },
  ar: { mot: { streak: 'سلسلة الأيام', longest: 'الأطول', due: 'للمراجعة', dailyGoal: 'الهدف اليومي', goalSize: 'الهدف', reminders: 'تذكيرات في تيليجرام', remindersHint: 'سنذكّرك عندما توجد بطاقات للمراجعة.', on: 'مُفعّلة', off: 'مُعطّلة' } },
  fr: { mot: { streak: 'Série de jours', longest: 'Record', due: 'À réviser', dailyGoal: 'Objectif quotidien', goalSize: 'Objectif', reminders: 'Rappels sur Telegram', remindersHint: 'On vous rappelle quand des cartes sont à réviser.', on: 'Activés', off: 'Désactivés' } },
  es: { mot: { streak: 'Racha de días', longest: 'Récord', due: 'Para repasar', dailyGoal: 'Objetivo diario', goalSize: 'Objetivo', reminders: 'Recordatorios en Telegram', remindersHint: 'Te avisamos cuando haya tarjetas para repasar.', on: 'Activados', off: 'Desactivados' } },
  en: { mot: { streak: 'Day streak', longest: 'Best', due: 'Due', dailyGoal: 'Daily goal', goalSize: 'Goal', reminders: 'Telegram reminders', remindersHint: 'We ping you when cards are due.', on: 'On', off: 'Off' } }
};
Object.entries(motStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

const podStrings: Record<string, any> = {
  ru: { nav: { podcast: 'Подкасты' }, podcast: { title: 'Podcast Studio', subtitle: 'Аудио → сегменты по времени → урок. Проходите по кусочкам.', level: 'Уровень', build: 'Собрать', building: 'Обрабатываем…', segments: 'Сегменты', cards: 'Карточки', exercises: 'Упражнения' } },
  uk: { nav: { podcast: 'Подкасти' }, podcast: { title: 'Podcast Studio', subtitle: 'Аудіо → сегменти за часом → урок. Проходьте частинами.', level: 'Рівень', build: 'Зібрати', building: 'Обробляємо…', segments: 'Сегменти', cards: 'Картки', exercises: 'Вправи' } },
  ar: { nav: { podcast: 'البودكاست' }, podcast: { title: 'استوديو البودكاست', subtitle: 'صوت ← مقاطع زمنية ← درس. تعلّم مقطعًا مقطعًا.', level: 'المستوى', build: 'إنشاء', building: 'جارٍ المعالجة…', segments: 'المقاطع', cards: 'البطاقات', exercises: 'التمارين' } },
  fr: { nav: { podcast: 'Podcasts' }, podcast: { title: 'Podcast Studio', subtitle: 'Audio → segments horodatés → leçon. Étudiez par morceaux.', level: 'Niveau', build: 'Créer', building: 'Traitement…', segments: 'Segments', cards: 'Cartes', exercises: 'Exercices' } },
  es: { nav: { podcast: 'Podcasts' }, podcast: { title: 'Podcast Studio', subtitle: 'Audio → segmentos con tiempo → lección. Estudia por partes.', level: 'Nivel', build: 'Crear', building: 'Procesando…', segments: 'Segmentos', cards: 'Tarjetas', exercises: 'Ejercicios' } },
  en: { nav: { podcast: 'Podcasts' }, podcast: { title: 'Podcast Studio', subtitle: 'Audio → timed segments → lesson. Study piece by piece.', level: 'Level', build: 'Build', building: 'Processing…', segments: 'Segments', cards: 'Flashcards', exercises: 'Exercises' } }
};
Object.entries(podStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

const simStrings: Record<string, any> = {
  ru: { nav: { sim: 'Симуляции' }, sim: { title: 'Ролевые симуляции', subtitle: 'Мини-миссии: у собеседника роль, у вас — цель, которую нужно достичь.', level: 'Уровень', start: 'Начать', goal: 'Цель', completed: 'Цель достигнута!', you: 'Вы', again: 'Другая симуляция', record: 'Запись', stop: 'Стоп', send: 'Отправить', type: 'Напишите сообщение…' } },
  uk: { nav: { sim: 'Симуляції' }, sim: { title: 'Рольові симуляції', subtitle: 'Міні-місії: у співрозмовника роль, у вас — ціль, яку треба досягти.', level: 'Рівень', start: 'Почати', goal: 'Ціль', completed: 'Ціль досягнута!', you: 'Ви', again: 'Інша симуляція', record: 'Запис', stop: 'Стоп', send: 'Надіслати', type: 'Напишіть повідомлення…' } },
  ar: { nav: { sim: 'محاكاة' }, sim: { title: 'محاكاة أدوار', subtitle: 'مهام صغيرة: للمحاور دور، ولك هدف يجب تحقيقه.', level: 'المستوى', start: 'ابدأ', goal: 'الهدف', completed: 'تحقق الهدف!', you: 'أنت', again: 'محاكاة أخرى', record: 'تسجيل', stop: 'إيقاف', send: 'إرسال', type: 'اكتب رسالة…' } },
  fr: { nav: { sim: 'Simulations' }, sim: { title: 'Simulations de rôle', subtitle: 'Mini-missions : l’interlocuteur a un rôle, vous avez un objectif à atteindre.', level: 'Niveau', start: 'Commencer', goal: 'Objectif', completed: 'Objectif atteint !', you: 'Vous', again: 'Autre simulation', record: 'Enregistrer', stop: 'Stop', send: 'Envoyer', type: 'Écrivez un message…' } },
  es: { nav: { sim: 'Simulaciones' }, sim: { title: 'Simulaciones de rol', subtitle: 'Mini-misiones: el interlocutor tiene un rol y tú, un objetivo que cumplir.', level: 'Nivel', start: 'Empezar', goal: 'Objetivo', completed: '¡Objetivo cumplido!', you: 'Tú', again: 'Otra simulación', record: 'Grabar', stop: 'Parar', send: 'Enviar', type: 'Escribe un mensaje…' } },
  en: { nav: { sim: 'Simulations' }, sim: { title: 'Role-play simulations', subtitle: 'Mini-missions: the other side has a role, you have a goal to reach.', level: 'Level', start: 'Start', goal: 'Goal', completed: 'Goal reached!', you: 'You', again: 'Another simulation', record: 'Record', stop: 'Stop', send: 'Send', type: 'Type a message…' } }
};
Object.entries(simStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

const settingsStrings: Record<string, any> = {
  ru: { nav: { settings: 'Настройки' }, settings: { title: 'Настройки', subtitle: 'Язык объяснений и интерфейса.', account: 'Аккаунт', nativeLang: 'Родной язык (объяснения ИИ)', nativeHint: 'На этом языке ИИ пишет переводы, объяснения и разборы в уроках.', interfaceLang: 'Язык интерфейса', interfaceHint: 'Язык меню и кнопок приложения.', saved: 'Сохранено' } },
  uk: { nav: { settings: 'Налаштування' }, settings: { title: 'Налаштування', subtitle: 'Мова пояснень та інтерфейсу.', account: 'Акаунт', nativeLang: 'Рідна мова (пояснення ШІ)', nativeHint: 'Цією мовою ШІ пише переклади, пояснення й розбори в уроках.', interfaceLang: 'Мова інтерфейсу', interfaceHint: 'Мова меню та кнопок застосунку.', saved: 'Збережено' } },
  ar: { nav: { settings: 'الإعدادات' }, settings: { title: 'الإعدادات', subtitle: 'لغة الشرح والواجهة.', account: 'الحساب', nativeLang: 'اللغة الأم (شرح الذكاء الاصطناعي)', nativeHint: 'بهذه اللغة يكتب الذكاء الاصطناعي الترجمات والشروح في الدروس.', interfaceLang: 'لغة الواجهة', interfaceHint: 'لغة القوائم والأزرار.', saved: 'تم الحفظ' } },
  fr: { nav: { settings: 'Paramètres' }, settings: { title: 'Paramètres', subtitle: 'Langue des explications et de l’interface.', account: 'Compte', nativeLang: 'Langue maternelle (explications IA)', nativeHint: 'Langue dans laquelle l’IA écrit les traductions et explications des leçons.', interfaceLang: 'Langue de l’interface', interfaceHint: 'Langue des menus et boutons.', saved: 'Enregistré' } },
  es: { nav: { settings: 'Ajustes' }, settings: { title: 'Ajustes', subtitle: 'Idioma de las explicaciones y de la interfaz.', account: 'Cuenta', nativeLang: 'Idioma nativo (explicaciones de IA)', nativeHint: 'Idioma en el que la IA escribe traducciones y explicaciones en las lecciones.', interfaceLang: 'Idioma de la interfaz', interfaceHint: 'Idioma de los menús y botones.', saved: 'Guardado' } },
  en: { nav: { settings: 'Settings' }, settings: { title: 'Settings', subtitle: 'Explanation and interface language.', account: 'Account', nativeLang: 'Native language (AI explanations)', nativeHint: 'The language the AI uses for translations and explanations in lessons.', interfaceLang: 'Interface language', interfaceHint: 'The language of menus and buttons.', saved: 'Saved' } }
};
Object.entries(settingsStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

const courseStrings: Record<string, any> = {
  ru: { progress: { words: 'Слова с примерами' }, course: { subtitle: 'Ваши уроки по уровням. Новые появляются из «Загрузок».', back: 'Назад', theory: 'Теория', words: 'Слова', exercises: 'Упражнения', lessons: 'уроков', none: 'нет уроков', empty: 'В этом уроке пока нет карточек.', buildHint: 'Пока нет уроков этого уровня — соберите урок в «Загрузках».', subtitleShort: '' } },
  uk: { progress: { words: 'Слова з прикладами' }, course: { subtitle: 'Ваші уроки за рівнями. Нові зʼявляються із «Завантажень».', back: 'Назад', theory: 'Теорія', words: 'Слова', exercises: 'Вправи', lessons: 'уроків', none: 'немає уроків', empty: 'У цьому уроці ще немає карток.', buildHint: 'Поки немає уроків цього рівня — зберіть урок у «Завантаженнях».' } },
  ar: { progress: { words: 'كلمات مع أمثلة' }, course: { subtitle: 'دروسك حسب المستوى. تظهر الجديدة من «التحميلات».', back: 'رجوع', theory: 'النظرية', words: 'كلمات', exercises: 'تمارين', lessons: 'دروس', none: 'لا دروس', empty: 'لا بطاقات في هذا الدرس بعد.', buildHint: 'لا دروس لهذا المستوى بعد — أنشئ درسًا من «التحميلات».' } },
  fr: { progress: { words: 'Mots avec exemples' }, course: { subtitle: 'Vos leçons par niveau. Les nouvelles viennent des « Imports ».', back: 'Retour', theory: 'Théorie', words: 'Mots', exercises: 'Exercices', lessons: 'leçons', none: 'aucune leçon', empty: 'Pas encore de cartes dans cette leçon.', buildHint: 'Aucune leçon à ce niveau — créez-en une dans « Imports ».' } },
  es: { progress: { words: 'Palabras con ejemplos' }, course: { subtitle: 'Tus lecciones por nivel. Las nuevas vienen de «Subidas».', back: 'Atrás', theory: 'Teoría', words: 'Palabras', exercises: 'Ejercicios', lessons: 'lecciones', none: 'sin lecciones', empty: 'Aún no hay tarjetas en esta lección.', buildHint: 'Aún no hay lecciones de este nivel — crea una en «Subidas».' } },
  en: { progress: { words: 'Words with examples' }, course: { subtitle: 'Your lessons by level. New ones come from Uploads.', back: 'Back', theory: 'Theory', words: 'Words', exercises: 'Exercises', lessons: 'lessons', none: 'no lessons', empty: 'No cards in this lesson yet.', buildHint: 'No lessons at this level yet — build one in Uploads.' } }
};
Object.entries(courseStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

const exStrings: Record<string, any> = {
  ru: { ex: { check: 'Проверить', correct: 'Верно!', wrong: 'Неверно. Правильный ответ:', type: 'Ваш ответ…' } },
  uk: { ex: { check: 'Перевірити', correct: 'Правильно!', wrong: 'Неправильно. Правильна відповідь:', type: 'Ваша відповідь…' } },
  ar: { ex: { check: 'تحقّق', correct: 'صحيح!', wrong: 'خطأ. الإجابة الصحيحة:', type: 'إجابتك…' } },
  fr: { ex: { check: 'Vérifier', correct: 'Correct !', wrong: 'Incorrect. Bonne réponse :', type: 'Votre réponse…' } },
  es: { ex: { check: 'Comprobar', correct: '¡Correcto!', wrong: 'Incorrecto. Respuesta correcta:', type: 'Tu respuesta…' } },
  en: { ex: { check: 'Check', correct: 'Correct!', wrong: 'Incorrect. Correct answer:', type: 'Your answer…' } }
};
Object.entries(exStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

const fcStrings: Record<string, any> = {
  ru: { flashcards: { subtitle: 'Из текста, файла (PDF/DOCX/фото/аудио/видео) или голоса. Карточки сохраняются в «Повторение».', matEs: 'Материал: испанский', matNative: 'Материал: мой язык', phEs: 'Вставьте испанский текст или слова…', phNative: 'Вставьте слова на своём языке — получите испанские карточки…', generate: 'Сгенерировать', speak: 'Голос', stop: 'Стоп', file: 'Файл', fileHint: 'txt, pdf, docx, jpg, png, mp3, mp4…', saved: 'Сохранено в колоду', tapToFlip: 'нажмите, чтобы перевернуть', review: 'Карточки добавлены в «Повторение».' } },
  uk: { flashcards: { subtitle: 'З тексту, файлу (PDF/DOCX/фото/аудіо/відео) або голосу. Картки зберігаються в «Повторення».', matEs: 'Матеріал: іспанська', matNative: 'Матеріал: моя мова', phEs: 'Вставте іспанський текст або слова…', phNative: 'Вставте слова своєю мовою — отримаєте іспанські картки…', generate: 'Згенерувати', speak: 'Голос', stop: 'Стоп', file: 'Файл', fileHint: 'txt, pdf, docx, jpg, png, mp3, mp4…', saved: 'Збережено в колоду', tapToFlip: 'натисніть, щоб перевернути', review: 'Картки додано в «Повторення».' } },
  ar: { flashcards: { subtitle: 'من نص أو ملف (PDF/DOCX/صورة/صوت/فيديو) أو صوتك. تُحفظ البطاقات في «المراجعة».', matEs: 'المادة: الإسبانية', matNative: 'المادة: لغتي', phEs: 'الصق نصًا أو كلمات بالإسبانية…', phNative: 'الصق كلمات بلغتك — واحصل على بطاقات إسبانية…', generate: 'إنشاء', speak: 'صوت', stop: 'إيقاف', file: 'ملف', fileHint: 'txt, pdf, docx, jpg, png, mp3, mp4…', saved: 'حُفظت في المجموعة', tapToFlip: 'اضغط للقلب', review: 'أُضيفت البطاقات إلى «المراجعة».' } },
  fr: { flashcards: { subtitle: 'Depuis un texte, un fichier (PDF/DOCX/photo/audio/vidéo) ou la voix. Les cartes vont dans « Révision ».', matEs: 'Matériel : espagnol', matNative: 'Matériel : ma langue', phEs: 'Collez un texte ou des mots en espagnol…', phNative: 'Collez des mots dans votre langue — obtenez des cartes en espagnol…', generate: 'Générer', speak: 'Voix', stop: 'Stop', file: 'Fichier', fileHint: 'txt, pdf, docx, jpg, png, mp3, mp4…', saved: 'Enregistré dans le paquet', tapToFlip: 'cliquez pour retourner', review: 'Cartes ajoutées à « Révision ».' } },
  es: { flashcards: { subtitle: 'Desde texto, archivo (PDF/DOCX/foto/audio/vídeo) o voz. Las tarjetas van a «Repaso».', matEs: 'Material: español', matNative: 'Material: mi idioma', phEs: 'Pega texto o palabras en español…', phNative: 'Pega palabras en tu idioma — obtén tarjetas en español…', generate: 'Generar', speak: 'Voz', stop: 'Parar', file: 'Archivo', fileHint: 'txt, pdf, docx, jpg, png, mp3, mp4…', saved: 'Guardado en el mazo', tapToFlip: 'toca para girar', review: 'Tarjetas añadidas a «Repaso».' } },
  en: { flashcards: { subtitle: 'From text, a file (PDF/DOCX/photo/audio/video) or your voice. Cards go to Review.', matEs: 'Material: Spanish', matNative: 'Material: my language', phEs: 'Paste Spanish text or words…', phNative: 'Paste words in your language — get Spanish cards…', generate: 'Generate', speak: 'Voice', stop: 'Stop', file: 'File', fileHint: 'txt, pdf, docx, jpg, png, mp3, mp4…', saved: 'Saved to deck', tapToFlip: 'tap to flip', review: 'Cards added to Review.' } }
};
Object.entries(fcStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

const vocabStrings: Record<string, any> = {
  ru: { nav: { vocab: 'Мой словарь' }, vocab: { title: 'Мой словарь', subtitle: 'Ваш личный банк слов и фраз из загруженных материалов. Ищите и повторяйте.', search: 'Поиск по-испански или по-русски…', all: 'Все', verbs: 'Глаголы', collocations: 'Сочетания', examples: 'Примеры', phrases: 'Фразы', random: '🎲 Случайные', randomHint: 'Случайная подборка — жмите ещё раз для новой.', count: '{{n}} совпадений', empty: 'Ничего не найдено. Измените запрос или вид.', loading: 'Загружаем…' } },
  uk: { nav: { vocab: 'Мій словник' }, vocab: { title: 'Мій словник', subtitle: 'Ваш особистий банк слів і фраз із завантажених матеріалів. Шукайте та повторюйте.', search: 'Пошук іспанською або українською…', all: 'Усі', verbs: 'Дієслова', collocations: 'Сполучення', examples: 'Приклади', phrases: 'Фрази', random: '🎲 Випадкові', randomHint: 'Випадкова добірка — натисніть ще раз для нової.', count: '{{n}} збігів', empty: 'Нічого не знайдено. Змініть запит або вид.', loading: 'Завантажуємо…' } },
  ar: { nav: { vocab: 'مفرداتي' }, vocab: { title: 'مفرداتي', subtitle: 'بنك كلماتك وعباراتك الشخصي من موادّك المرفوعة. ابحث وراجع.', search: 'ابحث بالإسبانية أو بلغتك…', all: 'الكل', verbs: 'الأفعال', collocations: 'المتلازمات', examples: 'أمثلة', phrases: 'عبارات', random: '🎲 عشوائي', randomHint: 'مجموعة عشوائية — اضغط مرة أخرى لغيرها.', count: '{{n}} نتيجة', empty: 'لا نتائج. غيّر البحث أو النوع.', loading: 'جارٍ التحميل…' } },
  fr: { nav: { vocab: 'Mon lexique' }, vocab: { title: 'Mon lexique', subtitle: 'Votre banque personnelle de mots et expressions issue de vos imports. Cherchez et révisez.', search: 'Rechercher en espagnol ou en français…', all: 'Tout', verbs: 'Verbes', collocations: 'Collocations', examples: 'Exemples', phrases: 'Expressions', random: '🎲 Aléatoire', randomHint: 'Sélection aléatoire — cliquez encore pour en changer.', count: '{{n}} résultats', empty: 'Aucun résultat. Changez la recherche ou le type.', loading: 'Chargement…' } },
  es: { nav: { vocab: 'Mi vocabulario' }, vocab: { title: 'Mi vocabulario', subtitle: 'Tu banco personal de palabras y frases de tus materiales subidos. Busca y repasa.', search: 'Busca en español o en tu idioma…', all: 'Todo', verbs: 'Verbos', collocations: 'Colocaciones', examples: 'Ejemplos', phrases: 'Frases', random: '🎲 Aleatorio', randomHint: 'Selección aleatoria — pulsa otra vez para cambiar.', count: '{{n}} resultados', empty: 'Sin resultados. Cambia la búsqueda o el tipo.', loading: 'Cargando…' } },
  en: { nav: { vocab: 'My vocabulary' }, vocab: { title: 'My vocabulary', subtitle: 'Your personal bank of words and phrases from your uploaded materials. Search and review.', search: 'Search in Spanish or your language…', all: 'All', verbs: 'Verbs', collocations: 'Collocations', examples: 'Examples', phrases: 'Phrases', random: '🎲 Random', randomHint: 'A random pick — tap again for a fresh set.', count: '{{n}} matches', empty: 'Nothing found. Change the search or type.', loading: 'Loading…' } }
};
Object.entries(vocabStrings).forEach(([lng, bundle]) => {
  i18n.addResourceBundle(lng, 'translation', bundle, true, true);
});

export function applyDir(locale: string) {
  const dir = RTL_LOCALES.includes(locale) ? 'rtl' : 'ltr';
  document.documentElement.setAttribute('dir', dir);
  document.documentElement.setAttribute('lang', locale);
}
applyDir(saved);

i18n.on('languageChanged', (lng) => {
  localStorage.setItem('locale', lng);
  applyDir(lng);
});

export default i18n;
