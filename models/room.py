from pydantic import BaseModel
from datetime import datetime


class Room(BaseModel):
    id:str 
    password:str 
    title: str 
    rules: str 
    start_time: datetime
    user_id: int 
    game_id: int