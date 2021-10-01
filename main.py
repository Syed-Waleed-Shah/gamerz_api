from logging import debug
from fastapi import FastAPI
import models
from routers import room, user
import uvicorn



app = FastAPI() 





app.include_router(room.router)
app.include_router(user.router)


if __name__ == '__main__':
    uvicorn.run('main:app', debug=True)
