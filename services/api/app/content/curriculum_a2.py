"""Full hand-authored A2 curriculum (syllabus Lessons 17–29), aligned to syllabus numbers.

Original, license-clean content (grammar facts + own exercises, no copyrighted text). Some
exercises use a cloze / multiple-choice format to build toward proficiency-test tasks. Each
exercise's correct_answer exactly matches one option.
"""

A2_LESSONS = [
    {
        'n': 17, 'level': 'A2', 'title': 'Прошедшее несовершенное (Imperfecto)',
        'theory': (
            'Imperfecto описывает привычки, повторяющиеся действия и фон в прошлом («что делал обычно»).\n\n'
            '• -ar: hablaba, hablabas, hablaba, hablábamos, hablabais, hablaban\n'
            '• -er/-ir: comía, comías... / vivía, vivías...\n\n'
            'Маркеры: antes, siempre, todos los días, cuando era niño.\n'
            'Пример: Cuando era pequeño, jugaba en el parque todos los días.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Antes yo ___ (vivir) en Valencia.',
             'options': ['viví', 'vivía', 'vivo'], 'correct_answer': 'vivía', 'explanation': 'Длительное состояние в прошлом → imperfecto.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Todos los días ella ___ (hablar) con su abuela.',
             'options': ['habló', 'hablaba', 'habla'], 'correct_answer': 'hablaba', 'explanation': 'Привычка → imperfecto.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Cuando ___ niños, comíamos juntos.',
             'options': ['somos', 'éramos', 'fuimos'], 'correct_answer': 'éramos', 'explanation': 'ser в imperfecto — éramos.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'De joven yo ___ mucho deporte.',
             'options': ['hacía', 'hice', 'hago'], 'correct_answer': 'hacía', 'explanation': 'hacer в imperfecto — hacía.'},
        ],
    },
    {
        'n': 18, 'level': 'A2', 'title': 'Imperfecto неправильных и возвратных',
        'theory': (
            'В imperfecto всего три неправильных глагола:\n'
            '• ser → era, eras, era, éramos, erais, eran\n'
            '• ir → iba, ibas, iba, íbamos, ibais, iban\n'
            '• ver → veía, veías, veía...\n\n'
            'Возвратные: me levantaba, se lavaba (местоимение сохраняется).\n'
            'Imperfecto и indefinido часто вместе: Mientras cenábamos (фон), llamó (событие) mi madre.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (ir) al colegio en autobús.',
             'options': ['fui', 'iba', 'voy'], 'correct_answer': 'iba', 'explanation': 'ir в imperfecto — iba.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ella ___ (ser) muy tímida de pequeña.',
             'options': ['fue', 'era', 'es'], 'correct_answer': 'era', 'explanation': 'Описание в прошлом → era.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Nosotros ___ (ver) esa serie cada noche.',
             'options': ['vimos', 'veíamos', 'vemos'], 'correct_answer': 'veíamos', 'explanation': 'ver в imperfecto — veíamos.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Mientras yo ___ (leer), sonó el teléfono.',
             'options': ['leí', 'leía', 'leo'], 'correct_answer': 'leía', 'explanation': 'Фон (imperfecto) + событие (indefinido).'},
        ],
    },
    {
        'n': 19, 'level': 'A2', 'title': 'Вопросы с предлогами. Tanto/tan',
        'theory': (
            'В испанском предлог ставится ПЕРЕД вопросительным словом (нельзя в конце):\n'
            '  ¿Con quién hablas? ¿De qué hablas? ¿A dónde vas?\n\n'
            'Сравнение количества/степени:\n'
            '• tan + прилагательное/наречие: Es tan alto como su padre.\n'
            '• tanto/tanta/tantos/tantas + существительное: Tengo tantos libros como tú.\n'
            '• tanto после глагола: Trabaja tanto como yo.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '¿___ quién hablas? — Con María.',
             'options': ['Con', 'De', 'A'], 'correct_answer': 'Con', 'explanation': 'Ответ «con María» → вопрос ¿Con quién?'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es ___ alto como su hermano.',
             'options': ['tanto', 'tan', 'tanta'], 'correct_answer': 'tan', 'explanation': 'Перед прилагательным → tan.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Tengo ___ libros como tú.',
             'options': ['tan', 'tanto', 'tantos'], 'correct_answer': 'tantos', 'explanation': 'Перед сущ. м. р. мн. → tantos.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿___ qué hablan? — De política.',
             'options': ['A', 'De', 'Con'], 'correct_answer': 'De', 'explanation': 'Ответ «de política» → ¿De qué?'},
        ],
    },
    {
        'n': 20, 'level': 'A2', 'title': 'Местоимения-дополнения. Poder, saber, conocer',
        'theory': (
            'Прямое дополнение: me, te, lo/la, nos, os, los/las. Косвенное: me, te, le, nos, os, les.\n'
            '  ¿Ves a Ana? — Sí, la veo. Le doy un regalo (a él).\n\n'
            'Три важных глагола:\n'
            '• poder (мочь): puedo, puedes, puede...\n'
            '• saber (знать факт/уметь): sé, sabes, sabe... — Sé nadar.\n'
            '• conocer (быть знакомым): conozco, conoces... — Conozco a María.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '¿Ves a Ana? — Sí, ___ veo.',
             'options': ['lo', 'la', 'le'], 'correct_answer': 'la', 'explanation': 'Ana — прямое доп. ж. р. → la.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ nadar muy bien. (я умею)',
             'options': ['Conozco', 'Sé', 'Puedo'], 'correct_answer': 'Sé', 'explanation': 'Уметь → saber: sé nadar.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ a tu hermano. (я знаком)',
             'options': ['Sé', 'Conozco', 'Puedo'], 'correct_answer': 'Conozco', 'explanation': 'Быть знакомым → conocer.'},
            {'exercise_type': 'fill_blank', 'prompt': 'A María ___ doy las gracias.',
             'options': ['la', 'le', 'lo'], 'correct_answer': 'le', 'explanation': 'Косвенное дополнение → le.'},
        ],
    },
    {
        'n': 21, 'level': 'A2', 'title': 'Безличная форма se и согласование',
        'theory': (
            'Безличное/пассивное se выражает обобщённое «делают/говорят»:\n'
            '• Se habla español. En España se cena tarde.\n'
            '• Пассив-рефлексив согласуется с существительным: Se vende piso / Se venden pisos.\n\n'
            'Это удобно, когда деятель не важен: Aquí se trabaja mucho.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Aquí ___ habla español.',
             'options': ['se', 'es', 'está'], 'correct_answer': 'se', 'explanation': 'Безличное se: se habla.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Se ___ pisos. (много квартир)',
             'options': ['vende', 'venden', 'vendo'], 'correct_answer': 'venden', 'explanation': 'Согласование с «pisos» (мн.) → venden.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'En este país ___ cena tarde.',
             'options': ['es', 'se', 'está'], 'correct_answer': 'se', 'explanation': 'Обобщённое действие → se cena.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Se ___ una casa. (одна)',
             'options': ['alquila', 'alquilan', 'alquilo'], 'correct_answer': 'alquila', 'explanation': 'Ед. ч. «una casa» → alquila.'},
        ],
    },
    {
        'n': 22, 'level': 'A2', 'title': 'Сложное прошедшее (Pretérito perfecto)',
        'theory': (
            'Perfecto = haber (presente) + participio. Про недавнее прошлое и опыт «до сих пор».\n'
            '• haber: he, has, ha, hemos, habéis, han\n'
            '• participio: -ar → -ado (hablado), -er/-ir → -ido (comido, vivido)\n\n'
            'Маркеры: hoy, esta semana, ya, todavía no, alguna vez.\n'
            'Пример: Hoy he trabajado mucho. ¿Alguna vez has estado en México?'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Hoy ___ (yo) trabajado mucho.',
             'options': ['he', 'has', 'ha'], 'correct_answer': 'he', 'explanation': 'haber, 1 л.: he trabajado.'},
            {'exercise_type': 'fill_blank', 'prompt': '¿Ya ___ (tú) comido? (perfecto)',
             'options': ['he', 'has', 'ha'], 'correct_answer': 'has', 'explanation': 'haber, 2 л.: has comido.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Participio от «vivir»:',
             'options': ['vivado', 'vivido', 'viviendo'], 'correct_answer': 'vivido', 'explanation': '-ir → -ido: vivido.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Esta semana nosotros ___ estudiado mucho.',
             'options': ['hemos', 'habéis', 'han'], 'correct_answer': 'hemos', 'explanation': 'haber, 1 л. мн.: hemos.'},
        ],
    },
    {
        'n': 23, 'level': 'A2', 'title': 'Perfecto II–III спряжений. Слово todo',
        'theory': (
            'Причастия на -ido у -er/-ir; но есть неправильные: hacer → hecho, ver → visto, '
            'escribir → escrito, decir → dicho, abrir → abierto, poner → puesto, volver → vuelto.\n\n'
            'todo/toda/todos/todas = весь/вся/все; согласуется: todo el día, toda la noche, '
            'todos los días, todas las casas.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'He ___ (hacer) la tarea.',
             'options': ['hacido', 'hecho', 'hacido'], 'correct_answer': 'hecho', 'explanation': 'Неправильное причастие: hecho.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿Has ___ (ver) la película?',
             'options': ['veído', 'visto', 'vido'], 'correct_answer': 'visto', 'explanation': 'ver → visto.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Trabajo ___ el día.',
             'options': ['todo', 'toda', 'todos'], 'correct_answer': 'todo', 'explanation': 'el día — м. р. ед.: todo.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ las casas son blancas.',
             'options': ['Todo', 'Todos', 'Todas'], 'correct_answer': 'Todas', 'explanation': 'las casas — ж. р. мн.: todas.'},
        ],
    },
    {
        'n': 24, 'level': 'A2', 'title': 'Личные местоимения во мн. числе',
        'theory': (
            'Дополнения во мн. числе: прямые nos, os, los/las; косвенные nos, os, les.\n'
            '  Nos ven. Os llamo. Los compro (los libros). Les escribo (a ellos).\n\n'
            'Полезные глаголы: ver (veo, ves, ve...), encontrar (encuentro, o→ue), '
            'pedir (pido, e→i).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '¿Compras los libros? — Sí, ___ compro.',
             'options': ['las', 'los', 'les'], 'correct_answer': 'los', 'explanation': 'los libros — м. р. мн. прямое → los.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'A mis padres ___ escribo a menudo.',
             'options': ['los', 'les', 'las'], 'correct_answer': 'les', 'explanation': 'Косвенное мн. → les.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (encontrar) la solución.',
             'options': ['encontro', 'encuentro', 'encontra'], 'correct_answer': 'encuentro', 'explanation': 'o→ue: encuentro.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (pedir) un café.',
             'options': ['pedo', 'pido', 'pide'], 'correct_answer': 'pido', 'explanation': 'e→i: pido.'},
        ],
    },
    {
        'n': 25, 'level': 'A2', 'title': 'Конструкция de + инфинитив. El que',
        'theory': (
            'de + инфинитив в некоторых оборотах: la hora de comer, acabar de llegar, '
            'tratar de ayudar.\n\n'
            'el que / la que / los que / las que = «тот, кто / который»:\n'
            '  El que estudia, aprueba. Los que llegan tarde esperan.\n\n'
            'Глагол decir (сказать): digo, dices, dice, decimos, decís, dicen.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Acabo ___ llegar.',
             'options': ['de', 'a', 'en'], 'correct_answer': 'de', 'explanation': 'acabar de + инфинитив.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ que estudia, aprueba.',
             'options': ['El', 'Lo', 'Al'], 'correct_answer': 'El', 'explanation': '«Тот, кто» → el que.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (decir) la verdad.',
             'options': ['dico', 'digo', 'dice'], 'correct_answer': 'digo', 'explanation': 'decir, 1 л.: digo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es la hora ___ comer.',
             'options': ['de', 'a', 'para'], 'correct_answer': 'de', 'explanation': 'la hora de + инфинитив.'},
        ],
    },
    {
        'n': 26, 'level': 'A2', 'title': 'Простое прошедшее (Indefinido). Артикль lo',
        'theory': (
            'Indefinido — завершённые однократные действия в прошлом.\n'
            '• -ar: hablé, hablaste, habló, hablamos, hablasteis, hablaron\n'
            '• -er/-ir: comí, comiste, comió, comimos, comisteis, comieron\n\n'
            'Маркеры: ayer, anoche, el año pasado, en 2020.\n\n'
            'Артикль lo + прилагательное = абстракция: lo importante (важное), lo bueno (хорошее).'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Ayer yo ___ (hablar) con el jefe.',
             'options': ['hablo', 'hablé', 'hablaba'], 'correct_answer': 'hablé', 'explanation': 'Завершённое → indefinido: hablé.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Anoche ellos ___ (comer) en casa.',
             'options': ['comen', 'comieron', 'comían'], 'correct_answer': 'comieron', 'explanation': 'Indefinido 3 л. мн.: comieron.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ importante es la salud.',
             'options': ['El', 'La', 'Lo'], 'correct_answer': 'Lo', 'explanation': 'lo + прилагательное = абстракция.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El año pasado ella ___ (viajar) a Perú.',
             'options': ['viaja', 'viajó', 'viajaba'], 'correct_answer': 'viajó', 'explanation': 'Завершённое в прошлом → viajó.'},
        ],
    },
    {
        'n': 27, 'level': 'A2', 'title': 'Indefinido неправильных. Двойное отрицание',
        'theory': (
            'Частые неправильные в indefinido:\n'
            '• estar → estuve...  • tener → tuve...  • dar → di, dio  • ver → vi, vio\n'
            '• ser/ir (совпадают) → fui, fuiste, fue, fuimos, fuisteis, fueron\n\n'
            'Двойное отрицание — норма: No vi a nadie. No dije nada. No fui nunca.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer yo ___ (estar) en casa.',
             'options': ['estuve', 'estaba', 'estoy'], 'correct_answer': 'estuve', 'explanation': 'estar indefinido: estuve.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Él ___ (ir) al médico ayer.',
             'options': ['iba', 'fue', 'va'], 'correct_answer': 'fue', 'explanation': 'ir indefinido: fue.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'No vi ___ en la calle.',
             'options': ['alguien', 'a nadie', 'alguno'], 'correct_answer': 'a nadie', 'explanation': 'Двойное отрицание: no…a nadie.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (tener) un problema ayer.',
             'options': ['tenía', 'tuve', 'tengo'], 'correct_answer': 'tuve', 'explanation': 'tener indefinido: tuve.'},
        ],
    },
    {
        'n': 28, 'level': 'A2', 'title': 'Indefinido: decir, ser, saber, querer',
        'theory': (
            'Ещё неправильные основы indefinido:\n'
            '• decir → dije, dijiste, dijo, dijimos, dijisteis, dijeron\n'
            '• saber → supe, supiste, supo...\n'
            '• querer → quise, quisiste, quiso...\n'
            '• hacer → hice, hiciste, hizo...\n\n'
            'Сводно: эти глаголы имеют особую основу + окончания -e, -iste, -o, -imos, -isteis, -ieron.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Él me ___ (decir) la verdad ayer.',
             'options': ['dice', 'dijo', 'decía'], 'correct_answer': 'dijo', 'explanation': 'decir indefinido: dijo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer yo ___ (hacer) la comida.',
             'options': ['hago', 'hice', 'hacía'], 'correct_answer': 'hice', 'explanation': 'hacer indefinido: hice.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ellos ___ (querer) ayudar.',
             'options': ['quisieron', 'querían', 'quieren'], 'correct_answer': 'quisieron', 'explanation': 'querer indefinido: quisieron.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo lo ___ (saber) ayer.',
             'options': ['sabía', 'supe', 'sé'], 'correct_answer': 'supe', 'explanation': 'saber indefinido: supe (= узнал).'},
        ],
    },
    {
        'n': 29, 'level': 'A2', 'title': 'Два местоимения при глаголе. Уменьшительные',
        'theory': (
            'Когда два местоимения вместе — сначала косвенное, потом прямое: '
            'Me lo das (мне это даёшь). Te la doy.\n'
            'le/les перед lo/la/los/las превращаются в se: Se lo doy (a él/ellos).\n\n'
            'Уменьшительные суффиксы: -ito/-ita (casita, momentito), -illo/-illa. '
            'Придают оттенок «маленький/милый».'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '¿El libro? — ___ lo doy (a ti).',
             'options': ['Te', 'Le', 'Se'], 'correct_answer': 'Te', 'explanation': 'Косвенное «тебе» → te lo doy.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿El regalo a Ana? — ___ lo doy.',
             'options': ['Le', 'Se', 'La'], 'correct_answer': 'Se', 'explanation': 'le + lo → se lo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Уменьшительное от «casa»:',
             'options': ['casona', 'casita', 'casaza'], 'correct_answer': 'casita', 'explanation': 'Суффикс -ita: casita.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Порядок: «мне это» —',
             'options': ['lo me', 'me lo', 'se me'], 'correct_answer': 'me lo', 'explanation': 'Косвенное (me) + прямое (lo): me lo.'},
        ],
    },
]
