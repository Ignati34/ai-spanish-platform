"""Seed reference data: CEFR levels A1-C2, plans (EUR), multilingual demo lessons,
and a bootstrap admin. Safe to run repeatedly (idempotent by natural keys)."""
from app.core.config import get_settings
from app.core.security import hash_password
from app.db.session import SessionLocal, engine
from app.db.base import Base
from app.content.seed_content import CEFR_LEVELS, SAMPLE_LESSONS
from app.content.curriculum import CURRICULUM
from app.models.course import CEFRLevel, CourseModule, Lesson
from app.models.subscription import Plan
from app.models.user import User, UserProfile

settings = get_settings()


def _seed_levels(db):
    existing = {l.code for l in db.query(CEFRLevel).all()}
    code_to_id = {}
    for lvl in CEFR_LEVELS:
        if lvl['code'] in existing:
            code_to_id[lvl['code']] = db.query(CEFRLevel).filter(CEFRLevel.code == lvl['code']).first().id
            continue
        row = CEFRLevel(code=lvl['code'], title=lvl['title']['es'], description=lvl['title'].get('en'), sort_order=lvl['sort'])
        db.add(row)
        db.flush()
        code_to_id[lvl['code']] = row.id
    return code_to_id


def _seed_lessons(db, code_to_id):
    if db.query(Lesson).first():
        return
    modules_by_title = {}
    for spec in SAMPLE_LESSONS:
        level_id = code_to_id[spec['level']]
        mkey = spec['module']['es']
        module = modules_by_title.get(mkey)
        if not module:
            module = CourseModule(cefr_level_id=level_id, title=mkey, description=spec['module'].get('en'), sort_order=1)
            db.add(module)
            db.flush()
            modules_by_title[mkey] = module
        lesson = Lesson(
            module_id=module.id,
            title=spec['title'],
            description=spec['topic']['es'],
            cefr_level=spec['level'],
            native_language='ru',
            lesson_type='course',
            content_json={
                'topic_i18n': spec['topic'],
                'vocabulary': spec['vocabulary'],
                'grammar_topic': spec['grammar_topic'],
                'explanations_i18n': spec['explanations'],
                'dialogue': spec['dialogue'],
            },
        )
        db.add(lesson)


def _seed_plans(db):
    if db.query(Plan).first():
        return
    # Prices in EUR. features_json carries provider-specific plan ids and the
    # marketing feature list rendered in the UI.
    db.add_all([
        Plan(code='free', name='Free', description='Empieza gratis', price_monthly=0, price_yearly=0, currency='eur',
             max_ai_requests_per_month=100, max_transcription_minutes=0, max_storage_mb=100, max_generated_images=3,
             features_json={'features': ['1 nivel', 'Tarjetas limitadas', '5 solicitudes IA/día']}),
        Plan(code='basic', name='Basic', description='Curso + tarjetas + tests', price_monthly=6.99, price_yearly=69.00, currency='eur',
             max_ai_requests_per_month=1500, max_transcription_minutes=30, max_storage_mb=1000, max_generated_images=30,
             features_json={'features': ['Todos los niveles A1–C2', 'Tarjetas y ejercicios', 'Analizador de texto']}),
        Plan(code='pro', name='Pro', description='Voz IA + subida de archivos', price_monthly=14.99, price_yearly=149.00, currency='eur',
             max_ai_requests_per_month=6000, max_transcription_minutes=300, max_storage_mb=5000, max_generated_images=200,
             voice_tutor_enabled=True, podcast_enabled=True, image_generation_enabled=True,
             features_json={'features': ['Tutor de voz IA', 'Subida de audio/PDF', 'Podcast e imágenes'], 'paypal_plan_id': None}),
        Plan(code='premium', name='Premium', description='Vídeo, DELE/SIELE, plan personal', price_monthly=24.99, price_yearly=249.00, currency='eur',
             max_ai_requests_per_month=20000, max_transcription_minutes=1200, max_storage_mb=20000, max_generated_images=1000,
             voice_tutor_enabled=True, podcast_enabled=True, image_generation_enabled=True, video_enabled=True,
             features_json={'features': ['Vídeo y transcripción', 'Preparación DELE/SIELE', 'Plan de estudio personal'], 'paypal_plan_id': None}),
    ])


def _seed_admin(db):
    email = settings.admin_bootstrap_email
    password = settings.admin_bootstrap_password
    if not email or not password:
        return
    if db.query(User).filter(User.email == email).first():
        return
    admin = User(email=email, password_hash=hash_password(password), role='super_admin', native_language='ru', interface_language='ru')
    db.add(admin)
    db.flush()
    db.add(UserProfile(user_id=admin.id, first_name='Admin', current_cefr_level='C2'))


def _seed_curriculum(db):
    """Insert the built-in curriculum (theory + practice). Idempotent.
    Lessons with a syllabus number `n` get a numbered title and store syllabus_n so the AI
    generator skips them. Also removes obsolete ad-hoc A1 lessons (no syllabus_n)."""
    # Cleanup: drop old ad-hoc A1 curriculum lessons that predate the syllabus-aligned A1 set.
    removed = 0
    for l in db.query(Lesson).filter(Lesson.lesson_type == 'curriculum', Lesson.cefr_level.in_(['A1', 'A2', 'B1', 'B2', 'C1', 'C2'])).all():
        if not (l.content_json or {}).get('syllabus_n'):
            db.delete(l)
            removed += 1
    if removed:
        print(f'Curriculum cleanup: -{removed} obsolete ad-hoc lessons.')

    all_cur = db.query(Lesson).filter(Lesson.lesson_type == 'curriculum').all()
    existing_titles = {l.title for l in all_cur}
    by_num = {(l.content_json or {}).get('syllabus_n'): l for l in all_cur if (l.content_json or {}).get('syllabus_n')}
    added = 0
    updated = 0
    for spec in CURRICULUM:
        n = spec.get('n')
        title = f"{n:03d}. {spec['title']}" if n else spec['title']
        if n and n in by_num:
            lesson = by_num[n]
            content = {'theory': spec['theory'], 'exercises': spec['exercises'], 'syllabus_n': n}
            if (lesson.content_json or {}).get('theory') != spec['theory'] or \
                    (lesson.content_json or {}).get('exercises') != spec['exercises'] or lesson.title != title:
                lesson.title = title
                lesson.description = spec['theory'][:400]
                lesson.content_json = content
                updated += 1
            continue
        if title in existing_titles:
            continue
        content = {'theory': spec['theory'], 'exercises': spec['exercises']}
        if n:
            content['syllabus_n'] = n
        db.add(Lesson(
            module_id=None, title=title, description=spec['theory'][:400],
            cefr_level=spec['level'], native_language='ru', lesson_type='curriculum',
            content_json=content,
        ))
        added += 1
    if added or updated:
        print(f'Curriculum seeded: +{added} lessons, updated {updated}.')


def seed() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        code_to_id = _seed_levels(db)
        _seed_lessons(db, code_to_id)
        _seed_curriculum(db)
        _seed_plans(db)
        _seed_admin(db)
        db.commit()
        print('Demo data seeded (levels A1-C2, plans, lessons, admin).')
    finally:
        db.close()


if __name__ == '__main__':
    seed()
