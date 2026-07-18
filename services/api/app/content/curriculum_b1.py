"""Hand-authored B1 curriculum, part 1 (syllabus Lessons 30–40), aligned to syllabus numbers.

Original, license-clean content. Cloze / multiple-choice exercises build toward proficiency
tasks. Each correct_answer exactly matches one option.
"""

B1_LESSONS_1 = [
    {
        'n': 30, 'level': 'B1', 'title': 'Согласование времён. Gerundio',
        'theory': (
            'Косвенная речь и согласование: при главном глаголе в прошлом времена в придаточном '
            'сдвигаются. Dice que viene → Dijo que venía. Dice que vendrá → Dijo que vendría.\n\n'
            'Gerundio (деепричастие): -ar → -ando (hablando), -er/-ir → -iendo (comiendo, viviendo). '
            'Неправильные: leyendo, oyendo, durmiendo, pidiendo.\n'
            'Estar + gerundio = действие в процессе: Estoy comiendo.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Gerundio от «hablar»:',
             'options': ['hablando', 'hablendo', 'hablado'], 'correct_answer': 'hablando', 'explanation': '-ar → -ando.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Gerundio от «leer»:',
             'options': ['leiendo', 'leyendo', 'leendo'], 'correct_answer': 'leyendo', 'explanation': 'Неправильное: leyendo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Dijo que ___ al día siguiente. (venir)',
             'options': ['viene', 'venía', 'vendrá'], 'correct_answer': 'venía', 'explanation': 'Сдвиг presente→imperfecto: venía.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Ahora estoy ___ (comer).',
             'options': ['comido', 'comiendo', 'comiando'], 'correct_answer': 'comiendo', 'explanation': 'estar + gerundio: comiendo.'},
        ],
    },
    {
        'n': 31, 'level': 'B1', 'title': 'Слово mismo. Ir в Indefinido',
        'theory': (
            'mismo меняет смысл по позиции:\n'
            '• el mismo libro — тот же самый; yo mismo — я сам.\n'
            '• ahora mismo — прямо сейчас; aquí mismo — прямо здесь.\n\n'
            'ir/ser в indefinido (совпадают): fui, fuiste, fue, fuimos, fuisteis, fueron.\n'
            'quedar + прилагательное = «оказаться/остаться»: La casa quedó vacía.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Es el ___ libro que yo tengo.',
             'options': ['mismo', 'misma', 'mismos'], 'correct_answer': 'mismo', 'explanation': 'el mismo libro — тот же.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ven ahora ___.',
             'options': ['mismo', 'misma', 'propio'], 'correct_answer': 'mismo', 'explanation': 'ahora mismo — прямо сейчас.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer yo ___ (ir) al médico.',
             'options': ['iba', 'fui', 'voy'], 'correct_answer': 'fui', 'explanation': 'ir indefinido: fui.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Lo hice yo ___. (сам)',
             'options': ['mismo', 'propio', 'solo'], 'correct_answer': 'mismo', 'explanation': 'yo mismo — я сам.'},
        ],
    },
    {
        'n': 32, 'level': 'B1', 'title': 'Pluscuamperfecto. Степени сравнения',
        'theory': (
            'Pluscuamperfecto = había + participio: действие ДО другого в прошлом. '
            'Cuando llegué, ya habían salido.\n'
            '  había, habías, había, habíamos, habíais, habían + participio.\n\n'
            'Сравнение: más ... que (больше чем), menos ... que, tan ... como (такой же как). '
            'Особые: mejor (лучше), peor (хуже), mayor (старше), menor (младше).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Cuando llegué, ellos ya ___ salido.',
             'options': ['han', 'habían', 'habrán'], 'correct_answer': 'habían', 'explanation': 'Действие до прошлого → pluscuamperfecto: habían.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ana es ___ alta que María.',
             'options': ['más', 'tan', 'mejor'], 'correct_answer': 'más', 'explanation': 'más … que — сравнение.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Este café es ___ que el otro. (лучше)',
             'options': ['más bueno', 'mejor', 'bien'], 'correct_answer': 'mejor', 'explanation': 'Особая форма: mejor.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ya ___ (comer) cuando llamaste.',
             'options': ['he', 'había', 'habría'], 'correct_answer': 'había', 'explanation': 'había comido — до прошлого.'},
        ],
    },
    {
        'n': 33, 'level': 'B1', 'title': 'Абсолютная превосходная. Mejor, peor, mayor',
        'theory': (
            'Абсолютная превосходная степень (очень + прилагательное) — суффикс -ísimo:\n'
            '  guapo → guapísimo, fácil → facilísimo, rico → riquísimo (орфография c→qu).\n\n'
            'Относительная превосходная: el más ... de: el más alto de la clase.\n'
            'Особые: el mejor, el peor, el mayor, el menor.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Absoluta от «guapo»:',
             'options': ['muy guapo', 'guapísimo', 'más guapo'], 'correct_answer': 'guapísimo', 'explanation': '-ísimo: guapísimo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es el ___ alumno de la clase. (лучший)',
             'options': ['más bueno', 'mejor', 'buenísimo'], 'correct_answer': 'mejor', 'explanation': 'el mejor — лучший.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Absoluta от «rico»:',
             'options': ['ricísimo', 'riquísimo', 'ricoísimo'], 'correct_answer': 'riquísimo', 'explanation': 'c→qu: riquísimo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es la ___ montaña del país. (самая высокая)',
             'options': ['más alta', 'altísima', 'tan alta'], 'correct_answer': 'más alta', 'explanation': 'Относительная: la más alta de.'},
        ],
    },
    {
        'n': 34, 'level': 'B1', 'title': 'Pretérito anterior. Наречия на -mente',
        'theory': (
            'Pretérito anterior (книжн./редкое) = hube + participio: сразу после другого действия. '
            'Apenas hubo terminado, salió. В современной речи чаще заменяют на indefinido.\n\n'
            'Наречия на -mente образуются от прилагательного (женская форма) + -mente:\n'
            '  rápido → rápidamente, fácil → fácilmente, feliz → felizmente.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Наречие от «rápido»:',
             'options': ['rápidomente', 'rápidamente', 'rápidmente'], 'correct_answer': 'rápidamente', 'explanation': 'жен. форма + -mente.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Наречие от «fácil»:',
             'options': ['fácilmente', 'fácilamente', 'facilemente'], 'correct_answer': 'fácilmente', 'explanation': 'fácil + -mente.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Наречие от «lento»:',
             'options': ['lentemente', 'lentamente', 'lentomente'], 'correct_answer': 'lentamente', 'explanation': 'lenta + -mente.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Habla ___. (ясно)',
             'options': ['claramente', 'claromente', 'claromiente'], 'correct_answer': 'claramente', 'explanation': 'clara + -mente.'},
        ],
    },
    {
        'n': 35, 'level': 'B1', 'title': 'Артикль с предлогом de. Soler и servir',
        'theory': (
            'del = de + el (обязательное слияние): la casa del vecino, vengo del trabajo.\n\n'
            'soler + инфинитив = «обычно делать»: Suelo levantarme temprano. '
            '(suelo, sueles, suele, solemos, soléis, suelen — o→ue).\n'
            'servir (e→i): sirvo, sirves, sirve... — servir para (годиться для).\n'
            'poco (мало) vs solo/sólo (только).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Vengo ___ trabajo. (de + el)',
             'options': ['de el', 'del', 'al'], 'correct_answer': 'del', 'explanation': 'de + el = del.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (soler) desayunar a las ocho.',
             'options': ['solo', 'suelo', 'soleo'], 'correct_answer': 'suelo', 'explanation': 'o→ue: suelo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Esto no ___ para nada. (servir)',
             'options': ['sirve', 'serve', 'sirva'], 'correct_answer': 'sirve', 'explanation': 'e→i: sirve.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Tengo ___ tiempo hoy. (мало)',
             'options': ['poco', 'solo', 'pocos'], 'correct_answer': 'poco', 'explanation': 'poco tiempo — мало.'},
        ],
    },
    {
        'n': 36, 'level': 'B1', 'title': 'Будущее время (Futuro imperfecto)',
        'theory': (
            'Futuro = инфинитив + -é, -ás, -á, -emos, -éis, -án: hablaré, comerás, vivirá.\n\n'
            'Неправильные основы: tener → tendr-, poner → pondr-, salir → saldr-, venir → vendr-, '
            'poder → podr-, hacer → har-, decir → dir-, querer → querr-, saber → sabr-.\n'
            'Futuro также выражает предположение: Serán las tres (наверное, три часа).'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Mañana yo ___ (hablar) con ella.',
             'options': ['hablé', 'hablaré', 'hablaba'], 'correct_answer': 'hablaré', 'explanation': 'Futuro 1 л.: hablaré.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Yo ___ (tener) tiempo el lunes.',
             'options': ['teneré', 'tendré', 'tenré'], 'correct_answer': 'tendré', 'explanation': 'tener → tendr-: tendré.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ellos lo ___ (hacer) pronto.',
             'options': ['hacerán', 'harán', 'harémos'], 'correct_answer': 'harán', 'explanation': 'hacer → har-: harán.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿Qué hora es? — ___ las cinco. (предположение)',
             'options': ['Son', 'Serán', 'Fueron'], 'correct_answer': 'Serán', 'explanation': 'Futuro вероятности: serán.'},
        ],
    },
    {
        'n': 37, 'level': 'B1', 'title': 'estar + gerundio и страдательный залог',
        'theory': (
            'estar + gerundio = действие в процессе (сейчас/тогда): Estoy leyendo. Estaba lloviendo.\n\n'
            'Страдательный залог: ser + participio (+ por + деятель): '
            'La casa fue construida por ellos. Причастие согласуется: fue construida, fueron vendidos.\n'
            'В речи чаще используют пассив-рефлексив: Se construyó la casa.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Ahora ___ (yo, estar) trabajando.',
             'options': ['soy', 'estoy', 'está'], 'correct_answer': 'estoy', 'explanation': 'estar + gerundio: estoy.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'La novela ___ escrita en 1990.',
             'options': ['estuvo', 'fue', 'se'], 'correct_answer': 'fue', 'explanation': 'Пассив ser + participio: fue escrita.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Los libros ___ vendidos rápidamente.',
             'options': ['fue', 'fueron', 'estaban'], 'correct_answer': 'fueron', 'explanation': 'Согласование мн.: fueron.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer ___ lloviendo toda la tarde.',
             'options': ['fue', 'estaba', 'era'], 'correct_answer': 'estaba', 'explanation': 'estar + gerundio в прошлом: estaba.'},
        ],
    },
    {
        'n': 38, 'level': 'B1', 'title': 'Притяжательные местоимения-существительные',
        'theory': (
            'Полные (ударные) притяжательные заменяют существительное: mío, tuyo, suyo, nuestro, '
            'vuestro, suyo. Согласуются в роде и числе:\n'
            '  Este libro es mío. La casa es tuya. Los coches son nuestros.\n'
            '  ¿De quién es? — Es el mío / la mía.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Este libro es ___. (мой)',
             'options': ['mío', 'mía', 'míos'], 'correct_answer': 'mío', 'explanation': 'libro — м. р.: mío.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'La casa es ___. (твоя)',
             'options': ['tuyo', 'tuya', 'tuyos'], 'correct_answer': 'tuya', 'explanation': 'casa — ж. р.: tuya.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Los coches son ___. (наши)',
             'options': ['nuestro', 'nuestros', 'nuestras'], 'correct_answer': 'nuestros', 'explanation': 'coches — м. р. мн.: nuestros.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿De quién es? — Es el ___. (мой)',
             'options': ['mío', 'mía', 'mí'], 'correct_answer': 'mío', 'explanation': 'el mío — мой (замена сущ. м. р.).'},
        ],
    },
    {
        'n': 39, 'level': 'B1', 'title': 'Будущее сложное (Futuro perfecto). Al + инфинитив',
        'theory': (
            'Futuro perfecto = habré + participio: действие, завершённое к моменту в будущем '
            '(или догадка о прошлом). Para mañana habré terminado. Habrá salido ya (наверное, уже вышел).\n\n'
            'al + инфинитив = «когда/при»: Al llegar, llamé. (= Cuando llegué)'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Para el viernes ya ___ terminado.',
             'options': ['he', 'habré', 'había'], 'correct_answer': 'habré', 'explanation': 'Futuro perfecto: habré terminado.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ llegar a casa, me duché. (когда)',
             'options': ['Al', 'En', 'De'], 'correct_answer': 'Al', 'explanation': 'al + инфинитив = «когда».'},
            {'exercise_type': 'multiple_choice', 'prompt': 'No contesta; ___ salido ya. (наверное)',
             'options': ['ha', 'habrá', 'había'], 'correct_answer': 'habrá', 'explanation': 'Futuro perfecto вероятности: habrá salido.'},
            {'exercise_type': 'fill_blank', 'prompt': '___ ver la foto, sonreí. (при виде)',
             'options': ['Al', 'En', 'Por'], 'correct_answer': 'Al', 'explanation': 'al + инфинитив: al ver.'},
        ],
    },
    {
        'n': 40, 'level': 'B1', 'title': 'Все времена изъявительного. Безличные формы',
        'theory': (
            'Изъявительное наклонение (indicativo) охватывает: presente, indefinido, imperfecto, '
            'perfecto, pluscuamperfecto, futuro, futuro perfecto — реальные факты.\n\n'
            'Безличные формы haber:\n'
            '• hay (есть) — во всех временах: había, hubo, habrá.\n'
            '• hay que + инфинитив = «нужно/следует» (обобщённо): Hay que estudiar. Había que esperar.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer ___ mucha gente en la plaza.',
             'options': ['hay', 'había', 'habrá'], 'correct_answer': 'había', 'explanation': 'hay в прошлом (фон) → había.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ que estudiar más. (нужно)',
             'options': ['Hay', 'Es', 'Está'], 'correct_answer': 'Hay', 'explanation': 'hay que + инфинитив = нужно.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Mañana ___ una reunión.',
             'options': ['había', 'hay', 'habrá'], 'correct_answer': 'habrá', 'explanation': 'hay в будущем → habrá.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Antes ___ que trabajar los sábados.',
             'options': ['hay', 'había', 'habrá'], 'correct_answer': 'había', 'explanation': 'hay que в прошлом → había que.'},
        ],
    },
]
