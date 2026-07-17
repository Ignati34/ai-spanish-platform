"""Course: CEFR levels and lessons (incl. lessons the learner built via Upload Studio)."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.course import CEFRLevel, Lesson

router = APIRouter(prefix='/course', tags=['course'])


@router.get('/levels')
def list_levels(db: Session = Depends(get_db)):
    levels = db.query(CEFRLevel).order_by(CEFRLevel.sort_order).all()
    if not levels:
        return [{'code': c, 'title': t} for c, t in
                [('A1', 'Beginner'), ('A2', 'Elementary'), ('B1', 'Intermediate'),
                 ('B2', 'Upper-Intermediate'), ('C1', 'Advanced'), ('C2', 'Proficiency')]]
    return [{'code': l.code, 'title': l.title, 'description': l.description} for l in levels]


@router.get('/lessons')
def list_lessons(db: Session = Depends(get_db)):
    lessons = db.query(Lesson).order_by(Lesson.created_at.desc()).limit(200).all()
    return [{'id': str(l.id), 'title': l.title, 'cefr_level': l.cefr_level,
             'description': l.description, 'lesson_type': l.lesson_type} for l in lessons]


@router.get('/lessons/{lesson_id}')
def get_lesson(lesson_id: str, db: Session = Depends(get_db)):
    lesson = db.get(Lesson, lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail='Lesson not found')
    content = lesson.content_json or {}
    return {
        'id': str(lesson.id), 'title': lesson.title, 'cefr_level': lesson.cefr_level,
        'description': lesson.description,
        'summary': (content.get('analysis') or {}).get('summary', lesson.description or ''),
        'analysis': content.get('analysis') or {},
        'cards': content.get('cards') or [],
        'exercises': content.get('exercises') or [],
    }
