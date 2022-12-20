from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db import models
from db.database import engine
from routers import league

app = FastAPI()

app.include_router(league.router)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
models.Base.metadata.create_all(engine)
app.mount("/images", StaticFiles(directory="images"), name="images")