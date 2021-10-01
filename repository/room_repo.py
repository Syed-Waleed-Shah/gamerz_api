from fastapi import params
from sqlalchemy.orm import query
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import text, select
from models import RoomCreate, RoomUpdate
from datetime import datetime
from sqlalchemy.engine.cursor import CursorResult
from utils.constants import MAX_RECORDS
from utils.helpers import generate_db_where, generate_db_insert, generate_db_update



def create(room: RoomCreate, user_id:int, db:Session):

    data = room.dict()
    data['user_id'] = user_id   # attaching user id with the dict
    data['date'] = datetime.now()    # attaching current datetime with the dict
    generated = generate_db_insert(data)
    query = f'INSERT INTO rooms{generated}'
    db.execute(query, params=data)
    return True
  


def view(db: Session, queries):
    filters = ''
    if queries:
        filters = generate_db_where(queries)

    query = f'SELECT * from rooms {filters}'

    result: CursorResult = db.execute(query, params=queries)
    if result.returns_rows:
        data = result.mappings().fetchmany(MAX_RECORDS)
        return data

def remove(room_id:int, db: Session):
    query = f'DELETE FROM rooms where id={room_id}'
    db.execute(query)
    return True


def update(room: RoomUpdate, id: int, db:Session):
    data = room.dict(exclude_unset=True)
    generated = generate_db_update(data)
    data['id'] = id
    query = f'UPDATE rooms {generated} WHERE id=:id'
    db.execute(query, params=data)
    return True