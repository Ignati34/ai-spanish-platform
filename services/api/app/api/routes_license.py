from fastapi import APIRouter

router = APIRouter(prefix='/license', tags=['license'])


@router.get('/status')
def status():
    return {'module': 'license', 'status': 'stub'}
