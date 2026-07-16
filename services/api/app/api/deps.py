from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.core.security import decode_token
from app.db.session import get_db
from app.models.user import User

bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:
    if not credentials:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authenticated')
    subject = decode_token(credentials.credentials)
    if not subject:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
    user = db.get(User, subject)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    return user


ADMIN_ROLES = {'super_admin', 'support_admin', 'billing_admin', 'content_admin', 'developer_admin', 'admin'}


def require_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role not in ADMIN_ROLES:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Admin privileges required')
    return current_user


def require_billing_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role not in {'super_admin', 'billing_admin', 'admin'}:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Billing admin privileges required')
    return current_user
