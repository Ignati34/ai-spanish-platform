from fastapi import APIRouter

router = APIRouter(prefix='/podcasts', tags=['podcasts'])


@router.get('/status')
def status():
    return {'module': 'podcasts', 'status': 'stub'}
