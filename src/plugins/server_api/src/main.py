from fastapi import FastAPI
from typing import Dict, List
from models.token import User, Tokens

from routers import task_board

app = FastAPI()
app.include_router(task_board.router)

@app.get('/')
async def check_health() -> Dict[str, str]:
    return {'Health': '100%'}

@app.post('/auth/sign-up')
async def sign_up() -> User:
    return {'username': '123', 'tokens': {'access_token': 'qwe', 'refresh_token': 'zxc'}, 'password': 'vav'}

@app.post('/auth/sign-in')
async def sign_in() -> Tokens:
    return Tokens(access_token='qwe', refresh_token='zxc')

@app.get('/me')
async def get_me() -> User:
    return {'username': '123', 'tokens': {'access_token': 'qwe', 'refresh_token': 'zxc'}, 'password': 'vav'}

@app.post('/update-token')
async def update_token(tokens: Tokens) -> Tokens:
    return Tokens(access_token='qwe', refresh_token='zxc1')