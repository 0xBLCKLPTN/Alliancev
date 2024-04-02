from typing import Dict, List
from pydantic import BaseModel

class Tokens(BaseModel):
    access_token: str
    refresh_token: str

class AllianceShortInfo(BaseModel):
    name: str
    token: str
    members: int

class User(BaseModel):
    username: str
    tokens: Tokens
    password: str
    alliance_info: AllianceShortInfo = None

class BoardInfo(BaseModel):
    name: str

class Task(BaseModel):
    name: str
    description: str

class Board(BaseModel):
    info: BoardInfo
    tasks: List[Task] = List[None]