from fastapi import APIRouter, Depends
from schemas import Room
from fastapi import Request, HTTPException


router = APIRouter(prefix='/room', tags=['Room']) 


@router.post('/')
def create(room : Room):
    return {'result':'Room created successfully', 'room':room}