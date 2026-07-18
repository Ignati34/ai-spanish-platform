"""Test harness.

Runs the full app against SQLite by shimming the only Postgres-specific column
type (UUID) to a portable CHAR(32). Uses AI_PROVIDER=stub so no network/keys are
needed. On a real Postgres, point TEST_DATABASE_URL at it instead.
"""
import os
import tempfile
import uuid

import pytest

# --- configure env BEFORE importing the app ---
_TMP = tempfile.mkdtemp()
os.environ.setdefault('DATABASE_URL', os.environ.get('TEST_DATABASE_URL', f'sqlite:///{_TMP}/test.db'))
os.environ.setdefault('JWT_SECRET', 'test-secret')
os.environ.setdefault('AI_PROVIDER', 'stub')
os.environ.setdefault('AI_CACHE_ENABLED', 'false')
os.environ.setdefault('UPLOAD_DIR', f'{_TMP}/uploads')
os.environ.setdefault('RATE_LIMIT_ENABLED', 'false')

from sqlalchemy import CHAR
from sqlalchemy.types import TypeDecorator
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class _GUID(TypeDecorator):
    """Portable UUID: native on Postgres, CHAR(32) hex on SQLite."""
    impl = CHAR(32)
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return (value if isinstance(value, uuid.UUID) else uuid.UUID(str(value))).hex

    def process_result_value(self, value, dialect):
        return None if value is None else uuid.UUID(value)


from app.db import base as db_base  # noqa: E402  (registers all models)
from app.db.session import Base, engine  # noqa: E402

# Only shim when running on SQLite; keep native UUID on Postgres.
if engine.dialect.name == 'sqlite':
    for _table in Base.metadata.tables.values():
        for _col in _table.columns:
            if isinstance(_col.type, PG_UUID):
                _col.type = _GUID()

from fastapi.testclient import TestClient  # noqa: E402
from app.main import app  # noqa: E402


@pytest.fixture(scope='session', autouse=True)
def _create_schema():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def auth(client):
    """Register a fresh user, return an Authorization header dict."""
    email = f'user_{uuid.uuid4().hex[:8]}@example.com'
    r = client.post('/api/auth/register', json={'email': email, 'password': 'password123', 'native_language': 'ru'})
    assert r.status_code == 200, r.text
    token = r.json()['access_token']
    return {'Authorization': f'Bearer {token}'}
