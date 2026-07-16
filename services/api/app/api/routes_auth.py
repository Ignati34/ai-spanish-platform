from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import hash_password, verify_password, create_access_token
from app.db.session import get_db
from app.models.user import User, UserProfile
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/register', response_model=TokenResponse)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email already registered')
    user = User(
        email=payload.email,
        password_hash=hash_password(payload.password),
        native_language=payload.native_language,
        interface_language=payload.native_language,
    )
    db.add(user)
    db.flush()
    db.add(UserProfile(user_id=user.id, current_cefr_level='A1'))
    db.commit()
    token = create_access_token(str(user.id))
    return TokenResponse(access_token=token)


@router.post('/login', response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    token = create_access_token(str(user.id))
    return TokenResponse(access_token=token)
