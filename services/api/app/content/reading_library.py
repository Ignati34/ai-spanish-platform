# -*- coding: utf-8 -*-
"""Seed content for the reading library.

READING_TEXTS: 5 original, license-clean graded reading passages per CEFR level (A1→C2),
readable in the browser and downloadable as .txt. Difficulty rises with the level.

ONLINE_RESOURCES: 20 curated links to well-known, generally free online Spanish textbooks
and web services. Links are editable data — verify/adjust in the admin if any change.
"""

READING_TEXTS = [
    # -------- A1 --------
    {'level': 'A1', 'title': 'Mi familia', 'body':
        'Me llamo Ana. Tengo veinte años y vivo en Madrid. Mi familia es pequeña. '
        'Tengo un hermano y una hermana. Mi padre trabaja en un banco y mi madre es '
        'profesora. Los fines de semana comemos juntos en casa. Me gusta mucho mi familia.'},
    {'level': 'A1', 'title': 'Un día normal', 'body':
        'Todos los días me levanto a las siete. Desayuno café con leche y pan. '
        'Voy al trabajo en autobús. A la una como con mis compañeros. Por la tarde '
        'estudio español en casa. Por la noche veo la televisión y leo un poco.'},
    {'level': 'A1', 'title': 'En el mercado', 'body':
        'Los sábados voy al mercado. Compro fruta, verdura y pan. Las manzanas son '
        'rojas y las naranjas son dulces. El pan está caliente. La vendedora es muy '
        'simpática. Todo es fresco y barato. Me gusta mucho comprar aquí.'},
    {'level': 'A1', 'title': 'Mi casa', 'body':
        'Vivo en un piso pequeño. Tiene dos habitaciones, una cocina y un baño. '
        'En el salón hay un sofá, una mesa y muchos libros. Mi habitación favorita '
        'es la cocina, porque me gusta cocinar. Desde la ventana veo un parque verde.'},
    {'level': 'A1', 'title': 'El fin de semana', 'body':
        'El sábado por la mañana voy al parque con mi perro. Por la tarde visito a '
        'mis amigos. El domingo descanso en casa. Preparo una comida rica y llamo a '
        'mi familia. Los fines de semana son cortos, pero me gustan mucho.'},

    # -------- A2 --------
    {'level': 'A2', 'title': 'Un viaje a la playa', 'body':
        'El verano pasado fui a la playa con mis amigos. Cogimos el tren por la mañana '
        'y llegamos a mediodía. Hacía mucho calor, así que nos bañamos en el mar y '
        'comimos un helado. Por la tarde dimos un paseo y sacamos muchas fotos. '
        'Volvimos cansados, pero muy contentos. Fue un día perfecto.'},
    {'level': 'A2', 'title': 'Buscando trabajo', 'body':
        'Marta terminó sus estudios el año pasado y ahora busca trabajo. Cada día '
        'lee anuncios en internet y envía su currículum. La semana pasada tuvo una '
        'entrevista en una empresa de turismo. Estaba nerviosa, pero respondió bien '
        'a todas las preguntas. Todavía espera una respuesta, pero se siente optimista.'},
    {'level': 'A2', 'title': 'Una receta fácil', 'body':
        'Hoy voy a preparar una tortilla de patatas. Primero corto las patatas y la '
        'cebolla. Después las frío en aceite. Mientras tanto, bato cuatro huevos con '
        'un poco de sal. Cuando las patatas están listas, las mezclo con los huevos y '
        'lo cocino todo en la sartén. ¡Es sencillo y está riquísimo!'},
    {'level': 'A2', 'title': 'Mi ciudad ha cambiado', 'body':
        'Cuando era niño, mi ciudad era muy tranquila. Había pocos coches y muchos '
        'árboles. Ahora hay más gente, más tráfico y edificios más altos. Antes '
        'jugábamos en la calle; hoy los niños juegan en casa. Me gusta el progreso, '
        'pero a veces echo de menos el silencio de antes.'},
    {'level': 'A2', 'title': 'Planes para las vacaciones', 'body':
        'El mes que viene vamos a viajar a Andalucía. Vamos a visitar Sevilla, '
        'Córdoba y Granada. Queremos ver la Alhambra y pasear por los barrios '
        'antiguos. Si hace buen tiempo, iremos también a la costa. Todavía no hemos '
        'reservado el hotel, pero lo haremos esta semana. ¡Estoy deseando ir!'},

    # -------- B1 --------
    {'level': 'B1', 'title': 'El primer día de trabajo', 'body':
        'Cuando llegué a la oficina, estaba tan nervioso que casi olvidé mi nombre. '
        'Mi jefa me presentó al equipo y me explicó mis tareas. Al principio todo me '
        'parecía complicado, pero mis compañeros me ayudaron con paciencia. Durante la '
        'comida hablamos de nuestras aficiones y me sentí más tranquilo. Al final del '
        'día entendí que había tomado la decisión correcta al aceptar aquel puesto.'},
    {'level': 'B1', 'title': 'Vivir en otro país', 'body':
        'Mudarse a otro país no es fácil. Además del idioma, hay que acostumbrarse a '
        'nuevas costumbres, horarios y sabores. Al principio me costaba entender los '
        'chistes y las expresiones, pero poco a poco todo empezó a tener sentido. Lo '
        'que más me ayudó fue hacer amigos locales. Gracias a ellos, hoy me siento '
        'como en casa, aunque a veces todavía extraño mi país.'},
    {'level': 'B1', 'title': 'La tecnología y nosotros', 'body':
        'Hoy en día es difícil imaginar la vida sin teléfonos móviles. Nos permiten '
        'trabajar, estudiar y mantenernos en contacto con la gente que queremos. Sin '
        'embargo, también nos quitan tiempo y atención. Muchos expertos recomiendan '
        'desconectar un rato cada día. En mi opinión, la tecnología es una herramienta '
        'útil, siempre que sepamos usarla con cabeza.'},
    {'level': 'B1', 'title': 'Un malentendido', 'body':
        'Había quedado con Luis a las seis, pero él no llegaba. Lo esperé media hora y '
        'empecé a preocuparme. Cuando por fin lo llamé, me di cuenta de que nos '
        'habíamos confundido de lugar: yo estaba en la cafetería del centro y él, en '
        'la de la estación. Nos reímos del malentendido y quedamos de nuevo para el '
        'día siguiente. A veces los pequeños errores se convierten en buenas historias.'},
    {'level': 'B1', 'title': 'El valor de leer', 'body':
        'Leer es una de las mejores maneras de aprender un idioma. Cuando leemos, no '
        'solo memorizamos palabras, sino que las vemos en contexto. Además, la lectura '
        'nos abre la puerta a otras culturas y formas de pensar. No importa si empezamos '
        'con textos sencillos: lo importante es hacerlo con regularidad. Con el tiempo, '
        'lo que antes parecía difícil se vuelve natural.'},

    # -------- B2 --------
    {'level': 'B2', 'title': 'El arte de equivocarse', 'body':
        'Solemos ver los errores como algo negativo, pero en realidad son una parte '
        'esencial del aprendizaje. Cada vez que nos equivocamos, nuestro cerebro presta '
        'más atención y corrige el rumbo. Los mejores estudiantes no son los que nunca '
        'fallan, sino los que no tienen miedo de intentarlo. Si tratáramos cada error '
        'como una lección, aprenderíamos mucho más rápido. Al fin y al cabo, nadie '
        'aprende a caminar sin caerse unas cuantas veces.'},
    {'level': 'B2', 'title': 'La ciudad de noche', 'body':
        'Cuando cae la noche, la ciudad cambia por completo. Las calles que de día '
        'están llenas de prisa se vuelven tranquilas y misteriosas. Los escaparates '
        'iluminados parecen pequeños cuadros y el eco de los pasos suena distinto. A '
        'algunos les asusta ese silencio; a mí, en cambio, me fascina. Es como si la '
        'ciudad, cansada del ruido, respirara por fin con calma.'},
    {'level': 'B2', 'title': 'Consumir con conciencia', 'body':
        'Vivimos en una sociedad que nos anima a comprar sin parar. La publicidad nos '
        'convence de que necesitamos cosas que en realidad podríamos evitar. Consumir '
        'con conciencia no significa renunciar a todo, sino elegir mejor: preferir la '
        'calidad a la cantidad y pensar en el impacto de nuestras decisiones. Pequeños '
        'cambios, si los adopta mucha gente, pueden transformar el mundo.'},
    {'level': 'B2', 'title': 'El primer viaje solo', 'body':
        'Nunca había viajado solo hasta aquel verano. Al principio, la idea me daba '
        'cierto miedo: no conocía a nadie y apenas hablaba el idioma. Sin embargo, '
        'aquella experiencia me enseñó más que cualquier libro. Aprendí a resolver '
        'problemas, a confiar en los demás y, sobre todo, a disfrutar de mi propia '
        'compañía. Volví con la maleta llena de recuerdos y con la sensación de '
        'haber crecido.'},
    {'level': 'B2', 'title': 'La memoria de los sabores', 'body':
        'Dicen que ningún sentido despierta los recuerdos como el gusto. Basta con '
        'probar un plato de la infancia para volver, por un instante, a la cocina de '
        'nuestros abuelos. Los sabores guardan historias que las palabras a veces no '
        'alcanzan a contar. Quizá por eso, cuando estamos lejos de casa, cocinar lo de '
        'siempre se convierte en una forma de no olvidar quiénes somos.'},

    # -------- C1 --------
    {'level': 'C1', 'title': 'El precio del progreso', 'body':
        'Cada avance tecnológico trae consigo promesas y renuncias. Ganamos comodidad, '
        'pero a menudo la pagamos con nuestra intimidad; ahorramos tiempo, aunque lo '
        'llenamos enseguida de nuevas obligaciones. No se trata de rechazar el progreso, '
        'sino de preguntarnos qué estamos dispuestos a ceder a cambio. Una sociedad '
        'madura no es la que más innova, sino la que reflexiona sobre las consecuencias '
        'de aquello que inventa. Al fin y al cabo, el progreso solo tiene sentido si '
        'mejora la vida de las personas.'},
    {'level': 'C1', 'title': 'Elogio de la lentitud', 'body':
        'En un mundo que premia la rapidez, detenerse se ha vuelto casi un acto de '
        'rebeldía. Corremos de una tarea a otra sin apenas saborear ninguna, como si el '
        'valor de la vida se midiera por la cantidad de cosas que logramos encajar en un '
        'día. Sin embargo, hay experiencias —una conversación, un paseo, una lectura— '
        'que solo se disfrutan despacio. Recuperar la lentitud no es perder el tiempo, '
        'sino devolverle su sentido.'},
    {'level': 'C1', 'title': 'La lengua que nos habita', 'body':
        'Aprender un idioma no consiste únicamente en acumular vocabulario y reglas; es '
        'adoptar una nueva manera de mirar el mundo. Cada lengua recorta la realidad a '
        'su manera, subraya unos matices y silencia otros. Por eso quien habla varias '
        'lenguas no solo dispone de más palabras, sino de más perspectivas. En cierto '
        'sentido, cada idioma que aprendemos nos vuelve una persona ligeramente distinta.'},
    {'level': 'C1', 'title': 'El extraño hábito de leer', 'body':
        'Resulta curioso que, pudiendo elegir entre mil distracciones inmediatas, haya '
        'quienes sigan prefiriendo el esfuerzo silencioso de la lectura. Leer exige '
        'paciencia y concentración, virtudes cada vez más escasas. Y, sin embargo, '
        'quienes se aficionan a los libros descubren un placer que no se agota: el de '
        'habitar, durante unas horas, una conciencia ajena. Ningún otro invento humano '
        'permite semejante viaje sin moverse del sitio.'},
    {'level': 'C1', 'title': 'Sobre la amistad', 'body':
        'La amistad verdadera se reconoce menos en los buenos momentos que en los '
        'difíciles. Es fácil acompañar a alguien cuando todo va bien; lo raro es '
        'permanecer cuando llegan las sombras. Un buen amigo no es el que siempre nos '
        'da la razón, sino el que se atreve a contradecirnos por nuestro bien. Cultivar '
        'esas relaciones lleva tiempo y cuidado, pero pocas cosas dan tanto sentido a '
        'la vida como saberse acompañado.'},

    # -------- C2 --------
    {'level': 'C2', 'title': 'La paradoja de la elección', 'body':
        'Se nos ha repetido que cuantas más opciones tengamos, más libres seremos; sin '
        'embargo, la experiencia cotidiana desmiente a menudo esa premisa. Ante un '
        'exceso de alternativas, no pocas veces nos paraliza el temor a equivocarnos, y '
        'aquello que prometía emanciparnos acaba abrumándonos. Quizá la verdadera '
        'libertad no resida en poder elegirlo todo, sino en saber renunciar con lucidez '
        'a lo superfluo. Elegir, al fin y al cabo, es también el arte de descartar sin '
        'lamentarlo demasiado.'},
    {'level': 'C2', 'title': 'El idioma como frontera', 'body':
        'Toda lengua traza, casi sin que lo advirtamos, los límites de lo pensable. '
        'Aquello para lo que carecemos de palabras tiende a difuminarse, como si no '
        'existiera del todo; y, a la inversa, nombrar algo es una manera de conferirle '
        'realidad. De ahí que aprender otra lengua sea, en el fondo, ensanchar las '
        'propias fronteras mentales: descubrimos matices que ignorábamos y conceptos '
        'que nuestra lengua materna jamás nos habría permitido formular con precisión.'},
    {'level': 'C2', 'title': 'Contra la nostalgia', 'body':
        'La nostalgia posee un encanto engañoso: embellece el pasado a fuerza de '
        'recortarle las asperezas. Recordamos los veranos infinitos y olvidamos el '
        'tedio; evocamos las voces queridas y silenciamos las discusiones. No es que el '
        'pasado fuera mejor, sino que la memoria, piadosa, lo maquilla. Rendirse a esa '
        'añoranza tiene un precio: mientras suspiramos por lo que fue, dejamos escapar '
        'lo que todavía podría ser. Vivir hacia atrás es una forma sutil de no vivir.'},
    {'level': 'C2', 'title': 'El silencio elocuente', 'body':
        'Solemos asociar la comunicación con la palabra, y no obstante buena parte de '
        'lo esencial se transmite en el silencio. Una pausa oportuna dice a veces más '
        'que un discurso; un silencio incómodo delata lo que ninguna frase se atrevería '
        'a confesar. Quien domina el arte de callar en el momento preciso posee un '
        'recurso expresivo tan poderoso como el de hablar. Al fin y al cabo, también '
        'los espacios en blanco forman parte de la música.'},
    {'level': 'C2', 'title': 'La utilidad de lo inútil', 'body':
        'En una época obsesionada con la rentabilidad, cuesta defender aquello que no '
        'produce beneficios tangibles: la poesía, la filosofía, el simple placer de '
        'contemplar. Y sin embargo, esas actividades presuntamente inútiles son las que '
        'nos distinguen y nos humanizan. Reducirlo todo a su valor económico equivale a '
        'empobrecer la existencia. Acaso lo verdaderamente imprescindible sea, '
        'precisamente, aquello que jamás cabría en una hoja de cálculo.'},
]


ONLINE_RESOURCES = [
    {'title': 'Diccionario de la RAE (DLE)', 'url': 'https://dle.rae.es', 'category': 'reference',
     'level': None, 'description': 'Diccionario oficial de la lengua española.'},
    {'title': 'WordReference', 'url': 'https://www.wordreference.com/es/', 'category': 'reference',
     'level': None, 'description': 'Diccionario bilingüe y foros de dudas.'},
    {'title': 'Conjugador Reverso', 'url': 'https://conjugador.reverso.net/conjugacion-espanol.html',
     'category': 'reference', 'level': None, 'description': 'Conjugación de cualquier verbo español.'},
    {'title': 'SpanishDict', 'url': 'https://www.spanishdict.com', 'category': 'course',
     'level': 'A1', 'description': 'Diccionario, conjugador y lecciones de gramática.'},
    {'title': 'StudySpanish', 'url': 'https://studyspanish.com', 'category': 'course',
     'level': 'A1', 'description': 'Curso gratuito con gramática, vocabulario y pronunciación.'},
    {'title': 'Lingolia Español', 'url': 'https://espanol.lingolia.com/es/', 'category': 'grammar',
     'level': 'A2', 'description': 'Explicaciones de gramática con ejercicios.'},
    {'title': 'Profe de ELE', 'url': 'https://www.profedeele.es', 'category': 'course',
     'level': 'B1', 'description': 'Actividades y vídeos para estudiantes de ELE.'},
    {'title': 'Centro Virtual Cervantes', 'url': 'https://cvc.cervantes.es', 'category': 'course',
     'level': 'B2', 'description': 'Recursos del Instituto Cervantes para aprender español.'},
    {'title': 'Practica Español (EFE)', 'url': 'https://www.practicaespanol.com', 'category': 'reading',
     'level': 'B1', 'description': 'Noticias con ejercicios y niveles.'},
    {'title': 'VeinteMundos', 'url': 'https://www.veintemundos.com', 'category': 'reading',
     'level': 'B1', 'description': 'Revistas de lectura graduada para estudiantes.'},
    {'title': 'Ciudad Seva (cuentos)', 'url': 'https://ciudadseva.com/biblioteca/', 'category': 'reading',
     'level': 'C1', 'description': 'Gran biblioteca digital de cuentos en español.'},
    {'title': 'AlbaLearning (audiolibros)', 'url': 'https://albalearning.com', 'category': 'reading',
     'level': 'B2', 'description': 'Textos clásicos con audio para leer y escuchar.'},
    {'title': 'News in Slow Spanish', 'url': 'https://www.newsinslowspanish.com', 'category': 'listening',
     'level': 'B1', 'description': 'Noticias narradas despacio, por niveles.'},
    {'title': 'Notes in Spanish', 'url': 'https://www.notesinspanish.com', 'category': 'listening',
     'level': 'A2', 'description': 'Pódcast de conversaciones reales con material de apoyo.'},
    {'title': 'Dreaming Spanish', 'url': 'https://www.dreamingspanish.com', 'category': 'listening',
     'level': 'A1', 'description': 'Vídeos de input comprensible para todos los niveles.'},
    {'title': 'Language Transfer', 'url': 'https://www.languagetransfer.org', 'category': 'listening',
     'level': 'A1', 'description': 'Curso de audio gratuito centrado en entender la lógica del idioma.'},
    {'title': 'Forvo (pronunciación)', 'url': 'https://forvo.com/languages/es/', 'category': 'pronunciation',
     'level': None, 'description': 'Pronunciación de palabras por hablantes nativos.'},
    {'title': 'LyricsTraining', 'url': 'https://lyricstraining.com/es', 'category': 'practice',
     'level': 'A2', 'description': 'Aprende con canciones rellenando las letras.'},
    {'title': 'Readlang', 'url': 'https://readlang.com', 'category': 'reading',
     'level': 'B1', 'description': 'Lee textos web con traducción al instante y tarjetas.'},
    {'title': 'Wikilibros: Español', 'url': 'https://es.wikibooks.org', 'category': 'course',
     'level': None, 'description': 'Manuales y libros de texto abiertos y gratuitos.'},
]
