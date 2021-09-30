from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.types import Date
from datetime import datetime
from database import Base


# This module represents a room
class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer)
    password = Column(String) 
    game = Column(String) 
    server = Column(String)
    date = Column(DateTime, default=datetime.now)
  

# This module represents a user
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String) 
    username = Column(String) 
    phone = Column(String) 
    password = Column(String) 
    country = Column(String) 
    fav_game = Column(String) 

