from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User, UserProfile
from app.schemas.user import UserOut

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/me', response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    return UserOut(
        id=current_user.id, email=current_user.email, native_language=current_user.native_language,
        interface_language=current_user.interface_language, target_language=current_user.target_language,
        role=current_user.role, status=current_user.status,
        current_cefr_level=(profile.current_cefr_level if profile else 'A1'),
    )
