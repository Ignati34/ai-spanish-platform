"""Spanish syllabus mirroring a well-known 61-lesson A1–B2 progression (Lesson 0–60).

Only the *topic outline* (grammar facts) is encoded here — not any copyrighted prose. Each
entry drives the AI lesson generator, which authors an original lesson (theory + exercises).
Hand-written lessons in content/curriculum.py provide guaranteed immediate coverage; the
generator fills the rest of this list on demand.

Each entry: (level, es, ru, focus).
"""

_TOPICS = [
    # ---- A1 (Lessons 0–15) ----
    ('A1', 'El alfabeto y la pronunciación', 'Алфавит и произношение', 'гласные, согласные, правила чтения, ударение'),
    ('A1', 'Género del sustantivo y artículo indeterminado', 'Род существительных и неопределённый артикль', 'esto/eso, глагол-связка es'),
    ('A1', 'Artículo determinado y el adjetivo', 'Определённый артикль и прилагательное', 'цвета, одежда, согласование прилагательных'),
    ('A1', 'Orden de palabras. Interrogación y negación', 'Порядок слов. Вопрос и отрицание', 'инверсия в вопросе, частица no'),
    ('A1', 'Ser y estar. Preposiciones de lugar', 'Глаголы es и está. Предлоги места', 'постоянное vs состояние/место'),
    ('A1', 'La construcción hay. Lugar del adjetivo', 'Конструкция hay. Место прилагательного', 'наличие предметов в пространстве'),
    ('A1', 'Plural del sustantivo y del adjetivo', 'Множественное число существительных и прилагательных', 'los/las, счёт до 5, cuánto'),
    ('A1', 'La omisión del artículo', 'Опущение артикля', 'нулевой артикль с веществами и числительными'),
    ('A1', 'Pronombres personales. Verbos en -ar', 'Личные местоимения. I спряжение (-ar)', 'настоящее время, профессия и рутина'),
    ('A1', 'a + el = al. El verbo comenzar (e>ie)', 'Слияние a + el = al. Глагол comenzar', 'время на часах, чередование e→ie'),
    ('A1', 'Verbos reflexivos: lavarse', 'Возвратные глаголы: lavarse', 'me/te/se, распорядок дня'),
    ('A1', 'Verbos en -er. Relaciones de caso', 'II спряжение (-er). Падежные отношения', 'предлоги de и a, слитный артикль del'),
    ('A1', 'Verbos en -ir. Mucho y muy', 'III спряжение (-ir). Mucho и muy', 'tener, дни недели, много/очень'),
    ('A1', 'El imperativo (modo imperativo)', 'Повелительное наклонение (Imperativo)', 'приказы и просьбы, глагол querer'),
    ('A1', 'Adjetivos posesivos', 'Притяжательные прилагательные', 'mi/tu/su, глаголы salir, oír, venir'),
    ('A1', 'Ir + a + infinitivo (futuro próximo)', 'Ir + a + инфинитив (ближайшее будущее)', 'планы, глаголы ser, poner, traer'),
    # ---- A2 (Lessons 16–28) ----
    ('A2', 'Pretérito imperfecto', 'Прошедшее несовершенное (Imperfecto)', 'привычки и описание фона в прошлом'),
    ('A2', 'Imperfecto de irregulares y reflexivos', 'Imperfecto неправильных и возвратных', 'ser, ir, ver; сводные таблицы'),
    ('A2', 'Preguntas con preposición. Tanto/tan', 'Вопросы с предлогами. Tanto/tan', 'с кем/о чём, описание внешности'),
    ('A2', 'Pronombres de objeto. Poder, saber, conocer', 'Местоимения-дополнения. Poder, saber, conocer', 'прямые и косвенные (me, te, le)'),
    ('A2', 'Se impersonal y concordancia', 'Безличная форма se и согласование', 'обобщённое «здесь говорят»'),
    ('A2', 'Pretérito perfecto compuesto', 'Сложное прошедшее (Pretérito perfecto)', 'haber + participio, счёт до 100'),
    ('A2', 'Perfecto (-er/-ir). La palabra todo', 'Perfecto II–III спряжений. Слово todo', 'причастия на -ido, артикли со странами'),
    ('A2', 'Pronombres personales en plural', 'Личные местоимения во мн. числе', 'nos, os, los, las; ver, encontrar, pedir'),
    ('A2', 'de + infinitivo. El que', 'Конструкция de + инфинитив. El que', 'сложноподчинённые, глагол decir'),
    ('A2', 'Pretérito indefinido. El artículo lo', 'Простое прошедшее (Indefinido). Артикль lo', 'завершённые однократные действия'),
    ('A2', 'Indefinido irregular y doble negación', 'Indefinido неправильных. Двойное отрицание', 'estar, dar, ver, tener; no…nada'),
    ('A2', 'Indefinido: decir, ser, saber, querer', 'Indefinido: decir, ser, saber, querer', 'сводные таблицы прошедших времён'),
    ('A2', 'Dos pronombres. Diminutivos', 'Два местоимения при глаголе. Уменьшительные', 'se lo, te la; суффиксы -ito/-illo'),
    # ---- B1 (Lessons 29–49) ----
    ('B1', 'Concordancia de tiempos. Gerundio', 'Согласование времён. Gerundio', 'косвенная речь, деепричастие'),
    ('B1', 'La palabra mismo. Ir en indefinido', 'Слово mismo. Ir в Indefinido', 'сам/тот же, quedar + прилагательное'),
    ('B1', 'Pluscuamperfecto. Grados de comparación', 'Давнопрошедшее (Pluscuamperfecto). Степени сравнения', 'хронология в прошлом, «лучше чем»'),
    ('B1', 'Superlativo absoluto. Mejor, peor, mayor', 'Абсолютная превосходная. Mejor, peor, mayor', 'суффикс -ísimo, особые формы'),
    ('B1', 'Pretérito anterior. Adverbios en -mente', 'Предпрошедшее (Pretérito anterior). Наречия', 'литературное прошлое, наречия на -mente'),
    ('B1', 'del. Verbos soler y servir', 'Артикль с предлогом de. Soler и servir', 'привычки (soler), poco/solo'),
    ('B1', 'Futuro imperfecto (futuro simple)', 'Будущее время (Futuro imperfecto)', 'правильные и неправильные основы'),
    ('B1', 'estar + gerundio y la voz pasiva', 'estar + gerundio и страдательный залог', 'длительность, пассив с ser'),
    ('B1', 'Pronombres posesivos', 'Притяжательные местоимения-существительные', 'mío, tuyo, suyo без повтора'),
    ('B1', 'Futuro perfecto. Al + infinitivo', 'Будущее сложное (Futuro perfecto). Al + инфинитив', 'догадки о прошлом, изящный оборот'),
    ('B1', 'Todos los tiempos del indicativo', 'Все времена изъявительного. Безличные формы', 'hay / hay que во всех временах'),
    ('B1', 'Estar, ser, ir, saber, hacer en todos los tiempos', 'Спряжение estar, ser, ir, saber, hacer', 'перифразы acabar de, dejar de'),
    ('B1', 'Estar, ser y formas impersonales de haber', 'Употребление estar, ser и форм haber', 'смена смысла: es bueno / está bueno'),
    ('B1', 'El cual, la preposición por. Sentir, soltar, poner', 'Местоимение el cual, предлог por', '7 значений por, оборот volver a'),
    ('B1', 'Subjuntivo. Imperativo negativo', 'Сослагательное (Subjuntivo). Повелительное', 'введение в presente de subjuntivo'),
    ('B1', 'Subjuntivo (-er/-ir). para que', 'Presente de subjuntivo II–III спряжений', 'отрицательные приказы, союз para que'),
    ('B1', 'Subjuntivo irregular. Es necesario que', 'Subjuntivo неправильных. Безличные обороты', 'hacer, decir, ir; «необходимо, чтобы»'),
    ('B1', 'Uso del subjuntivo: a que / para que. He de', 'Употребление subjuntivo. He de', 'гипотетические объекты, оборот he de'),
    ('B1', 'Subjuntivo: saber, sentir, encontrar', 'Subjuntivo: saber, sentir, encontrar', 'эмоции, сомнение, уступки (aunque)'),
    ('B1', 'Subjuntivo tras cuando, mientras, ojalá, quizás', 'Subjuntivo после cuando, mientras, ojalá, quizás', 'будущее через союзы, «ojalá»'),
    ('B1', 'La conjunción sino. La preposición a', 'Союз sino, предлог a', 'будущее для предположения'),
    # ---- B2 (Lessons 50–60) ----
    ('B2', 'Condicional simple (potencial) y concordancia', 'Условное наклонение (Potencial) и согласование', 'согласование времён (будущее в прошлом)'),
    ('B2', 'Imperfecto de subjuntivo. Condicionales con si', 'Imperfecto de subjuntivo. Условия с si', 'нереальные условия, формы -ara/-ase'),
    ('B2', 'Imperfecto de subjuntivo (-er/-ir e irregulares)', 'Imperfecto de subjuntivo II, III и неправильных', 'универсальное образование от Indefinido'),
    ('B2', 'Perfecto de subjuntivo', 'Сложное прошедшее сослагательного (Perfecto de subjuntivo)', 'haya hecho; глагол coger; junto'),
    ('B2', 'Condicional compuesto y pluscuamperfecto de subjuntivo', 'Potencial compuesto и Pluscuamperfecto de subjuntivo', 'нереальные условия в прошлом'),
    ('B2', 'Concordancia de los tiempos verbales', 'Согласование глагольных времён (Concordancia)', 'сдвиг времён в indicativo и subjuntivo'),
    ('B2', 'El infinitivo compuesto. El artículo: reglas generales', 'Сложная форма инфинитива. Артикль: общие правила', 'haber + participio как инфинитив'),
    ('B2', 'Casos especiales del artículo', 'Особые случаи употребления артикля', 'артикль с именами, титулами, датами'),
    ('B2', 'Orden de palabras y colocación de pronombres', 'Порядок слов и место местоимений-дополнений', 'энклиза и проклиза, два местоимения'),
    ('B2', 'Preposiciones y numerales de 100 a un millón', 'Предлоги и числительные от 100 до миллиона', 'годы и даты, 4 главных предлога'),
    ('B2', 'Reglas de división y puntuación', 'Правила переносов и пунктуация', 'знаки препинания, деление на слоги'),
]


def _build() -> list[dict]:
    return [{'n': i + 1, 'level': lvl, 'es': es, 'ru': ru, 'focus': focus}
            for i, (lvl, es, ru, focus) in enumerate(_TOPICS)]


SYLLABUS = _build()
