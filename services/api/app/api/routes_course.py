from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.course import CEFRLevel, Lesson

router = APIRouter(prefix='/course', tags=['course'])


@router.get('/levels')
def list_levels(db: Session = Depends(get_db)):
    levels = db.query(CEFRLevel).order_by(CEFRLevel.sort_order).all()
    if not levels:
        return [
            {'code': 'A1', 'title': 'Beginner'},
            {'code': 'A2', 'title': 'Elementary'},
            {'code': 'B1', 'title': 'Intermediate'},
        ]
    return levels


@router.get('/lessons')
def list_lessons(db: Session = Depends(get_db)):
    lessons = db.query(Lesson).limit(50).all()
    if not lessons:
        return [
            {'id': 'demo-a1-1', 'title': 'Saludos y presentaciones', 'cefr_level': 'A1'},
            {'id': 'demo-a1-2', 'title': 'En el café', 'cefr_level': 'A1'},
        ]
    return lessons
