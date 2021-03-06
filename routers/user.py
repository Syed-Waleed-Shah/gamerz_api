from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm.session import Session 
from database import db
from auth.user_auth import signJWT


router = APIRouter(prefix='/user', tags=['User']) 

# get_db = get_db

# @router.post('/')
# def create_user(user: schemas.UserCreate, db: Session = Depends(db)):
#     userModel = models.User(name=user.name, username=user.name, phone=user.phone, password=user.password, country=user.country, fav_game=user.fav_game)
#     db.add(userModel)
#     db.commit()
#     db.refresh(userModel)
#     return signJWT(userModel.id)    
