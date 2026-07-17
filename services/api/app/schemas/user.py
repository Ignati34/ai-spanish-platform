import uuid
from pydantic import BaseModel, EmailStr, field_validator

SUPPORTED_LANGUAGES = {'ru', 'uk', 'ar', 'fr', 'es', 'en'}


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


class UserUpdate(BaseModel):
    native_language: str | None = None
    interface_language: str | None = None

    @field_validator('native_language', 'interface_language')
    @classmethod
    def _check_lang(cls, v):
        if v is not None and v not in SUPPORTED_LANGUAGES:
            raise ValueError(f'Unsupported language: {v}')
        return v
