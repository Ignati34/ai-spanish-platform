# -*- coding: utf-8 -*-
"""Upgraded A1 lessons 7–9 (full theory + 3 exercise blocks of 10 items with translations)."""

A1_FULL_2 = [
    {
        'n': 7, 'level': 'A1', 'title': 'Множественное число существительных и прилагательных',
        'theory': (
            'Множественное число существительных образуется по трём основным правилам:\n\n'
            '1. Слово оканчивается на БЕЗУДАРНУЮ ГЛАСНУЮ → добавляется -s:\n'
            '  la casa → las casas (дома), el coche → los coches (машины), el estudiante → los '
            'estudiantes.\n\n'
            '2. Слово оканчивается на СОГЛАСНУЮ (а также на ударную -í/-ú у ряда слов) → '
            'добавляется -es:\n'
            '  el profesor → los profesores, la ciudad → las ciudades (города), el español → '
            'los españoles.\n\n'
            '3. Слово оканчивается на -z → z меняется на c и добавляется -es:\n'
            '  el lápiz → los lápices (карандаши), la vez → las veces (разы), la luz → las luces (огни).\n\n'
            '4. Особые случаи:\n'
            '• слова, оканчивающиеся на безударный слог с -s, во мн. числе НЕ меняются — меняется '
            'только артикль: el lunes → los lunes (понедельники), la crisis → las crisis;\n'
            '• при образовании мн. числа может исчезать или появляться тильда, чтобы сохранить '
            'место ударения: la canción → las canciones, el joven → los jóvenes (молодые люди);\n'
            '• смешанная группа лиц обозначается мужским родом: los padres (родители: отец и мать), '
            'los hermanos (братья и сёстры).\n\n'
            '5. Артикли во множественном числе: el → los, la → las; un → unos, una → unas.\n\n'
            '6. Прилагательные образуют множественное число по тем же правилам и согласуются '
            'с существительным: el coche rojo → los coches rojos; la casa grande → las casas grandes; '
            'el examen difícil → los exámenes difíciles.\n\n'
            '7. Вопрос о количестве — cuánto, который согласуется как прилагательное: '
            '¿Cuánto pan? (сколько хлеба?), ¿Cuánta agua?, ¿Cuántos libros?, ¿Cuántas casas? '
            'Счёт до пяти: uno, dos, tres, cuatro, cinco. Обратите внимание: uno перед '
            'существительным мужского рода усекается — un libro, но: Tengo uno (у меня один).'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Образуйте множественное число', 'exercise_type': 'multiple_choice',
             'prompt': 'la casa →', 'options': ['las casas', 'las cases', 'los casas'], 'correct_answer': 'las casas',
             'translation': 'casa — дом', 'explanation': 'Гласная → +s.'},
            {'section': 'Упражнение 1. Образуйте множественное число', 'exercise_type': 'multiple_choice',
             'prompt': 'el profesor →', 'options': ['los profesors', 'los profesores', 'las profesores'], 'correct_answer': 'los profesores',
             'translation': 'profesor — преподаватель', 'explanation': 'Согласная → +es.'},
            {'section': 'Упражнение 1. Образуйте множественное число', 'exercise_type': 'multiple_choice',
             'prompt': 'el lápiz →', 'options': ['los lápizes', 'los lápices', 'los lápizs'], 'correct_answer': 'los lápices',
             'translation': 'lápiz — карандаш', 'explanation': '-z → -ces.'},
            {'section': 'Упражнение 1. Образуйте множественное число', 'exercise_type': 'multiple_choice',
             'prompt': 'la ciudad →', 'options': ['las ciudads', 'las ciudades', 'los ciudades'], 'correct_answer': 'las ciudades',
             'translation': 'ciudad — город', 'explanation': 'Согласная → +es.'},
            {'section': 'Упражнение 1. Образуйте множественное число', 'exercise_type': 'multiple_choice',
             'prompt': 'el lunes →', 'options': ['los luneses', 'los lunes', 'las lunes'], 'correct_answer': 'los lunes',
             'translation': 'lunes — понедельник', 'explanation': 'Безударный -s: меняется только артикль.'},
            {'section': 'Упражнение 1. Образуйте множественное число', 'exercise_type': 'multiple_choice',
             'prompt': 'la canción →', 'options': ['las canciónes', 'las canciones', 'los canciones'], 'correct_answer': 'las canciones',
             'translation': 'canción — песня', 'explanation': 'Тильда исчезает: canciones.'},
            {'section': 'Упражнение 1. Образуйте множественное число', 'exercise_type': 'multiple_choice',
             'prompt': 'la vez →', 'options': ['las veces', 'las vezes', 'los veces'], 'correct_answer': 'las veces',
             'translation': 'vez — раз', 'explanation': '-z → -ces: veces.'},
            {'section': 'Упражнение 1. Образуйте множественное число', 'exercise_type': 'multiple_choice',
             'prompt': 'el joven →', 'options': ['los jovenes', 'los jóvenes', 'las jóvenes'], 'correct_answer': 'los jóvenes',
             'translation': 'joven — молодой человек', 'explanation': 'Появляется тильда: jóvenes.'},
            {'section': 'Упражнение 1. Образуйте множественное число', 'exercise_type': 'multiple_choice',
             'prompt': 'el coche →', 'options': ['los coches', 'los cochees', 'las coches'], 'correct_answer': 'los coches',
             'translation': 'coche — машина', 'explanation': 'Гласная → +s.'},
            {'section': 'Упражнение 1. Образуйте множественное число', 'exercise_type': 'multiple_choice',
             'prompt': 'la crisis →', 'options': ['las crisises', 'las crisis', 'los crisis'], 'correct_answer': 'las crisis',
             'translation': 'crisis — кризис', 'explanation': 'Не меняется: las crisis.'},
            # 2
            {'section': 'Упражнение 2. Согласуйте во множественном числе', 'exercise_type': 'fill_blank',
             'prompt': 'Los coches ___ (rojo).', 'options': ['rojos', 'rojas', 'rojo'], 'correct_answer': 'rojos',
             'translation': 'Красные машины.', 'explanation': 'м. р. мн.: rojos.'},
            {'section': 'Упражнение 2. Согласуйте во множественном числе', 'exercise_type': 'fill_blank',
             'prompt': 'Las casas ___ (grande).', 'options': ['grandes', 'grandas', 'grande'], 'correct_answer': 'grandes',
             'translation': 'Большие дома.', 'explanation': '-e → +s: grandes.'},
            {'section': 'Упражнение 2. Согласуйте во множественном числе', 'exercise_type': 'fill_blank',
             'prompt': 'Los exámenes ___ (difícil).', 'options': ['difíciles', 'difícils', 'difícil'], 'correct_answer': 'difíciles',
             'translation': 'Трудные экзамены.', 'explanation': 'Согласная → +es.'},
            {'section': 'Упражнение 2. Согласуйте во множественном числе', 'exercise_type': 'fill_blank',
             'prompt': '¿___ libros tienes?', 'options': ['Cuántos', 'Cuántas', 'Cuánto'], 'correct_answer': 'Cuántos',
             'translation': 'Сколько у тебя книг?', 'explanation': 'libros — м. р. мн.: cuántos.'},
            {'section': 'Упражнение 2. Согласуйте во множественном числе', 'exercise_type': 'fill_blank',
             'prompt': '¿___ agua bebes?', 'options': ['Cuánto', 'Cuánta', 'Cuántas'], 'correct_answer': 'Cuánta',
             'translation': 'Сколько воды ты пьёшь?', 'explanation': 'agua — ж. р.: cuánta.'},
            {'section': 'Упражнение 2. Согласуйте во множественном числе', 'exercise_type': 'fill_blank',
             'prompt': '___ estudiantes son españoles. (артикль)', 'options': ['Los', 'Las', 'Unos las'], 'correct_answer': 'Los',
             'translation': 'Студенты — испанцы.', 'explanation': 'м. р. мн.: los.'},
            {'section': 'Упражнение 2. Согласуйте во множественном числе', 'exercise_type': 'fill_blank',
             'prompt': 'Tengo ___ amigas. (несколько)', 'options': ['unas', 'unos', 'una'], 'correct_answer': 'unas',
             'translation': 'У меня есть несколько подруг.', 'explanation': 'ж. р. мн.: unas.'},
            {'section': 'Упражнение 2. Согласуйте во множественном числе', 'exercise_type': 'fill_blank',
             'prompt': 'Las ciudades ___ (bonito).', 'options': ['bonitas', 'bonitos', 'bonita'], 'correct_answer': 'bonitas',
             'translation': 'Красивые города.', 'explanation': 'ж. р. мн.: bonitas.'},
            {'section': 'Упражнение 2. Согласуйте во множественном числе', 'exercise_type': 'fill_blank',
             'prompt': 'Los días son ___ (largo).', 'options': ['largos', 'largas', 'largo'], 'correct_answer': 'largos',
             'translation': 'Дни длинные.', 'explanation': 'los días — м. р. мн.'},
            {'section': 'Упражнение 2. Согласуйте во множественном числе', 'exercise_type': 'fill_blank',
             'prompt': '¿___ hermanas tienes?', 'options': ['Cuántas', 'Cuántos', 'Cuánta'], 'correct_answer': 'Cuántas',
             'translation': 'Сколько у тебя сестёр?', 'explanation': 'hermanas — ж. р. мн.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «белые дома»',
             'options': ['las casas blancas', 'las casas blancos', 'los casas blancas'],
             'correct_answer': 'las casas blancas', 'explanation': 'ж. р. мн.: las … blancas.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «карандаши»',
             'options': ['los lápices', 'los lápizes', 'las lápices'],
             'correct_answer': 'los lápices', 'explanation': '-z → -ces.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Сколько стоят книги?» (досл. «сколько стоят»)',
             'options': ['¿Cuánto cuestan los libros?', '¿Cuántos cuestan los libros?', '¿Cuánto cuesta los libros?'],
             'correct_answer': '¿Cuánto cuestan los libros?', 'explanation': 'cuánto при глаголе не меняется; глагол во мн. ч.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «По понедельникам я работаю.»',
             'options': ['Los lunes trabajo.', 'Los luneses trabajo.', 'El lunes trabajos.'],
             'correct_answer': 'Los lunes trabajo.', 'explanation': 'los lunes = по понедельникам.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «трудные города» (шутл.: «трудные экзамены»)',
             'options': ['los exámenes difíciles', 'los exámenes difícils', 'las exámenes difíciles'],
             'correct_answer': 'los exámenes difíciles', 'explanation': 'Согласная → +es у обоих слов.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «У меня три брата.»',
             'options': ['Tengo tres hermanos.', 'Tengo tres hermanoes.', 'Tengo hermanos tres.'],
             'correct_answer': 'Tengo tres hermanos.', 'explanation': 'Числительное перед сущ.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «песни»',
             'options': ['las canciones', 'las canciónes', 'los canciones'],
             'correct_answer': 'las canciones', 'explanation': 'Тильда уходит: canciones.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «молодые люди»',
             'options': ['los jóvenes', 'los jovenes', 'las jóvenes hombres'],
             'correct_answer': 'los jóvenes', 'explanation': 'Тильда появляется: jóvenes.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Сколько окон в доме?»',
             'options': ['¿Cuántas ventanas hay en la casa?', '¿Cuántos ventanas hay en la casa?', '¿Cuánta ventanas hay en la casa?'],
             'correct_answer': '¿Cuántas ventanas hay en la casa?', 'explanation': 'ventanas — ж. р. мн.: cuántas + hay.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «несколько раз»',
             'options': ['unas veces', 'unas vezes', 'unos veces'],
             'correct_answer': 'unas veces', 'explanation': 'la vez → unas veces.'},
        ],
    },
    {
        'n': 8, 'level': 'A1', 'title': 'Опущение артикля',
        'theory': (
            'Существительное нередко употребляется вовсе без артикля — это называют нулевым '
            'артиклем. Отсутствие артикля тоже несёт смысл: предмет берётся неопределённо, как '
            'категория или вещество, а не как конкретная вещь. Основные случаи:\n\n'
            '1. Профессия, национальность, род занятий после ser: Soy médico (я врач). Es profesora. '
            'Son estudiantes. НО: если есть определение, появляется артикль неопределённый: '
            'Es un buen médico (он хороший врач). Es una profesora excelente.\n\n'
            '2. Неисчисляемые вещества и неопределённое количество после глагола: Bebo agua (пью '
            'воду), Como pan (ем хлеб), ¿Tienes dinero? (у тебя есть деньги?). Сравните: '
            'El pan está en la mesa (тот самый хлеб — с артиклем).\n\n'
            '3. Существительное во множественном числе в общем, неопределённом значении: '
            'Compro libros (покупаю книги — вообще), Tiene amigos en Madrid.\n\n'
            '4. Большинство стран и городов: Vivo en España. Trabajo en Madrid. Vengo de Rusia. '
            '(исключения-страны с артиклем встречаются, но их немного).\n\n'
            '5. Устойчивые сочетания с предлогами: en casa (дома), a casa (домой), en clase '
            '(на занятии), por favor (пожалуйста), de memoria (наизусть), a pie (пешком), '
            'en coche (на машине).\n\n'
            '6. При обращении: ¡Buenos días, señor García! (но о нём же в рассказе — с артиклем: '
            'El señor García trabaja aquí).\n\n'
            '7. После haber (hay) вещество и неопределённое мн. число идут без артикля: '
            'Hay pan. Hay flores en el jarrón (в вазе цветы).\n\n'
            'Итог-ориентир: конкретный известный предмет → el/la; один из многих, впервые → un/una; '
            'категория, вещество, профессия, устойчивый оборот → без артикля.'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Нужен ли артикль?', 'exercise_type': 'multiple_choice',
             'prompt': 'Soy ___ médico.', 'options': ['un', '— (без артикля)', 'el'], 'correct_answer': '— (без артикля)',
             'translation': 'Я врач.', 'explanation': 'Профессия после ser — без артикля.'},
            {'section': 'Упражнение 1. Нужен ли артикль?', 'exercise_type': 'multiple_choice',
             'prompt': 'Es ___ buen médico.', 'options': ['un', '— (без артикля)', 'el'], 'correct_answer': 'un',
             'translation': 'Он хороший врач.', 'explanation': 'С определением артикль возвращается.'},
            {'section': 'Упражнение 1. Нужен ли артикль?', 'exercise_type': 'multiple_choice',
             'prompt': 'Bebo ___ agua.', 'options': ['el', 'una', '— (без артикля)'], 'correct_answer': '— (без артикля)',
             'translation': 'Я пью воду.', 'explanation': 'Вещество, неопр. количество.'},
            {'section': 'Упражнение 1. Нужен ли артикль?', 'exercise_type': 'multiple_choice',
             'prompt': '___ pan está en la mesa.', 'options': ['El', '— (без артикля)', 'Un'], 'correct_answer': 'El',
             'translation': 'Хлеб (тот самый) на столе.', 'explanation': 'Конкретный известный → el.'},
            {'section': 'Упражнение 1. Нужен ли артикль?', 'exercise_type': 'multiple_choice',
             'prompt': 'Vivo en ___ España.', 'options': ['la', '— (без артикля)', 'una'], 'correct_answer': '— (без артикля)',
             'translation': 'Я живу в Испании.', 'explanation': 'Страны обычно без артикля.'},
            {'section': 'Упражнение 1. Нужен ли артикль?', 'exercise_type': 'multiple_choice',
             'prompt': 'Estoy en ___ casa.', 'options': ['la', '— (без артикля)', 'una'], 'correct_answer': '— (без артикля)',
             'translation': 'Я дома.', 'explanation': 'Оборот en casa — без артикля.'},
            {'section': 'Упражнение 1. Нужен ли артикль?', 'exercise_type': 'multiple_choice',
             'prompt': 'Compro ___ libros. (вообще)', 'options': ['los', 'unos', '— (без артикля)'], 'correct_answer': '— (без артикля)',
             'translation': 'Я покупаю книги.', 'explanation': 'Неопределённое мн. ч. — без артикля.'},
            {'section': 'Упражнение 1. Нужен ли артикль?', 'exercise_type': 'multiple_choice',
             'prompt': '¿Tienes ___ dinero?', 'options': ['el', '— (без артикля)', 'un'], 'correct_answer': '— (без артикля)',
             'translation': 'У тебя есть деньги?', 'explanation': 'Вещество/неопр. количество.'},
            {'section': 'Упражнение 1. Нужен ли артикль?', 'exercise_type': 'multiple_choice',
             'prompt': 'Voy a la escuela ___ pie.', 'options': ['a', 'al', 'en el'], 'correct_answer': 'a',
             'translation': 'Я иду в школу пешком.', 'explanation': 'Оборот a pie — без артикля.'},
            {'section': 'Упражнение 1. Нужен ли артикль?', 'exercise_type': 'multiple_choice',
             'prompt': 'Buenos días, ___ señora López.', 'options': ['la', '— (без артикля)', 'una'], 'correct_answer': '— (без артикля)',
             'translation': 'Добрый день, сеньора Лопес!', 'explanation': 'При обращении — без артикля.'},
            # 2
            {'section': 'Упражнение 2. Выберите правильный вариант', 'exercise_type': 'multiple_choice',
             'prompt': '«Она учительница.»', 'options': ['Es profesora.', 'Es una profesora.'], 'correct_answer': 'Es profesora.',
             'translation': 'profesora — учительница', 'explanation': 'Профессия без определения — без артикля.'},
            {'section': 'Упражнение 2. Выберите правильный вариант', 'exercise_type': 'multiple_choice',
             'prompt': '«Она отличная учительница.»', 'options': ['Es profesora excelente.', 'Es una profesora excelente.'],
             'correct_answer': 'Es una profesora excelente.', 'translation': 'excelente — отличный',
             'explanation': 'С определением — un/una.'},
            {'section': 'Упражнение 2. Выберите правильный вариант', 'exercise_type': 'multiple_choice',
             'prompt': '«Есть хлеб?»', 'options': ['¿Hay pan?', '¿Hay el pan?'], 'correct_answer': '¿Hay pan?',
             'translation': 'pan — хлеб', 'explanation': 'После hay вещество без артикля.'},
            {'section': 'Упражнение 2. Выберите правильный вариант', 'exercise_type': 'multiple_choice',
             'prompt': '«Я еду домой.»', 'options': ['Voy a casa.', 'Voy a la casa.'], 'correct_answer': 'Voy a casa.',
             'translation': 'a casa — домой', 'explanation': 'Оборот a casa — без артикля.'},
            {'section': 'Упражнение 2. Выберите правильный вариант', 'exercise_type': 'multiple_choice',
             'prompt': '«Я работаю в Мадриде.»', 'options': ['Trabajo en Madrid.', 'Trabajo en el Madrid.'], 'correct_answer': 'Trabajo en Madrid.',
             'translation': 'Madrid — Мадрид', 'explanation': 'Города без артикля.'},
            {'section': 'Упражнение 2. Выберите правильный вариант', 'exercise_type': 'multiple_choice',
             'prompt': '«Я знаю это наизусть.»', 'options': ['Lo sé de memoria.', 'Lo sé de la memoria.'], 'correct_answer': 'Lo sé de memoria.',
             'translation': 'de memoria — наизусть', 'explanation': 'Устойчивый оборот.'},
            {'section': 'Упражнение 2. Выберите правильный вариант', 'exercise_type': 'multiple_choice',
             'prompt': '«У него есть друзья в Мадриде.»', 'options': ['Tiene amigos en Madrid.', 'Tiene los amigos en Madrid.'],
             'correct_answer': 'Tiene amigos en Madrid.', 'translation': 'amigos — друзья', 'explanation': 'Неопр. мн. ч. — без артикля.'},
            {'section': 'Упражнение 2. Выберите правильный вариант', 'exercise_type': 'multiple_choice',
             'prompt': '«Мы едем на машине.»', 'options': ['Vamos en coche.', 'Vamos en el coche.'], 'correct_answer': 'Vamos en coche.',
             'translation': 'en coche — на машине', 'explanation': 'Способ передвижения — без артикля.'},
            {'section': 'Упражнение 2. Выберите правильный вариант', 'exercise_type': 'multiple_choice',
             'prompt': '«Сеньор Гарсия работает здесь.» (о нём)', 'options': ['Señor García trabaja aquí.', 'El señor García trabaja aquí.'],
             'correct_answer': 'El señor García trabaja aquí.', 'translation': 'trabaja — работает',
             'explanation': 'О человеке с титулом — с артиклем.'},
            {'section': 'Упражнение 2. Выберите правильный вариант', 'exercise_type': 'multiple_choice',
             'prompt': '«В вазе цветы.»', 'options': ['Hay flores en el jarrón.', 'Hay las flores en el jarrón.'],
             'correct_answer': 'Hay flores en el jarrón.', 'translation': 'flores — цветы', 'explanation': 'hay + неопр. мн. ч.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я студент.»',
             'options': ['Soy estudiante.', 'Soy un estudiante.', 'Estoy estudiante.'],
             'correct_answer': 'Soy estudiante.', 'explanation': 'Род занятий — без артикля.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я ем хлеб.» (вообще)',
             'options': ['Como pan.', 'Como el pan.', 'Como un pan.'],
             'correct_answer': 'Como pan.', 'explanation': 'Вещество — без артикля.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы дома.»',
             'options': ['Estamos en casa.', 'Estamos en la casa.', 'Somos en casa.'],
             'correct_answer': 'Estamos en casa.', 'explanation': 'en casa — устойчиво, без артикля.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Она из России.»',
             'options': ['Es de Rusia.', 'Es de la Rusia.', 'Está de Rusia.'],
             'correct_answer': 'Es de Rusia.', 'explanation': 'Страна — без артикля; происхождение → ser de.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он хороший преподаватель.»',
             'options': ['Es un buen profesor.', 'Es buen profesor un.', 'Es bueno profesor.'],
             'correct_answer': 'Es un buen profesor.', 'explanation': 'С определением — un; buen перед сущ.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Есть вода?»',
             'options': ['¿Hay agua?', '¿Hay el agua?', '¿Está agua?'],
             'correct_answer': '¿Hay agua?', 'explanation': 'hay + вещество без артикля.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Пожалуйста!»',
             'options': ['Por favor.', 'Por el favor.', 'Para favor.'],
             'correct_answer': 'Por favor.', 'explanation': 'Устойчивое сочетание.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я иду пешком.»',
             'options': ['Voy a pie.', 'Voy al pie.', 'Voy en pie.'],
             'correct_answer': 'Voy a pie.', 'explanation': 'a pie — пешком.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Хлеб на столе.» (тот самый)',
             'options': ['El pan está en la mesa.', 'Pan está en la mesa.', 'Hay el pan en la mesa.'],
             'correct_answer': 'El pan está en la mesa.', 'explanation': 'Конкретный → el + está.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Они врачи.»',
             'options': ['Son médicos.', 'Son unos médicos.', 'Están médicos.'],
             'correct_answer': 'Son médicos.', 'explanation': 'Профессия во мн. ч. — тоже без артикля.'},
        ],
    },
    {
        'n': 9, 'level': 'A1', 'title': 'Личные местоимения. I спряжение (-ar)',
        'theory': (
            '1. Личные местоимения-подлежащие:\n'
            '• yo — я; tú — ты; él — он; ella — она; usted — Вы (вежливо, к одному человеку);\n'
            '• nosotros/nosotras — мы; vosotros/vosotras — вы (к нескольким «на ты», Испания); '
            'ellos/ellas — они; ustedes — Вы (к нескольким; в Латинской Америке — любое «вы» мн. ч.).\n\n'
            'Важно: usted и ustedes сочетаются с глаголом в ТРЕТЬЕМ лице: ¿Habla usted español? '
            '(Вы говорите по-испански?)\n\n'
            '2. Местоимение-подлежащее обычно ОПУСКАЕТСЯ, потому что окончание глагола уже '
            'показывает лицо и число: Hablo español (я говорю по-испански). Местоимение ставят '
            'для контраста или уточнения: Yo trabajo y tú descansas (я работаю, а ты отдыхаешь).\n\n'
            '3. Испанские глаголы делятся на три спряжения по окончанию инфинитива: -ar, -er, -ir. '
            'Первое спряжение (-ar) — самое многочисленное. Настоящее время (presente de '
            'indicativo) образуется заменой -ar на личные окончания:\n\n'
            '  hablar (говорить): hablo, hablas, habla, hablamos, habláis, hablan\n\n'
            'Так же спрягаются: trabajar (работать), estudiar (учиться), comprar (покупать), '
            'escuchar (слушать), mirar (смотреть), cantar (петь), bailar (танцевать), '
            'descansar (отдыхать), preguntar (спрашивать), contestar (отвечать).\n\n'
            '4. Настоящее время означает и действие сейчас, и регулярное действие: Trabajo en un '
            'banco (я работаю в банке). Estudiamos español (мы учим испанский). María canta muy '
            'bien (Мария очень хорошо поёт).\n\n'
            '5. Вопрос и отрицание с -ar глаголами строятся как обычно: ¿Trabajas aquí? — No, '
            'no trabajo aquí. ¿Qué estudias? (Что ты изучаешь?)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Поставьте глагол в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (hablar) español.', 'options': ['hablo', 'hablas', 'habla'], 'correct_answer': 'hablo',
             'translation': 'Я говорю по-испански.', 'explanation': '1 л. ед.: -o.'},
            {'section': 'Упражнение 1. Поставьте глагол в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Tú ___ (trabajar) mucho.', 'options': ['trabajo', 'trabajas', 'trabaja'], 'correct_answer': 'trabajas',
             'translation': 'Ты много работаешь.', 'explanation': '2 л. ед.: -as.'},
            {'section': 'Упражнение 1. Поставьте глагол в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Ella ___ (estudiar) medicina.', 'options': ['estudio', 'estudias', 'estudia'], 'correct_answer': 'estudia',
             'translation': 'Она изучает медицину.', 'explanation': '3 л. ед.: -a.'},
            {'section': 'Упражнение 1. Поставьте глагол в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ (comprar) fruta.', 'options': ['compramos', 'compran', 'compra'], 'correct_answer': 'compramos',
             'translation': 'Мы покупаем фрукты.', 'explanation': '1 л. мн.: -amos.'},
            {'section': 'Упражнение 1. Поставьте глагол в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Vosotros ___ (cantar) bien.', 'options': ['cantáis', 'cantan', 'cantamos'], 'correct_answer': 'cantáis',
             'translation': 'Вы хорошо поёте.', 'explanation': '2 л. мн.: -áis.'},
            {'section': 'Упражнение 1. Поставьте глагол в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ (bailar) salsa.', 'options': ['bailan', 'bailáis', 'baila'], 'correct_answer': 'bailan',
             'translation': 'Они танцуют сальсу.', 'explanation': '3 л. мн.: -an.'},
            {'section': 'Упражнение 1. Поставьте глагол в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': '¿___ usted español? (hablar)', 'options': ['Habla', 'Hablas', 'Hablo'], 'correct_answer': 'Habla',
             'translation': 'Вы говорите по-испански?', 'explanation': 'usted → 3 л. ед.: habla.'},
            {'section': 'Упражнение 1. Поставьте глагол в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (escuchar) música.', 'options': ['escucho', 'escuchas', 'escucha'], 'correct_answer': 'escucho',
             'translation': 'Я слушаю музыку.', 'explanation': '1 л. ед.: escucho.'},
            {'section': 'Упражнение 1. Поставьте глагол в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'María y Ana ___ (descansar).', 'options': ['descansan', 'descansa', 'descansamos'], 'correct_answer': 'descansan',
             'translation': 'Мария и Ана отдыхают.', 'explanation': 'Они → -an.'},
            {'section': 'Упражнение 1. Поставьте глагол в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': '¿Qué ___ (mirar, tú)?', 'options': ['miras', 'mira', 'miro'], 'correct_answer': 'miras',
             'translation': 'Что ты смотришь?', 'explanation': '2 л. ед.: miras.'},
            # 2
            {'section': 'Упражнение 2. Выберите местоимение', 'exercise_type': 'multiple_choice',
             'prompt': '___ hablamos ruso. (мы)', 'options': ['Nosotros', 'Vosotros', 'Ellos'], 'correct_answer': 'Nosotros',
             'translation': 'Мы говорим по-русски.', 'explanation': '-amos → nosotros.'},
            {'section': 'Упражнение 2. Выберите местоимение', 'exercise_type': 'multiple_choice',
             'prompt': '___ trabaja en un banco. (она)', 'options': ['Él', 'Ella', 'Tú'], 'correct_answer': 'Ella',
             'translation': 'Она работает в банке.', 'explanation': 'Она → ella.'},
            {'section': 'Упражнение 2. Выберите местоимение', 'exercise_type': 'multiple_choice',
             'prompt': '¿Habla ___ inglés? (Вы, вежливо)', 'options': ['tú', 'usted', 'vosotros'], 'correct_answer': 'usted',
             'translation': 'Вы говорите по-английски?', 'explanation': 'Вежливое «Вы» → usted + 3 л.'},
            {'section': 'Упражнение 2. Выберите местоимение', 'exercise_type': 'multiple_choice',
             'prompt': '___ cantan muy bien. (они, женщины)', 'options': ['Ellos', 'Ellas', 'Ustedes'], 'correct_answer': 'Ellas',
             'translation': 'Они (женщины) очень хорошо поют.', 'explanation': 'Женская группа → ellas.'},
            {'section': 'Упражнение 2. Выберите местоимение', 'exercise_type': 'multiple_choice',
             'prompt': '___ estudias y ___ trabajo. (контраст: ты… я…)', 'options': ['Tú … yo', 'Yo … tú', 'Él … tú'], 'correct_answer': 'Tú … yo',
             'translation': 'Ты учишься, а я работаю.', 'explanation': 'estudias → tú; trabajo → yo.'},
            {'section': 'Упражнение 2. Выберите местоимение', 'exercise_type': 'multiple_choice',
             'prompt': 'Кому соответствует форма «habláis»?', 'options': ['nosotros', 'vosotros', 'ellos'], 'correct_answer': 'vosotros',
             'translation': 'habláis — (вы) говорите', 'explanation': '-áis → vosotros.'},
            {'section': 'Упражнение 2. Выберите местоимение', 'exercise_type': 'multiple_choice',
             'prompt': 'Кому соответствует форма «compra»?', 'options': ['yo', 'él/ella/usted', 'ellos'], 'correct_answer': 'él/ella/usted',
             'translation': 'compra — покупает', 'explanation': '-a → 3 л. ед. (и usted).'},
            {'section': 'Упражнение 2. Выберите местоимение', 'exercise_type': 'multiple_choice',
             'prompt': '¿Hablan ___ español? (Вы, к нескольким)', 'options': ['vosotros', 'ustedes', 'ellos'], 'correct_answer': 'ustedes',
             'translation': 'Вы (все) говорите по-испански?', 'explanation': 'Вежливое мн. → ustedes + 3 л. мн.'},
            {'section': 'Упражнение 2. Выберите местоимение', 'exercise_type': 'multiple_choice',
             'prompt': 'Нужно ли местоимение: «(Я) работаю здесь»?', 'options': ['Trabajo aquí.', 'Yo trabajo aquí. (обязательно)'],
             'correct_answer': 'Trabajo aquí.', 'translation': 'Я работаю здесь.', 'explanation': 'Окончание уже показывает лицо.'},
            {'section': 'Упражнение 2. Выберите местоимение', 'exercise_type': 'multiple_choice',
             'prompt': '___ descansamos los domingos. (мы, женщины)', 'options': ['Nosotros', 'Nosotras', 'Vosotras'], 'correct_answer': 'Nosotras',
             'translation': 'Мы (женщины) отдыхаем по воскресеньям.', 'explanation': 'Женская группа → nosotras.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я работаю в банке.»',
             'options': ['Trabajo en un banco.', 'Trabajas en un banco.', 'Trabajo en banco un.'],
             'correct_answer': 'Trabajo en un banco.', 'explanation': '1 л.: trabajo.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы учим испанский.»',
             'options': ['Estudiamos español.', 'Estudian español.', 'Estudiamos el español mucho bien.'],
             'correct_answer': 'Estudiamos español.', 'explanation': '1 л. мн.: estudiamos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Ты поёшь очень хорошо.»',
             'options': ['Cantas muy bien.', 'Canta muy bien.', 'Cantas mucho bien.'],
             'correct_answer': 'Cantas muy bien.', 'explanation': '2 л.: cantas; muy bien.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Вы говорите по-испански?» (вежливо, к одному)',
             'options': ['¿Habla usted español?', '¿Hablas usted español?', '¿Habláis usted español?'],
             'correct_answer': '¿Habla usted español?', 'explanation': 'usted + 3 л. ед.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Они танцуют.»',
             'options': ['Bailan.', 'Bailamos.', 'Bailáis.'],
             'correct_answer': 'Bailan.', 'explanation': '3 л. мн.: bailan.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Что ты изучаешь?»',
             'options': ['¿Qué estudias?', '¿Qué estudia?', '¿Que estudias?'],
             'correct_answer': '¿Qué estudias?', 'explanation': 'qué с тильдой; 2 л.: estudias.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я не работаю по воскресеньям.»',
             'options': ['No trabajo los domingos.', 'Trabajo no los domingos.', 'No trabajos los domingos.'],
             'correct_answer': 'No trabajo los domingos.', 'explanation': 'no + trabajo; los domingos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я работаю, а ты отдыхаешь.»',
             'options': ['Yo trabajo y tú descansas.', 'Yo trabajas y tú descanso.', 'Trabajo yo y descansas tú y.'],
             'correct_answer': 'Yo trabajo y tú descansas.', 'explanation': 'Контраст — местоимения уместны.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мария слушает музыку.»',
             'options': ['María escucha música.', 'María escuchas música.', 'María escucha la música mucho.'],
             'correct_answer': 'María escucha música.', 'explanation': '3 л. ед.: escucha.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы покупаем хлеб.»',
             'options': ['Compramos pan.', 'Compran pan.', 'Compramos un pan bueno mucho.'],
             'correct_answer': 'Compramos pan.', 'explanation': '1 л. мн.: compramos; pan без артикля.'},
        ],
    },
]

_B2 = [
    {
        'n': 10, 'level': 'A1', 'title': 'Слияние a + el = al. Глагол comenzar (e→ie). Время',
        'theory': (
            '1. Слияние артикля с предлогами. Предлоги a и de, встречаясь с артиклем el, '
            'ОБЯЗАТЕЛЬНО сливаются:\n'
            '• a + el = al: Voy al cine (иду в кино). Llegamos al centro.\n'
            '• de + el = del: Vengo del trabajo (иду с работы). La puerta del coche.\n'
            'С остальными артиклями слияния нет: a la escuela, de los amigos, a las chicas. '
            'Перед именами собственными тоже нет: Voy a El Escorial.\n\n'
            '2. Глаголы с чередованием e→ie. У многих глаголов корневая гласная e под ударением '
            'превращается в ie — во всех формах ед. числа и в 3 л. мн. числа; формы nosotros и '
            'vosotros сохраняют e:\n\n'
            '  comenzar (начинать): comienzo, comienzas, comienza, comenzamos, comenzáis, comienzan\n\n'
            'Так же спрягаются: empezar (начинать), pensar (думать), cerrar (закрывать), '
            'despertar (будить), а из других спряжений — querer (хотеть, любить): quiero, quieres, '
            'quiere, queremos, queréis, quieren.\n'
            'После comenzar/empezar перед инфинитивом ставится a: Comienzo a trabajar a las nueve '
            '(начинаю работать в девять).\n\n'
            '3. Который час. Время выражается глаголом ser:\n'
            '• Es la una (час дня) — единственное число только для часа;\n'
            '• Son las dos / las tres / las diez (два, три, десять часов);\n'
            '• минуты: y — «с минутами», menos — «без»: Son las dos y diez (2:10), '
            'Son las tres menos cuarto (без четверти три), Es la una y media (полвторого);\n'
            '• y cuarto — четверть, y media — половина.\n'
            'Вопрос: ¿Qué hora es? (Который час?) «Во сколько?» — ¿A qué hora…? Ответ с a: '
            'La clase comienza a las nueve (занятие начинается в девять). A la una — в час.'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Вставьте al, del, a la или de la', 'exercise_type': 'fill_blank',
             'prompt': 'Voy ___ cine.', 'options': ['al', 'a el', 'a la'], 'correct_answer': 'al',
             'translation': 'Я иду в кино.', 'explanation': 'a + el = al.'},
            {'section': 'Упражнение 1. Вставьте al, del, a la или de la', 'exercise_type': 'fill_blank',
             'prompt': 'Vengo ___ trabajo.', 'options': ['del', 'de el', 'de la'], 'correct_answer': 'del',
             'translation': 'Я иду с работы.', 'explanation': 'de + el = del.'},
            {'section': 'Упражнение 1. Вставьте al, del, a la или de la', 'exercise_type': 'fill_blank',
             'prompt': 'Voy ___ escuela.', 'options': ['al', 'a la', 'del'], 'correct_answer': 'a la',
             'translation': 'Я иду в школу.', 'explanation': 'С la слияния нет.'},
            {'section': 'Упражнение 1. Вставьте al, del, a la или de la', 'exercise_type': 'fill_blank',
             'prompt': 'La puerta ___ coche.', 'options': ['del', 'de la', 'al'], 'correct_answer': 'del',
             'translation': 'Дверь машины.', 'explanation': 'de + el = del.'},
            {'section': 'Упражнение 1. Вставьте al, del, a la или de la', 'exercise_type': 'fill_blank',
             'prompt': 'Llegamos ___ centro.', 'options': ['al', 'a la', 'de la'], 'correct_answer': 'al',
             'translation': 'Мы приезжаем в центр.', 'explanation': 'a + el = al.'},
            {'section': 'Упражнение 1. Вставьте al, del, a la или de la', 'exercise_type': 'fill_blank',
             'prompt': 'Vengo ___ farmacia.', 'options': ['del', 'de la', 'al'], 'correct_answer': 'de la',
             'translation': 'Я иду из аптеки.', 'explanation': 'ж. р.: de la.'},
            {'section': 'Упражнение 1. Вставьте al, del, a la или de la', 'exercise_type': 'fill_blank',
             'prompt': 'El libro ___ profesor está aquí.', 'options': ['del', 'de el', 'al'], 'correct_answer': 'del',
             'translation': 'Книга преподавателя здесь.', 'explanation': 'del.'},
            {'section': 'Упражнение 1. Вставьте al, del, a la или de la', 'exercise_type': 'fill_blank',
             'prompt': 'Vamos ___ parque.', 'options': ['al', 'a la', 'del'], 'correct_answer': 'al',
             'translation': 'Мы идём в парк.', 'explanation': 'al parque.'},
            {'section': 'Упражнение 1. Вставьте al, del, a la или de la', 'exercise_type': 'fill_blank',
             'prompt': 'Salgo ___ casa a las ocho.', 'options': ['del', 'de', 'al'], 'correct_answer': 'de',
             'translation': 'Я выхожу из дома в восемь.', 'explanation': 'Оборот de casa — без артикля.'},
            {'section': 'Упражнение 1. Вставьте al, del, a la или de la', 'exercise_type': 'fill_blank',
             'prompt': 'La ventana ___ aula.', 'options': ['de la', 'del', 'al'], 'correct_answer': 'del',
             'translation': 'Окно аудитории.', 'explanation': 'el aula (ударное a-) → del aula.'},
            # 2
            {'section': 'Упражнение 2. Спрягайте comenzar и querer', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (comenzar) ahora.', 'options': ['comenzo', 'comienzo', 'comienza'], 'correct_answer': 'comienzo',
             'translation': 'Я начинаю сейчас.', 'explanation': 'e→ie под ударением.'},
            {'section': 'Упражнение 2. Спрягайте comenzar и querer', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ (comenzar) a las nueve.', 'options': ['comenzamos', 'comienzamos', 'comienzan'], 'correct_answer': 'comenzamos',
             'translation': 'Мы начинаем в девять.', 'explanation': 'nosotros сохраняет e.'},
            {'section': 'Упражнение 2. Спрягайте comenzar и querer', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ (empezar) el trabajo.', 'options': ['empiezan', 'empezan', 'empezáis'], 'correct_answer': 'empiezan',
             'translation': 'Они начинают работу.', 'explanation': '3 л. мн.: e→ie.'},
            {'section': 'Упражнение 2. Спрягайте comenzar и querer', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (querer) un café.', 'options': ['quero', 'quiero', 'quiere'], 'correct_answer': 'quiero',
             'translation': 'Я хочу кофе.', 'explanation': 'querer: quiero.'},
            {'section': 'Упражнение 2. Спрягайте comenzar и querer', 'exercise_type': 'fill_blank',
             'prompt': '¿Tú ___ (pensar) en el examen?', 'options': ['pensas', 'piensas', 'piensa'], 'correct_answer': 'piensas',
             'translation': 'Ты думаешь об экзамене?', 'explanation': 'pensar: piensas.'},
            {'section': 'Упражнение 2. Спрягайте comenzar и querer', 'exercise_type': 'fill_blank',
             'prompt': 'Ella ___ (cerrar) la ventana.', 'options': ['cerra', 'cierra', 'cierras'], 'correct_answer': 'cierra',
             'translation': 'Она закрывает окно.', 'explanation': 'cerrar: cierra.'},
            {'section': 'Упражнение 2. Спрягайте comenzar и querer', 'exercise_type': 'fill_blank',
             'prompt': 'Vosotros ___ (querer) descansar.', 'options': ['queréis', 'quieréis', 'quieren'], 'correct_answer': 'queréis',
             'translation': 'Вы хотите отдохнуть.', 'explanation': 'vosotros сохраняет e: queréis.'},
            {'section': 'Упражнение 2. Спрягайте comenzar и querer', 'exercise_type': 'fill_blank',
             'prompt': 'La clase ___ (comenzar) a las diez.', 'options': ['comienza', 'comenza', 'comienzan'], 'correct_answer': 'comienza',
             'translation': 'Занятие начинается в десять.', 'explanation': '3 л. ед.: comienza.'},
            {'section': 'Упражнение 2. Спрягайте comenzar и querer', 'exercise_type': 'fill_blank',
             'prompt': 'Comienzo ___ trabajar. (предлог)', 'options': ['a', 'de', 'en'], 'correct_answer': 'a',
             'translation': 'Я начинаю работать.', 'explanation': 'comenzar a + инфинитив.'},
            {'section': 'Упражнение 2. Спрягайте comenzar и querer', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ (querer) aprender.', 'options': ['queremos', 'quieremos', 'quieren'], 'correct_answer': 'queremos',
             'translation': 'Мы хотим учиться.', 'explanation': 'nosotros: queremos.'},
            # 3
            {'section': 'Упражнение 3. Который час? Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Час дня.»',
             'options': ['Es la una.', 'Son la una.', 'Es una.'],
             'correct_answer': 'Es la una.', 'explanation': 'Один час → es la una.'},
            {'section': 'Упражнение 3. Который час? Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Три часа.»',
             'options': ['Son las tres.', 'Es las tres.', 'Son tres.'],
             'correct_answer': 'Son las tres.', 'explanation': 'Мн. ч. → son las tres.'},
            {'section': 'Упражнение 3. Который час? Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «2:10.»',
             'options': ['Son las dos y diez.', 'Son las dos menos diez.', 'Es las dos y diez.'],
             'correct_answer': 'Son las dos y diez.', 'explanation': '«с минутами» → y.'},
            {'section': 'Упражнение 3. Который час? Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Без четверти три.»',
             'options': ['Son las tres menos cuarto.', 'Son las tres y cuarto.', 'Son las dos menos cuarto.'],
             'correct_answer': 'Son las tres menos cuarto.', 'explanation': '«без» → menos cuarto.'},
            {'section': 'Упражнение 3. Который час? Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Полвторого.» (час тридцать)',
             'options': ['Es la una y media.', 'Son las dos y media.', 'Es la una y cuarto.'],
             'correct_answer': 'Es la una y media.', 'explanation': '1:30 → es la una y media.'},
            {'section': 'Упражнение 3. Который час? Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Который час?»',
             'options': ['¿Qué hora es?', '¿Cuánta hora es?', '¿Qué horas son siempre?'],
             'correct_answer': '¿Qué hora es?', 'explanation': 'Устойчивый вопрос.'},
            {'section': 'Упражнение 3. Который час? Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Во сколько начинается занятие?»',
             'options': ['¿A qué hora comienza la clase?', '¿Qué hora comienza la clase?', '¿A qué hora comienzan la clase?'],
             'correct_answer': '¿A qué hora comienza la clase?', 'explanation': '«во сколько» → a qué hora.'},
            {'section': 'Упражнение 3. Который час? Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Занятие начинается в девять.»',
             'options': ['La clase comienza a las nueve.', 'La clase comienza en las nueve.', 'La clase comienzan a las nueve.'],
             'correct_answer': 'La clase comienza a las nueve.', 'explanation': '«в …часов» → a las …'},
            {'section': 'Упражнение 3. Который час? Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я иду в кино в семь.»',
             'options': ['Voy al cine a las siete.', 'Voy al cine en las siete.', 'Voy a el cine a las siete.'],
             'correct_answer': 'Voy al cine a las siete.', 'explanation': 'al + a las siete.'},
            {'section': 'Упражнение 3. Который час? Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Четверть пятого.» (4:15)',
             'options': ['Son las cuatro y cuarto.', 'Son las cinco menos cuarto.', 'Son las cuatro y media.'],
             'correct_answer': 'Son las cuatro y cuarto.', 'explanation': '4:15 → las cuatro y cuarto.'},
        ],
    },
    {
        'n': 11, 'level': 'A1', 'title': 'Возвратные глаголы: lavarse',
        'theory': (
            'Возвратные (местоименные) глаголы обозначают действие, направленное на самого себя, '
            'и в инфинитиве оканчиваются на -se: lavarse (умываться), levantarse (вставать), '
            'ducharse (принимать душ).\n\n'
            '1. Возвратные местоимения: me, te, se, nos, os, se. Они меняются по лицам вместе с '
            'глаголом и ставятся ПЕРЕД спрягаемой формой:\n\n'
            '  lavarse: me lavo, te lavas, se lava, nos lavamos, os laváis, se lavan\n\n'
            '2. Разница с невозвратным употреблением: Lavo el coche (я мою машину) — Me lavo '
            '(я умываюсь, мою себя). Despierto a mi hijo (бужу сына) — Me despierto (просыпаюсь).\n\n'
            '3. Глаголы распорядка дня:\n'
            '• despertarse (e→ie) — просыпаться: Me despierto a las siete (просыпаюсь в семь);\n'
            '• levantarse — вставать: Me levanto a las siete y diez;\n'
            '• ducharse — принимать душ; lavarse — умываться: Me lavo la cara y los dientes '
            '(умываю лицо и чищу зубы — обратите внимание: с частями тела употребляется '
            'определённый артикль, а не притяжательное);\n'
            '• peinarse — причёсываться; vestirse (e→i) — одеваться: me visto;\n'
            '• acostarse (o→ue) — ложиться спать: Me acuesto a las once (ложусь в одиннадцать).\n\n'
            '4. В отрицании no ставится перед возвратным местоимением: No me levanto temprano '
            '(я не встаю рано). В вопросе порядок сохраняется: ¿A qué hora te levantas? '
            '(во сколько ты встаёшь?)\n\n'
            '5. При инфинитиве местоимение присоединяется к нему в конце и согласуется с '
            'подлежащим: Quiero ducharme (хочу принять душ). ¿Quieres levantarte? — '
            'заметьте: quiero ducharME, quieres levantarTE.'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Вставьте возвратное местоимение', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ lavo por la mañana.', 'options': ['me', 'te', 'se'], 'correct_answer': 'me',
             'translation': 'Я умываюсь по утрам.', 'explanation': 'yo → me.'},
            {'section': 'Упражнение 1. Вставьте возвратное местоимение', 'exercise_type': 'fill_blank',
             'prompt': '¿A qué hora ___ levantas?', 'options': ['me', 'te', 'se'], 'correct_answer': 'te',
             'translation': 'Во сколько ты встаёшь?', 'explanation': 'tú → te.'},
            {'section': 'Упражнение 1. Вставьте возвратное местоимение', 'exercise_type': 'fill_blank',
             'prompt': 'Ella ___ ducha por la noche.', 'options': ['se', 'te', 'nos'], 'correct_answer': 'se',
             'translation': 'Она принимает душ вечером.', 'explanation': 'ella → se.'},
            {'section': 'Упражнение 1. Вставьте возвратное местоимение', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ levantamos temprano.', 'options': ['nos', 'os', 'se'], 'correct_answer': 'nos',
             'translation': 'Мы встаём рано.', 'explanation': 'nosotros → nos.'},
            {'section': 'Упражнение 1. Вставьте возвратное местоимение', 'exercise_type': 'fill_blank',
             'prompt': 'Vosotros ___ acostáis tarde.', 'options': ['os', 'nos', 'se'], 'correct_answer': 'os',
             'translation': 'Вы поздно ложитесь.', 'explanation': 'vosotros → os.'},
            {'section': 'Упражнение 1. Вставьте возвратное местоимение', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ peinan.', 'options': ['se', 'os', 'me'], 'correct_answer': 'se',
             'translation': 'Они причёсываются.', 'explanation': 'ellos → se.'},
            {'section': 'Упражнение 1. Вставьте возвратное местоимение', 'exercise_type': 'fill_blank',
             'prompt': 'Yo no ___ levanto temprano.', 'options': ['me', 'te', 'se'], 'correct_answer': 'me',
             'translation': 'Я не встаю рано.', 'explanation': 'no + me + глагол.'},
            {'section': 'Упражнение 1. Вставьте возвратное местоимение', 'exercise_type': 'fill_blank',
             'prompt': 'Quiero duchar___. (инфинитив)', 'options': ['me', 'te', 'se'], 'correct_answer': 'me',
             'translation': 'Я хочу принять душ.', 'explanation': 'При инфинитиве — в конце: ducharme.'},
            {'section': 'Упражнение 1. Вставьте возвратное местоимение', 'exercise_type': 'fill_blank',
             'prompt': '¿Quieres levantar___ ya?', 'options': ['te', 'me', 'se'], 'correct_answer': 'te',
             'translation': 'Ты хочешь уже встать?', 'explanation': 'Согласуется с tú: levantarte.'},
            {'section': 'Упражнение 1. Вставьте возвратное местоимение', 'exercise_type': 'fill_blank',
             'prompt': 'Mi hijo ___ viste solo.', 'options': ['se', 'me', 'os'], 'correct_answer': 'se',
             'translation': 'Мой сын одевается сам.', 'explanation': '3 л.: se viste.'},
            # 2
            {'section': 'Упражнение 2. Выберите форму глагола', 'exercise_type': 'multiple_choice',
             'prompt': 'Yo me ___ (despertar) a las siete.', 'options': ['despierto', 'desperto', 'despierta'], 'correct_answer': 'despierto',
             'translation': 'Я просыпаюсь в семь.', 'explanation': 'e→ie: despierto.'},
            {'section': 'Упражнение 2. Выберите форму глагола', 'exercise_type': 'multiple_choice',
             'prompt': 'Él se ___ (acostar) a las once.', 'options': ['acosta', 'acuesta', 'acuestan'], 'correct_answer': 'acuesta',
             'translation': 'Он ложится в одиннадцать.', 'explanation': 'o→ue: se acuesta.'},
            {'section': 'Упражнение 2. Выберите форму глагола', 'exercise_type': 'multiple_choice',
             'prompt': 'Nosotros nos ___ (acostar) temprano.', 'options': ['acostamos', 'acuestamos', 'acuestan'], 'correct_answer': 'acostamos',
             'translation': 'Мы рано ложимся.', 'explanation': 'nosotros сохраняет o: acostamos.'},
            {'section': 'Упражнение 2. Выберите форму глагола', 'exercise_type': 'multiple_choice',
             'prompt': 'Yo me ___ (vestir) rápido.', 'options': ['visto', 'vesto', 'viste'], 'correct_answer': 'visto',
             'translation': 'Я быстро одеваюсь.', 'explanation': 'e→i: me visto.'},
            {'section': 'Упражнение 2. Выберите форму глагола', 'exercise_type': 'multiple_choice',
             'prompt': 'Me lavo ___ dientes.', 'options': ['mis', 'los', 'unos'], 'correct_answer': 'los',
             'translation': 'Я чищу зубы.', 'explanation': 'С частями тела — определённый артикль.'},
            {'section': 'Упражнение 2. Выберите форму глагола', 'exercise_type': 'multiple_choice',
             'prompt': '«Я мою машину» —', 'options': ['Me lavo el coche.', 'Lavo el coche.'], 'correct_answer': 'Lavo el coche.',
             'translation': 'lavar — мыть (что-то)', 'explanation': 'Действие не на себя → без se.'},
            {'section': 'Упражнение 2. Выберите форму глагола', 'exercise_type': 'multiple_choice',
             'prompt': '«Я умываюсь» —', 'options': ['Lavo.', 'Me lavo.'], 'correct_answer': 'Me lavo.',
             'translation': 'lavarse — умываться', 'explanation': 'На себя → me lavo.'},
            {'section': 'Упражнение 2. Выберите форму глагола', 'exercise_type': 'multiple_choice',
             'prompt': 'Ella se ___ (peinar) delante del espejo.', 'options': ['peina', 'peinas', 'peino'], 'correct_answer': 'peina',
             'translation': 'Она причёсывается перед зеркалом.', 'explanation': '3 л.: se peina.'},
            {'section': 'Упражнение 2. Выберите форму глагола', 'exercise_type': 'multiple_choice',
             'prompt': '¿Vosotros os ___ (duchar) por la mañana?', 'options': ['ducháis', 'duchan', 'duchamos'], 'correct_answer': 'ducháis',
             'translation': 'Вы принимаете душ по утрам?', 'explanation': 'vosotros → -áis.'},
            {'section': 'Упражнение 2. Выберите форму глагола', 'exercise_type': 'multiple_choice',
             'prompt': 'Los niños se ___ (despertar) tarde.', 'options': ['despiertan', 'despertan', 'despierta'], 'correct_answer': 'despiertan',
             'translation': 'Дети поздно просыпаются.', 'explanation': '3 л. мн.: despiertan.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я встаю в семь.»',
             'options': ['Me levanto a las siete.', 'Levanto a las siete.', 'Me levanta a las siete.'],
             'correct_answer': 'Me levanto a las siete.', 'explanation': 'me + levanto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Во сколько ты ложишься?»',
             'options': ['¿A qué hora te acuestas?', '¿A qué hora acuestas?', '¿A qué hora te acostas?'],
             'correct_answer': '¿A qué hora te acuestas?', 'explanation': 'te + acuestas (o→ue).'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Она умывается.»',
             'options': ['Se lava.', 'Lava.', 'Se lavo.'],
             'correct_answer': 'Se lava.', 'explanation': 'se + lava.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы принимаем душ по утрам.»',
             'options': ['Nos duchamos por la mañana.', 'Duchamos por la mañana.', 'Nos duchan por la mañana.'],
             'correct_answer': 'Nos duchamos por la mañana.', 'explanation': 'nos + duchamos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я хочу принять душ.»',
             'options': ['Quiero ducharme.', 'Quiero me duchar.', 'Me quiero ducho.'],
             'correct_answer': 'Quiero ducharme.', 'explanation': 'Местоимение к инфинитиву: ducharme.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я чищу зубы.»',
             'options': ['Me lavo los dientes.', 'Me lavo mis dientes.', 'Lavo los dientes me.'],
             'correct_answer': 'Me lavo los dientes.', 'explanation': 'Части тела — с los, не с mis.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я не встаю рано.»',
             'options': ['No me levanto temprano.', 'Me no levanto temprano.', 'No levanto me temprano.'],
             'correct_answer': 'No me levanto temprano.', 'explanation': 'no перед me.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он одевается быстро.»',
             'options': ['Se viste rápido.', 'Viste rápido.', 'Se vesta rápido.'],
             'correct_answer': 'Se viste rápido.', 'explanation': 'vestirse e→i: se viste.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Дети просыпаются в восемь.»',
             'options': ['Los niños se despiertan a las ocho.', 'Los niños despiertan a las ocho.', 'Los niños se despertan a las ocho.'],
             'correct_answer': 'Los niños se despiertan a las ocho.', 'explanation': 'se + despiertan (e→ie).'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я бужу сына в семь.» (не возвратный!)',
             'options': ['Despierto a mi hijo a las siete.', 'Me despierto a mi hijo a las siete.', 'Despierto mi hijo a las siete.'],
             'correct_answer': 'Despierto a mi hijo a las siete.', 'explanation': 'Действие на другого → без se; личное a.'},
        ],
    },
    {
        'n': 12, 'level': 'A1', 'title': 'II спряжение (-er). Падежные отношения',
        'theory': (
            '1. Второе спряжение — глаголы на -er. Настоящее время образуется заменой -er на '
            'окончания -o, -es, -e, -emos, -éis, -en:\n\n'
            '  comer (есть): como, comes, come, comemos, coméis, comen\n\n'
            'Так же спрягаются: beber (пить), leer (читать), aprender (учить, изучать), '
            'comprender (понимать), vender (продавать), responder (отвечать), creer (верить, '
            'полагать). Обратите внимание: окончания почти как у -ar, только с гласной e.\n\n'
            '2. Падежные отношения. В испанском нет падежных окончаний — отношения между словами '
            'передают ПРЕДЛОГИ:\n'
            '• родительный падеж (кого? чего? чей?) → предлог de: el libro de María (книга Марии), '
            'la capital de España (столица Испании), un vaso de agua (стакан воды);\n'
            '• дательный падеж (кому? чему?) → предлог a: Escribo una carta a mi madre (пишу '
            'письмо маме). Vendo el coche a Juan (продаю машину Хуану);\n'
            '• винительный падеж: без предлога для предметов (Leo un libro — читаю книгу), '
            'но с «личным a» для КОНКРЕТНЫХ ЛЮДЕЙ: Veo a María (вижу Марию), Comprendo a mi '
            'amigo (понимаю своего друга).\n\n'
            '3. Не забывайте про слияния: de + el = del, a + el = al: la puerta del aula, '
            'Respondo al profesor (отвечаю преподавателю).\n\n'
            '4. Примеры в предложениях:\n'
            '• Como pan y bebo agua (ем хлеб и пью воду).\n'
            '• ¿Comprendes la pregunta del profesor? (понимаешь вопрос преподавателя?)\n'
            '• Los estudiantes aprenden español (студенты учат испанский).\n'
            '• Leemos los libros de la biblioteca (читаем библиотечные книги).'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Поставьте глагол -er в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (comer) fruta.', 'options': ['como', 'comes', 'come'], 'correct_answer': 'como',
             'translation': 'Я ем фрукты.', 'explanation': '1 л.: como.'},
            {'section': 'Упражнение 1. Поставьте глагол -er в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Tú ___ (beber) agua.', 'options': ['bebo', 'bebes', 'bebe'], 'correct_answer': 'bebes',
             'translation': 'Ты пьёшь воду.', 'explanation': '2 л.: bebes.'},
            {'section': 'Упражнение 1. Поставьте глагол -er в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Ella ___ (leer) una novela.', 'options': ['leo', 'lees', 'lee'], 'correct_answer': 'lee',
             'translation': 'Она читает роман.', 'explanation': '3 л.: lee.'},
            {'section': 'Упражнение 1. Поставьте глагол -er в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ (aprender) español.', 'options': ['aprendemos', 'aprenden', 'aprende'], 'correct_answer': 'aprendemos',
             'translation': 'Мы учим испанский.', 'explanation': '1 л. мн.: -emos.'},
            {'section': 'Упражнение 1. Поставьте глагол -er в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Vosotros ___ (comprender) la regla.', 'options': ['comprendéis', 'comprenden', 'comprendemos'], 'correct_answer': 'comprendéis',
             'translation': 'Вы понимаете правило.', 'explanation': '2 л. мн.: -éis.'},
            {'section': 'Упражнение 1. Поставьте глагол -er в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ (vender) frutas.', 'options': ['venden', 'vendéis', 'vende'], 'correct_answer': 'venden',
             'translation': 'Они продают фрукты.', 'explanation': '3 л. мн.: -en.'},
            {'section': 'Упражнение 1. Поставьте глагол -er в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': '¿___ (creer, tú) esto?', 'options': ['Crees', 'Cree', 'Creo'], 'correct_answer': 'Crees',
             'translation': 'Ты веришь в это?', 'explanation': '2 л.: crees.'},
            {'section': 'Упражнение 1. Поставьте глагол -er в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (responder) a la pregunta.', 'options': ['respondo', 'respondes', 'responde'], 'correct_answer': 'respondo',
             'translation': 'Я отвечаю на вопрос.', 'explanation': '1 л.: respondo.'},
            {'section': 'Упражнение 1. Поставьте глагол -er в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'El niño ___ (comer) mucho.', 'options': ['come', 'comes', 'comen'], 'correct_answer': 'come',
             'translation': 'Ребёнок много ест.', 'explanation': '3 л.: come.'},
            {'section': 'Упражнение 1. Поставьте глагол -er в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ (leer) el periódico.', 'options': ['leemos', 'leen', 'leéis'], 'correct_answer': 'leemos',
             'translation': 'Мы читаем газету.', 'explanation': '1 л. мн.: leemos.'},
            # 2
            {'section': 'Упражнение 2. Вставьте предлог de, a, del или al', 'exercise_type': 'fill_blank',
             'prompt': 'El libro ___ María.', 'options': ['de', 'a', 'del'], 'correct_answer': 'de',
             'translation': 'Книга Марии.', 'explanation': 'Принадлежность → de.'},
            {'section': 'Упражнение 2. Вставьте предлог de, a, del или al', 'exercise_type': 'fill_blank',
             'prompt': 'Escribo una carta ___ mi madre.', 'options': ['de', 'a', 'del'], 'correct_answer': 'a',
             'translation': 'Я пишу письмо маме.', 'explanation': 'Кому → a.'},
            {'section': 'Упражнение 2. Вставьте предлог de, a, del или al', 'exercise_type': 'fill_blank',
             'prompt': 'La capital ___ España.', 'options': ['de', 'a', 'al'], 'correct_answer': 'de',
             'translation': 'Столица Испании.', 'explanation': 'Чего → de.'},
            {'section': 'Упражнение 2. Вставьте предлог de, a, del или al', 'exercise_type': 'fill_blank',
             'prompt': 'Respondo ___ profesor.', 'options': ['al', 'del', 'a'], 'correct_answer': 'al',
             'translation': 'Я отвечаю преподавателю.', 'explanation': 'a + el = al.'},
            {'section': 'Упражнение 2. Вставьте предлог de, a, del или al', 'exercise_type': 'fill_blank',
             'prompt': 'Un vaso ___ agua.', 'options': ['de', 'a', 'con'], 'correct_answer': 'de',
             'translation': 'Стакан воды.', 'explanation': 'Мера чего → de.'},
            {'section': 'Упражнение 2. Вставьте предлог de, a, del или al', 'exercise_type': 'fill_blank',
             'prompt': 'La puerta ___ aula.', 'options': ['del', 'de la', 'al'], 'correct_answer': 'del',
             'translation': 'Дверь аудитории.', 'explanation': 'el aula → del aula.'},
            {'section': 'Упражнение 2. Вставьте предлог de, a, del или al', 'exercise_type': 'fill_blank',
             'prompt': 'Veo ___ María en la calle.', 'options': ['a', 'de', '— (без предлога)'], 'correct_answer': 'a',
             'translation': 'Я вижу Марию на улице.', 'explanation': 'Личное a перед человеком.'},
            {'section': 'Упражнение 2. Вставьте предлог de, a, del или al', 'exercise_type': 'fill_blank',
             'prompt': 'Leo ___ libro. (просто предмет)', 'options': ['a un', 'un', 'al'], 'correct_answer': 'un',
             'translation': 'Я читаю книгу.', 'explanation': 'Предмет — без личного a.'},
            {'section': 'Упражнение 2. Вставьте предлог de, a, del или al', 'exercise_type': 'fill_blank',
             'prompt': 'Vendo el coche ___ Juan.', 'options': ['a', 'de', 'del'], 'correct_answer': 'a',
             'translation': 'Я продаю машину Хуану.', 'explanation': 'Кому → a.'},
            {'section': 'Упражнение 2. Вставьте предлог de, a, del или al', 'exercise_type': 'fill_blank',
             'prompt': 'Comprendo ___ mi amigo.', 'options': ['a', 'de', '— (без предлога)'], 'correct_answer': 'a',
             'translation': 'Я понимаю своего друга.', 'explanation': 'Конкретный человек → личное a.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я ем хлеб и пью воду.»',
             'options': ['Como pan y bebo agua.', 'Como pan y bebes agua.', 'Como el pan y bebo la agua.'],
             'correct_answer': 'Como pan y bebo agua.', 'explanation': '1 л. оба глагола; вещества без артикля.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы учим испанский.»',
             'options': ['Aprendemos español.', 'Aprenden español.', 'Aprendemos al español.'],
             'correct_answer': 'Aprendemos español.', 'explanation': 'aprender: aprendemos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «книга преподавателя»',
             'options': ['el libro del profesor', 'el libro al profesor', 'el libro de el profesor'],
             'correct_answer': 'el libro del profesor', 'explanation': 'de + el = del.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я пишу письмо другу.»',
             'options': ['Escribo una carta a un amigo.', 'Escribo una carta de un amigo.', 'Escribo a una carta un amigo.'],
             'correct_answer': 'Escribo una carta a un amigo.', 'explanation': 'Кому → a.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Ты понимаешь вопрос?»',
             'options': ['¿Comprendes la pregunta?', '¿Comprende la pregunta?', '¿Comprendes a la pregunta?'],
             'correct_answer': '¿Comprendes la pregunta?', 'explanation': 'Предмет — без личного a.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я вижу Хуана.»',
             'options': ['Veo a Juan.', 'Veo Juan.', 'Veo de Juan.'],
             'correct_answer': 'Veo a Juan.', 'explanation': 'Человек → личное a.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Они продают дом.»',
             'options': ['Venden la casa.', 'Vende la casa.', 'Venden a la casa.'],
             'correct_answer': 'Venden la casa.', 'explanation': '3 л. мн.: venden; дом — предмет.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «стакан воды»',
             'options': ['un vaso de agua', 'un vaso a agua', 'un vaso del agua'],
             'correct_answer': 'un vaso de agua', 'explanation': 'Мера → de без артикля.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я отвечаю преподавателю.»',
             'options': ['Respondo al profesor.', 'Respondo del profesor.', 'Respondo a el profesor.'],
             'correct_answer': 'Respondo al profesor.', 'explanation': 'a + el = al.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Она читает библиотечные книги.» (книги библиотеки)',
             'options': ['Lee los libros de la biblioteca.', 'Lee los libros a la biblioteca.', 'Lee los libros del biblioteca.'],
             'correct_answer': 'Lee los libros de la biblioteca.', 'explanation': 'de la biblioteca.'},
        ],
    },
]
A1_FULL_2 = A1_FULL_2 + _B2
