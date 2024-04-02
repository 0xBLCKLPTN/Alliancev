from fastapi import APIRouter

router = APIRouter()

@router.get('/task-board')
async def get_task_board():
    return ['zxc', 'qwe']