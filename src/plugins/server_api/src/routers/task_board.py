from fastapi import APIRouter
from models.token import *
router = APIRouter()

@router.get('/task-board')
async def get_task_board():
    return ['zxc', 'qwe']


@router.post('/create-board')
async def create_board(board: Board) -> Board:
    