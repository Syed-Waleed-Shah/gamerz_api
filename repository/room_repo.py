from sqlalchemy.orm.session import Session
from sqlalchemy.sql import text, select
from models import RoomCreate
from datetime import datetime
from sqlalchemy.engine.cursor import CursorResult
from utils.constants import MAX_RECORDS
from utils.helpers import generate_db_where


def create_room(room: RoomCreate, user_id:int, db:Session):

    data = room.dict()
    data['user_id'] = user_id   # attaching user id with the dict
    data['date'] = datetime.now()    # attaching current datetime with the dict
    db.execute('INSERT INTO rooms(room_id, password, game, server, map, type, user_id, date) values(:room_id, :password, :game, :server, :map, :type, :user_id, :date)', params=data)
    db.commit()
    db.close()
    return True
  


    
def view_all(db: Session):
    result: CursorResult = db.execute('SELECT * from rooms LIMIT :max', params={'max':MAX_RECORDS})
    if result.returns_rows:
        data = result.mappings().all() 
        return data
    

def filter(db: Session, queries):
    if queries:
        filters = generate_db_where(queries)

    result: CursorResult = db.execute('SELECT * from rooms mapper.filters', params={'mapper':{'filters':filters}})
    if result.returns_rows:
        data = result.mappings().all() 
        return data
