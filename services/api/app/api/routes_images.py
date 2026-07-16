from fastapi import APIRouter

router = APIRouter(prefix='/images', tags=['images'])


@router.get('/status')
def status():
    return {'module': 'images', 'status': 'stub'}
