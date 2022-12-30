from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db import models
from db.database import engine
from routers import league,team, player

app = FastAPI()

app.include_router(league.router)
app.include_router(team.router)
app.include_router(player.router)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
models.Base.metadata.create_all(engine)
app.mount("/images", StaticFiles(directory="images"), name="images")