from fastapi import APIRouter, Request, HTTPException
from pydantic.fields import Field
from models import RoomCreate
from fastapi.params import Depends, Body, Query, Param
from sqlalchemy.orm.session import Session 
from database import db
from utils.api_docs import docs
from api_docs.paths import room_view_doc
from datetime import datetime
from repository import room_repo


router = APIRouter(prefix='/room', tags=['Room']) 


# Create a new room
@router.post('/', description='Create a room')
def create(room : RoomCreate, user_id:int = Body(...), db: Session = Depends(db)):
    success: bool = room_repo.create_room(room, user_id, db)
    if success:
        return {'success': 'room created'}
    else:
        return {'failed':'unable to create room'}

# View rooms
@router.get('/', description=docs(room_view_doc))
def view(user_id:int = Query(None), game:str = Query(None), db: Session = Depends(db)):
    queries={} 
    if user_id!=None: queries['user_id'] = user_id 
    if game!=None : queries['game'] = game

    
    return room_repo.filter(db, queries=queries)


   


# Delete a room
@router.delete('/', description='Delete a room') 
def delete(room_id: int):
    pass 
