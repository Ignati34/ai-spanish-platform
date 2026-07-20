# -*- coding: utf-8 -*-
"""Upgraded C2 lessons 74–84 (full-page theory with translated examples + 3 blocks of 10 items)."""

C2_FULL = [
    {
        'n': 74, 'level': 'C2', 'title': 'Индивидуальное спряжение: ir, hacer, decir, tener',
        'theory': (
            '1. ЗАЧЕМ НА C2. Эти четыре глагола вы спрягаете с уровня A1 — но на C2 пора '
            'владеть ПОЛНОЙ картой каждого: все времена, оба наклонения, императив, '
            'причастие и герундий, без единой заминки.\n\n'
            '2. IR (идти): voy / fui / iba / iré / vaya / fuera / ¡ve! (¡vete! — уходи) / '
            'ido / YENDO.\n'
            '• Ловушки: iba — один из трёх неправильных imperfecto; fui делит форму с ser; '
            'герундий yendo: Voy yendo al centro (я потихоньку двигаюсь в центр); '
            'императив vosotros id, а «уходите» — ¡idos!\n\n'
            '3. HACER (делать): hago / hice (él HIZO — c→z!) / hacía / haré / haga / '
            'hiciera / ¡haz! / HECHO / haciendo.\n'
            '• Hizo un frío terrible (было жутко холодно); ¡Haz la maleta! (собирай '
            'чемодан!); Lo hecho, hecho está (что сделано, то сделано); производные '
            'наследуют всё: deshacer → deshizo, rehacer → rehecho.\n\n'
            '4. DECIR (говорить): digo / dije (ellos DIJERON — без i!) / decía / DIRÉ / '
            'diga / dijera / ¡di! / DICHO / DICIENDO.\n'
            '• Se lo dije y se lo repetiré: te lo diré mil veces (я это сказал и повторю: '
            'скажу тебе тысячу раз); Dicho y hecho (сказано — сделано); ¡Dime! (скажи '
            'мне / слушаю!); del dicho al hecho hay mucho trecho (от слова до дела — '
            'дистанция огромная).\n\n'
            '5. TENER (иметь): tengo / TUVE / tenía / TENDRÉ / tenga / tuviera / ¡TEN! / '
            'tenido / teniendo.\n'
            '• ¡Ten paciencia! (имей терпение!); Tuve que salir corriendo (мне пришлось '
            'убегать); Que tengas suerte (удачи тебе!); производные: mantener → mantuvo, '
            'obtener → obtuvo, contener → contuvo.\n\n'
            '6. МИНИ-ДИАЛОГ:\n'
            '— ¿Qué hiciste ayer? Te llamé y nada. (Что ты вчера делал? Я звонил — и '
            'ничего.)\n'
            '— Tuve un día imposible: fui al banco, hice mil gestiones… (День был '
            'невозможный: сходил в банк, переделал тысячу дел…)\n'
            '— ¡Haberlo dicho! Te habría acompañado. (Так сказал бы! Я бы составил '
            'компанию.)\n'
            '— Tranquilo. Hoy iré otra vez: ven conmigo y ten paciencia en la cola. '
            '(Спокойно. Сегодня пойду снова: идём со мной — и запасись терпением в '
            'очереди.)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Формы ir и hacer', 'exercise_type': 'fill_blank',
             'prompt': 'Ayer ___ (ir, yo) al médico.', 'options': ['fui', 'iba una vez', 'fue'], 'correct_answer': 'fui',
             'translation': 'Вчера я сходил к врачу.', 'explanation': 'indefinido: fui.'},
            {'section': 'Упражнение 1. Формы ir и hacer', 'exercise_type': 'fill_blank',
             'prompt': 'De niño ___ (ir, yo) al pueblo cada verano.', 'options': ['iba', 'fui', 'iré'], 'correct_answer': 'iba',
             'translation': 'В детстве я каждое лето ездил в деревню.', 'explanation': 'imperfecto: iba.'},
            {'section': 'Упражнение 1. Формы ir и hacer', 'exercise_type': 'fill_blank',
             'prompt': 'Герундий ir: Vamos ___ poco a poco.', 'options': ['yendo', 'iendo', 'vayendo'], 'correct_answer': 'yendo',
             'translation': 'Мы потихоньку двигаемся.', 'explanation': 'yendo.'},
            {'section': 'Упражнение 1. Формы ir и hacer', 'exercise_type': 'fill_blank',
             'prompt': '¡ ___ ya, que llegas tarde! (уходи)', 'options': ['Vete', 'Va', 'Ve a te'], 'correct_answer': 'Vete',
             'translation': 'Уходи уже, а то опоздаешь!', 'explanation': 've + te = vete.'},
            {'section': 'Упражнение 1. Формы ir и hacer', 'exercise_type': 'fill_blank',
             'prompt': 'Ayer ___ (hacer, él) un frío terrible.', 'options': ['hizo', 'hació', 'hico'], 'correct_answer': 'hizo',
             'translation': 'Вчера было жутко холодно.', 'explanation': 'hizo (c→z).'},
            {'section': 'Упражнение 1. Формы ir и hacer', 'exercise_type': 'fill_blank',
             'prompt': '¡ ___ la maleta! (собирай)', 'options': ['Haz', 'Hace', 'Haga tú'], 'correct_answer': 'Haz',
             'translation': 'Собирай чемодан!', 'explanation': 'Императив tú: haz.'},
            {'section': 'Упражнение 1. Формы ir и hacer', 'exercise_type': 'fill_blank',
             'prompt': 'Lo ___ , hecho está.', 'options': ['hecho', 'hacido', 'haciendo'], 'correct_answer': 'hecho',
             'translation': 'Что сделано, то сделано.', 'explanation': 'Причастие hecho.'},
            {'section': 'Упражнение 1. Формы ir и hacer', 'exercise_type': 'fill_blank',
             'prompt': 'Quiere que ___ (hacer, yo) el informe hoy.', 'options': ['haga', 'hago', 'hiciera ayer'], 'correct_answer': 'haga',
             'translation': 'Он хочет, чтобы я сделал отчёт сегодня.', 'explanation': 'subjuntivo: haga.'},
            {'section': 'Упражнение 1. Формы ir и hacer', 'exercise_type': 'fill_blank',
             'prompt': 'Deshacer в indefinido (él): ___ la maleta.', 'options': ['deshizo', 'deshació', 'deshacía una vez'], 'correct_answer': 'deshizo',
             'translation': 'Он распаковал чемодан.', 'explanation': 'Производные наследуют: deshizo.'},
            {'section': 'Упражнение 1. Формы ir и hacer', 'exercise_type': 'fill_blank',
             'prompt': 'Mañana ___ (hacer, nosotros) la compra.', 'options': ['haremos', 'haceremos', 'hagamos mañana'], 'correct_answer': 'haremos',
             'translation': 'Завтра мы сделаем покупки.', 'explanation': 'har- + emos.'},
            # 2
            {'section': 'Упражнение 2. Формы decir и tener', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ (decir) la verdad ayer.', 'options': ['dijeron', 'dijieron', 'decieron'], 'correct_answer': 'dijeron',
             'translation': 'Вчера они сказали правду.', 'explanation': 'dijeron — без i!'},
            {'section': 'Упражнение 2. Формы decir и tener', 'exercise_type': 'fill_blank',
             'prompt': 'Te lo ___ (decir, yo) mil veces mañana también.', 'options': ['diré', 'deciré', 'digaré'], 'correct_answer': 'diré',
             'translation': 'Я и завтра скажу тебе это тысячу раз.', 'explanation': 'dir- + é.'},
            {'section': 'Упражнение 2. Формы decir и tener', 'exercise_type': 'fill_blank',
             'prompt': '¡ ___ la verdad! (скажи)', 'options': ['Di', 'Dice', 'Diga tú'], 'correct_answer': 'Di',
             'translation': 'Скажи правду!', 'explanation': 'Императив tú: di.'},
            {'section': 'Упражнение 2. Формы decir и tener', 'exercise_type': 'fill_blank',
             'prompt': '___ y hecho. (сказано — сделано)', 'options': ['Dicho', 'Decido', 'Diciendo'], 'correct_answer': 'Dicho',
             'translation': 'Сказано — сделано.', 'explanation': 'Причастие dicho.'},
            {'section': 'Упражнение 2. Формы decir и tener', 'exercise_type': 'fill_blank',
             'prompt': 'Está ___ tonterías otra vez. (говорит)', 'options': ['diciendo', 'deciendo', 'dichendo'], 'correct_answer': 'diciendo',
             'translation': 'Он опять говорит глупости.', 'explanation': 'Герундий diciendo.'},
            {'section': 'Упражнение 2. Формы decir и tener', 'exercise_type': 'fill_blank',
             'prompt': '___ (tener, yo) que salir corriendo ayer.', 'options': ['Tuve', 'Tení', 'Tenía que una vez'], 'correct_answer': 'Tuve',
             'translation': 'Вчера мне пришлось убегать.', 'explanation': 'tuve.'},
            {'section': 'Упражнение 2. Формы decir и tener', 'exercise_type': 'fill_blank',
             'prompt': '¡ ___ paciencia! (имей)', 'options': ['Ten', 'Tiene', 'Tenga tú'], 'correct_answer': 'Ten',
             'translation': 'Имей терпение!', 'explanation': 'Императив tú: ten.'},
            {'section': 'Упражнение 2. Формы decir и tener', 'exercise_type': 'fill_blank',
             'prompt': 'Que ___ (tener, tú) suerte.', 'options': ['tengas', 'tienes', 'tendrás'], 'correct_answer': 'tengas',
             'translation': 'Удачи тебе!', 'explanation': 'que + subjuntivo: tengas.'},
            {'section': 'Упражнение 2. Формы decir и tener', 'exercise_type': 'fill_blank',
             'prompt': 'Obtener в indefinido (él): ___ el premio.', 'options': ['obtuvo', 'obtenió', 'obtenía una vez'], 'correct_answer': 'obtuvo',
             'translation': 'Он получил премию.', 'explanation': 'obtener → obtuvo.'},
            {'section': 'Упражнение 2. Формы decir и tener', 'exercise_type': 'fill_blank',
             'prompt': 'Mañana ___ (tener, nosotros) más tiempo.', 'options': ['tendremos', 'teneremos', 'tengamos mañana'], 'correct_answer': 'tendremos',
             'translation': 'Завтра у нас будет больше времени.', 'explanation': 'tendr- + emos.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Вчера я много всего сделал.»',
             'options': ['Ayer hice muchas cosas.', 'Ayer hací muchas cosas.', 'Ayer hacía muchas cosas una vez.'],
             'correct_answer': 'Ayer hice muchas cosas.', 'explanation': 'hice.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Скажи мне правду!»',
             'options': ['¡Dime la verdad!', '¡Díceme la verdad!', '¡Di me la verdad a!'],
             'correct_answer': '¡Dime la verdad!', 'explanation': 'di + me = dime.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мне пришлось уйти рано.»',
             'options': ['Tuve que irme temprano.', 'Tení que irme temprano.', 'Tenía que fui temprano.'],
             'correct_answer': 'Tuve que irme temprano.', 'explanation': 'tuve que.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Они мне ничего не сказали.»',
             'options': ['No me dijeron nada.', 'No me dijieron nada.', 'No me decieron nada.'],
             'correct_answer': 'No me dijeron nada.', 'explanation': 'dijeron.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Уходи отсюда!»',
             'options': ['¡Vete de aquí!', '¡Va de aquí!', '¡Ve te de aquí!'],
             'correct_answer': '¡Vete de aquí!', 'explanation': 'vete.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Что сделано, то сделано.»',
             'options': ['Lo hecho, hecho está.', 'Lo hacido, hacido está.', 'Lo haciendo, hecho es.'],
             'correct_answer': 'Lo hecho, hecho está.', 'explanation': 'hecho.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Завтра я скажу тебе всё.»',
             'options': ['Mañana te lo diré todo.', 'Mañana te lo deciré todo.', 'Mañana te lo diga todo.'],
             'correct_answer': 'Mañana te lo diré todo.', 'explanation': 'diré.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Пусть у тебя всё будет хорошо!» (que tengas…)',
             'options': ['¡Que tengas un buen día!', '¡Que tienes un buen día!', '¡Que tendrás un buen día!'],
             'correct_answer': '¡Que tengas un buen día!', 'explanation': 'que tengas.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «В детстве мы ходили в школу пешком.»',
             'options': ['De niños íbamos al colegio a pie.', 'De niños fuimos al colegio a pie cada día.', 'De niños vamos al colegio a pie.'],
             'correct_answer': 'De niños íbamos al colegio a pie.', 'explanation': 'íbamos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он получил (obtener) визу за неделю.»',
             'options': ['Obtuvo el visado en una semana.', 'Obtenió el visado en una semana.', 'Obtenía el visado en una semana una vez.'],
             'correct_answer': 'Obtuvo el visado en una semana.', 'explanation': 'obtuvo.'},
        ],
    },
    {
        'n': 75, 'level': 'C2', 'title': 'Индивидуальное спряжение: poder, poner, venir, salir',
        'theory': (
            '1. PODER (мочь): puedo (o→ue) / PUDE / podía / PODRÉ / pueda / pudiera / — / '
            'podido / PUDIENDO.\n'
            '• No pude venir (я не смог прийти); ¿Podrás terminarlo? (сможешь закончить?); '
            'Puede que llueva (может быть, пойдёт дождь — puede que + subj!); герундий '
            'pudiendo: Pudiendo elegir, elijo el mar (имея выбор, выбираю море).\n\n'
            '2. PONER (класть): pongo / PUSE / ponía / PONDRÉ / ponga / pusiera / ¡PON! / '
            'PUESTO / poniendo.\n'
            '• ¡Pon la mesa! (накрой на стол!); Se puso el abrigo (он надел пальто); '
            '¿Dónde has puesto las llaves? (куда ты положил ключи?); производные: '
            'proponer → propuso, suponer → supuesto (¡por supuesto! — конечно!).\n\n'
            '3. VENIR (приходить): vengo (e→ie: vienes) / VINE / venía / VENDRÉ / venga / '
            'viniera / ¡VEN! / venido / VINIENDO.\n'
            '• ¡Ven aquí! (иди сюда!); Vine, vi y vencí (пришёл, увидел, победил); '
            'El año que viene (в следующем году); ¡Venga! — разговорное «давай!/ну!»: '
            '¡Venga, anímate! (ну давай, взбодрись!).\n\n'
            '4. SALIR (выходить): SALGO / salí (правильный в indefinido!) / salía / '
            'SALDRÉ / salga / saliera / ¡SAL! / salido / saliendo.\n'
            '• Salgo de casa a las ocho (я выхожу из дома в восемь); ¡Sal de ahí! (выйди '
            'оттуда!); Todo saldrá bien (всё получится); salir bien/mal — удаться/не '
            'удаться: El plan salió redondo (план удался на славу).\n\n'
            '5. МИНИ-ШПАРГАЛКА ИМПЕРАТИВОВ-«КОРОТЫШЕК» (все восемь): pon, ven, sal, ten, '
            'haz, di, ve, sé. Запомните хором — и половина разговорных приказов ваша.\n\n'
            '6. МИНИ-ДИАЛОГ:\n'
            '— ¡Venga, sal ya! El taxi está abajo. (Давай, выходи уже! Такси внизу.)\n'
            '— ¡No puedo! No sé dónde puse el pasaporte. (Не могу! Не знаю, куда положил '
            'паспорт.)\n'
            '— ¿No lo pusiste en la mochila? Ven, te ayudo. (Ты не клал его в рюкзак? '
            'Иди сюда, помогу.)\n'
            '— ¡Aquí está! Todo saldrá bien: llegaremos a tiempo. (Вот он! Всё '
            'получится: успеем вовремя.)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Формы poder и poner', 'exercise_type': 'fill_blank',
             'prompt': 'Ayer no ___ (poder, yo) venir.', 'options': ['pude', 'podí', 'podía una vez'], 'correct_answer': 'pude',
             'translation': 'Вчера я не смог прийти.', 'explanation': 'pude.'},
            {'section': 'Упражнение 1. Формы poder и poner', 'exercise_type': 'fill_blank',
             'prompt': '¿ ___ (poder, tú) terminarlo mañana?', 'options': ['Podrás', 'Poderás', 'Puedas mañana'], 'correct_answer': 'Podrás',
             'translation': 'Сможешь закончить это завтра?', 'explanation': 'podr- + ás.'},
            {'section': 'Упражнение 1. Формы poder и poner', 'exercise_type': 'fill_blank',
             'prompt': 'Puede que ___ (llover) esta tarde.', 'options': ['llueva', 'llueve', 'lloverá'], 'correct_answer': 'llueva',
             'translation': 'Может быть, днём пойдёт дождь.', 'explanation': 'puede que + subjuntivo.'},
            {'section': 'Упражнение 1. Формы poder и poner', 'exercise_type': 'fill_blank',
             'prompt': 'Quería que ___ (poder, nosotros) descansar.', 'options': ['pudiéramos', 'podamos', 'podíamos'], 'correct_answer': 'pudiéramos',
             'translation': 'Он хотел, чтобы мы могли отдохнуть.', 'explanation': 'pudieron → pudiéramos.'},
            {'section': 'Упражнение 1. Формы poder и poner', 'exercise_type': 'fill_blank',
             'prompt': '¿Dónde has ___ (poner) las llaves?', 'options': ['puesto', 'ponido', 'poniendo'], 'correct_answer': 'puesto',
             'translation': 'Куда ты положил ключи?', 'explanation': 'Причастие puesto.'},
            {'section': 'Упражнение 1. Формы poder и poner', 'exercise_type': 'fill_blank',
             'prompt': '¡ ___ la mesa, por favor! (накрой)', 'options': ['Pon', 'Pone', 'Ponga tú'], 'correct_answer': 'Pon',
             'translation': 'Накрой на стол, пожалуйста!', 'explanation': 'Императив tú: pon.'},
            {'section': 'Упражнение 1. Формы poder и poner', 'exercise_type': 'fill_blank',
             'prompt': 'Se ___ (poner, él) el abrigo y salió.', 'options': ['puso', 'ponió', 'ponía una vez'], 'correct_answer': 'puso',
             'translation': 'Он надел пальто и вышел.', 'explanation': 'puso.'},
            {'section': 'Упражнение 1. Формы poder и poner', 'exercise_type': 'fill_blank',
             'prompt': 'Proponer в indefinido (ella): ___ un cambio.', 'options': ['propuso', 'proponió', 'proponía una vez'], 'correct_answer': 'propuso',
             'translation': 'Она предложила изменение.', 'explanation': 'proponer → propuso.'},
            {'section': 'Упражнение 1. Формы poder и poner', 'exercise_type': 'fill_blank',
             'prompt': '¡Por ___ ! (конечно!)', 'options': ['supuesto', 'suponido', 'suponiendo'], 'correct_answer': 'supuesto',
             'translation': 'Конечно!', 'explanation': 'por supuesto.'},
            {'section': 'Упражнение 1. Формы poder и poner', 'exercise_type': 'fill_blank',
             'prompt': 'Mañana te ___ (poner, yo) un ejemplo mejor.', 'options': ['pondré', 'poneré', 'ponga mañana'], 'correct_answer': 'pondré',
             'translation': 'Завтра я приведу тебе пример получше.', 'explanation': 'pondr- + é.'},
            # 2
            {'section': 'Упражнение 2. Формы venir и salir', 'exercise_type': 'fill_blank',
             'prompt': '___ (venir, yo) en cuanto pude.', 'options': ['Vine', 'Vení', 'Venía una vez'], 'correct_answer': 'Vine',
             'translation': 'Я пришёл, как только смог.', 'explanation': 'vine.'},
            {'section': 'Упражнение 2. Формы venir и salir', 'exercise_type': 'fill_blank',
             'prompt': '¡ ___ aquí ahora mismo! (иди сюда)', 'options': ['Ven', 'Viene', 'Venga tú'], 'correct_answer': 'Ven',
             'translation': 'Иди сюда сейчас же!', 'explanation': 'Императив tú: ven.'},
            {'section': 'Упражнение 2. Формы venir и salir', 'exercise_type': 'fill_blank',
             'prompt': 'El año que ___ iremos a Chile.', 'options': ['viene', 'venga', 'vendrá que'], 'correct_answer': 'viene',
             'translation': 'В следующем году мы поедем в Чили.', 'explanation': 'el año que viene.'},
            {'section': 'Упражнение 2. Формы venir и salir', 'exercise_type': 'fill_blank',
             'prompt': '¿ ___ (venir, tú) a la cena del sábado?', 'options': ['Vendrás', 'Venirás', 'Vengas'], 'correct_answer': 'Vendrás',
             'translation': 'Придёшь на субботний ужин?', 'explanation': 'vendr- + ás.'},
            {'section': 'Упражнение 2. Формы venir и salir', 'exercise_type': 'fill_blank',
             'prompt': 'Está ___ mucha gente. (приходит — герундий)', 'options': ['viniendo', 'veniendo', 'venido'], 'correct_answer': 'viniendo',
             'translation': 'Приходит много народу.', 'explanation': 'viniendo.'},
            {'section': 'Упражнение 2. Формы venir и salir', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (salir) de casa a las ocho.', 'options': ['salgo', 'salo', 'sálgo de'], 'correct_answer': 'salgo',
             'translation': 'Я выхожу из дома в восемь.', 'explanation': 'salgo.'},
            {'section': 'Упражнение 2. Формы venir и salir', 'exercise_type': 'fill_blank',
             'prompt': '¡ ___ de ahí! (выйди)', 'options': ['Sal', 'Sale', 'Salga tú'], 'correct_answer': 'Sal',
             'translation': 'Выйди оттуда!', 'explanation': 'Императив tú: sal.'},
            {'section': 'Упражнение 2. Формы venir и salir', 'exercise_type': 'fill_blank',
             'prompt': 'Todo ___ (salir) bien, ya verás.', 'options': ['saldrá', 'salirá', 'salga seguro'], 'correct_answer': 'saldrá',
             'translation': 'Всё получится, вот увидишь.', 'explanation': 'saldr- + á.'},
            {'section': 'Упражнение 2. Формы venir и salir', 'exercise_type': 'fill_blank',
             'prompt': 'Espera hasta que ___ (venir, ellos).', 'options': ['vengan', 'vienen', 'vendrán'], 'correct_answer': 'vengan',
             'translation': 'Подожди, пока они не придут.', 'explanation': 'hasta que + vengan.'},
            {'section': 'Упражнение 2. Формы venir и salir', 'exercise_type': 'multiple_choice',
             'prompt': 'Восемь императивов-«коротышек»:', 'options': ['pon, ven, sal, ten, haz, di, ve, sé', 'pone, viene, sale, tiene, hace, dice, va, es', 'ponga, venga, salga, tenga, haga, diga, vaya, sea'],
             'correct_answer': 'pon, ven, sal, ten, haz, di, ve, sé', 'translation': '—', 'explanation': 'Короткие императивы tú.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я не смог тебе позвонить.»',
             'options': ['No pude llamarte.', 'No podí llamarte.', 'No podía llamarte una vez.'],
             'correct_answer': 'No pude llamarte.', 'explanation': 'pude.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Может быть, он придёт позже.» (puede que)',
             'options': ['Puede que venga más tarde.', 'Puede que viene más tarde.', 'Puede que vendrá más tarde.'],
             'correct_answer': 'Puede que venga más tarde.', 'explanation': 'puede que + venga.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Куда ты положил мой телефон?»',
             'options': ['¿Dónde has puesto mi móvil?', '¿Dónde has ponido mi móvil?', '¿Dónde pusiste has mi móvil?'],
             'correct_answer': '¿Dónde has puesto mi móvil?', 'explanation': 'puesto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Надень куртку: холодно.» (ponerse)',
             'options': ['Ponte la chaqueta: hace frío.', 'Pon te la chaqueta: hace frío.', 'Ponete la chaqueta: hace frío.'],
             'correct_answer': 'Ponte la chaqueta: hace frío.', 'explanation': 'pon + te = ponte.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Иди сюда и помоги мне.»',
             'options': ['Ven aquí y ayúdame.', 'Viene aquí y ayúdame.', 'Ven aquí y me ayuda.'],
             'correct_answer': 'Ven aquí y ayúdame.', 'explanation': 'ven + ayúdame.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Она вышла, не сказав ни слова.»',
             'options': ['Salió sin decir una palabra.', 'Salí sin decir una palabra ella.', 'Salía sin dicho una palabra.'],
             'correct_answer': 'Salió sin decir una palabra.', 'explanation': 'salió + sin decir.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Всё выйдет хорошо.»',
             'options': ['Todo saldrá bien.', 'Todo salirá bien.', 'Todo salga bien seguro.'],
             'correct_answer': 'Todo saldrá bien.', 'explanation': 'saldrá.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он предложил (proponer) новый план.»',
             'options': ['Propuso un plan nuevo.', 'Proponió un plan nuevo.', 'Proponía un plan nuevo una vez.'],
             'correct_answer': 'Propuso un plan nuevo.', 'explanation': 'propuso.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я пришёл, как только узнал.»',
             'options': ['Vine en cuanto lo supe.', 'Vení en cuanto lo supe.', 'Venía en cuanto lo sabía.'],
             'correct_answer': 'Vine en cuanto lo supe.', 'explanation': 'vine + supe.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Выйди на минутку, пожалуйста.»',
             'options': ['Sal un momento, por favor.', 'Sale un momento, por favor.', 'Salga tú un momento, por favor.'],
             'correct_answer': 'Sal un momento, por favor.', 'explanation': 'sal.'},
        ],
    },
]

_K2 = [
    {
        'n': 76, 'level': 'C2', 'title': 'Индивидуальное спряжение: caer, oír, traer, ver',
        'theory': (
            '1. CAER (падать): CAIGO / caí, él CAYÓ, ellos CAYERON (i→y между гласными!) / '
            'caía / caeré / caiga / cayera / ¡cae! / CAÍDO / CAYENDO.\n'
            '• Se cayó de la bici (он упал с велосипеда); Están cayendo copos enormes '
            '(падают огромные хлопья); идиома caer bien/mal: Tu amigo me cae genial (твой '
            'друг мне очень симпатичен).\n\n'
            '2. OÍR (слышать): OIGO, OYES, OYE, oímos, oís, OYEN / oí, OYÓ, OYERON / oía / '
            'oiré / OIGA / oyera / ¡OYE! / OÍDO / OYENDO.\n'
            '• ¿Me oyes? (ты меня слышишь?); No oí el despertador (я не услышал '
            'будильник); обращения: ¡Oye! (слушай! — на ты), ¡Oiga! (послушайте! — '
            'подозвать официанта или незнакомца); He oído hablar de él (я о нём слышал).\n\n'
            '3. TRAER (приносить): TRAIGO / TRAJE, trajo, TRAJERON (без i, как dijeron!) / '
            'traía / traeré / TRAIGA / trajera / ¡trae! / TRAÍDO / TRAYENDO.\n'
            '• ¿Qué te traigo del súper? (что тебе принести из супермаркета?); Trajeron '
            'buenas noticias (они принесли хорошие новости); ¡Trae! (дай сюда!); Me trae '
            'sin cuidado (мне это безразлично).\n\n'
            '4. VER (видеть): VEO / VI, VIO (обе без тильды!) / VEÍA (неправильный '
            'imperfecto — третий и последний: iba, era, veía!) / veré / VEA / viera / '
            '¡ve! (совпадает с ir!) / VISTO / viendo.\n'
            '• Lo vi con mis propios ojos (я видел это собственными глазами); De niño '
            'veía dibujos cada tarde (в детстве я каждый вечер смотрел мультики); '
            '¡Nos vemos! (увидимся!); Ya veremos (посмотрим); ¡A ver! (ну-ка!/посмотрим!); '
            'visto: ¿Has visto qué cielo? (видел, какое небо?).\n\n'
            '5. МИНИ-ДИАЛОГ:\n'
            '— ¡Oye! ¿Has visto mis gafas? (Слушай! Ты не видел мои очки?)\n'
            '— Las vi en la cocina. Creo que se cayeron detrás del sofá cuando trajiste '
            'las bolsas. (Видел на кухне. Кажется, они упали за диван, когда ты принёс '
            'пакеты.)\n'
            '— ¡Aquí están! No oí ni el golpe. (Вот они! Я даже стука не услышал.)\n'
            '— Ya veo… ¡Ve al médico a revisarte el oído! (Понятно… Сходи к врачу '
            'проверить слух!)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Формы caer и oír', 'exercise_type': 'fill_blank',
             'prompt': 'El niño se ___ (caer) de la bici ayer.', 'options': ['cayó', 'caió', 'caí'], 'correct_answer': 'cayó',
             'translation': 'Вчера ребёнок упал с велосипеда.', 'explanation': 'i→y: cayó.'},
            {'section': 'Упражнение 1. Формы caer и oír', 'exercise_type': 'fill_blank',
             'prompt': 'Yo no me ___ (caer) nunca esquiando. (presente)', 'options': ['caigo', 'cao', 'cayo'], 'correct_answer': 'caigo',
             'translation': 'Я никогда не падаю на лыжах.', 'explanation': 'caigo.'},
            {'section': 'Упражнение 1. Формы caer и oír', 'exercise_type': 'fill_blank',
             'prompt': 'Están ___ (caer) copos enormes.', 'options': ['cayendo', 'caiendo', 'caído'], 'correct_answer': 'cayendo',
             'translation': 'Падают огромные хлопья.', 'explanation': 'cayendo.'},
            {'section': 'Упражнение 1. Формы caer и oír', 'exercise_type': 'fill_blank',
             'prompt': 'Tu amigo me ___ (caer) genial.', 'options': ['cae', 'cai', 'caiga'], 'correct_answer': 'cae',
             'translation': 'Твой друг мне очень симпатичен.', 'explanation': 'caer bien: me cae.'},
            {'section': 'Упражнение 1. Формы caer и oír', 'exercise_type': 'fill_blank',
             'prompt': '¿Me ___ (oír, tú)? La línea va mal.', 'options': ['oyes', 'oies', 'oís'], 'correct_answer': 'oyes',
             'translation': 'Ты меня слышишь? Связь плохая.', 'explanation': 'oyes.'},
            {'section': 'Упражнение 1. Формы caer и oír', 'exercise_type': 'fill_blank',
             'prompt': 'No ___ (oír, yo) el despertador esta mañana.', 'options': ['oí', 'oyí', 'oigo ayer'], 'correct_answer': 'oí',
             'translation': 'Сегодня утром я не услышал будильник.', 'explanation': 'oí.'},
            {'section': 'Упражнение 1. Формы caer и oír', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ (oír) un ruido extraño.', 'options': ['oyeron', 'oieron', 'oíron'], 'correct_answer': 'oyeron',
             'translation': 'Они услышали странный шум.', 'explanation': 'oyeron.'},
            {'section': 'Упражнение 1. Формы caer и oír', 'exercise_type': 'multiple_choice',
             'prompt': 'Подозвать официанта (на Вы):', 'options': ['¡Oiga!', '¡Oye!', '¡Oyó!'], 'correct_answer': '¡Oiga!',
             'translation': 'Послушайте!', 'explanation': 'usted → ¡oiga!'},
            {'section': 'Упражнение 1. Формы caer и oír', 'exercise_type': 'fill_blank',
             'prompt': 'He ___ (oír) hablar mucho de ti.', 'options': ['oído', 'oyido', 'oyendo'], 'correct_answer': 'oído',
             'translation': 'Я много о тебе слышал.', 'explanation': 'Причастие oído.'},
            {'section': 'Упражнение 1. Формы caer и oír', 'exercise_type': 'fill_blank',
             'prompt': 'Está ___ (oír) música con cascos.', 'options': ['oyendo', 'oiendo', 'oído'], 'correct_answer': 'oyendo',
             'translation': 'Он слушает музыку в наушниках.', 'explanation': 'oyendo.'},
            # 2
            {'section': 'Упражнение 2. Формы traer и ver', 'exercise_type': 'fill_blank',
             'prompt': '¿Qué te ___ (traer, yo) del súper? (presente)', 'options': ['traigo', 'trao', 'trae yo'], 'correct_answer': 'traigo',
             'translation': 'Что тебе принести из супермаркета?', 'explanation': 'traigo.'},
            {'section': 'Упражнение 2. Формы traer и ver', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ (traer) buenas noticias.', 'options': ['trajeron', 'trajieron', 'traieron'], 'correct_answer': 'trajeron',
             'translation': 'Они принесли хорошие новости.', 'explanation': 'trajeron — без i.'},
            {'section': 'Упражнение 2. Формы traer и ver', 'exercise_type': 'fill_blank',
             'prompt': '¿Has ___ (traer) el pan?', 'options': ['traído', 'trajido', 'trayendo'], 'correct_answer': 'traído',
             'translation': 'Ты принёс хлеб?', 'explanation': 'traído.'},
            {'section': 'Упражнение 2. Формы traer и ver', 'exercise_type': 'fill_blank',
             'prompt': 'Quiere que le ___ (traer, yo) un recuerdo.', 'options': ['traiga', 'traigo', 'traje'], 'correct_answer': 'traiga',
             'translation': 'Он хочет, чтобы я привёз ему сувенир.', 'explanation': 'subjuntivo: traiga.'},
            {'section': 'Упражнение 2. Формы traer и ver', 'exercise_type': 'fill_blank',
             'prompt': 'Lo ___ (ver, yo) con mis propios ojos.', 'options': ['vi', 'ví', 'veí'], 'correct_answer': 'vi',
             'translation': 'Я видел это собственными глазами.', 'explanation': 'vi — без тильды!'},
            {'section': 'Упражнение 2. Формы traer и ver', 'exercise_type': 'fill_blank',
             'prompt': 'Ella lo ___ (ver) todo desde el balcón.', 'options': ['vio', 'vió', 'veyó'], 'correct_answer': 'vio',
             'translation': 'Она видела всё с балкона.', 'explanation': 'vio — без тильды!'},
            {'section': 'Упражнение 2. Формы traer и ver', 'exercise_type': 'fill_blank',
             'prompt': 'De niño ___ (ver, yo) dibujos cada tarde.', 'options': ['veía', 'vía', 'vi cada día'], 'correct_answer': 'veía',
             'translation': 'В детстве я каждый вечер смотрел мультики.', 'explanation': 'veía — неправильный imperfecto.'},
            {'section': 'Упражнение 2. Формы traer и ver', 'exercise_type': 'multiple_choice',
             'prompt': 'Три неправильных imperfecto:', 'options': ['iba, era, veía', 'iba, era, hacía', 'era, veía, tenía'], 'correct_answer': 'iba, era, veía',
             'translation': '—', 'explanation': 'Только ir, ser, ver.'},
            {'section': 'Упражнение 2. Формы traer и ver', 'exercise_type': 'fill_blank',
             'prompt': '¿Has ___ (ver) qué cielo?', 'options': ['visto', 'veído', 'viendo'], 'correct_answer': 'visto',
             'translation': 'Видел, какое небо?', 'explanation': 'visto.'},
            {'section': 'Упражнение 2. Формы traer и ver', 'exercise_type': 'fill_blank',
             'prompt': 'Ya ___ (ver, nosotros): no hay prisa. (посмотрим)', 'options': ['veremos', 'vemos ya', 'veamos ya'], 'correct_answer': 'veremos',
             'translation': 'Посмотрим: спешки нет.', 'explanation': 'ya veremos.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я не слышал звонка.»',
             'options': ['No oí el timbre.', 'No oyí el timbre.', 'No oía el timbre una vez.'],
             'correct_answer': 'No oí el timbre.', 'explanation': 'oí.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Стакан упал и разбился.»',
             'options': ['El vaso se cayó y se rompió.', 'El vaso se caió y se rompió.', 'El vaso se cayo y se rompía.'],
             'correct_answer': 'El vaso se cayó y se rompió.', 'explanation': 'se cayó.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Они принесли вино и сыр.»',
             'options': ['Trajeron vino y queso.', 'Trajieron vino y queso.', 'Traieron vino y queso.'],
             'correct_answer': 'Trajeron vino y queso.', 'explanation': 'trajeron.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я видел этот фильм дважды.» (vi)',
             'options': ['Vi esa película dos veces.', 'Ví esa película dos veces.', 'Veía esa película dos veces ayer.'],
             'correct_answer': 'Vi esa película dos veces.', 'explanation': 'vi без тильды.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Раньше мы виделись каждую неделю.»',
             'options': ['Antes nos veíamos cada semana.', 'Antes nos vimos cada semana.', 'Antes nos vemos cada semana.'],
             'correct_answer': 'Antes nos veíamos cada semana.', 'explanation': 'veíamos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Слушай, принеси мне воды, пожалуйста.»',
             'options': ['Oye, tráeme agua, por favor.', 'Oiga tú, tráeme agua, por favor.', 'Oye, tráigame agua, por favor.'],
             'correct_answer': 'Oye, tráeme agua, por favor.', 'explanation': 'oye + tráeme.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Твоя сестра мне очень симпатична.» (caer bien)',
             'options': ['Tu hermana me cae muy bien.', 'Tu hermana me cae muy bueno.', 'Tu hermana me cayó muy bien es.'],
             'correct_answer': 'Tu hermana me cae muy bien.', 'explanation': 'me cae bien.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Увидимся в субботу!»',
             'options': ['¡Nos vemos el sábado!', '¡Nos veremos en el sábado!', '¡Vémonos el sábado!'],
             'correct_answer': '¡Nos vemos el sábado!', 'explanation': 'nos vemos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Она услышала шаги и обернулась.»',
             'options': ['Oyó pasos y se volvió.', 'Oió pasos y se volvió.', 'Oía pasos y se volvía una vez.'],
             'correct_answer': 'Oyó pasos y se volvió.', 'explanation': 'oyó.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Посмотрим, что скажет врач.»',
             'options': ['Ya veremos qué dice el médico.', 'Ya vemos qué dice el médico mañana.', 'Ya veamos qué diga el médico.'],
             'correct_answer': 'Ya veremos qué dice el médico.', 'explanation': 'ya veremos.'},
        ],
    },
    {
        'n': 77, 'level': 'C2', 'title': 'Управление прилагательных: lleno de, capaz de, dispuesto a',
        'theory': (
            '1. ПРИНЦИП. Как и глаголы (уроки 70–71), прилагательные тянут за собой СВОЙ '
            'предлог. Учим связками.\n\n'
            '2. ПРИЛАГАТЕЛЬНЫЕ С DE:\n'
            '• lleno de — полный чего-л.: La sala está llena de gente (зал полон народу);\n'
            '• capaz de — способный на: Es capaz de todo (он способен на всё);\n'
            '• harto de — сыт по горло: Estoy harto de esperar (мне надоело ждать);\n'
            '• responsable de — ответственный за: Eres responsable de tu equipo;\n'
            '• orgulloso de, seguro de, culpable de, digno de (достойный): un final digno '
            'de la película.\n\n'
            '3. FÁCIL/DIFÍCIL DE + ИНФИНИТИВ — важная конструкция:\n'
            '• Este texto es fácil de leer (этот текст легко читать) — у объекта есть '
            'свойство;\n'
            '• сравните безличное: Es fácil leer este texto (легко читать этот текст) — '
            'без de!\n'
            '• Es una persona difícil de convencer (его трудно убедить). Imposible de '
            'explicar (невозможно объяснить).\n\n'
            '4. ПРИЛАГАТЕЛЬНЫЕ С A:\n'
            '• dispuesto a — готовый (настроенный): Estoy dispuesto a ayudar (я готов '
            'помочь);\n'
            '• acostumbrado a — привыкший к: acostumbrado al calor;\n'
            '• parecido a / similar a — похожий на: Es muy parecido a su padre (он очень '
            'похож на отца).\n\n'
            '5. С EN, CON, PARA:\n'
            '• interesado en — заинтересованный в: interesados en colaborar;\n'
            '• el primero/el último en — первый/последний в: Fuiste el primero en llegar '
            '(ты пришёл первым);\n'
            '• rico en — богатый чем-л.: rico en vitaminas;\n'
            '• contento con — довольный: contento con el resultado; amable con — любезный '
            'с; casado con — женатый на; compatible con;\n'
            '• bueno/malo para — полезный/вредный для: El deporte es bueno para la salud; '
            'listo para — готовый к (собранный): ¡Listos para salir!\n\n'
            '6. МИНИ-ДИАЛОГ:\n'
            '— ¿Estás listo para la mudanza? (Ты готов к переезду?)\n'
            '— Casi. Aunque estoy harto de cajas: el piso está lleno de ellas. (Почти. '
            'Хотя коробки мне надоели: квартира ими полна.)\n'
            '— Yo estoy dispuesto a echarte una mano. (Я готов подсобить.)\n'
            '— ¡Gracias! Eres digno de un monumento. Y el primero en ofrecerte, por '
            'cierto. (Спасибо! Ты достоин памятника. И, кстати, первый, кто предложил.)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Прилагательные с de', 'exercise_type': 'multiple_choice',
             'prompt': 'La sala está llena ___ gente.', 'options': ['de', 'con', 'por'], 'correct_answer': 'de',
             'translation': 'Зал полон народу.', 'explanation': 'lleno de.'},
            {'section': 'Упражнение 1. Прилагательные с de', 'exercise_type': 'multiple_choice',
             'prompt': 'Es capaz ___ todo.', 'options': ['de', 'a', 'para'], 'correct_answer': 'de',
             'translation': 'Он способен на всё.', 'explanation': 'capaz de.'},
            {'section': 'Упражнение 1. Прилагательные с de', 'exercise_type': 'multiple_choice',
             'prompt': 'Estoy harto ___ esperar.', 'options': ['de', 'por', 'con'], 'correct_answer': 'de',
             'translation': 'Мне надоело ждать.', 'explanation': 'harto de.'},
            {'section': 'Упражнение 1. Прилагательные с de', 'exercise_type': 'multiple_choice',
             'prompt': 'Eres responsable ___ tu equipo.', 'options': ['de', 'por', 'para'], 'correct_answer': 'de',
             'translation': 'Ты отвечаешь за свою команду.', 'explanation': 'responsable de.'},
            {'section': 'Упражнение 1. Прилагательные с de', 'exercise_type': 'multiple_choice',
             'prompt': 'Un final digno ___ la película.', 'options': ['de', 'a', 'para'], 'correct_answer': 'de',
             'translation': 'Финал, достойный фильма.', 'explanation': 'digno de.'},
            {'section': 'Упражнение 1. Прилагательные с de', 'exercise_type': 'multiple_choice',
             'prompt': 'Este texto es fácil ___ leer.', 'options': ['de', 'a', 'para'], 'correct_answer': 'de',
             'translation': 'Этот текст легко читать.', 'explanation': 'fácil de + инф.'},
            {'section': 'Упражнение 1. Прилагательные с de', 'exercise_type': 'multiple_choice',
             'prompt': 'Безличное: Es fácil ___ este texto.', 'options': ['leer', 'de leer', 'a leer'], 'correct_answer': 'leer',
             'translation': 'Легко читать этот текст.', 'explanation': 'Безличное — без de.'},
            {'section': 'Упражнение 1. Прилагательные с de', 'exercise_type': 'multiple_choice',
             'prompt': 'Es una persona difícil ___ convencer.', 'options': ['de', 'a', 'en'], 'correct_answer': 'de',
             'translation': 'Его трудно убедить.', 'explanation': 'difícil de.'},
            {'section': 'Упражнение 1. Прилагательные с de', 'exercise_type': 'multiple_choice',
             'prompt': 'No se siente culpable ___ nada.', 'options': ['de', 'por siempre', 'a'], 'correct_answer': 'de',
             'translation': 'Он не чувствует себя виноватым ни в чём.', 'explanation': 'culpable de.'},
            {'section': 'Упражнение 1. Прилагательные с de', 'exercise_type': 'multiple_choice',
             'prompt': 'Estoy seguro ___ su honestidad.', 'options': ['de', 'en', 'con'], 'correct_answer': 'de',
             'translation': 'Я уверен в его честности.', 'explanation': 'seguro de.'},
            # 2
            {'section': 'Упражнение 2. A, en, con или para?', 'exercise_type': 'multiple_choice',
             'prompt': 'Estoy dispuesto ___ ayudar.', 'options': ['a', 'de', 'en'], 'correct_answer': 'a',
             'translation': 'Я готов помочь.', 'explanation': 'dispuesto a.'},
            {'section': 'Упражнение 2. A, en, con или para?', 'exercise_type': 'multiple_choice',
             'prompt': 'Está acostumbrado ___ calor.', 'options': ['al', 'del', 'con el'], 'correct_answer': 'al',
             'translation': 'Он привык к жаре.', 'explanation': 'acostumbrado a + el.'},
            {'section': 'Упражнение 2. A, en, con или para?', 'exercise_type': 'multiple_choice',
             'prompt': 'Es muy parecido ___ su padre.', 'options': ['a', 'de', 'con'], 'correct_answer': 'a',
             'translation': 'Он очень похож на отца.', 'explanation': 'parecido a.'},
            {'section': 'Упражнение 2. A, en, con или para?', 'exercise_type': 'multiple_choice',
             'prompt': 'Estamos interesados ___ colaborar.', 'options': ['en', 'de', 'a'], 'correct_answer': 'en',
             'translation': 'Мы заинтересованы в сотрудничестве.', 'explanation': 'interesado en.'},
            {'section': 'Упражнение 2. A, en, con или para?', 'exercise_type': 'multiple_choice',
             'prompt': 'Fuiste el primero ___ llegar.', 'options': ['en', 'a', 'de'], 'correct_answer': 'en',
             'translation': 'Ты пришёл первым.', 'explanation': 'el primero en.'},
            {'section': 'Упражнение 2. A, en, con или para?', 'exercise_type': 'multiple_choice',
             'prompt': 'La naranja es rica ___ vitaminas.', 'options': ['en', 'de', 'con'], 'correct_answer': 'en',
             'translation': 'Апельсин богат витаминами.', 'explanation': 'rico en.'},
            {'section': 'Упражнение 2. A, en, con или para?', 'exercise_type': 'multiple_choice',
             'prompt': 'Estoy contento ___ el resultado.', 'options': ['con', 'de siempre', 'por'], 'correct_answer': 'con',
             'translation': 'Я доволен результатом.', 'explanation': 'contento con.'},
            {'section': 'Упражнение 2. A, en, con или para?', 'exercise_type': 'multiple_choice',
             'prompt': 'El deporte es bueno ___ la salud.', 'options': ['para', 'por', 'a'], 'correct_answer': 'para',
             'translation': 'Спорт полезен для здоровья.', 'explanation': 'bueno para.'},
            {'section': 'Упражнение 2. A, en, con или para?', 'exercise_type': 'multiple_choice',
             'prompt': '¡Listos ___ salir!', 'options': ['para', 'a', 'de'], 'correct_answer': 'para',
             'translation': 'Готовы к выходу!', 'explanation': 'listo para.'},
            {'section': 'Упражнение 2. A, en, con или para?', 'exercise_type': 'multiple_choice',
             'prompt': 'Es muy amable ___ los clientes.', 'options': ['con', 'a', 'de'], 'correct_answer': 'con',
             'translation': 'Он очень любезен с клиентами.', 'explanation': 'amable con.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Холодильник полон еды.»',
             'options': ['La nevera está llena de comida.', 'La nevera está llena con comida.', 'La nevera está llena por comida.'],
             'correct_answer': 'La nevera está llena de comida.', 'explanation': 'llena de.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мне надоели твои отговорки.» (harto de)',
             'options': ['Estoy harto de tus excusas.', 'Estoy harto con tus excusas.', 'Soy harto de tus excusas.'],
             'correct_answer': 'Estoy harto de tus excusas.', 'explanation': 'harto de.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Она способна решить это сама.»',
             'options': ['Es capaz de resolverlo sola.', 'Es capaz a resolverlo sola.', 'Está capaz de resolverlo sola.'],
             'correct_answer': 'Es capaz de resolverlo sola.', 'explanation': 'capaz de.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это слово трудно произнести.» (difícil de)',
             'options': ['Esta palabra es difícil de pronunciar.', 'Esta palabra es difícil a pronunciar.', 'Esta palabra es difícil pronunciar de.'],
             'correct_answer': 'Esta palabra es difícil de pronunciar.', 'explanation': 'difícil de + инф.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы готовы подписать контракт.» (dispuestos)',
             'options': ['Estamos dispuestos a firmar el contrato.', 'Estamos dispuestos de firmar el contrato.', 'Estamos dispuestos en firmar el contrato.'],
             'correct_answer': 'Estamos dispuestos a firmar el contrato.', 'explanation': 'dispuesto a.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Ты очень похожа на свою мать.»',
             'options': ['Eres muy parecida a tu madre.', 'Eres muy parecida de tu madre.', 'Eres muy parecida con tu madre.'],
             'correct_answer': 'Eres muy parecida a tu madre.', 'explanation': 'parecida a.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он был последним, кто ушёл.» (el último en)',
             'options': ['Fue el último en irse.', 'Fue el último a irse.', 'Fue el último de irse.'],
             'correct_answer': 'Fue el último en irse.', 'explanation': 'el último en.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я привык вставать рано.» (acostumbrado)',
             'options': ['Estoy acostumbrado a madrugar.', 'Estoy acostumbrado de madrugar.', 'Estoy acostumbrado en madrugar.'],
             'correct_answer': 'Estoy acostumbrado a madrugar.', 'explanation': 'acostumbrado a.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Курение вредно для здоровья.»',
             'options': ['Fumar es malo para la salud.', 'Fumar es malo por la salud.', 'Fumar es malo a la salud.'],
             'correct_answer': 'Fumar es malo para la salud.', 'explanation': 'malo para.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы очень довольны новым домом.»',
             'options': ['Estamos muy contentos con la casa nueva.', 'Estamos muy contentos de en la casa nueva.', 'Somos muy contentos con la casa nueva.'],
             'correct_answer': 'Estamos muy contentos con la casa nueva.', 'explanation': 'contento con.'},
        ],
    },
]
C2_FULL = C2_FULL + _K2

_K3 = [
    {
        'n': 78, 'level': 'C2', 'title': 'Subjuntivo и indicativo: смена смысла при выборе наклонения',
        'theory': (
            '1. ВЫСШИЙ ПИЛОТАЖ. На C2 наклонение — не правило, а ИНСТРУМЕНТ СМЫСЛА: одна '
            'и та же фраза с indicativo и subjuntivo значит разное.\n\n'
            '2. DECIR QUE — сообщение или приказ:\n'
            '• + indicativo = передаёт факт: Dice que vienes mañana (он говорит, что ты '
            'завтра приезжаешь);\n'
            '• + subjuntivo = передаёт приказ: Dice que vengas mañana (он велит, чтобы ты '
            'завтра пришёл).\n\n'
            '3. SENTIR QUE — чувство или сожаление:\n'
            '• Siento que algo va mal (я чувствую, что что-то не так);\n'
            '• Siento que no puedas venir (мне жаль, что ты не можешь прийти).\n\n'
            '4. COMPRENDER QUE — констатация или сочувствие:\n'
            '• Comprendo que estás cansado (я вижу/понимаю как факт, что ты устал);\n'
            '• Comprendo que estés cansado (по-человечески понимаю тебя — немудрено '
            'устать).\n\n'
            '5. DE MANERA/MODO QUE — следствие или цель:\n'
            '• + indicativo = так что (итог): Llovía, de manera que nos quedamos (шёл '
            'дождь, так что мы остались);\n'
            '• + subjuntivo = так, чтобы (цель): Explícalo de manera que todos lo '
            'entiendan (объясни так, чтобы все поняли).\n\n'
            '6. MIENTRAS — время или условие:\n'
            '• + indicativo = пока (одновременность): Mientras yo cocino, tú pones la '
            'mesa;\n'
            '• + subjuntivo = пока/если только (условие на будущее): Mientras no cambies '
            'de actitud, no hablaremos (пока не сменишь тон, разговора не будет).\n\n'
            '7. NO PORQUE + SUBJUNTIVO — отвергаем причину: No lo hago porque me paguen, '
            'sino porque quiero (я делаю это не потому, что мне платят, а потому что '
            'хочу). Сравните: Lo hago porque me pagan (делаю, потому что платят — факт).\n\n'
            '8. EL HECHO DE QUE — «тот факт, что» обычно тянет subjuntivo: El hecho de '
            'que no llamara me preocupa (то, что он не позвонил, меня беспокоит).\n\n'
            '9. МИНИ-ДИАЛОГ:\n'
            '— Papá dice que estudies más. (Папа велит, чтобы ты больше занимался.)\n'
            '— ¿Y también dice que estudio poco? (А он ещё и говорит, что я мало '
            'занимаюсь?)\n'
            '— Comprendo que estés molesto, pero lo dice de manera que mejores. (Понимаю '
            'твою досаду, но он говорит это, чтобы ты стал лучше.)\n'
            '— Ya. Mientras no me lo diga a gritos, lo escucharé. (Ладно. Пока он не '
            'говорит это криком — я буду слушать.)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Что меняет наклонение?', 'exercise_type': 'multiple_choice',
             'prompt': 'Dice que ___ mañana. (сообщает факт)', 'options': ['vienes', 'vengas', 'vinieras'], 'correct_answer': 'vienes',
             'translation': 'Он говорит, что ты завтра приезжаешь.', 'explanation': 'Факт → indicativo.'},
            {'section': 'Упражнение 1. Что меняет наклонение?', 'exercise_type': 'multiple_choice',
             'prompt': 'Dice que ___ mañana. (велит)', 'options': ['vengas', 'vienes', 'vendrás'], 'correct_answer': 'vengas',
             'translation': 'Он велит, чтобы ты завтра пришёл.', 'explanation': 'Приказ → subjuntivo.'},
            {'section': 'Упражнение 1. Что меняет наклонение?', 'exercise_type': 'multiple_choice',
             'prompt': 'Siento que algo ___ mal. (чувствую)', 'options': ['va', 'vaya', 'fuera'], 'correct_answer': 'va',
             'translation': 'Я чувствую, что что-то не так.', 'explanation': 'Ощущение-факт → va.'},
            {'section': 'Упражнение 1. Что меняет наклонение?', 'exercise_type': 'multiple_choice',
             'prompt': 'Siento que no ___ venir. (сожалею)', 'options': ['puedas', 'puedes', 'podrás'], 'correct_answer': 'puedas',
             'translation': 'Мне жаль, что ты не можешь прийти.', 'explanation': 'Сожаление → puedas.'},
            {'section': 'Упражнение 1. Что меняет наклонение?', 'exercise_type': 'multiple_choice',
             'prompt': 'Comprendo que ___ cansado. (сочувствую: немудрено)', 'options': ['estés', 'estás', 'estarás'], 'correct_answer': 'estés',
             'translation': 'Понимаю тебя — немудрено устать.', 'explanation': 'Сочувствие → estés.'},
            {'section': 'Упражнение 1. Что меняет наклонение?', 'exercise_type': 'multiple_choice',
             'prompt': 'Llovía, de manera que nos ___ en casa. (итог)', 'options': ['quedamos', 'quedáramos', 'quedemos'], 'correct_answer': 'quedamos',
             'translation': 'Шёл дождь, так что мы остались дома.', 'explanation': 'Следствие → indicativo.'},
            {'section': 'Упражнение 1. Что меняет наклонение?', 'exercise_type': 'multiple_choice',
             'prompt': 'Explícalo de manera que todos lo ___ . (цель)', 'options': ['entiendan', 'entienden', 'entenderán'], 'correct_answer': 'entiendan',
             'translation': 'Объясни так, чтобы все поняли.', 'explanation': 'Цель → subjuntivo.'},
            {'section': 'Упражнение 1. Что меняет наклонение?', 'exercise_type': 'multiple_choice',
             'prompt': 'Mientras no ___ de actitud, no hablaremos. (условие)', 'options': ['cambies', 'cambias', 'cambiarás'], 'correct_answer': 'cambies',
             'translation': 'Пока не сменишь тон, разговора не будет.', 'explanation': 'Условие → cambies.'},
            {'section': 'Упражнение 1. Что меняет наклонение?', 'exercise_type': 'multiple_choice',
             'prompt': 'Mientras yo ___ , tú descansas. (одновременность)', 'options': ['cocino', 'cocine', 'cocinara'], 'correct_answer': 'cocino',
             'translation': 'Пока я готовлю, ты отдыхаешь.', 'explanation': 'Время-факт → cocino.'},
            {'section': 'Упражнение 1. Что меняет наклонение?', 'exercise_type': 'multiple_choice',
             'prompt': 'El hecho de que no ___ me preocupa. (llamar, él)', 'options': ['llamara', 'llamó seguro', 'llama'], 'correct_answer': 'llamara',
             'translation': 'То, что он не позвонил, меня беспокоит.', 'explanation': 'el hecho de que + subj.'},
            # 2
            {'section': 'Упражнение 2. Причина и её отрицание', 'exercise_type': 'multiple_choice',
             'prompt': 'Lo hago porque me ___ . (факт: платят)', 'options': ['pagan', 'paguen', 'pagaran'], 'correct_answer': 'pagan',
             'translation': 'Я делаю это, потому что мне платят.', 'explanation': 'porque + indicativo.'},
            {'section': 'Упражнение 2. Причина и её отрицание', 'exercise_type': 'multiple_choice',
             'prompt': 'No lo hago porque me ___ , sino porque quiero.', 'options': ['paguen', 'pagan', 'pagarán'], 'correct_answer': 'paguen',
             'translation': 'Я делаю это не потому, что платят, а потому что хочу.', 'explanation': 'no porque + subj.'},
            {'section': 'Упражнение 2. Причина и её отрицание', 'exercise_type': 'multiple_choice',
             'prompt': 'Te llamo no porque ___ ayuda, sino para saludarte.', 'options': ['necesite', 'necesito', 'necesitaré'], 'correct_answer': 'necesite',
             'translation': 'Звоню не потому, что нужна помощь, а поздороваться.', 'explanation': 'no porque + necesite.'},
            {'section': 'Упражнение 2. Причина и её отрицание', 'exercise_type': 'multiple_choice',
             'prompt': 'Mi madre dice que la ___ más a menudo. (велит звонить)', 'options': ['llame', 'llamo', 'llamaré'], 'correct_answer': 'llame',
             'translation': 'Мама велит звонить ей почаще.', 'explanation': 'Приказ → llame.'},
            {'section': 'Упражнение 2. Причина и её отрицание', 'exercise_type': 'multiple_choice',
             'prompt': 'La radio dice que mañana ___ . (сообщает: будет дождь)', 'options': ['lloverá', 'llueva', 'lloviera'], 'correct_answer': 'lloverá',
             'translation': 'По радио говорят, что завтра будет дождь.', 'explanation': 'Сообщение → indicativo.'},
            {'section': 'Упражнение 2. Причина и её отрицание', 'exercise_type': 'multiple_choice',
             'prompt': 'Habla más alto, de modo que te ___ todos. (чтобы)', 'options': ['oigan', 'oyen', 'oirán'], 'correct_answer': 'oigan',
             'translation': 'Говори громче, чтобы тебя все слышали.', 'explanation': 'Цель → oigan.'},
            {'section': 'Упражнение 2. Причина и её отрицание', 'exercise_type': 'multiple_choice',
             'prompt': 'Perdí el tren, de modo que ___ en taxi. (итог)', 'options': ['fui', 'fuera', 'vaya'], 'correct_answer': 'fui',
             'translation': 'Я опоздал на поезд, так что поехал на такси.', 'explanation': 'Итог → fui.'},
            {'section': 'Упражнение 2. Причина и её отрицание', 'exercise_type': 'multiple_choice',
             'prompt': 'Comprendo que la decisión ___ difícil. (констатирую факт)', 'options': ['es', 'sea', 'fuera'], 'correct_answer': 'es',
             'translation': 'Я понимаю (вижу), что решение трудное.', 'explanation': 'Констатация → es.'},
            {'section': 'Упражнение 2. Причина и её отрицание', 'exercise_type': 'multiple_choice',
             'prompt': 'Mientras ___ fiebre, quédate en cama. (пока есть — впредь)', 'options': ['tengas', 'tienes', 'tendrás'], 'correct_answer': 'tengas',
             'translation': 'Пока есть температура — оставайся в постели.', 'explanation': 'mientras + subj.'},
            {'section': 'Упражнение 2. Причина и её отрицание', 'exercise_type': 'multiple_choice',
             'prompt': 'Siento que este proyecto ___ un error. (интуиция)', 'options': ['es', 'sea', 'fuera'], 'correct_answer': 'es',
             'translation': 'Я чувствую, что этот проект — ошибка.', 'explanation': 'Ощущение → es.'},
            # 3
            {'section': 'Упражнение 3. Переведите, выбрав наклонение', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он говорит, что ты много работаешь.» (сообщает)',
             'options': ['Dice que trabajas mucho.', 'Dice que trabajes mucho.', 'Dice que trabajaras mucho.'],
             'correct_answer': 'Dice que trabajas mucho.', 'explanation': 'Факт → trabajas.'},
            {'section': 'Упражнение 3. Переведите, выбрав наклонение', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он велит, чтобы ты работал больше.»',
             'options': ['Dice que trabajes más.', 'Dice que trabajas más.', 'Dice que trabajarás más.'],
             'correct_answer': 'Dice que trabajes más.', 'explanation': 'Приказ → trabajes.'},
            {'section': 'Упражнение 3. Переведите, выбрав наклонение', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мне жаль, что ты уезжаешь.»',
             'options': ['Siento que te vayas.', 'Siento que te vas seguro.', 'Siento irte que.'],
             'correct_answer': 'Siento que te vayas.', 'explanation': 'Сожаление → vayas.'},
            {'section': 'Упражнение 3. Переведите, выбрав наклонение', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Понимаю, что тебе страшно (по-человечески).»',
             'options': ['Comprendo que tengas miedo.', 'Comprendo que tienes miedo un hecho.', 'Comprendo tener miedo que.'],
             'correct_answer': 'Comprendo que tengas miedo.', 'explanation': 'Сочувствие → tengas.'},
            {'section': 'Упражнение 3. Переведите, выбрав наклонение', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Говори медленно, чтобы тебя понимали.» (de manera que)',
             'options': ['Habla despacio, de manera que te entiendan.', 'Habla despacio, de manera que te entienden.', 'Habla despacio, de manera que te entenderán.'],
             'correct_answer': 'Habla despacio, de manera que te entiendan.', 'explanation': 'Цель → entiendan.'},
            {'section': 'Упражнение 3. Переведите, выбрав наклонение', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Было поздно, так что мы взяли такси.»',
             'options': ['Era tarde, de manera que cogimos un taxi.', 'Era tarde, de manera que cogiéramos un taxi.', 'Era tarde, de manera que cojamos un taxi.'],
             'correct_answer': 'Era tarde, de manera que cogimos un taxi.', 'explanation': 'Итог → cogimos.'},
            {'section': 'Упражнение 3. Переведите, выбрав наклонение', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Пока ты живёшь здесь, будешь соблюдать правила.» (условие)',
             'options': ['Mientras vivas aquí, seguirás las normas.', 'Mientras vives aquí, seguirás las normas.', 'Mientras vivirás aquí, sigues las normas.'],
             'correct_answer': 'Mientras vivas aquí, seguirás las normas.', 'explanation': 'Условие → vivas.'},
            {'section': 'Упражнение 3. Переведите, выбрав наклонение', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я учу испанский не потому, что это модно, а потому что люблю его.»',
             'options': ['Estudio español no porque esté de moda, sino porque me encanta.', 'Estudio español no porque está de moda, sino porque me encanta.', 'Estudio español no porque estará de moda, sino porque me encanta.'],
             'correct_answer': 'Estudio español no porque esté de moda, sino porque me encanta.', 'explanation': 'no porque + esté.'},
            {'section': 'Упражнение 3. Переведите, выбрав наклонение', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Тот факт, что он молчит, меня беспокоит.»',
             'options': ['El hecho de que calle me preocupa.', 'El hecho de que calla seguro me preocupa.', 'El hecho de callar que me preocupa.'],
             'correct_answer': 'El hecho de que calle me preocupa.', 'explanation': 'el hecho de que + calle.'},
            {'section': 'Упражнение 3. Переведите, выбрав наклонение', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Чувствую, что мы на верном пути.» (интуиция-факт)',
             'options': ['Siento que vamos por buen camino.', 'Siento que vayamos por buen camino.', 'Siento ir que por buen camino.'],
             'correct_answer': 'Siento que vamos por buen camino.', 'explanation': 'Ощущение → vamos.'},
        ],
    },
    {
        'n': 79, 'level': 'C2', 'title': 'Маркеры дискурса и регистр: от бара до делового письма',
        'theory': (
            '1. РЕГИСТР — умение звучать «к месту». Одна мысль, два костюма:\n'
            '• бар: Bueno, pues al final no voy, es que estoy hecho polvo, ¿sabes? (ну, '
            'короче, я в итоге не иду — я просто никакой, понимаешь?);\n'
            '• письмо: Lamento comunicarle que no podré asistir (с сожалением сообщаю '
            'Вам, что не смогу присутствовать).\n\n'
            '2. РАЗГОВОРНЫЕ МАРКЕРЫ (смазка живой речи):\n'
            '• bueno — ну, ладно; pues — ну, так; o sea — то есть; es que — дело в том, '
            'что (универсальное оправдание): Es que no tenía batería;\n'
            '• vale — окей; venga — давай!/ну!; anda — да ладно!/иди ты!; ¡hombre!/'
            '¡mujer! — ну ты что! (не «мужчина/женщина»!);\n'
            '• ¿sabes?, ¿no?, ¿verdad? — да?, правда? (поиск отклика); a ver — ну-ка, '
            'посмотрим; en plan — типа (молодёжное): Fue en plan raro (было типа '
            'странно).\n\n'
            '3. ФОРМАЛЬНЫЕ МАРКЕРЫ (доклад, письмо, статья):\n'
            '• en efecto — действительно; cabe destacar que — стоит подчеркнуть; '
            'conviene señalar que — следует отметить;\n'
            '• dicho de otro modo — иными словами; a mi juicio — на мой взгляд; en lo '
            'que respecta a — в том, что касается; no cabe duda de que — нет сомнений, '
            'что; si bien — хотя (книжное): Si bien el plan es caro, es viable.\n\n'
            '4. ЭТИКЕТ ПИСЬМА:\n'
            '• формально: Estimado señor García: … Atentamente / Un cordial saludo;\n'
            '• дружески: Querido Pablo: / ¡Hola, Ana! … Un abrazo / Un beso / ¡Nos '
            'vemos!;\n'
            '• смягчители просьб: Le agradecería que me enviara… (я был бы Вам '
            'признателен, если бы Вы прислали…); ¿Te importaría echarme una mano? (тебя '
            'не затруднит подсобить?).\n\n'
            '5. ВЫБОР TÚ/USTED: usted — незнакомые старшие, клиенты, официальные '
            'ситуации; tú — почти всё остальное в Испании (в Латинской Америке usted '
            'шире). Переход на «ты» предлагают: Podemos tutearnos, ¿no? (можем на «ты», '
            'да?).\n\n'
            '6. МИНИ-ДИАЛОГ (два регистра одной просьбы):\n'
            '— Oye, ¿me pasas el informe? Es que lo necesito ya. (Слушай, скинешь отчёт? '
            'Просто он мне нужен уже.)\n'
            '— ¡Venga, claro! Ahora mismo. (Да конечно! Прямо сейчас.)\n'
            '…y por escrito: (…и письменно:)\n'
            '— Estimada señora Ruiz: Le agradecería que me enviara el informe a la mayor '
            'brevedad. Atentamente, I. Petrov. (Уважаемая сеньора Руис! Буду признателен '
            'за скорейшую отправку отчёта. С уважением, И. Петров.)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Разговорные маркеры', 'exercise_type': 'multiple_choice',
             'prompt': '«Дело в том, что…» (оправдание):', 'options': ['es que', 'cabe destacar', 'en efecto'], 'correct_answer': 'es que',
             'translation': 'дело в том, что…', 'explanation': 'es que — разговорное.'},
            {'section': 'Упражнение 1. Разговорные маркеры', 'exercise_type': 'multiple_choice',
             'prompt': '¡ ___ , anímate! (давай!)', 'options': ['Venga', 'Conviene', 'Asimismo'], 'correct_answer': 'Venga',
             'translation': 'Ну давай, взбодрись!', 'explanation': '¡venga!'},
            {'section': 'Упражнение 1. Разговорные маркеры', 'exercise_type': 'multiple_choice',
             'prompt': '— ¿Me ayudas? — ¡ ___ , claro! (окей)', 'options': ['Vale', 'En efecto', 'No obstante'], 'correct_answer': 'Vale',
             'translation': '— Поможешь? — Окей, конечно!', 'explanation': 'vale.'},
            {'section': 'Упражнение 1. Разговорные маркеры', 'exercise_type': 'multiple_choice',
             'prompt': '¡ ___ ! ¡Cuánto tiempo sin verte! (ну ты что / здорово)', 'options': ['Hombre', 'Señor', 'Usted'], 'correct_answer': 'Hombre',
             'translation': 'Ого! Сколько лет, сколько зим!', 'explanation': '¡hombre! — восклицание.'},
            {'section': 'Упражнение 1. Разговорные маркеры', 'exercise_type': 'multiple_choice',
             'prompt': 'No fui, ___ estaba agotado. (просто/дело в том что)', 'options': ['es que', 'si bien', 'a mi juicio'], 'correct_answer': 'es que',
             'translation': 'Я не пошёл — просто был вымотан.', 'explanation': 'es que.'},
            {'section': 'Упражнение 1. Разговорные маркеры', 'exercise_type': 'multiple_choice',
             'prompt': 'Молодёжное «типа»:', 'options': ['en plan', 'en efecto', 'en lo que respecta'], 'correct_answer': 'en plan',
             'translation': 'типа', 'explanation': 'en plan.'},
            {'section': 'Упражнение 1. Разговорные маркеры', 'exercise_type': 'multiple_choice',
             'prompt': '___ , ¿empezamos? (ну-ка / посмотрим)', 'options': ['A ver', 'Cabe destacar', 'Dicho de otro modo'], 'correct_answer': 'A ver',
             'translation': 'Ну-ка, начнём?', 'explanation': 'a ver.'},
            {'section': 'Упражнение 1. Разговорные маркеры', 'exercise_type': 'multiple_choice',
             'prompt': '¡ ___ ! ¿En serio te ha tocado la lotería? (да ладно!)', 'options': ['Anda', 'Conviene', 'Atentamente'], 'correct_answer': 'Anda',
             'translation': 'Да ладно! Ты серьёзно выиграл в лотерею?', 'explanation': '¡anda!'},
            {'section': 'Упражнение 1. Разговорные маркеры', 'exercise_type': 'multiple_choice',
             'prompt': 'Hace frío, ¿ ___ ? (поиск отклика)', 'options': ['verdad', 'en efecto', 'cabe'], 'correct_answer': 'verdad',
             'translation': 'Холодно, правда?', 'explanation': '¿verdad?'},
            {'section': 'Упражнение 1. Разговорные маркеры', 'exercise_type': 'multiple_choice',
             'prompt': '___ , pues nada, me voy. (ну / ладно)', 'options': ['Bueno', 'No cabe duda', 'Asimismo'], 'correct_answer': 'Bueno',
             'translation': 'Ну ладно, я пошёл.', 'explanation': 'bueno, pues nada.'},
            # 2
            {'section': 'Упражнение 2. Формальный регистр и письма', 'exercise_type': 'multiple_choice',
             'prompt': '«Стоит подчеркнуть, что…» (доклад):', 'options': ['Cabe destacar que', 'Es que', 'En plan'], 'correct_answer': 'Cabe destacar que',
             'translation': 'стоит подчеркнуть, что…', 'explanation': 'Формальный маркер.'},
            {'section': 'Упражнение 2. Формальный регистр и письма', 'exercise_type': 'multiple_choice',
             'prompt': '«Иными словами»:', 'options': ['dicho de otro modo', 'o sea tío', 'venga'], 'correct_answer': 'dicho de otro modo',
             'translation': 'иными словами', 'explanation': 'Формальный аналог o sea.'},
            {'section': 'Упражнение 2. Формальный регистр и письма', 'exercise_type': 'multiple_choice',
             'prompt': '«На мой взгляд» (статья):', 'options': ['a mi juicio', 'en plan yo', 'es que yo'], 'correct_answer': 'a mi juicio',
             'translation': 'на мой взгляд', 'explanation': 'a mi juicio.'},
            {'section': 'Упражнение 2. Формальный регистр и письма', 'exercise_type': 'multiple_choice',
             'prompt': '___ el plan es caro, es viable. (хотя — книжно)', 'options': ['Si bien', 'Es que', 'Venga'], 'correct_answer': 'Si bien',
             'translation': 'Хотя план дорог, он осуществим.', 'explanation': 'si bien + indicativo.'},
            {'section': 'Упражнение 2. Формальный регистр и письма', 'exercise_type': 'multiple_choice',
             'prompt': 'Начало формального письма:', 'options': ['Estimado señor García:', '¡Hola García!', 'Oye, García:'], 'correct_answer': 'Estimado señor García:',
             'translation': 'Уважаемый сеньор Гарсия!', 'explanation': 'Estimado + двоеточие.'},
            {'section': 'Упражнение 2. Формальный регистр и письма', 'exercise_type': 'multiple_choice',
             'prompt': 'Формальная подпись:', 'options': ['Atentamente', 'Un beso', '¡Nos vemos!'], 'correct_answer': 'Atentamente',
             'translation': 'С уважением', 'explanation': 'Atentamente.'},
            {'section': 'Упражнение 2. Формальный регистр и письма', 'exercise_type': 'multiple_choice',
             'prompt': 'Дружеская подпись:', 'options': ['Un abrazo', 'Atentamente', 'Le saluda cordialmente'], 'correct_answer': 'Un abrazo',
             'translation': 'Обнимаю', 'explanation': 'Un abrazo.'},
            {'section': 'Упражнение 2. Формальный регистр и письма', 'exercise_type': 'multiple_choice',
             'prompt': 'Вежливая просьба в письме: Le agradecería que me ___ el contrato.', 'options': ['enviara', 'envías', 'envía'], 'correct_answer': 'enviara',
             'translation': 'Буду признателен, если Вы пришлёте контракт.', 'explanation': 'agradecería que + -ara.'},
            {'section': 'Упражнение 2. Формальный регистр и письма', 'exercise_type': 'multiple_choice',
             'prompt': 'Предложить перейти на «ты»:', 'options': ['Podemos tutearnos, ¿no?', 'Háblame de usted.', '¡Oiga, señor!'], 'correct_answer': 'Podemos tutearnos, ¿no?',
             'translation': 'Можем на «ты», да?', 'explanation': 'tutearse.'},
            {'section': 'Упражнение 2. Формальный регистр и письма', 'exercise_type': 'multiple_choice',
             'prompt': '«Нет сомнений, что…»:', 'options': ['No cabe duda de que', 'Anda que', 'En plan que'], 'correct_answer': 'No cabe duda de que',
             'translation': 'нет сомнений, что…', 'explanation': 'no cabe duda de que.'},
            # 3
            {'section': 'Упражнение 3. Переведите в нужном регистре', 'exercise_type': 'translation',
             'prompt': 'Переведите (другу): «Слушай, дело в том, что я не смогу прийти.»',
             'options': ['Oye, es que no voy a poder venir.', 'Estimado amigo: lamento comunicarle mi ausencia.', 'Cabe destacar que no vendré.'],
             'correct_answer': 'Oye, es que no voy a poder venir.', 'explanation': 'Разговорный регистр.'},
            {'section': 'Упражнение 3. Переведите в нужном регистре', 'exercise_type': 'translation',
             'prompt': 'Переведите (в деловом письме): «С сожалением сообщаю Вам, что не смогу присутствовать.»',
             'options': ['Lamento comunicarle que no podré asistir.', 'Es que no puedo ir, ¿vale?', 'Bueno, pues no voy.'],
             'correct_answer': 'Lamento comunicarle que no podré asistir.', 'explanation': 'Формальный регистр.'},
            {'section': 'Упражнение 3. Переведите в нужном регистре', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Тебя не затруднит помочь мне с переездом?»',
             'options': ['¿Te importaría ayudarme con la mudanza?', '¿Le agradecería ayudarme con la mudanza?', '¡Ayúdame con la mudanza, venga ya!'],
             'correct_answer': '¿Te importaría ayudarme con la mudanza?', 'explanation': 'Смягчитель ¿te importaría?'},
            {'section': 'Упражнение 3. Переведите в нужном регистре', 'exercise_type': 'translation',
             'prompt': 'Переведите (доклад): «Следует отметить, что расходы выросли.»',
             'options': ['Conviene señalar que los gastos han aumentado.', 'O sea, en plan, gastamos más.', 'Es que gastamos un montón, ¿sabes?'],
             'correct_answer': 'Conviene señalar que los gastos han aumentado.', 'explanation': 'conviene señalar que.'},
            {'section': 'Упражнение 3. Переведите в нужном регистре', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Да ладно! Не может быть!»',
             'options': ['¡Anda! ¡No puede ser!', '¡En efecto! ¡No puede ser!', '¡Atentamente! ¡No puede ser!'],
             'correct_answer': '¡Anda! ¡No puede ser!', 'explanation': '¡anda!'},
            {'section': 'Упражнение 3. Переведите в нужном регистре', 'exercise_type': 'translation',
             'prompt': 'Переведите (статья): «Хотя проект амбициозен, он осуществим.» (si bien)',
             'options': ['Si bien el proyecto es ambicioso, es viable.', 'En plan, el proyecto es ambicioso pero va.', 'Venga, el proyecto es ambicioso, ¿vale?'],
             'correct_answer': 'Si bien el proyecto es ambicioso, es viable.', 'explanation': 'si bien.'},
            {'section': 'Упражнение 3. Переведите в нужном регистре', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Ну ладно, до завтра, обнимаю!» (другу)',
             'options': ['Bueno, hasta mañana, ¡un abrazo!', 'No obstante, hasta mañana, atentamente.', 'Cabe destacar: hasta mañana.'],
             'correct_answer': 'Bueno, hasta mañana, ¡un abrazo!', 'explanation': 'Дружеский регистр.'},
            {'section': 'Упражнение 3. Переведите в нужном регистре', 'exercise_type': 'translation',
             'prompt': 'Переведите (письмо): «Буду признателен, если Вы ответите как можно скорее.»',
             'options': ['Le agradecería que respondiera a la mayor brevedad.', 'Responde ya, venga.', 'O sea, contesta rápido, ¿vale?'],
             'correct_answer': 'Le agradecería que respondiera a la mayor brevedad.', 'explanation': 'agradecería que + respondiera.'},
            {'section': 'Упражнение 3. Переведите в нужном регистре', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Действительно, данные это подтверждают.» (формально)',
             'options': ['En efecto, los datos lo confirman.', 'Pues sí, en plan, los datos van bien.', 'Anda, los datos lo dicen, tío.'],
             'correct_answer': 'En efecto, los datos lo confirman.', 'explanation': 'en efecto.'},
            {'section': 'Упражнение 3. Переведите в нужном регистре', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Можем перейти на „ты“, если хочешь.»',
             'options': ['Podemos tutearnos, si quieres.', 'Podemos hablarnos de usted, si quieres.', 'Podemos decirnos tú a usted, si quieres.'],
             'correct_answer': 'Podemos tutearnos, si quieres.', 'explanation': 'tutearse.'},
        ],
    },
]
C2_FULL = C2_FULL + _K3
