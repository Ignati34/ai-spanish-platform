import uuid
from pydantic import BaseModel, EmailStr


class UserOut(BaseModel):
    id: uuid.UUID
    email: EmailStr
    native_language: str
    interface_language: str
    target_language: str
    role: str
    status: str
    current_cefr_level: str = 'A1'

    model_config = {'from_attributes': True}
