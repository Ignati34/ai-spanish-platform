# -*- coding: utf-8 -*-
"""Upgraded B1 lessons 30–36 (full-page theory with translated examples + 3 blocks of 10 items)."""

B1_FULL = [
    {
        'n': 30, 'level': 'B1', 'title': 'Согласование времён. Gerundio',
        'theory': (
            '1. GERUNDIO — испанское «деепричастие» («делая, работая»). Образование:\n'
            '• -ar → -ando: hablar → hablando (говоря), trabajar → trabajando;\n'
            '• -er/-ir → -iendo: comer → comiendo, vivir → viviendo.\n'
            'Неправильные формы: leer → leyendo, oír → oyendo, ir → yendo, dormir → durmiendo, '
            'pedir → pidiendo, decir → diciendo, venir → viniendo, seguir → siguiendo.\n\n'
            '2. ESTAR + GERUNDIO — действие, происходящее прямо сейчас (аналог английского '
            'Continuous):\n'
            '• ¿Qué estás haciendo? — Estoy preparando la cena (что ты делаешь? — готовлю ужин);\n'
            '• Los niños están durmiendo (дети спят);\n'
            '• No puedo salir: está lloviendo (не могу выйти: идёт дождь).\n'
            'В прошлом — estar в imperfecto: Estaba leyendo cuando llamaste (я читал, когда ты '
            'позвонил). Местоимения — перед estar или приклеенными к герундию: Lo estoy leyendo '
            '= Estoy leyéndolo.\n\n'
            '3. SEGUIR + GERUNDIO — «продолжать делать»: Sigo estudiando español (я продолжаю '
            'учить испанский). ¿Sigues trabajando en el banco? (ты всё ещё работаешь в банке?)\n\n'
            '4. СОГЛАСОВАНИЕ ВРЕМЁН (concordancia de tiempos). Время придаточного зависит от '
            'времени главного глагола:\n'
            '• Главный в НАСТОЯЩЕМ → придаточное как есть: Dice que trabaja mucho (он говорит, '
            'что много работает). Dice que trabajará mañana (что будет работать завтра);\n'
            '• Главный в ПРОШЕДШЕМ → времена сдвигаются назад: presente → imperfecto: '
            'Dijo que trabajaba mucho (он сказал, что много работает/работал);\n'
            '  Me explicó que no podía venir (он объяснил мне, что не может прийти);\n'
            '  Pensaba que vivías en Madrid (я думал, что ты живёшь в Мадриде).\n'
            'Это основа косвенной речи — полную систему сдвигов пройдём на C1, здесь главное '
            'правило: «сказал, что + imperfecto».\n\n'
            '5. МИНИ-ДИАЛОГ:\n'
            '— ¿Qué estás haciendo? (Что ты делаешь?)\n'
            '— Estoy escribiendo un mensaje a Marta. Dice que sigue buscando piso. (Пишу '
            'сообщение Марте. Она говорит, что всё ещё ищет квартиру.)\n'
            '— ¿No dijo que ya tenía uno? (Разве она не говорила, что у неё уже есть?)\n'
            '— Sí, pero al final no lo aguantó: era ruidosísimo. (Да, но в итоге она его не '
            'вынесла: он был жутко шумный.)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Образуйте gerundio и estar + gerundio', 'exercise_type': 'fill_blank',
             'prompt': '¿Qué estás ___ (hacer)?', 'options': ['haciendo', 'hacendo', 'haciendo a'], 'correct_answer': 'haciendo',
             'translation': 'Что ты делаешь?', 'explanation': 'hacer → haciendo.'},
            {'section': 'Упражнение 1. Образуйте gerundio и estar + gerundio', 'exercise_type': 'fill_blank',
             'prompt': 'Estoy ___ (preparar) la cena.', 'options': ['preparando', 'prepariendo', 'preparado'], 'correct_answer': 'preparando',
             'translation': 'Я готовлю ужин.', 'explanation': '-ar → -ando.'},
            {'section': 'Упражнение 1. Образуйте gerundio и estar + gerundio', 'exercise_type': 'fill_blank',
             'prompt': 'Los niños están ___ (dormir).', 'options': ['durmiendo', 'dormiendo', 'dormando'], 'correct_answer': 'durmiendo',
             'translation': 'Дети спят.', 'explanation': 'o→u: durmiendo.'},
            {'section': 'Упражнение 1. Образуйте gerundio и estar + gerundio', 'exercise_type': 'fill_blank',
             'prompt': 'Está ___ (llover): coge el paraguas.', 'options': ['lloviendo', 'llovando', 'llovido'], 'correct_answer': 'lloviendo',
             'translation': 'Идёт дождь: возьми зонт.', 'explanation': '-er → -iendo.'},
            {'section': 'Упражнение 1. Образуйте gerundio и estar + gerundio', 'exercise_type': 'fill_blank',
             'prompt': 'Ella está ___ (leer) una novela.', 'options': ['leyendo', 'leiendo', 'leendo'], 'correct_answer': 'leyendo',
             'translation': 'Она читает роман.', 'explanation': 'leer → leyendo.'},
            {'section': 'Упражнение 1. Образуйте gerundio и estar + gerundio', 'exercise_type': 'fill_blank',
             'prompt': '¿Me estás ___ (oír)?', 'options': ['oyendo', 'oiendo', 'oyendo a'], 'correct_answer': 'oyendo',
             'translation': 'Ты меня слышишь (слушаешь)?', 'explanation': 'oír → oyendo.'},
            {'section': 'Упражнение 1. Образуйте gerundio и estar + gerundio', 'exercise_type': 'fill_blank',
             'prompt': 'El camarero está ___ (pedir) la comanda.', 'options': ['pidiendo', 'pediendo', 'pedando'], 'correct_answer': 'pidiendo',
             'translation': 'Официант принимает заказ.', 'explanation': 'e→i: pidiendo.'},
            {'section': 'Упражнение 1. Образуйте gerundio и estar + gerundio', 'exercise_type': 'fill_blank',
             'prompt': '___ leyendo cuando llamaste. (я читал)', 'options': ['Estaba', 'Estuve', 'Estoy'], 'correct_answer': 'Estaba',
             'translation': 'Я читал, когда ты позвонил.', 'explanation': 'Фон → estaba + gerundio.'},
            {'section': 'Упражнение 1. Образуйте gerundio и estar + gerundio', 'exercise_type': 'fill_blank',
             'prompt': '¿Sigues ___ (trabajar) en el banco?', 'options': ['trabajando', 'trabajar', 'trabajado'], 'correct_answer': 'trabajando',
             'translation': 'Ты всё ещё работаешь в банке?', 'explanation': 'seguir + gerundio.'},
            {'section': 'Упражнение 1. Образуйте gerundio и estar + gerundio', 'exercise_type': 'multiple_choice',
             'prompt': '«Я это читаю (сейчас)» — оба верных варианта:', 'options': ['Lo estoy leyendo / Estoy leyéndolo', 'Estoy lo leyendo / Leyendo lo estoy'], 'correct_answer': 'Lo estoy leyendo / Estoy leyéndolo',
             'translation': 'Я это (сейчас) читаю.', 'explanation': 'Местоимение перед estar или к герундию.'},
            # 2
            {'section': 'Упражнение 2. Согласование времён (dice que / dijo que)', 'exercise_type': 'multiple_choice',
             'prompt': 'Dice que ___ mucho. (сейчас, работает)', 'options': ['trabaja', 'trabajaba', 'trabajó'], 'correct_answer': 'trabaja',
             'translation': 'Он говорит, что много работает.', 'explanation': 'Главный в настоящем → presente.'},
            {'section': 'Упражнение 2. Согласование времён (dice que / dijo que)', 'exercise_type': 'multiple_choice',
             'prompt': 'Dijo que ___ mucho.', 'options': ['trabajaba', 'trabaja', 'trabajará'], 'correct_answer': 'trabajaba',
             'translation': 'Он сказал, что много работает.', 'explanation': 'dijo → imperfecto.'},
            {'section': 'Упражнение 2. Согласование времён (dice que / dijo que)', 'exercise_type': 'multiple_choice',
             'prompt': 'Me explicó que no ___ venir.', 'options': ['podía', 'puede', 'pudo siempre'], 'correct_answer': 'podía',
             'translation': 'Он объяснил мне, что не может прийти.', 'explanation': 'explicó → podía.'},
            {'section': 'Упражнение 2. Согласование времён (dice que / dijo que)', 'exercise_type': 'multiple_choice',
             'prompt': 'Pensaba que ___ en Madrid. (ты живёшь)', 'options': ['vivías', 'vives', 'viviste'], 'correct_answer': 'vivías',
             'translation': 'Я думал, что ты живёшь в Мадриде.', 'explanation': 'pensaba → vivías.'},
            {'section': 'Упражнение 2. Согласование времён (dice que / dijo que)', 'exercise_type': 'multiple_choice',
             'prompt': 'María dice que ___ cansada. (сейчас)', 'options': ['está', 'estaba', 'estuvo'], 'correct_answer': 'está',
             'translation': 'Мария говорит, что устала.', 'explanation': 'dice → presente.'},
            {'section': 'Упражнение 2. Согласование времён (dice que / dijo que)', 'exercise_type': 'multiple_choice',
             'prompt': 'María dijo que ___ cansada.', 'options': ['estaba', 'está', 'estará'], 'correct_answer': 'estaba',
             'translation': 'Мария сказала, что устала.', 'explanation': 'dijo → imperfecto.'},
            {'section': 'Упражнение 2. Согласование времён (dice que / dijo que)', 'exercise_type': 'multiple_choice',
             'prompt': 'Creía que el examen ___ fácil.', 'options': ['era', 'es', 'fue ser'], 'correct_answer': 'era',
             'translation': 'Я считал, что экзамен лёгкий.', 'explanation': 'creía → era.'},
            {'section': 'Упражнение 2. Согласование времён (dice que / dijo que)', 'exercise_type': 'multiple_choice',
             'prompt': 'Dijo que ___ buscando piso. (всё ещё ищет)', 'options': ['seguía', 'sigue', 'siguió siempre'], 'correct_answer': 'seguía',
             'translation': 'Она сказала, что всё ещё ищет квартиру.', 'explanation': 'dijo → seguía + gerundio.'},
            {'section': 'Упражнение 2. Согласование времён (dice que / dijo que)', 'exercise_type': 'multiple_choice',
             'prompt': 'Me contó que ___ ganas de verte. (что очень хочет)', 'options': ['tenía', 'tiene', 'tuvo una vez'], 'correct_answer': 'tenía',
             'translation': 'Он рассказал мне, что ему не терпится тебя увидеть.', 'explanation': 'contó → tenía ganas.'},
            {'section': 'Упражнение 2. Согласование времён (dice que / dijo que)', 'exercise_type': 'multiple_choice',
             'prompt': 'Siempre dice que la práctica ___ lo importante.', 'options': ['es', 'era', 'fue'], 'correct_answer': 'es',
             'translation': 'Он всегда говорит, что практика — это главное.', 'explanation': 'dice → presente.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Что ты делаешь? — Готовлю ужин.»',
             'options': ['¿Qué estás haciendo? — Estoy preparando la cena.', '¿Qué haces estar? — Preparo estando la cena.', '¿Qué estás hacer? — Estoy preparar la cena.'],
             'correct_answer': '¿Qué estás haciendo? — Estoy preparando la cena.', 'explanation': 'estar + gerundio.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Идёт дождь.» (прямо сейчас)',
             'options': ['Está lloviendo.', 'Llueve estando.', 'Está llover.'],
             'correct_answer': 'Está lloviendo.', 'explanation': 'está + lloviendo.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я продолжаю учить испанский.»',
             'options': ['Sigo estudiando español.', 'Sigo estudiar español.', 'Sigo a estudiando español.'],
             'correct_answer': 'Sigo estudiando español.', 'explanation': 'seguir + gerundio.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я спал, когда ты пришёл.»',
             'options': ['Estaba durmiendo cuando llegaste.', 'Estuve durmiendo cuando llegabas.', 'Estaba dormiendo cuando llegaste.'],
             'correct_answer': 'Estaba durmiendo cuando llegaste.', 'explanation': 'Фон estaba durmiendo + событие llegaste.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он говорит, что живёт один.»',
             'options': ['Dice que vive solo.', 'Dice que vivía solo.', 'Dijo que vive solo.'],
             'correct_answer': 'Dice que vive solo.', 'explanation': 'dice → presente.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он сказал, что живёт один.»',
             'options': ['Dijo que vivía solo.', 'Dijo que vive solo.', 'Dice que vivía solo.'],
             'correct_answer': 'Dijo que vivía solo.', 'explanation': 'dijo → imperfecto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Она объяснила, что не может прийти.»',
             'options': ['Explicó que no podía venir.', 'Explicó que no puede venir.', 'Explica que no podía venir.'],
             'correct_answer': 'Explicó que no podía venir.', 'explanation': 'explicó → podía.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я думал, что ты работаешь сегодня.»',
             'options': ['Pensaba que trabajabas hoy.', 'Pensaba que trabajas hoy.', 'Pensé que trabajarás hoy.'],
             'correct_answer': 'Pensaba que trabajabas hoy.', 'explanation': 'pensaba → trabajabas.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Дети всё ещё спят.»',
             'options': ['Los niños siguen durmiendo.', 'Los niños siguen dormir.', 'Los niños están seguir durmiendo.'],
             'correct_answer': 'Los niños siguen durmiendo.', 'explanation': 'siguen + durmiendo.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я это сейчас читаю.»',
             'options': ['Lo estoy leyendo.', 'Estoy lo leyendo.', 'Leo lo estando.'],
             'correct_answer': 'Lo estoy leyendo.', 'explanation': 'lo + estoy leyendo.'},
        ],
    },
    {
        'n': 31, 'level': 'B1', 'title': 'Слово mismo. Ir в indefinido. Quedar(se)',
        'theory': (
            '1. СЛОВО MISMO имеет несколько значений в зависимости от позиции:\n'
            '• el mismo / la misma + сущ. — «тот же самый»: Trabajamos en la misma oficina '
            '(мы работаем в одном и том же офисе). Es el mismo problema de siempre (это всё '
            'та же проблема);\n'
            '• после местоимения/имени — «сам»: Yo mismo lo hice (я сам это сделал). '
            'Ella misma lo dijo (она сама это сказала);\n'
            '• lo mismo — «то же самое»: Para mí, lo mismo (мне то же самое — в кафе). '
            'Siempre dices lo mismo (ты всегда говоришь одно и то же);\n'
            '• усиление места/времени: ahora mismo (прямо сейчас), aquí mismo (прямо здесь), '
            'hoy mismo (сегодня же): Te llamo ahora mismo (звоню тебе прямо сейчас).\n\n'
            '2. IR В INDEFINIDO — закрепляем самый нужный неправильный глагол:\n'
            '  fui, fuiste, fue, fuimos, fuisteis, fueron\n'
            '• Ayer fui de compras (вчера я сходил за покупками);\n'
            '• El verano pasado fuimos de vacaciones a Italia (прошлым летом мы съездили '
            'в отпуск в Италию);\n'
            '• ¿Adónde fuisteis anoche? (куда вы ходили вчера вечером?)\n'
            'IRSE — «уйти, уехать»: Me fui a casa temprano (я рано ушёл домой). Se fue sin '
            'decir nada (он ушёл, ничего не сказав).\n\n'
            '3. QUEDAR / QUEDARSE — многоликий глагол:\n'
            '• quedarse — остаться: Me quedé en casa todo el día (я весь день просидел дома). '
            'Nos quedamos dos noches en el hotel;\n'
            '• quedarse + прилагательное — «стать/остаться в состоянии» (результат): '
            'Se quedó sorprendido (он был поражён). Me quedé dormido (я заснул/уснул '
            'нечаянно);\n'
            '• quedar con — договориться о встрече: He quedado con Ana a las ocho '
            '(я договорился встретиться с Аной в восемь);\n'
            '• quedar bien/mal — хорошо/плохо сидеть (одежда) или произвести впечатление: '
            'Esta chaqueta te queda muy bien (эта куртка тебе очень идёт);\n'
            '• quedar — оставаться (в наличии): No queda pan (хлеба не осталось). '
            'Quedan dos entradas (осталось два билета).\n\n'
            '4. МИНИ-ДИАЛОГ:\n'
            '— ¿Adónde fuiste ayer? Te llamé y nada. (Куда ты вчера ходил? Я тебе звонил — и '
            'ничего.)\n'
            '— Fui de compras y luego quedé con Marta aquí mismo, en la plaza. (Ходил за '
            'покупками, а потом встретился с Мартой прямо здесь, на площади.)\n'
            '— ¡Siempre haces lo mismo y no me dices nada! (Вечно одно и то же — и мне ни '
            'слова!)\n'
            '— Perdona, hombre. Hoy mismo te lo cuento todo. (Прости, дружище. Сегодня же '
            'всё тебе расскажу.)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Употребите mismo', 'exercise_type': 'multiple_choice',
             'prompt': 'Trabajamos en la ___ oficina.', 'options': ['misma', 'mismo', 'mismas'], 'correct_answer': 'misma',
             'translation': 'Мы работаем в одном и том же офисе.', 'explanation': 'la oficina → misma.'},
            {'section': 'Упражнение 1. Употребите mismo', 'exercise_type': 'multiple_choice',
             'prompt': 'Yo ___ lo hice.', 'options': ['mismo', 'misma cosa', 'lo mismo'], 'correct_answer': 'mismo',
             'translation': 'Я сам это сделал.', 'explanation': 'yo mismo — я сам.'},
            {'section': 'Упражнение 1. Употребите mismo', 'exercise_type': 'multiple_choice',
             'prompt': 'Para mí, ___ , por favor.', 'options': ['lo mismo', 'el mismo', 'mismo'], 'correct_answer': 'lo mismo',
             'translation': 'Мне то же самое, пожалуйста.', 'explanation': 'lo mismo — то же самое.'},
            {'section': 'Упражнение 1. Употребите mismo', 'exercise_type': 'multiple_choice',
             'prompt': 'Te llamo ahora ___ .', 'options': ['mismo', 'misma', 'lo mismo'], 'correct_answer': 'mismo',
             'translation': 'Звоню тебе прямо сейчас.', 'explanation': 'ahora mismo.'},
            {'section': 'Упражнение 1. Употребите mismo', 'exercise_type': 'multiple_choice',
             'prompt': 'Ella ___ lo dijo.', 'options': ['misma', 'mismo', 'la misma'], 'correct_answer': 'misma',
             'translation': 'Она сама это сказала.', 'explanation': 'ella misma.'},
            {'section': 'Упражнение 1. Употребите mismo', 'exercise_type': 'multiple_choice',
             'prompt': 'Es el ___ problema de siempre.', 'options': ['mismo', 'misma', 'lo mismo'], 'correct_answer': 'mismo',
             'translation': 'Это всё та же вечная проблема.', 'explanation': 'el mismo + сущ. м. р.'},
            {'section': 'Упражнение 1. Употребите mismo', 'exercise_type': 'multiple_choice',
             'prompt': 'Vivimos en el ___ barrio.', 'options': ['mismo', 'misma', 'mismos'], 'correct_answer': 'mismo',
             'translation': 'Мы живём в одном районе.', 'explanation': 'el barrio → mismo.'},
            {'section': 'Упражнение 1. Употребите mismo', 'exercise_type': 'multiple_choice',
             'prompt': 'Siempre dices ___ .', 'options': ['lo mismo', 'el mismo', 'mismo lo'], 'correct_answer': 'lo mismo',
             'translation': 'Ты всегда говоришь одно и то же.', 'explanation': 'decir lo mismo.'},
            {'section': 'Упражнение 1. Употребите mismo', 'exercise_type': 'multiple_choice',
             'prompt': 'Espérame aquí ___ .', 'options': ['mismo', 'misma', 'mismos'], 'correct_answer': 'mismo',
             'translation': 'Подожди меня прямо здесь.', 'explanation': 'aquí mismo.'},
            {'section': 'Упражнение 1. Употребите mismo', 'exercise_type': 'multiple_choice',
             'prompt': 'Hoy ___ te lo mando.', 'options': ['mismo', 'misma', 'lo mismo'], 'correct_answer': 'mismo',
             'translation': 'Сегодня же тебе это отправлю.', 'explanation': 'hoy mismo — сегодня же.'},
            # 2
            {'section': 'Упражнение 2. Ir/irse в indefinido. Quedar(se)', 'exercise_type': 'fill_blank',
             'prompt': 'Ayer yo ___ (ir) de compras.', 'options': ['fui', 'fuí', 'iba'], 'correct_answer': 'fui',
             'translation': 'Вчера я сходил за покупками.', 'explanation': 'ir → fui.'},
            {'section': 'Упражнение 2. Ir/irse в indefinido. Quedar(se)', 'exercise_type': 'fill_blank',
             'prompt': 'El verano pasado ___ (ir, nosotros) a Italia.', 'options': ['fuimos', 'íbamos', 'vamos'], 'correct_answer': 'fuimos',
             'translation': 'Прошлым летом мы съездили в Италию.', 'explanation': 'fuimos.'},
            {'section': 'Упражнение 2. Ir/irse в indefinido. Quedar(se)', 'exercise_type': 'fill_blank',
             'prompt': 'Él se ___ (ir) sin decir nada.', 'options': ['fue', 'fué', 'iba'], 'correct_answer': 'fue',
             'translation': 'Он ушёл, ничего не сказав.', 'explanation': 'irse: se fue.'},
            {'section': 'Упражнение 2. Ir/irse в indefinido. Quedar(se)', 'exercise_type': 'fill_blank',
             'prompt': 'Yo me ___ (quedar) en casa todo el día.', 'options': ['quedé', 'quedaba', 'quedo'], 'correct_answer': 'quedé',
             'translation': 'Я весь день просидел дома.', 'explanation': 'me quedé.'},
            {'section': 'Упражнение 2. Ir/irse в indefinido. Quedar(se)', 'exercise_type': 'fill_blank',
             'prompt': 'Ella se ___ (quedar) sorprendida.', 'options': ['quedó', 'quedaba', 'queda'], 'correct_answer': 'quedó',
             'translation': 'Она была поражена.', 'explanation': 'quedarse + прилагательное.'},
            {'section': 'Упражнение 2. Ir/irse в indefinido. Quedar(se)', 'exercise_type': 'fill_blank',
             'prompt': 'He ___ (quedar) con Ana a las ocho.', 'options': ['quedado', 'quedada', 'quedando'], 'correct_answer': 'quedado',
             'translation': 'Я договорился встретиться с Аной в восемь.', 'explanation': 'quedar con — договориться.'},
            {'section': 'Упражнение 2. Ir/irse в indefinido. Quedar(se)', 'exercise_type': 'multiple_choice',
             'prompt': 'Esta chaqueta te ___ muy bien.', 'options': ['queda', 'quedas', 'quedan'], 'correct_answer': 'queda',
             'translation': 'Эта куртка тебе очень идёт.', 'explanation': 'te queda bien (как gustar).'},
            {'section': 'Упражнение 2. Ir/irse в indefinido. Quedar(se)', 'exercise_type': 'multiple_choice',
             'prompt': 'No ___ pan: hay que comprar.', 'options': ['queda', 'quedan', 'quedo'], 'correct_answer': 'queda',
             'translation': 'Хлеба не осталось: надо купить.', 'explanation': 'pan — ед.: no queda.'},
            {'section': 'Упражнение 2. Ir/irse в indefinido. Quedar(se)', 'exercise_type': 'multiple_choice',
             'prompt': 'Solo ___ dos entradas.', 'options': ['quedan', 'queda', 'quedáis'], 'correct_answer': 'quedan',
             'translation': 'Осталось только два билета.', 'explanation': 'entradas — мн.: quedan.'},
            {'section': 'Упражнение 2. Ir/irse в indefinido. Quedar(se)', 'exercise_type': 'fill_blank',
             'prompt': 'Anoche me ___ (quedar) dormido en el sofá.', 'options': ['quedé', 'quedaba', 'quedo'], 'correct_answer': 'quedé',
             'translation': 'Вчера вечером я заснул на диване.', 'explanation': 'quedarse dormido — уснуть.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы живём в одном и том же доме.»',
             'options': ['Vivimos en la misma casa.', 'Vivimos en la casa misma.', 'Vivimos en lo mismo casa.'],
             'correct_answer': 'Vivimos en la misma casa.', 'explanation': 'la misma + сущ.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я сам это написал.»',
             'options': ['Yo mismo lo escribí.', 'Yo lo mismo escribí.', 'Mismo yo lo escribí.'],
             'correct_answer': 'Yo mismo lo escribí.', 'explanation': 'yo mismo + indefinido.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Прямо сейчас я тебе это отправляю.»',
             'options': ['Ahora mismo te lo mando.', 'Mismo ahora te lo mando.', 'Ahora lo mismo te mando.'],
             'correct_answer': 'Ahora mismo te lo mando.', 'explanation': 'ahora mismo + te lo.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Куда вы ходили вчера вечером?»',
             'options': ['¿Adónde fuisteis anoche?', '¿Adónde ibais anoche una vez?', '¿Adónde fuistes anoche?'],
             'correct_answer': '¿Adónde fuisteis anoche?', 'explanation': 'fuisteis.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я рано ушёл домой.»',
             'options': ['Me fui a casa temprano.', 'Fui me a casa temprano.', 'Me iba a casa temprano una vez.'],
             'correct_answer': 'Me fui a casa temprano.', 'explanation': 'irse: me fui.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы остались дома.»',
             'options': ['Nos quedamos en casa.', 'Quedamos nos en casa.', 'Nos quedamos a casa.'],
             'correct_answer': 'Nos quedamos en casa.', 'explanation': 'quedarse en casa.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он был поражён.» (остался поражённым)',
             'options': ['Se quedó sorprendido.', 'Se quedó sorprender.', 'Quedó se sorprendido.'],
             'correct_answer': 'Se quedó sorprendido.', 'explanation': 'quedarse + прилагательное.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я договорился встретиться с друзьями.»',
             'options': ['He quedado con mis amigos.', 'He quedado a mis amigos.', 'Me he quedado mis amigos.'],
             'correct_answer': 'He quedado con mis amigos.', 'explanation': 'quedar con.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Эти брюки тебе очень идут.»',
             'options': ['Estos pantalones te quedan muy bien.', 'Estos pantalones te queda muy bien.', 'Estos pantalones quedan te muy bien.'],
             'correct_answer': 'Estos pantalones te quedan muy bien.', 'explanation': 'pantalones — мн.: quedan.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Молока не осталось.»',
             'options': ['No queda leche.', 'No quedan leche.', 'No queda la leche nunca.'],
             'correct_answer': 'No queda leche.', 'explanation': 'leche — ед.: no queda.'},
        ],
    },
]

_D2 = [
    {
        'n': 32, 'level': 'B1', 'title': 'Давнопрошедшее (Pluscuamperfecto). Степени сравнения',
        'theory': (
            '1. PLUSCUAMPERFECTO — «прошлое до прошлого»: действие, случившееся РАНЬШЕ другого '
            'прошедшего события. Образование: haber в imperfecto + причастие:\n'
            '  había, habías, había, habíamos, habíais, habían + hablado/comido/vivido\n'
            '• Cuando llegué, el tren ya había salido (когда я пришёл, поезд уже ушёл);\n'
            '• No comí nada porque ya había cenado (я ничего не ел, потому что уже поужинал);\n'
            '• Nunca había visto nada parecido (я никогда прежде не видел ничего подобного);\n'
            '• Me dijo que había terminado el trabajo (он сказал мне, что закончил работу) — '
            'так perfecto/indefinido сдвигаются в косвенной речи.\n'
            'Неправильные причастия те же: había hecho, había visto, había escrito, había puesto. '
            'Частые спутники: ya (уже), todavía no (ещё не), nunca antes (никогда прежде).\n\n'
            '2. СТЕПЕНИ СРАВНЕНИЯ ПРИЛАГАТЕЛЬНЫХ И НАРЕЧИЙ:\n'
            '• превосходство: más + прил. + que: Madrid es más grande que Ávila (Мадрид больше '
            'Авилы). Este libro es más interesante que el otro;\n'
            '• уступание: menos + прил. + que: El metro es menos caro que el taxi (метро '
            'дешевле такси);\n'
            '• равенство (повторение): tan + прил. + como: Es tan alto como yo.\n'
            'То же с наречиями: Habla más despacio que yo (он говорит медленнее меня).\n\n'
            '3. ДЕТАЛИ, КОТОРЫЕ ПРОВЕРЯЮТ НА ЭКЗАМЕНАХ:\n'
            '• перед ЧИСЛОМ — de, а не que: Hay más de veinte personas (больше двадцати '
            'человек). Cuesta menos de diez euros;\n'
            '• сравнение с местоимением — именительные формы: más alto que yo / que tú / '
            'que él (не *que mí);\n'
            '• «чем …-ее, тем …-ее»: cuanto más estudias, más aprendes (чем больше занимаешься, '
            'тем больше выучиваешь);\n'
            '• превосходная относительная: el/la más + прил. + de: Es la ciudad más bonita '
            'del país (это самый красивый город страны).\n\n'
            '4. МИНИ-ДИАЛОГ:\n'
            '— Llegué al teatro a las ocho, pero la obra ya había empezado. (Я пришёл в театр '
            'в восемь, но спектакль уже начался.)\n'
            '— ¡Vaya! ¿Y qué hiciste? (Вот это да! И что ты сделал?)\n'
            '— Esperé fuera. Fue más aburrido que la obra misma. (Ждал снаружи. Это было '
            'скучнее самого спектакля.)\n'
            '— La próxima vez sal más temprano: es menos arriesgado. (В следующий раз выходи '
            'пораньше: так надёжнее.)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Постройте pluscuamperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Cuando llegué, el tren ya ___ salido.', 'options': ['había', 'ha', 'hubo'], 'correct_answer': 'había',
             'translation': 'Когда я пришёл, поезд уже ушёл.', 'explanation': 'Раньше прошлого → había salido.'},
            {'section': 'Упражнение 1. Постройте pluscuamperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'No comí porque ya ___ cenado.', 'options': ['había', 'he', 'habías'], 'correct_answer': 'había',
             'translation': 'Я не ел, потому что уже поужинал.', 'explanation': '1 л.: había cenado.'},
            {'section': 'Упражнение 1. Постройте pluscuamperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Nunca ___ visto nada parecido. (я прежде)', 'options': ['había', 'he', 'hube'], 'correct_answer': 'había',
             'translation': 'Я никогда прежде не видел ничего подобного.', 'explanation': 'До момента в прошлом → había visto.'},
            {'section': 'Упражнение 1. Постройте pluscuamperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Me dijo que ___ terminado el trabajo.', 'options': ['había', 'ha', 'habrá'], 'correct_answer': 'había',
             'translation': 'Он сказал, что закончил работу.', 'explanation': 'Косвенная речь → había terminado.'},
            {'section': 'Упражнение 1. Постройте pluscuamperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Cuando volvimos, los niños ya se ___ dormido.', 'options': ['habían', 'había', 'han'], 'correct_answer': 'habían',
             'translation': 'Когда мы вернулись, дети уже уснули.', 'explanation': '3 л. мн.: habían.'},
            {'section': 'Упражнение 1. Постройте pluscuamperfecto', 'exercise_type': 'fill_blank',
             'prompt': '¿Nunca antes ___ (tú) probado la paella?', 'options': ['habías', 'has', 'había'], 'correct_answer': 'habías',
             'translation': 'Ты никогда раньше не пробовал паэлью?', 'explanation': '2 л.: habías probado.'},
            {'section': 'Упражнение 1. Постройте pluscuamperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'La película ya ___ empezado cuando entramos.', 'options': ['había', 'ha', 'habían'], 'correct_answer': 'había',
             'translation': 'Фильм уже начался, когда мы вошли.', 'explanation': 'había empezado.'},
            {'section': 'Упражнение 1. Постройте pluscuamperfecto', 'exercise_type': 'multiple_choice',
             'prompt': '«Он сказал, что уже сделал это» → Dijo que ya lo ___ .', 'options': ['había hecho', 'ha hecho', 'hizo haber'], 'correct_answer': 'había hecho',
             'translation': 'Он сказал, что уже это сделал.', 'explanation': 'hecho + сдвиг → había hecho.'},
            {'section': 'Упражнение 1. Постройте pluscuamperfecto', 'exercise_type': 'multiple_choice',
             'prompt': 'Причастие: «она уже написала письмо» → ya había ___ la carta.', 'options': ['escrito', 'escribido', 'escrita'], 'correct_answer': 'escrito',
             'translation': 'Она уже написала письмо.', 'explanation': 'escribir → escrito (не меняется).'},
            {'section': 'Упражнение 1. Постройте pluscuamperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Todavía no ___ (nosotros) comido cuando llamaste.', 'options': ['habíamos', 'hemos', 'habían'], 'correct_answer': 'habíamos',
             'translation': 'Мы ещё не поели, когда ты позвонил.', 'explanation': '1 л. мн.: habíamos.'},
            # 2
            {'section': 'Упражнение 2. Сравнение: más/menos/tan, de/que', 'exercise_type': 'multiple_choice',
             'prompt': 'Madrid es ___ grande que Ávila.', 'options': ['más', 'tan', 'muy'], 'correct_answer': 'más',
             'translation': 'Мадрид больше Авилы.', 'explanation': 'más … que.'},
            {'section': 'Упражнение 2. Сравнение: más/menos/tan, de/que', 'exercise_type': 'multiple_choice',
             'prompt': 'El metro es ___ caro que el taxi.', 'options': ['menos', 'menor', 'poco'], 'correct_answer': 'menos',
             'translation': 'Метро дешевле такси.', 'explanation': 'menos … que.'},
            {'section': 'Упражнение 2. Сравнение: más/menos/tan, de/que', 'exercise_type': 'multiple_choice',
             'prompt': 'Hay más ___ veinte personas.', 'options': ['de', 'que', 'como'], 'correct_answer': 'de',
             'translation': 'Здесь больше двадцати человек.', 'explanation': 'Перед числом → de.'},
            {'section': 'Упражнение 2. Сравнение: más/menos/tan, de/que', 'exercise_type': 'multiple_choice',
             'prompt': 'Cuesta menos ___ diez euros.', 'options': ['de', 'que', 'a'], 'correct_answer': 'de',
             'translation': 'Это стоит меньше десяти евро.', 'explanation': 'menos de + число.'},
            {'section': 'Упражнение 2. Сравнение: más/menos/tan, de/que', 'exercise_type': 'multiple_choice',
             'prompt': 'Es más alto que ___ .', 'options': ['yo', 'mí', 'me'], 'correct_answer': 'yo',
             'translation': 'Он выше меня.', 'explanation': 'que + именительная форма: que yo.'},
            {'section': 'Упражнение 2. Сравнение: más/menos/tan, de/que', 'exercise_type': 'multiple_choice',
             'prompt': 'Habla más despacio ___ yo.', 'options': ['que', 'de', 'como'], 'correct_answer': 'que',
             'translation': 'Он говорит медленнее меня.', 'explanation': 'Сравнение → que.'},
            {'section': 'Упражнение 2. Сравнение: más/menos/tan, de/que', 'exercise_type': 'multiple_choice',
             'prompt': 'Es la ciudad más bonita ___ país.', 'options': ['del', 'que el', 'de la'], 'correct_answer': 'del',
             'translation': 'Это самый красивый город страны.', 'explanation': 'Превосходная + de: del país.'},
            {'section': 'Упражнение 2. Сравнение: más/menos/tan, de/que', 'exercise_type': 'multiple_choice',
             'prompt': 'Cuanto más estudias, ___ aprendes.', 'options': ['más', 'menos mal', 'tan'], 'correct_answer': 'más',
             'translation': 'Чем больше занимаешься, тем больше выучиваешь.', 'explanation': 'cuanto más …, más …'},
            {'section': 'Упражнение 2. Сравнение: más/menos/tan, de/que', 'exercise_type': 'multiple_choice',
             'prompt': 'Este barrio es ___ tranquilo como el nuestro.', 'options': ['tan', 'más', 'menos'], 'correct_answer': 'tan',
             'translation': 'Этот район такой же спокойный, как наш.', 'explanation': 'tan … como.'},
            {'section': 'Упражнение 2. Сравнение: más/menos/tan, de/que', 'exercise_type': 'multiple_choice',
             'prompt': 'Trabajo más ___ antes.', 'options': ['que', 'de', 'como'], 'correct_answer': 'que',
             'translation': 'Я работаю больше, чем раньше.', 'explanation': 'más que antes.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Когда я пришёл, фильм уже начался.»',
             'options': ['Cuando llegué, la película ya había empezado.', 'Cuando llegaba, la película ya empezó.', 'Cuando llegué, la película ya ha empezado.'],
             'correct_answer': 'Cuando llegué, la película ya había empezado.', 'explanation': 'Раньше прошлого → pluscuamperfecto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я никогда прежде не был в этом городе.»',
             'options': ['Nunca había estado en esta ciudad.', 'Nunca he estado en esta ciudad antes ayer.', 'Nunca hube estado en esta ciudad.'],
             'correct_answer': 'Nunca había estado en esta ciudad.', 'explanation': 'До момента в прошлом → había estado.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Она сказала, что уже поела.»',
             'options': ['Dijo que ya había comido.', 'Dijo que ya ha comido.', 'Dijo que ya comía.'],
             'correct_answer': 'Dijo que ya había comido.', 'explanation': 'Сдвиг в косвенной речи.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Эта книга интереснее той.»',
             'options': ['Este libro es más interesante que aquel.', 'Este libro es más interesante de aquel.', 'Este libro es tan interesante que aquel.'],
             'correct_answer': 'Este libro es más interesante que aquel.', 'explanation': 'más … que.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Здесь больше ста человек.»',
             'options': ['Aquí hay más de cien personas.', 'Aquí hay más que cien personas.', 'Aquí hay más cien de personas.'],
             'correct_answer': 'Aquí hay más de cien personas.', 'explanation': 'más de + число.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Ты выше меня.»',
             'options': ['Eres más alto que yo.', 'Eres más alto que mí.', 'Eres más alto de yo.'],
             'correct_answer': 'Eres más alto que yo.', 'explanation': 'que yo.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это самый дорогой ресторан района.»',
             'options': ['Es el restaurante más caro del barrio.', 'Es el más restaurante caro del barrio.', 'Es el restaurante más caro que el barrio.'],
             'correct_answer': 'Es el restaurante más caro del barrio.', 'explanation': 'el más … del.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Чем больше читаешь, тем больше знаешь.»',
             'options': ['Cuanto más lees, más sabes.', 'Que más lees, más sabes.', 'Cuando más lees, tanto sabes.'],
             'correct_answer': 'Cuanto más lees, más sabes.', 'explanation': 'cuanto más …, más …'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы ещё не закончили, когда он пришёл.»',
             'options': ['Todavía no habíamos terminado cuando llegó.', 'Todavía no hemos terminado cuando llegó.', 'Todavía no terminábamos haber cuando llegó.'],
             'correct_answer': 'Todavía no habíamos terminado cuando llegó.', 'explanation': 'habíamos terminado.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Такси дороже автобуса.»',
             'options': ['El taxi es más caro que el autobús.', 'El taxi es más caro del autobús.', 'El taxi es caro más que el autobús.'],
             'correct_answer': 'El taxi es más caro que el autobús.', 'explanation': 'más caro que.'},
        ],
    },
    {
        'n': 33, 'level': 'B1', 'title': 'Абсолютная превосходная (-ísimo). Mejor, peor, mayor, menor',
        'theory': (
            '1. СУФФИКС -ÍSIMO — «очень-очень, в высшей степени» (абсолютная превосходная, '
            'без сравнения с кем-либо). Заменяет muy + прилагательное и звучит выразительнее:\n'
            '• alto → altísimo: Es un edificio altísimo (это высоченное здание);\n'
            '• fácil → facilísimo: El examen fue facilísimo (экзамен был легчайший);\n'
            '• guapo → guapísimo, cansado → cansadísimo, caro → carísimo, '
            'interesante → interesantísimo.\n'
            'Суффикс согласуется: altísima, altísimos, altísimas. НЕЛЬЗЯ сочетать с muy: '
            '*muy altísimo.\n\n'
            '2. ОРФОГРАФИЧЕСКИЕ ЗАМЕНЫ ПЕРЕД -ÍSIMO (чтобы сохранить звук):\n'
            '• -co → -quísimo: rico → riquísimo (вкуснейший): ¡La paella está riquísima!;\n'
            '• -go → -guísimo: largo → larguísimo (длиннющий);\n'
            '• -z → -císimo: feliz → felicísimo (счастливейший);\n'
            '• -ble → -bilísimo: amable → amabilísimo (любезнейший).\n\n'
            '3. ОСОБЫЕ СТЕПЕНИ СРАВНЕНИЯ — четыре прилагательных образуют их не по правилу:\n'
            '• bueno → mejor (лучше): Este café es mejor que aquel (этот кофе лучше того). '
            'Cada día hablas mejor (с каждым днём ты говоришь лучше — и как наречие от bien);\n'
            '• malo → peor (хуже): La segunda parte es peor que la primera;\n'
            '• grande → mayor (больше; старше о возрасте): Mi hermano mayor (мой старший '
            'брат). Ana es mayor que yo (Ана старше меня);\n'
            '• pequeño → menor (меньше; младше): mi hermana menor (моя младшая сестра).\n'
            'Формы mejor/peor/mayor/menor НЕ меняются по родам, только по числам: mejores, '
            'peores, mayores, menores.\n\n'
            '4. ОТНОСИТЕЛЬНАЯ ПРЕВОСХОДНАЯ с особыми формами: el mejor / la mejor / los '
            'mejores + de: Es el mejor restaurante de la ciudad (это лучший ресторан города). '
            'Fue el peor día de mi vida (это был худший день моей жизни).\n\n'
            '5. МИНИ-ДИАЛОГ:\n'
            '— ¿Qué tal el restaurante nuevo? (Как новый ресторан?)\n'
            '— ¡Buenísimo! La tortilla estaba riquísima, y el camarero fue amabilísimo. '
            '(Отличнейший! Тортилья была вкуснейшая, а официант — любезнейший.)\n'
            '— ¿Mejor que el de la plaza? (Лучше того, что на площади?)\n'
            '— ¡Muchísimo mejor! Aunque un poquito más caro. (Намного лучше! Хотя чуточку '
            'дороже.)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Образуйте форму на -ísimo', 'exercise_type': 'multiple_choice',
             'prompt': 'alto → un edificio ___', 'options': ['altísimo', 'altoísimo', 'altísimos'], 'correct_answer': 'altísimo',
             'translation': 'высоченное здание', 'explanation': 'alto → altísimo.'},
            {'section': 'Упражнение 1. Образуйте форму на -ísimo', 'exercise_type': 'multiple_choice',
             'prompt': 'rico → ¡La paella está ___ !', 'options': ['riquísima', 'ricísima', 'riquísimo'], 'correct_answer': 'riquísima',
             'translation': 'Паэлья вкуснейшая!', 'explanation': '-co → -quísimo; ж. р.: riquísima.'},
            {'section': 'Упражнение 1. Образуйте форму на -ísimo', 'exercise_type': 'multiple_choice',
             'prompt': 'largo → un viaje ___', 'options': ['larguísimo', 'largísimo', 'larguísima'], 'correct_answer': 'larguísimo',
             'translation': 'длиннющее путешествие', 'explanation': '-go → -guísimo.'},
            {'section': 'Упражнение 1. Образуйте форму на -ísimo', 'exercise_type': 'multiple_choice',
             'prompt': 'feliz → un hombre ___', 'options': ['felicísimo', 'felizísimo', 'felísimo'], 'correct_answer': 'felicísimo',
             'translation': 'счастливейший человек', 'explanation': '-z → -císimo.'},
            {'section': 'Упражнение 1. Образуйте форму на -ísimo', 'exercise_type': 'multiple_choice',
             'prompt': 'fácil → El examen fue ___ .', 'options': ['facilísimo', 'fácilísimo', 'facilísima'], 'correct_answer': 'facilísimo',
             'translation': 'Экзамен был легчайший.', 'explanation': 'fácil → facilísimo.'},
            {'section': 'Упражнение 1. Образуйте форму на -ísimo', 'exercise_type': 'multiple_choice',
             'prompt': 'cansado → Estoy ___ .', 'options': ['cansadísimo', 'cansísimo', 'cansadoísimo'], 'correct_answer': 'cansadísimo',
             'translation': 'Я жутко устал.', 'explanation': 'cansado → cansadísimo.'},
            {'section': 'Упражнение 1. Образуйте форму на -ísimo', 'exercise_type': 'multiple_choice',
             'prompt': 'amable → un señor ___', 'options': ['amabilísimo', 'amablísimo', 'amabilísima'], 'correct_answer': 'amabilísimo',
             'translation': 'любезнейший господин', 'explanation': '-ble → -bilísimo.'},
            {'section': 'Упражнение 1. Образуйте форму на -ísimo', 'exercise_type': 'multiple_choice',
             'prompt': 'caro → unos precios ___', 'options': ['carísimos', 'carísimo', 'carísimas'], 'correct_answer': 'carísimos',
             'translation': 'запредельные цены', 'explanation': 'precios — мн.: carísimos.'},
            {'section': 'Упражнение 1. Образуйте форму на -ísimo', 'exercise_type': 'multiple_choice',
             'prompt': 'Что НЕПРАВИЛЬНО?', 'options': ['muy altísimo', 'altísimo', 'muy alto'], 'correct_answer': 'muy altísimo',
             'translation': '—', 'explanation': 'muy + -ísimo не сочетаются.'},
            {'section': 'Упражнение 1. Образуйте форму на -ísimo', 'exercise_type': 'multiple_choice',
             'prompt': 'mucho → ¡ ___ gracias!', 'options': ['Muchísimas', 'Muchísimos', 'Muchísima'], 'correct_answer': 'Muchísimas',
             'translation': 'Огромное спасибо!', 'explanation': 'gracias — ж. р. мн.: muchísimas.'},
            # 2
            {'section': 'Упражнение 2. Mejor, peor, mayor, menor', 'exercise_type': 'multiple_choice',
             'prompt': 'Este café es ___ que aquel. (лучше)', 'options': ['mejor', 'más bueno', 'buenísimo que'], 'correct_answer': 'mejor',
             'translation': 'Этот кофе лучше того.', 'explanation': 'bueno → mejor.'},
            {'section': 'Упражнение 2. Mejor, peor, mayor, menor', 'exercise_type': 'multiple_choice',
             'prompt': 'La segunda parte es ___ que la primera. (хуже)', 'options': ['peor', 'más mala', 'malísima que'], 'correct_answer': 'peor',
             'translation': 'Вторая часть хуже первой.', 'explanation': 'malo → peor.'},
            {'section': 'Упражнение 2. Mejor, peor, mayor, menor', 'exercise_type': 'multiple_choice',
             'prompt': 'Mi hermano ___ tiene treinta años. (старший)', 'options': ['mayor', 'más grande', 'grandísimo'], 'correct_answer': 'mayor',
             'translation': 'Моему старшему брату тридцать лет.', 'explanation': 'Старший → mayor.'},
            {'section': 'Упражнение 2. Mejor, peor, mayor, menor', 'exercise_type': 'multiple_choice',
             'prompt': 'Mi hermana ___ estudia en el colegio. (младшая)', 'options': ['menor', 'más pequeña de todo', 'pequeñísima'], 'correct_answer': 'menor',
             'translation': 'Моя младшая сестра учится в школе.', 'explanation': 'Младшая → menor.'},
            {'section': 'Упражнение 2. Mejor, peor, mayor, menor', 'exercise_type': 'multiple_choice',
             'prompt': 'Ana es ___ que yo: tiene dos años más.', 'options': ['mayor', 'mejor', 'más vieja siempre'], 'correct_answer': 'mayor',
             'translation': 'Ана старше меня: ей на два года больше.', 'explanation': 'О возрасте → mayor que.'},
            {'section': 'Упражнение 2. Mejor, peor, mayor, menor', 'exercise_type': 'multiple_choice',
             'prompt': 'Cada día hablas ___ . (лучше)', 'options': ['mejor', 'más bien', 'buenísimo'], 'correct_answer': 'mejor',
             'translation': 'С каждым днём ты говоришь лучше.', 'explanation': 'bien → mejor.'},
            {'section': 'Упражнение 2. Mejor, peor, mayor, menor', 'exercise_type': 'multiple_choice',
             'prompt': 'Es el ___ restaurante de la ciudad.', 'options': ['mejor', 'más mejor', 'mejor de'], 'correct_answer': 'mejor',
             'translation': 'Это лучший ресторан города.', 'explanation': 'el mejor + de.'},
            {'section': 'Упражнение 2. Mejor, peor, mayor, menor', 'exercise_type': 'multiple_choice',
             'prompt': 'Fue el ___ día de mi vida.', 'options': ['peor', 'más peor', 'malísimo de'], 'correct_answer': 'peor',
             'translation': 'Это был худший день моей жизни.', 'explanation': 'el peor + de.'},
            {'section': 'Упражнение 2. Mejor, peor, mayor, menor', 'exercise_type': 'multiple_choice',
             'prompt': 'Estas notas son ___ que las de ayer. (лучше, мн.)', 'options': ['mejores', 'mejor', 'más buenas'], 'correct_answer': 'mejores',
             'translation': 'Эти оценки лучше вчерашних.', 'explanation': 'Мн. ч.: mejores.'},
            {'section': 'Упражнение 2. Mejor, peor, mayor, menor', 'exercise_type': 'multiple_choice',
             'prompt': 'Los ___ de edad no pueden entrar. (несовершеннолетние)', 'options': ['menores', 'menors', 'más pequeños siempre'], 'correct_answer': 'menores',
             'translation': 'Несовершеннолетним вход воспрещён.', 'explanation': 'menores de edad.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Фильм был интереснейший.»',
             'options': ['La película fue interesantísima.', 'La película fue muy interesantísima.', 'La película fue interesantísimo.'],
             'correct_answer': 'La película fue interesantísima.', 'explanation': 'ж. р.: interesantísima; без muy.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Суп вкуснейший!»',
             'options': ['¡La sopa está riquísima!', '¡La sopa está ricísima!', '¡La sopa es riquísimo!'],
             'correct_answer': '¡La sopa está riquísima!', 'explanation': 'rico → riquísima (qu!).'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Огромное спасибо!»',
             'options': ['¡Muchísimas gracias!', '¡Muy muchas gracias!', '¡Muchísimos gracias!'],
             'correct_answer': '¡Muchísimas gracias!', 'explanation': 'muchísimas gracias.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Твой испанский лучше моего.»',
             'options': ['Tu español es mejor que el mío.', 'Tu español es más bueno que el mío.', 'Tu español es mejor del mío.'],
             'correct_answer': 'Tu español es mejor que el mío.', 'explanation': 'mejor que.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Сегодня погода хуже, чем вчера.»',
             'options': ['Hoy el tiempo es peor que ayer.', 'Hoy el tiempo es más malo que ayer.', 'Hoy el tiempo es peor de ayer.'],
             'correct_answer': 'Hoy el tiempo es peor que ayer.', 'explanation': 'peor que.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мой старший брат живёт в Мадриде.»',
             'options': ['Mi hermano mayor vive en Madrid.', 'Mi mayor hermano vive en Madrid.', 'Mi hermano más grande vive en Madrid.'],
             'correct_answer': 'Mi hermano mayor vive en Madrid.', 'explanation': 'hermano mayor.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Она младше меня.»',
             'options': ['Es menor que yo.', 'Es más pequeña de yo.', 'Es menor de yo.'],
             'correct_answer': 'Es menor que yo.', 'explanation': 'menor que yo.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это лучший день моей жизни.»',
             'options': ['Es el mejor día de mi vida.', 'Es el más mejor día de mi vida.', 'Es el mejor día que mi vida.'],
             'correct_answer': 'Es el mejor día de mi vida.', 'explanation': 'el mejor … de.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я жутко устал (устал-преустал).»',
             'options': ['Estoy cansadísimo.', 'Estoy muy cansadísimo.', 'Soy cansadísimo.'],
             'correct_answer': 'Estoy cansadísimo.', 'explanation': 'estar + cansadísimo.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «С каждым разом ты пишешь лучше.»',
             'options': ['Cada vez escribes mejor.', 'Cada vez escribes más bien.', 'Cada vez escribes mejor que.'],
             'correct_answer': 'Cada vez escribes mejor.', 'explanation': 'escribir mejor.'},
        ],
    },
]
B1_FULL = B1_FULL + _D2

_D3 = [
    {
        'n': 34, 'level': 'B1', 'title': 'Предпрошедшее (Pretérito anterior). Наречия на -mente',
        'theory': (
            '1. PRETÉRITO ANTERIOR — книжное «предпрошедшее»: действие, завершившееся '
            'НЕПОСРЕДСТВЕННО перед другим прошедшим. Образование: haber в indefinido + '
            'причастие:\n'
            '  hube, hubiste, hubo, hubimos, hubisteis, hubieron + hablado/comido/vivido\n'
            'Употребляется после союзов немедленности: cuando (когда), apenas (едва), '
            'en cuanto (как только), así que (как только), después de que:\n'
            '• Apenas hubo terminado, salió (едва он закончил, он вышел);\n'
            '• En cuanto hubieron cenado, se acostaron (как только они поужинали, легли спать);\n'
            '• Cuando hubo dicho eso, todos callaron (когда он это сказал, все замолчали).\n\n'
            'ВАЖНО ПРО СТИЛЬ: это время живёт почти только в литературе. В разговорной речи '
            'его заменяют indefinido или pluscuamperfecto: Apenas terminó, salió. / Cuando '
            'había terminado, salió. Узнавать его нужно (встретится в книгах и тестах), '
            'активно употреблять — нет.\n\n'
            '2. НАРЕЧИЯ НА -MENTE — главный способ сказать «как?» (аналог русского «-о» и '
            'английского -ly). Образование: ЖЕНСКАЯ форма прилагательного + -mente:\n'
            '• rápido → rápida → rápidamente (быстро): Contestó rápidamente (он быстро ответил);\n'
            '• lento → lentamente (медленно); claro → claramente (ясно);\n'
            '• perfecto → perfectamente: Te entiendo perfectamente (я прекрасно тебя понимаю);\n'
            '• прилагательные на -e/-согласную не меняются: fácil → fácilmente (легко), '
            'frecuente → frecuentemente, feliz → felizmente (к счастью).\n'
            'Тильда прилагательного СОХРАНЯЕТСЯ: fácilmente, rápidamente.\n\n'
            '3. ДВА НАРЕЧИЯ ПОДРЯД — суффикс -mente получает только ПОСЛЕДНЕЕ:\n'
            '• Habla clara y lentamente (он говорит ясно и медленно);\n'
            '• Trabaja rápida y eficazmente (он работает быстро и эффективно).\n\n'
            '4. ПОЛЕЗНЫЕ НАРЕЧИЯ-СВЯЗКИ: normalmente (обычно), generalmente (как правило), '
            'realmente (действительно), exactamente (точно), afortunadamente (к счастью), '
            'desgraciadamente (к сожалению), últimamente (в последнее время): Últimamente '
            'duermo poco (в последнее время я мало сплю).\n\n'
            '5. МИНИ-ДИАЛОГ:\n'
            '— ¿Cómo te fue la entrevista? (Как прошло собеседование?)\n'
            '— Realmente bien. Contesté tranquila y claramente. (Действительно хорошо. Я '
            'отвечала спокойно и ясно.)\n'
            '— ¿Y el resultado? (А результат?)\n'
            '— Afortunadamente, me llamaron hoy mismo: ¡el puesto es mío! (К счастью, мне '
            'позвонили сегодня же: место моё!)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Узнайте pretérito anterior', 'exercise_type': 'fill_blank',
             'prompt': 'Apenas ___ terminado, salió.', 'options': ['hubo', 'había', 'ha'], 'correct_answer': 'hubo',
             'translation': 'Едва он закончил, он вышел.', 'explanation': 'apenas + hubo + причастие.'},
            {'section': 'Упражнение 1. Узнайте pretérito anterior', 'exercise_type': 'fill_blank',
             'prompt': 'En cuanto ___ cenado, se acostaron.', 'options': ['hubieron', 'habían', 'han'], 'correct_answer': 'hubieron',
             'translation': 'Как только они поужинали, они легли.', 'explanation': '3 л. мн.: hubieron.'},
            {'section': 'Упражнение 1. Узнайте pretérito anterior', 'exercise_type': 'fill_blank',
             'prompt': 'Cuando ___ dicho eso, todos callaron.', 'options': ['hubo', 'ha', 'habría'], 'correct_answer': 'hubo',
             'translation': 'Когда он это сказал, все замолчали.', 'explanation': 'cuando + hubo dicho.'},
            {'section': 'Упражнение 1. Узнайте pretérito anterior', 'exercise_type': 'multiple_choice',
             'prompt': 'Где употреблено pretérito anterior?', 'options': ['Apenas hubo llegado, llamó.', 'Apenas había llegado, llamó.', 'Apenas llegó, llamó.'],
             'correct_answer': 'Apenas hubo llegado, llamó.', 'translation': 'Едва он приехал, он позвонил.',
             'explanation': 'hube/hubo + причастие = anterior.'},
            {'section': 'Упражнение 1. Узнайте pretérito anterior', 'exercise_type': 'multiple_choice',
             'prompt': 'Разговорная замена «Apenas hubo terminado, salió»:', 'options': ['Apenas terminó, salió.', 'Apenas termina, salga.', 'Apenas terminaba, salía siempre.'],
             'correct_answer': 'Apenas terminó, salió.', 'translation': 'Едва он закончил, он вышел.',
             'explanation': 'В речи anterior → indefinido.'},
            {'section': 'Упражнение 1. Узнайте pretérito anterior', 'exercise_type': 'fill_blank',
             'prompt': 'Así que ___ (nosotros) comido, seguimos el viaje.', 'options': ['hubimos', 'habíamos', 'hemos'], 'correct_answer': 'hubimos',
             'translation': 'Как только мы поели, мы продолжили путь.', 'explanation': '1 л. мн.: hubimos.'},
            {'section': 'Упражнение 1. Узнайте pretérito anterior', 'exercise_type': 'multiple_choice',
             'prompt': 'Pretérito anterior употребляется в основном…', 'options': ['в литературе', 'в бытовой речи', 'в SMS'], 'correct_answer': 'в литературе',
             'translation': '—', 'explanation': 'Книжное время; в речи заменяется.'},
            {'section': 'Упражнение 1. Узнайте pretérito anterior', 'exercise_type': 'multiple_choice',
             'prompt': 'После какого слова часто идёт anterior?', 'options': ['apenas', 'mañana', 'ojalá'], 'correct_answer': 'apenas',
             'translation': 'apenas — едва', 'explanation': 'apenas/en cuanto/cuando.'},
            {'section': 'Упражнение 1. Узнайте pretérito anterior', 'exercise_type': 'fill_blank',
             'prompt': 'Apenas me ___ levantado, sonó el timbre.', 'options': ['hube', 'había', 'he'], 'correct_answer': 'hube',
             'translation': 'Едва я встал, раздался звонок в дверь.', 'explanation': '1 л.: hube.'},
            {'section': 'Упражнение 1. Узнайте pretérito anterior', 'exercise_type': 'multiple_choice',
             'prompt': 'Полная форма: apenas hubo ___ (escribir) la carta…', 'options': ['escrito', 'escribido', 'escribiendo'], 'correct_answer': 'escrito',
             'translation': 'едва он написал письмо…', 'explanation': 'Причастие то же: escrito.'},
            # 2
            {'section': 'Упражнение 2. Образуйте наречие на -mente', 'exercise_type': 'multiple_choice',
             'prompt': 'rápido → Contestó ___ .', 'options': ['rápidamente', 'rápidomente', 'rápida'], 'correct_answer': 'rápidamente',
             'translation': 'Он быстро ответил.', 'explanation': 'rápida + mente.'},
            {'section': 'Упражнение 2. Образуйте наречие на -mente', 'exercise_type': 'multiple_choice',
             'prompt': 'fácil → Lo aprendí ___ .', 'options': ['fácilmente', 'fácilamente', 'facilmente'], 'correct_answer': 'fácilmente',
             'translation': 'Я легко это выучил.', 'explanation': 'Тильда сохраняется: fácilmente.'},
            {'section': 'Упражнение 2. Образуйте наречие на -mente', 'exercise_type': 'multiple_choice',
             'prompt': 'perfecto → Te entiendo ___ .', 'options': ['perfectamente', 'perfectomente', 'perfecta'], 'correct_answer': 'perfectamente',
             'translation': 'Я прекрасно тебя понимаю.', 'explanation': 'perfecta + mente.'},
            {'section': 'Упражнение 2. Образуйте наречие на -mente', 'exercise_type': 'multiple_choice',
             'prompt': 'lento → Habla más ___ , por favor.', 'options': ['lentamente', 'lentomente', 'lenta'], 'correct_answer': 'lentamente',
             'translation': 'Говори медленнее, пожалуйста.', 'explanation': 'lenta + mente.'},
            {'section': 'Упражнение 2. Образуйте наречие на -mente', 'exercise_type': 'multiple_choice',
             'prompt': 'feliz → ___ , todo salió bien.', 'options': ['Felizmente', 'Felizamente', 'Felicemente'], 'correct_answer': 'Felizmente',
             'translation': 'К счастью, всё вышло хорошо.', 'explanation': 'feliz + mente.'},
            {'section': 'Упражнение 2. Образуйте наречие на -mente', 'exercise_type': 'multiple_choice',
             'prompt': 'Два наречия: Habla ___ y lentamente.', 'options': ['clara', 'claramente', 'claro'], 'correct_answer': 'clara',
             'translation': 'Он говорит ясно и медленно.', 'explanation': '-mente только у последнего; первое — ж. р.'},
            {'section': 'Упражнение 2. Образуйте наречие на -mente', 'exercise_type': 'multiple_choice',
             'prompt': 'Trabaja rápida y ___ .', 'options': ['eficazmente', 'eficaz', 'eficazamente'], 'correct_answer': 'eficazmente',
             'translation': 'Он работает быстро и эффективно.', 'explanation': 'Последнее получает -mente.'},
            {'section': 'Упражнение 2. Образуйте наречие на -mente', 'exercise_type': 'multiple_choice',
             'prompt': '«В последнее время я мало сплю» → ___ duermo poco.', 'options': ['Últimamente', 'Último', 'Ultimamente'], 'correct_answer': 'Últimamente',
             'translation': 'В последнее время я мало сплю.', 'explanation': 'últimamente (с тильдой).'},
            {'section': 'Упражнение 2. Образуйте наречие на -mente', 'exercise_type': 'multiple_choice',
             'prompt': '«К сожалению» =', 'options': ['desgraciadamente', 'afortunadamente', 'exactamente'], 'correct_answer': 'desgraciadamente',
             'translation': 'desgraciadamente — к сожалению', 'explanation': 'afortunadamente — к счастью.'},
            {'section': 'Упражнение 2. Образуйте наречие на -mente', 'exercise_type': 'multiple_choice',
             'prompt': '«Обычно» =', 'options': ['normalmente', 'normalamente', 'normamente'], 'correct_answer': 'normalmente',
             'translation': 'normalmente — обычно', 'explanation': 'normal + mente.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он быстро ответил.»',
             'options': ['Contestó rápidamente.', 'Contestó rápido mente.', 'Contestó rápida.'],
             'correct_answer': 'Contestó rápidamente.', 'explanation': 'rápidamente.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я прекрасно тебя понимаю.»',
             'options': ['Te entiendo perfectamente.', 'Te entiendo perfecto.', 'Te entiendo perfectamente a ti mucho.'],
             'correct_answer': 'Te entiendo perfectamente.', 'explanation': 'perfectamente.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Говори медленно и ясно.»',
             'options': ['Habla lenta y claramente.', 'Habla lentamente y claramente.', 'Habla lento y claro mente.'],
             'correct_answer': 'Habla lenta y claramente.', 'explanation': '-mente у последнего.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «К счастью, никто не пострадал.» (no pasó nada a nadie ≈)',
             'options': ['Afortunadamente, no le pasó nada a nadie.', 'Afortunadamente, pasó nada a nadie.', 'Afortunada, no le pasó nada a nadie.'],
             'correct_answer': 'Afortunadamente, no le pasó nada a nadie.', 'explanation': 'afortunadamente + двойное отрицание.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Обычно я встаю в семь.»',
             'options': ['Normalmente me levanto a las siete.', 'Normal me levanto a las siete.', 'Normalmente levanto a las siete.'],
             'correct_answer': 'Normalmente me levanto a las siete.', 'explanation': 'normalmente + возвратный.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «В последнее время он много работает.»',
             'options': ['Últimamente trabaja mucho.', 'Último trabaja mucho.', 'Últimamente trabaja muy.'],
             'correct_answer': 'Últimamente trabaja mucho.', 'explanation': 'últimamente.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это легко объясняется.» (объясняется легко)',
             'options': ['Se explica fácilmente.', 'Se explica fácil mente.', 'Explica se fácilmente.'],
             'correct_answer': 'Se explica fácilmente.', 'explanation': 'se + fácilmente.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите (книжно): «Едва он поужинал, он лёг спать.»',
             'options': ['Apenas hubo cenado, se acostó.', 'Apenas ha cenado, se acostó.', 'Apenas hubo cenar, se acostó.'],
             'correct_answer': 'Apenas hubo cenado, se acostó.', 'explanation': 'apenas + anterior.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите (разговорно то же): «Едва он поужинал, он лёг спать.»',
             'options': ['Apenas cenó, se acostó.', 'Apenas cenaba, se acostaba una vez.', 'Apenas cena, se acuesta ayer.'],
             'correct_answer': 'Apenas cenó, se acostó.', 'explanation': 'Речь → indefinido.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Точно! Именно это я и сказал.»',
             'options': ['¡Exactamente! Eso mismo dije.', '¡Exacto mente! Eso mismo dije.', '¡Exactamente! Eso mismo dije yo mismo a mí.'],
             'correct_answer': '¡Exactamente! Eso mismo dije.', 'explanation': 'exactamente + eso mismo.'},
        ],
    },
    {
        'n': 35, 'level': 'B1', 'title': 'Soler и servir. Poco и solo. Обороты с de',
        'theory': (
            '1. SOLER (o→ue) + ИНФИНИТИВ — «обычно делать, иметь привычку». Незаменим для '
            'рассказа о распорядке:\n'
            '  suelo, sueles, suele, solemos, soléis, suelen\n'
            '• Suelo levantarme a las siete (обычно я встаю в семь);\n'
            '• ¿Qué sueles hacer los domingos? (что ты обычно делаешь по воскресеньям?);\n'
            '• Solemos cenar a las nueve (мы обычно ужинаем в девять).\n'
            'В imperfecto — «раньше обычно»: De niño solía pasar el verano en el pueblo '
            '(в детстве я обычно проводил лето в деревне). Solía jugar al fútbol.\n\n'
            '2. SERVIR (e→i) — «служить, годиться; подавать»:\n'
            '  sirvo, sirves, sirve, servimos, servís, sirven\n'
            '• servir para — годиться для: Este cuchillo no sirve para nada (этот нож ни на '
            'что не годится). ¿Para qué sirve esto? (для чего это?);\n'
            '• servir de — служить чем-то: El sofá sirve de cama (диван служит кроватью);\n'
            '• в ресторане: ¿Qué le sirvo? (что вам подать?) La cena está servida (ужин подан);\n'
            '• вежливое: ¿En qué puedo servirle? (чем могу служить/помочь?).\n\n'
            '3. POCO — «мало» (противоположность mucho), согласуется с существительным:\n'
            '• poco tiempo (мало времени), poca gente (мало народу), pocos amigos, pocas veces '
            '(редко); после глагола не меняется: Duermo poco (я мало сплю);\n'
            '• UN poco de — «немного» (положительный оттенок): Hay un poco de pan (есть '
            'немного хлеба). Сравните: Tengo poco dinero (у меня мало денег — жалоба) / '
            'Tengo un poco de dinero (у меня есть немного денег — уже кое-что!);\n'
            '• poco + прилагательное = «мало-, не-»: poco interesante (малоинтересный), '
            'poco probable (маловероятный).\n\n'
            '4. SOLO — два разных слова:\n'
            '• прилагательное solo/sola — «один, одинокий»: Vive solo (он живёт один). '
            'Estaba sola en casa (она была дома одна);\n'
            '• наречие solo — «только» (= solamente): Solo quiero un café (я хочу только '
            'кофе). Solo quedan dos días (осталось только два дня).\n\n'
            '5. МИНИ-ДИАЛОГ:\n'
            '— ¿Qué sueles desayunar? (Что ты обычно ешь на завтрак?)\n'
            '— Solo un café y un poco de pan con tomate. (Только кофе и немного хлеба с '
            'томатом.)\n'
            '— ¡Qué poco! Yo no sirvo para trabajar sin un buen desayuno. (Как мало! Я не '
            'гожусь для работы без хорошего завтрака.)\n'
            '— Ya, pero suelo comer fuerte a mediodía. (Ну да, зато в полдень я обычно ем '
            'плотно.)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Спрягайте soler и servir', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (soler) levantarme a las siete.', 'options': ['suelo', 'solo', 'sole'], 'correct_answer': 'suelo',
             'translation': 'Обычно я встаю в семь.', 'explanation': 'o→ue: suelo.'},
            {'section': 'Упражнение 1. Спрягайте soler и servir', 'exercise_type': 'fill_blank',
             'prompt': '¿Qué ___ (soler, tú) hacer los domingos?', 'options': ['sueles', 'soles', 'suelas'], 'correct_answer': 'sueles',
             'translation': 'Что ты обычно делаешь по воскресеньям?', 'explanation': 'sueles.'},
            {'section': 'Упражнение 1. Спрягайте soler и servir', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ (soler) cenar a las nueve.', 'options': ['solemos', 'suelemos', 'suelen'], 'correct_answer': 'solemos',
             'translation': 'Мы обычно ужинаем в девять.', 'explanation': 'nosotros без чередования: solemos.'},
            {'section': 'Упражнение 1. Спрягайте soler и servir', 'exercise_type': 'fill_blank',
             'prompt': 'De niño ___ (soler, yo) jugar en la calle.', 'options': ['solía', 'suelía', 'solí'], 'correct_answer': 'solía',
             'translation': 'В детстве я обычно играл на улице.', 'explanation': '«Раньше обычно» → solía.'},
            {'section': 'Упражнение 1. Спрягайте soler и servir', 'exercise_type': 'fill_blank',
             'prompt': 'Este cuchillo no ___ (servir) para nada.', 'options': ['sirve', 'serve', 'sirva'], 'correct_answer': 'sirve',
             'translation': 'Этот нож ни на что не годится.', 'explanation': 'e→i: sirve.'},
            {'section': 'Упражнение 1. Спрягайте soler и servir', 'exercise_type': 'fill_blank',
             'prompt': '¿Para qué ___ (servir) esto?', 'options': ['sirve', 'serve', 'sirvo'], 'correct_answer': 'sirve',
             'translation': 'Для чего это?', 'explanation': '¿Para qué sirve?'},
            {'section': 'Упражнение 1. Спрягайте soler и servir', 'exercise_type': 'fill_blank',
             'prompt': 'El sofá ___ (servir) de cama.', 'options': ['sirve', 'serve', 'sirven'], 'correct_answer': 'sirve',
             'translation': 'Диван служит кроватью.', 'explanation': 'servir de.'},
            {'section': 'Упражнение 1. Спрягайте soler и servir', 'exercise_type': 'fill_blank',
             'prompt': '¿En qué puedo ___ (servir)le?', 'options': ['servir', 'sirvir', 'sirviendo'], 'correct_answer': 'servir',
             'translation': 'Чем могу вам помочь?', 'explanation': 'После poder — инфинитив.'},
            {'section': 'Упражнение 1. Спрягайте soler и servir', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ (soler) venir en tren.', 'options': ['suelen', 'solen', 'soléis'], 'correct_answer': 'suelen',
             'translation': 'Они обычно приезжают на поезде.', 'explanation': 'suelen.'},
            {'section': 'Упражнение 1. Спрягайте soler и servir', 'exercise_type': 'fill_blank',
             'prompt': 'Yo no ___ (servir) para mentir.', 'options': ['sirvo', 'servo', 'sirve'], 'correct_answer': 'sirvo',
             'translation': 'Я не гожусь для вранья (не умею врать).', 'explanation': '1 л.: sirvo.'},
            # 2
            {'section': 'Упражнение 2. Poco, un poco de, solo', 'exercise_type': 'multiple_choice',
             'prompt': 'Tengo ___ tiempo: date prisa.', 'options': ['poco', 'un poco', 'poca'], 'correct_answer': 'poco',
             'translation': 'У меня мало времени: поторопись.', 'explanation': 'poco + tiempo (м. р.).'},
            {'section': 'Упражнение 2. Poco, un poco de, solo', 'exercise_type': 'multiple_choice',
             'prompt': 'Hay ___ de pan en la cocina.', 'options': ['un poco', 'poco', 'pocos'], 'correct_answer': 'un poco',
             'translation': 'На кухне есть немного хлеба.', 'explanation': 'un poco de + вещество.'},
            {'section': 'Упражнение 2. Poco, un poco de, solo', 'exercise_type': 'multiple_choice',
             'prompt': 'Había ___ gente en la calle.', 'options': ['poca', 'poco', 'un poco'], 'correct_answer': 'poca',
             'translation': 'На улице было мало народу.', 'explanation': 'gente — ж. р.: poca.'},
            {'section': 'Упражнение 2. Poco, un poco de, solo', 'exercise_type': 'multiple_choice',
             'prompt': 'Duermo ___ últimamente.', 'options': ['poco', 'poca', 'pocos'], 'correct_answer': 'poco',
             'translation': 'В последнее время я мало сплю.', 'explanation': 'После глагола — poco.'},
            {'section': 'Упражнение 2. Poco, un poco de, solo', 'exercise_type': 'multiple_choice',
             'prompt': 'El libro es ___ interesante. (малоинтересный)', 'options': ['poco', 'un poco', 'pocos'], 'correct_answer': 'poco',
             'translation': 'Книга малоинтересная.', 'explanation': 'poco + прилагательное.'},
            {'section': 'Упражнение 2. Poco, un poco de, solo', 'exercise_type': 'multiple_choice',
             'prompt': 'Estoy ___ cansado, pero puedo seguir. (немного)', 'options': ['un poco', 'poco', 'poca'], 'correct_answer': 'un poco',
             'translation': 'Я немного устал, но могу продолжать.', 'explanation': 'un poco + прилагательное.'},
            {'section': 'Упражнение 2. Poco, un poco de, solo', 'exercise_type': 'multiple_choice',
             'prompt': 'Vive ___ desde enero. (один)', 'options': ['solo', 'sólo siempre', 'un solo'], 'correct_answer': 'solo',
             'translation': 'Он живёт один с января.', 'explanation': 'solo — один.'},
            {'section': 'Упражнение 2. Poco, un poco de, solo', 'exercise_type': 'multiple_choice',
             'prompt': '___ quiero un café. (только)', 'options': ['Solo', 'Un solo', 'Poco'], 'correct_answer': 'Solo',
             'translation': 'Я хочу только кофе.', 'explanation': 'solo = только.'},
            {'section': 'Упражнение 2. Poco, un poco de, solo', 'exercise_type': 'multiple_choice',
             'prompt': 'Ella estaba ___ en casa. (одна)', 'options': ['sola', 'solo', 'un poco'], 'correct_answer': 'sola',
             'translation': 'Она была дома одна.', 'explanation': 'ж. р.: sola.'},
            {'section': 'Упражнение 2. Poco, un poco de, solo', 'exercise_type': 'multiple_choice',
             'prompt': '___ quedan dos días. (только)', 'options': ['Solo', 'Sola', 'Poca'], 'correct_answer': 'Solo',
             'translation': 'Осталось только два дня.', 'explanation': 'Наречие solo не меняется.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Обычно я завтракаю дома.»',
             'options': ['Suelo desayunar en casa.', 'Solo desayunar en casa.', 'Suelo desayuno en casa.'],
             'correct_answer': 'Suelo desayunar en casa.', 'explanation': 'suelo + инфинитив.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Что вы обычно делаете летом?» (vosotros)',
             'options': ['¿Qué soléis hacer en verano?', '¿Qué suelen hacer en verano vosotros suelen?', '¿Qué soléis hacéis en verano?'],
             'correct_answer': '¿Qué soléis hacer en verano?', 'explanation': 'soléis + инфинитив.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Раньше он обычно ездил на велосипеде.»',
             'options': ['Solía ir en bici.', 'Suele ir en bici ayer.', 'Solía yendo en bici.'],
             'correct_answer': 'Solía ir en bici.', 'explanation': 'solía + инфинитив.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Для чего служит эта кнопка?»',
             'options': ['¿Para qué sirve este botón?', '¿De qué sirve este botón para?', '¿Para qué serve este botón?'],
             'correct_answer': '¿Para qué sirve este botón?', 'explanation': 'servir para.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Эта коробка служит столом.»',
             'options': ['Esta caja sirve de mesa.', 'Esta caja sirve para de mesa.', 'Esta caja serve de mesa.'],
             'correct_answer': 'Esta caja sirve de mesa.', 'explanation': 'servir de.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «У меня мало друзей, но хорошие.»',
             'options': ['Tengo pocos amigos, pero buenos.', 'Tengo poco amigos, pero buenos.', 'Tengo un poco de amigos, pero buenos.'],
             'correct_answer': 'Tengo pocos amigos, pero buenos.', 'explanation': 'pocos + amigos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Дай мне немного воды, пожалуйста.»',
             'options': ['Dame un poco de agua, por favor.', 'Dame poca agua, por favor siempre.', 'Dame un poco agua, por favor.'],
             'correct_answer': 'Dame un poco de agua, por favor.', 'explanation': 'un poco de + agua.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я живу один.»',
             'options': ['Vivo solo.', 'Vivo sólo un.', 'Vivo un solo.'],
             'correct_answer': 'Vivo solo.', 'explanation': 'solo — один.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я хочу только воды.»',
             'options': ['Solo quiero agua.', 'Sola quiero agua.', 'Poco quiero agua.'],
             'correct_answer': 'Solo quiero agua.', 'explanation': 'solo = только.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это маловероятно.»',
             'options': ['Es poco probable.', 'Es un poco probable.', 'Es poca probable.'],
             'correct_answer': 'Es poco probable.', 'explanation': 'poco + прилагательное.'},
        ],
    },
    {
        'n': 36, 'level': 'B1', 'title': 'Будущее время (Futuro imperfecto / futuro simple)',
        'theory': (
            '1. ОБРАЗОВАНИЕ. Футуро — редкий подарок: окончания добавляются к ЦЕЛОМУ '
            'инфинитиву и ОДИНАКОВЫ для всех трёх спряжений:\n'
            '  -é, -ás, -á, -emos, -éis, -án\n'
            '• hablar: hablaré, hablarás, hablará, hablaremos, hablaréis, hablarán;\n'
            '• comer: comeré, comerás…; vivir: viviré, vivirás…\n'
            '• Mañana te llamaré (завтра я тебе позвоню);\n'
            '• El año que viene viviremos en la costa (в следующем году мы будем жить на '
            'побережье);\n'
            '• ¿A qué hora llegarás? (во сколько ты приедешь?)\n\n'
            '2. ДВЕНАДЦАТЬ НЕПРАВИЛЬНЫХ ОСНОВ (окончания те же!):\n'
            '• tener → tendré, salir → saldré, poner → pondré, venir → vendré (выпадает '
            'гласная, появляется d);\n'
            '• poder → podré, saber → sabré, querer → querré, haber → habré, caber → cabré '
            '(выпадает гласная);\n'
            '• hacer → haré, decir → diré (особые короткие основы).\n'
            '• Te lo diré mañana (я скажу тебе это завтра). No podré venir (я не смогу '
            'прийти). Tendrás que esperar (тебе придётся подождать). Habrá mucha gente '
            '(будет много народу).\n\n'
            '3. УПОТРЕБЛЕНИЕ:\n'
            '• будущие действия и планы: Este verano viajaremos por Andalucía;\n'
            '• обещания: Te prometo que lo haré (обещаю, что сделаю это);\n'
            '• прогнозы: Mañana lloverá en el norte (завтра на севере будет дождь);\n'
            '• ПРЕДПОЛОЖЕНИЕ О НАСТОЯЩЕМ (очень испанская черта!): ¿Qué hora será? — Serán '
            'las tres (который, интересно, час? — наверное, часа три). ¿Dónde estará Juan? '
            '(где же может быть Хуан?) Estará en el trabajo (наверное, на работе).\n\n'
            '4. МАРКЕРЫ БУДУЩЕГО: mañana, pasado mañana, la semana que viene / la próxima '
            'semana, el mes que viene, dentro de una semana (через неделю): Dentro de un mes '
            'me mudaré (через месяц я перееду).\n'
            'Напоминание: для ближайших планов жив и ir a + инфинитив: Voy a llamarte esta '
            'noche ≈ Te llamaré esta noche.\n\n'
            '5. МИНИ-ДИАЛОГ:\n'
            '— ¿Qué harás el año que viene? (Что ты будешь делать в следующем году?)\n'
            '— Terminaré el curso y buscaré trabajo en España. (Закончу курс и буду искать '
            'работу в Испании.)\n'
            '— ¿Y dónde vivirás? (А где будешь жить?)\n'
            '— Todavía no lo sé. ¡Ya se verá! (Ещё не знаю. Там видно будет!)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Правильное futuro', 'exercise_type': 'fill_blank',
             'prompt': 'Mañana te ___ (llamar, yo).', 'options': ['llamaré', 'llamo', 'llamaría'], 'correct_answer': 'llamaré',
             'translation': 'Завтра я тебе позвоню.', 'explanation': 'llamar + é.'},
            {'section': 'Упражнение 1. Правильное futuro', 'exercise_type': 'fill_blank',
             'prompt': '¿A qué hora ___ (llegar, tú)?', 'options': ['llegarás', 'llegas', 'llegaste'], 'correct_answer': 'llegarás',
             'translation': 'Во сколько ты приедешь?', 'explanation': 'llegar + ás.'},
            {'section': 'Упражнение 1. Правильное futuro', 'exercise_type': 'fill_blank',
             'prompt': 'El año que viene ___ (vivir, nosotros) en la costa.', 'options': ['viviremos', 'vivimos', 'vivíamos'], 'correct_answer': 'viviremos',
             'translation': 'В следующем году мы будем жить на побережье.', 'explanation': 'vivir + emos.'},
            {'section': 'Упражнение 1. Правильное futuro', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ (volver) el domingo.', 'options': ['volverán', 'vuelven ya', 'volvieron'], 'correct_answer': 'volverán',
             'translation': 'Они вернутся в воскресенье.', 'explanation': 'volver + án.'},
            {'section': 'Упражнение 1. Правильное futuro', 'exercise_type': 'fill_blank',
             'prompt': 'Mañana ___ (llover) en el norte.', 'options': ['lloverá', 'llueve', 'llovió'], 'correct_answer': 'lloverá',
             'translation': 'Завтра на севере будет дождь.', 'explanation': 'Прогноз → lloverá.'},
            {'section': 'Упражнение 1. Правильное futuro', 'exercise_type': 'fill_blank',
             'prompt': 'Te prometo que lo ___ (terminar, yo).', 'options': ['terminaré', 'termino', 'terminaba'], 'correct_answer': 'terminaré',
             'translation': 'Обещаю тебе, что закончу это.', 'explanation': 'Обещание → futuro.'},
            {'section': 'Упражнение 1. Правильное futuro', 'exercise_type': 'fill_blank',
             'prompt': 'Dentro de un mes me ___ (mudar, yo).', 'options': ['mudaré', 'mudo', 'mudé'], 'correct_answer': 'mudaré',
             'translation': 'Через месяц я перееду.', 'explanation': 'dentro de → futuro.'},
            {'section': 'Упражнение 1. Правильное futuro', 'exercise_type': 'fill_blank',
             'prompt': '¿ ___ (estudiar, vosotros) juntos mañana?', 'options': ['Estudiaréis', 'Estudiáis', 'Estudiasteis'], 'correct_answer': 'Estudiaréis',
             'translation': 'Вы будете завтра заниматься вместе?', 'explanation': '2 л. мн.: -éis.'},
            {'section': 'Упражнение 1. Правильное futuro', 'exercise_type': 'fill_blank',
             'prompt': 'La fiesta ___ (empezar) a las diez.', 'options': ['empezará', 'empieza ayer', 'empezó'], 'correct_answer': 'empezará',
             'translation': 'Праздник начнётся в десять.', 'explanation': 'empezar + á.'},
            {'section': 'Упражнение 1. Правильное futuro', 'exercise_type': 'fill_blank',
             'prompt': 'Este verano ___ (viajar, nosotros) por Andalucía.', 'options': ['viajaremos', 'viajamos ayer', 'viajábamos'], 'correct_answer': 'viajaremos',
             'translation': 'Этим летом мы будем путешествовать по Андалусии.', 'explanation': 'viajar + emos.'},
            # 2
            {'section': 'Упражнение 2. Неправильные основы. Предположение', 'exercise_type': 'fill_blank',
             'prompt': 'No ___ (poder, yo) venir mañana.', 'options': ['podré', 'poderé', 'puedo'], 'correct_answer': 'podré',
             'translation': 'Я не смогу прийти завтра.', 'explanation': 'poder → podr-.'},
            {'section': 'Упражнение 2. Неправильные основы. Предположение', 'exercise_type': 'fill_blank',
             'prompt': '___ (tener, tú) que esperar un poco.', 'options': ['Tendrás', 'Tenerás', 'Tienes'], 'correct_answer': 'Tendrás',
             'translation': 'Тебе придётся немного подождать.', 'explanation': 'tener → tendr-.'},
            {'section': 'Упражнение 2. Неправильные основы. Предположение', 'exercise_type': 'fill_blank',
             'prompt': 'Te lo ___ (decir, yo) mañana.', 'options': ['diré', 'deciré', 'digo'], 'correct_answer': 'diré',
             'translation': 'Я скажу тебе это завтра.', 'explanation': 'decir → dir-.'},
            {'section': 'Упражнение 2. Неправильные основы. Предположение', 'exercise_type': 'fill_blank',
             'prompt': '¿Qué ___ (hacer, nosotros) sin ti?', 'options': ['haremos', 'haceremos', 'hacemos'], 'correct_answer': 'haremos',
             'translation': 'Что мы будем делать без тебя?', 'explanation': 'hacer → har-.'},
            {'section': 'Упражнение 2. Неправильные основы. Предположение', 'exercise_type': 'fill_blank',
             'prompt': '___ (haber) mucha gente en el concierto.', 'options': ['Habrá', 'Haberá', 'Hay'], 'correct_answer': 'Habrá',
             'translation': 'На концерте будет много народу.', 'explanation': 'haber → habrá.'},
            {'section': 'Упражнение 2. Неправильные основы. Предположение', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ (venir) en tren.', 'options': ['vendrán', 'venirán', 'vienen ya'], 'correct_answer': 'vendrán',
             'translation': 'Они приедут на поезде.', 'explanation': 'venir → vendr-.'},
            {'section': 'Упражнение 2. Неправильные основы. Предположение', 'exercise_type': 'fill_blank',
             'prompt': '¿A qué hora ___ (salir, tú)?', 'options': ['saldrás', 'salirás', 'sales ayer'], 'correct_answer': 'saldrás',
             'translation': 'Во сколько ты выйдешь?', 'explanation': 'salir → saldr-.'},
            {'section': 'Упражнение 2. Неправильные основы. Предположение', 'exercise_type': 'fill_blank',
             'prompt': 'Mañana lo ___ (saber, nosotros) todo.', 'options': ['sabremos', 'saberemos', 'sabemos ya'], 'correct_answer': 'sabremos',
             'translation': 'Завтра мы всё узнаем.', 'explanation': 'saber → sabr-.'},
            {'section': 'Упражнение 2. Неправильные основы. Предположение', 'exercise_type': 'multiple_choice',
             'prompt': '¿Qué hora será? — ___ las tres. (наверное)', 'options': ['Serán', 'Son', 'Fueron'], 'correct_answer': 'Serán',
             'translation': 'Который, интересно, час? — Наверное, часа три.', 'explanation': 'Futuro = предположение.'},
            {'section': 'Упражнение 2. Неправильные основы. Предположение', 'exercise_type': 'multiple_choice',
             'prompt': '¿Dónde está Juan? — ___ en el trabajo. (наверное)', 'options': ['Estará', 'Está', 'Estuvo'], 'correct_answer': 'Estará',
             'translation': 'Где Хуан? — Наверное, на работе.', 'explanation': 'Предположение о настоящем → futuro.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Завтра я тебе позвоню.»',
             'options': ['Mañana te llamaré.', 'Mañana te llamo ayer.', 'Mañana te llamaría.'],
             'correct_answer': 'Mañana te llamaré.', 'explanation': 'llamaré.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я не смогу прийти.»',
             'options': ['No podré venir.', 'No poderé venir.', 'No puedo veniré.'],
             'correct_answer': 'No podré venir.', 'explanation': 'podr- + é.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я скажу тебе это позже.»',
             'options': ['Te lo diré más tarde.', 'Te lo deciré más tarde.', 'Te diré lo más tarde.'],
             'correct_answer': 'Te lo diré más tarde.', 'explanation': 'te lo + diré.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Что ты будешь делать в выходные?»',
             'options': ['¿Qué harás el fin de semana?', '¿Qué hacerás el fin de semana?', '¿Qué haces el fin de semana pasado?'],
             'correct_answer': '¿Qué harás el fin de semana?', 'explanation': 'har- + ás.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Тебе придётся подождать.»',
             'options': ['Tendrás que esperar.', 'Tenerás que esperar.', 'Tienes que esperarás.'],
             'correct_answer': 'Tendrás que esperar.', 'explanation': 'tendr- + ás + que.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Будет много народу.»',
             'options': ['Habrá mucha gente.', 'Haberá mucha gente.', 'Habrán mucha gente.'],
             'correct_answer': 'Habrá mucha gente.', 'explanation': 'habrá — одна форма.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Через неделю мы всё узнаем.»',
             'options': ['Dentro de una semana lo sabremos todo.', 'En una semana dentro lo saberemos todo.', 'Dentro una semana lo sabremos todo.'],
             'correct_answer': 'Dentro de una semana lo sabremos todo.', 'explanation': 'dentro de + sabremos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Они приедут в следующем месяце.»',
             'options': ['Vendrán el mes que viene.', 'Venirán el mes que viene.', 'Vienen el mes pasado.'],
             'correct_answer': 'Vendrán el mes que viene.', 'explanation': 'vendr- + án.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Наверное, сейчас часа два.» (предположение)',
             'options': ['Serán las dos.', 'Son las dos seguro que sí.', 'Fueron las dos.'],
             'correct_answer': 'Serán las dos.', 'explanation': 'Futuro-предположение.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Обещаю, что сделаю это.»',
             'options': ['Prometo que lo haré.', 'Prometo que lo haceré.', 'Prometo que lo hago ayer.'],
             'correct_answer': 'Prometo que lo haré.', 'explanation': 'haré.'},
        ],
    },
]
B1_FULL = B1_FULL + _D3
