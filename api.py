from models.room import Room
from fastapi import FastAPI
from models import *

app = FastAPI()

rooms = []



@app.get('/')
def index():    
    return 'Index page'


@app.get('/rooms')
def get_room():
    return rooms

@app.post('/rooms')
def add_room(room:Room):
    rooms.append(room.dict())
    

    