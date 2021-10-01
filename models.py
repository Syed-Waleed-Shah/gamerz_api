# This file will contain all the model classes which inherit from pydantic BaseModel. These models will be used in API request body
from pydantic import BaseModel, Field
from sqlalchemy.sql.sqltypes import DateTime 
from datetime import datetime
from typing import Optional
# ---------------------------------------------------------------------
# 1) User schemas
# ---------------------------------------------------------------------
class User(BaseModel):
    name: str = Field(...) 
    username: str = Field(...) 
    phone: str = Field(...) 
    password: str = Field(...) 
    country: str = Optional[str] 
    fav_game: str = Optional[str]

    class Config:
        orm_mode = True



class UserCreate(BaseModel):
    name: str = Field(...) 
    phone: str = Field(...) 
    password: str = Field(...) 
    country: str = None 
    fav_game: str = None

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    phone: str = Field(...) 
    password: str = Field(...)

    class Config:
        orm_mode = True



# ---------------------------------------------------------------------
# 2) Room schemas
# ---------------------------------------------------------------------
class RoomCreate(BaseModel):
    room_id: int = Field(..., gt=0)
    password: str  = Field(default=None)
    game: str  = Field(..., min_length=1)
    server: str  = Field(..., min_length=1)
    map: str  = Field(..., min_length=1)
    type: str  = Field(...,min_length=1)

class RoomUpdate(BaseModel):
    room_id: Optional[int] = None
    password: Optional[str] = None
    game: Optional[str] = None
    server: Optional[str] = None
    map: Optional[str] = None
    type: Optional[str] = None




