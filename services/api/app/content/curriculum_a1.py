"""Full hand-authored A1 curriculum (Lessons 1–16), aligned to syllabus numbers.

Original, license-clean content (grammar facts, own wording + exercises). Each lesson maps
to a syllabus topic via `n`, so the AI generator skips these numbers and only fills the rest.
Every exercise's correct_answer exactly matches one option.
"""

A1_LESSONS = [
    {
        'n': 1, 'level': 'A1', 'title': 'Алфавит и произношение',
        'theory': (
            'В испанском 27 букв. Читается почти как пишется. Ключевые правила:\n\n'
            '• ñ — «нь»: niño.  • ll — «й»: llamar.  • ch — «ч»: chico.\n'
            '• j и g (перед e, i) — резкое «х»: jamón, gente.  • h — не читается: hola.\n'
            '• c перед e, i — «с» (в Испании «θ»): cine; в остальных случаях «к»: casa.\n'
            '• z — «с/θ»: zapato.  • v читается как b: vino.\n\n'
            'Ударение: слова на гласную, -n, -s — на предпоследний слог (casa, hablan); '
            'на согласную (кроме -n, -s) — на последний (hablar). Знак акцента (tilde) '
            'показывает исключение: canción, árbol.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Как читается буква «ñ» в слове niño?',
             'options': ['н', 'нь', 'й'], 'correct_answer': 'нь', 'explanation': 'ñ = «нь»: niño.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Как звучит «j» в jamón?',
             'options': ['ж', 'х', 'дж'], 'correct_answer': 'х', 'explanation': 'j — резкое «х».'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Буква «h» в слове hola…',
             'options': ['читается как х', 'не читается', 'читается как г'], 'correct_answer': 'не читается',
             'explanation': 'h немая: hola → «ола».'},
            {'exercise_type': 'multiple_choice', 'prompt': 'На какой слог падает ударение в слове «casa» (без акцента)?',
             'options': ['на первый (ca)', 'на второй (sa)', 'на последний'], 'correct_answer': 'на первый (ca)',
             'explanation': 'Слово на гласную → ударение на предпоследний слог: CA-sa.'},
        ],
    },
    {
        'n': 2, 'level': 'A1', 'title': 'Род существительных и неопределённый артикль',
        'theory': (
            'Существительные бывают мужского или женского рода.\n'
            '• Обычно -o → м. р. (el libro), -a → ж. р. (la mesa). Исключения запоминают '
            '(el día, la mano, el problema).\n\n'
            'Неопределённый артикль (что-то одно из многих): un (м. р.), una (ж. р.).\n'
            '  un libro, una mesa.\n\n'
            'Указательные: este/esta (этот/эта), ese/esa (тот/та). Связка es = «есть/является»: '
            'Esto es un libro.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Выберите артикль: ___ mesa.',
             'options': ['un', 'una', 'unos'], 'correct_answer': 'una', 'explanation': 'mesa — ж. р.: una mesa.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Выберите артикль: ___ libro.',
             'options': ['una', 'un', 'unas'], 'correct_answer': 'un', 'explanation': 'libro — м. р.: un libro.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Esto ___ un coche.',
             'options': ['es', 'está', 'son'], 'correct_answer': 'es', 'explanation': 'Связка «является» → es.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Какого рода слово «día»?',
             'options': ['женского', 'мужского', 'среднего'], 'correct_answer': 'мужского',
             'explanation': 'el día — исключение, мужской род.'},
        ],
    },
    {
        'n': 3, 'level': 'A1', 'title': 'Определённый артикль и прилагательное',
        'theory': (
            'Определённый артикль (о чём-то известном): el (м. р.), la (ж. р.).\n'
            '  el libro, la casa.\n\n'
            'Прилагательное согласуется в роде и числе и обычно стоит ПОСЛЕ существительного:\n'
            '  el coche rojo, la casa blanca, los coches rojos.\n\n'
            'Прилагательные на -e и на согласную не меняются по роду: verde, azul '
            '(un libro verde, una mesa verde).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '___ casa es grande.',
             'options': ['El', 'La', 'Los'], 'correct_answer': 'La', 'explanation': 'casa — ж. р.: la casa.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El coche ___ (rojo).',
             'options': ['roja', 'rojo', 'rojos'], 'correct_answer': 'rojo', 'explanation': 'coche — м. р. ед. ч.: rojo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'La casa ___ (blanco).',
             'options': ['blanco', 'blanca', 'blancos'], 'correct_answer': 'blanca', 'explanation': 'casa — ж. р.: blanca.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Una mesa ___ (verde).',
             'options': ['verde', 'verda', 'verdo'], 'correct_answer': 'verde', 'explanation': 'verde не меняется по роду.'},
        ],
    },
    {
        'n': 4, 'level': 'A1', 'title': 'Порядок слов. Вопрос и отрицание',
        'theory': (
            'Обычный порядок: подлежащее + сказуемое + дополнение. María come pan.\n\n'
            'Вопрос: часто инверсия (глагол перед подлежащим), знаки ¿ ?: ¿Come María pan?\n'
            'Вопросительные слова: qué, quién, dónde, cómo, cuándo, por qué.\n\n'
            'Отрицание: no перед глаголом: María no come pan. Возможно двойное отрицание: '
            'No come nada.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '¿___ vives? — En Madrid.',
             'options': ['Qué', 'Dónde', 'Quién'], 'correct_answer': 'Dónde', 'explanation': 'Место → dónde.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Отрицание: María ___ come pan.',
             'options': ['no', 'nada', 'nunca'], 'correct_answer': 'no', 'explanation': 'no перед глаголом.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿___ es? — Es mi amigo.',
             'options': ['Dónde', 'Quién', 'Cómo'], 'correct_answer': 'Quién', 'explanation': 'О человеке → quién.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'No veo ___.',
             'options': ['algo', 'nada', 'todo'], 'correct_answer': 'nada', 'explanation': 'Двойное отрицание: no…nada.'},
        ],
    },
    {
        'n': 5, 'level': 'A1', 'title': 'Ser и estar. Предлоги места',
        'theory': (
            'ser (soy, eres, es, somos, sois, son) — о постоянном: кто/что, профессия, качество.\n'
            'estar (estoy, estás, está, estamos, estáis, están) — о состоянии и месте.\n\n'
            '  Soy médico. La sopa está caliente. Estoy en casa.\n\n'
            'Предлоги места: en (в/на), sobre (на), bajo (под), entre (между), '
            'al lado de (рядом с), delante de (перед), detrás de (за).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Yo ___ profesor.',
             'options': ['soy', 'estoy', 'es'], 'correct_answer': 'soy', 'explanation': 'Профессия → ser: soy.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El libro ___ sobre la mesa.',
             'options': ['es', 'está', 'son'], 'correct_answer': 'está', 'explanation': 'Местоположение → estar.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'La sopa ___ caliente.',
             'options': ['es', 'está', 'son'], 'correct_answer': 'está', 'explanation': 'Временное состояние → estar.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El gato está ___ la mesa (под).',
             'options': ['sobre', 'bajo', 'entre'], 'correct_answer': 'bajo', 'explanation': 'bajo = под.'},
        ],
    },
    {
        'n': 6, 'level': 'A1', 'title': 'Конструкция hay. Место прилагательного',
        'theory': (
            'hay (от haber) — «есть/имеется/находится», безлично, форма одна:\n'
            '  Hay un libro en la mesa. Hay muchos coches.\n\n'
            'Разница с estar: hay — вводит новое/неизвестное (с un/muchos/числами); '
            'estar — о конкретном известном (с el/la): El libro está en la mesa.\n\n'
            'Прилагательное обычно после существительного, но некоторые (buen, gran, mal) '
            'могут стоять перед: un buen amigo, una gran casa.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '___ un libro en la mesa.',
             'options': ['Hay', 'Está', 'Es'], 'correct_answer': 'Hay', 'explanation': 'Новое, с «un» → hay.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El coche ___ en la calle.',
             'options': ['hay', 'está', 'es'], 'correct_answer': 'está', 'explanation': 'Известное «el coche» → está.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿Cuántos alumnos ___ en clase?',
             'options': ['hay', 'están', 'son'], 'correct_answer': 'hay', 'explanation': 'Наличие/количество → hay.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es un ___ amigo.',
             'options': ['bueno', 'buen', 'buena'], 'correct_answer': 'buen', 'explanation': 'bueno → buen перед сущ. м. р.'},
        ],
    },
    {
        'n': 7, 'level': 'A1', 'title': 'Множественное число существительных и прилагательных',
        'theory': (
            'Множественное число:\n'
            '• на гласную → +s: casa → casas, coche → coches.\n'
            '• на согласную → +es: profesor → profesores, ciudad → ciudades.\n'
            '• на -z → -ces: lápiz → lápices.\n\n'
            'Артикли мн. ч.: los (м. р.), las (ж. р.). Прилагательное тоже во мн. ч.: '
            'los coches rojos, las casas blancas.\n\n'
            'Вопрос о количестве: ¿Cuánto? / ¿Cuántos? / ¿Cuántas?'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Множественное от «profesor»:',
             'options': ['profesors', 'profesores', 'profesor'], 'correct_answer': 'profesores',
             'explanation': 'На согласную → +es.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Множественное от «lápiz»:',
             'options': ['lápizs', 'lápices', 'lápizes'], 'correct_answer': 'lápices',
             'explanation': '-z → -ces: lápices.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ casas son blancas.',
             'options': ['Los', 'Las', 'El'], 'correct_answer': 'Las', 'explanation': 'casas — ж. р. мн.: las.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿___ libros tienes?',
             'options': ['Cuánto', 'Cuántos', 'Cuánta'], 'correct_answer': 'Cuántos',
             'explanation': 'libros — м. р. мн.: cuántos.'},
        ],
    },
    {
        'n': 8, 'level': 'A1', 'title': 'Опущение артикля',
        'theory': (
            'Артикль опускают:\n'
            '• перед профессией после ser: Soy médico. (но: Soy un buen médico — с прилагательным артикль есть)\n'
            '• перед неисчисляемым/неопределённым количеством: Bebo agua. Como pan.\n'
            '• с большинством стран и городов: Vivo en España.\n'
            '• в устойчивых оборотах: con gusto, en casa, por favor.\n\n'
            'Сравните: Hay pan (вообще хлеб) — El pan está en la mesa (конкретный хлеб).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Soy ___ médico. (профессия)',
             'options': ['un', '— (без артикля)', 'el'], 'correct_answer': '— (без артикля)',
             'explanation': 'После ser профессия без артикля: soy médico.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Bebo ___ agua.',
             'options': ['la', 'una', '— (без артикля)'], 'correct_answer': '— (без артикля)',
             'explanation': 'Неопределённое количество вещества → без артикля.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Vivo en ___ España.',
             'options': ['la', '— (без артикля)', 'una'], 'correct_answer': '— (без артикля)',
             'explanation': 'Большинство стран без артикля.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Estoy en ___ casa.',
             'options': ['la', '— (без артикля)', 'una'], 'correct_answer': '— (без артикля)',
             'explanation': 'Устойчивое «en casa» — без артикля.'},
        ],
    },
    {
        'n': 9, 'level': 'A1', 'title': 'Личные местоимения. I спряжение (-ar)',
        'theory': (
            'Местоимения: yo, tú, él/ella/usted, nosotros, vosotros, ellos/ellas/ustedes. '
            'Часто опускаются, т. к. окончание глагола уже показывает лицо.\n\n'
            'Глаголы на -ar в настоящем: hablar → hablo, hablas, habla, hablamos, habláis, hablan.\n'
            '  (yo) hablo español. (nosotros) trabajamos aquí.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (hablar) español.',
             'options': ['hablo', 'hablas', 'habla'], 'correct_answer': 'hablo', 'explanation': '1 л. ед.: hablo.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Nosotros ___ (trabajar) aquí.',
             'options': ['trabaja', 'trabajamos', 'trabajan'], 'correct_answer': 'trabajamos',
             'explanation': '1 л. мн.: trabajamos.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Ella ___ (estudiar) mucho.',
             'options': ['estudio', 'estudias', 'estudia'], 'correct_answer': 'estudia', 'explanation': '3 л. ед.: estudia.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿Tú ___ (cantar) bien?',
             'options': ['canto', 'cantas', 'canta'], 'correct_answer': 'cantas', 'explanation': '2 л. ед.: cantas.'},
        ],
    },
    {
        'n': 10, 'level': 'A1', 'title': 'a + el = al. Глагол comenzar (e→ie)',
        'theory': (
            'Слияние предлогов с артиклем el: a + el = al; de + el = del.\n'
            '  Voy al cine. Vengo del trabajo.\n\n'
            'Глаголы с чередованием e→ie (в ударных формах): comenzar → comienzo, comienzas, '
            'comienza, comenzamos, comenzáis, comienzan. Так же: querer, pensar, empezar.\n\n'
            'Время на часах: Es la una. Son las tres. Son las cinco y media.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Voy ___ cine. (a + el)',
             'options': ['a el', 'al', 'del'], 'correct_answer': 'al', 'explanation': 'a + el = al.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Vengo ___ trabajo. (de + el)',
             'options': ['de el', 'al', 'del'], 'correct_answer': 'del', 'explanation': 'de + el = del.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (comenzar) ahora.',
             'options': ['comenzo', 'comienzo', 'comienza'], 'correct_answer': 'comienzo',
             'explanation': 'e→ie в ударной форме: comienzo.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿Qué hora es? — ___ las dos.',
             'options': ['Es', 'Son', 'Está'], 'correct_answer': 'Son', 'explanation': 'Мн. число часов → son las dos.'},
        ],
    },
    {
        'n': 11, 'level': 'A1', 'title': 'Возвратные глаголы: lavarse',
        'theory': (
            'Возвратные глаголы действуют «на себя». Возвратные местоимения: me, te, se, nos, os, se '
            '— перед спрягаемым глаголом.\n\n'
            '  lavarse: me lavo, te lavas, se lava, nos lavamos, os laváis, se lavan.\n\n'
            'Распорядок дня: levantarse (вставать), ducharse (принимать душ), acostarse (ложиться). '
            'Me levanto a las siete.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ lavo por la mañana.',
             'options': ['me', 'te', 'se'], 'correct_answer': 'me', 'explanation': '1 л. возвратное: me.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Ella ___ ducha por la noche.',
             'options': ['me', 'te', 'se'], 'correct_answer': 'se', 'explanation': '3 л. возвратное: se.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Nosotros ___ levantamos temprano.',
             'options': ['me', 'nos', 'se'], 'correct_answer': 'nos', 'explanation': '1 л. мн.: nos.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿A qué hora ___ acuestas?',
             'options': ['me', 'te', 'se'], 'correct_answer': 'te', 'explanation': '2 л. ед.: te.'},
        ],
    },
    {
        'n': 12, 'level': 'A1', 'title': 'II спряжение (-er). Падежные отношения',
        'theory': (
            'Глаголы на -er: comer → como, comes, come, comemos, coméis, comen.\n\n'
            'Русские падежи передаются предлогами:\n'
            '• родительный (кого/чего) → de: el libro de María.\n'
            '• дательный (кому) → a: Doy el libro a Juan.\n'
            'Слитный артикль: de + el = del, a + el = al.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (comer) fruta.',
             'options': ['como', 'comes', 'come'], 'correct_answer': 'como', 'explanation': '-er, 1 л.: como.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El libro ___ María.',
             'options': ['a', 'de', 'en'], 'correct_answer': 'de', 'explanation': 'Принадлежность → de.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Doy el regalo ___ Juan.',
             'options': ['de', 'a', 'en'], 'correct_answer': 'a', 'explanation': 'Кому (дат.) → a.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Nosotros ___ (beber) agua.',
             'options': ['bebe', 'bebemos', 'beben'], 'correct_answer': 'bebemos', 'explanation': '-er, 1 л. мн.: bebemos.'},
        ],
    },
    {
        'n': 13, 'level': 'A1', 'title': 'III спряжение (-ir). Mucho и muy. Tener',
        'theory': (
            'Глаголы на -ir: vivir → vivo, vives, vive, vivimos, vivís, viven.\n\n'
            'Важный глагол tener (иметь): tengo, tienes, tiene, tenemos, tenéis, tienen. '
            'Возраст: Tengo veinte años.\n\n'
            'mucho vs muy: muy + прилагательное/наречие (muy bueno, muy bien); '
            'mucho + существительное или после глагола (mucho dinero, trabajo mucho). '
            'mucho согласуется: muchos libros, mucha agua.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (vivir) en Madrid.',
             'options': ['vivo', 'vives', 'vive'], 'correct_answer': 'vivo', 'explanation': '-ir, 1 л.: vivo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El café está ___ caliente.',
             'options': ['mucho', 'muy', 'mucha'], 'correct_answer': 'muy', 'explanation': 'Перед прилагательным → muy.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Tengo ___ trabajo.',
             'options': ['muy', 'mucho', 'muchos'], 'correct_answer': 'mucho',
             'explanation': 'Перед существительным (м. р. ед.) → mucho.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (tener) dos hermanos.',
             'options': ['tengo', 'tienes', 'tiene'], 'correct_answer': 'tengo', 'explanation': 'tener, 1 л.: tengo.'},
        ],
    },
    {
        'n': 14, 'level': 'A1', 'title': 'Повелительное наклонение (Imperativo)',
        'theory': (
            'Утвердительный императив для tú (совпадает с 3 л. ед. настоящего):\n'
            '  hablar → habla, comer → come, vivir → vive.\n'
            'Неправильные для tú: hacer → haz, poner → pon, salir → sal, tener → ten, venir → ven, '
            'decir → di, ir → ve.\n\n'
            'Для usted берётся форма subjuntivo: hable, coma, viva.\n'
            'Глагол querer (хотеть): quiero, quieres, quiere...'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Императив (tú) от hablar:',
             'options': ['habla', 'hable', 'hablas'], 'correct_answer': 'habla', 'explanation': 'tú: habla.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Императив (tú) от hacer:',
             'options': ['hace', 'haz', 'haga'], 'correct_answer': 'haz', 'explanation': 'Неправильный: haz.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Императив (tú) от venir:',
             'options': ['viene', 'ven', 'venga'], 'correct_answer': 'ven', 'explanation': 'Неправильный: ven.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (querer) un café.',
             'options': ['quero', 'quiero', 'quiere'], 'correct_answer': 'quiero', 'explanation': 'querer, 1 л.: quiero.'},
        ],
    },
    {
        'n': 15, 'level': 'A1', 'title': 'Притяжательные прилагательные',
        'theory': (
            'Притяжательные перед существительным: mi (мой), tu (твой), su (его/её/Ваш), '
            'nuestro (наш), vuestro (ваш), su (их).\n'
            'Согласуются в числе (mi/mis, tu/tus), а nuestro/vuestro — и в роде '
            '(nuestra casa, nuestros libros).\n\n'
            '  mi casa, tus amigos, nuestra familia.\n\n'
            'Неправильные глаголы: salir → salgo, oír → oigo, venir → vengo.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '___ casa es grande. (моя)',
             'options': ['Mi', 'Mis', 'Tu'], 'correct_answer': 'Mi', 'explanation': 'мой (ед.) → mi.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ amigos son simpáticos. (твои)',
             'options': ['Tu', 'Tus', 'Su'], 'correct_answer': 'Tus', 'explanation': 'твои (мн.) → tus.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ familia vive en Cádiz. (наша)',
             'options': ['Nuestro', 'Nuestra', 'Nuestros'], 'correct_answer': 'Nuestra',
             'explanation': 'familia — ж. р.: nuestra.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (salir) a las ocho.',
             'options': ['salo', 'salgo', 'sale'], 'correct_answer': 'salgo', 'explanation': 'salir, 1 л.: salgo.'},
        ],
    },
    {
        'n': 16, 'level': 'A1', 'title': 'Ir + a + инфинитив (ближайшее будущее)',
        'theory': (
            'Ближайшее будущее (планы, намерения): ir a + инфинитив.\n'
            '  ir: voy, vas, va, vamos, vais, van.\n'
            '  Voy a estudiar. Vamos a comer. ¿Qué vas a hacer?\n\n'
            'Полезные неправильные глаголы: ser → soy; poner → pongo; traer → traigo.\n'
            'Пример: Esta noche voy a ver una película.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ a estudiar. (ir)',
             'options': ['voy', 'vas', 'va'], 'correct_answer': 'voy', 'explanation': 'ir, 1 л.: voy a estudiar.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Nosotros ___ a comer.',
             'options': ['va', 'vamos', 'van'], 'correct_answer': 'vamos', 'explanation': 'ir, 1 л. мн.: vamos.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿Qué ___ a hacer (tú) hoy?',
             'options': ['voy', 'vas', 'va'], 'correct_answer': 'vas', 'explanation': 'ir, 2 л.: vas a hacer.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (poner) la mesa.',
             'options': ['pono', 'pongo', 'pone'], 'correct_answer': 'pongo', 'explanation': 'poner, 1 л.: pongo.'},
        ],
    },
]
