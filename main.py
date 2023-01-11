from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from db import models
from db.database import engine
from routers import league, team, player, user
from auth import authentication

app = FastAPI()

app.include_router(league.router)
app.include_router(team.router)
app.include_router(player.router)
app.include_router(user.router)
app.include_router(authentication.router)

# origins = [
#     "http://localhost:8001"
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
async def root():
    return {"welcome": "Welcome in LTP!",
            "docs" : "To see the full functionality of website type "
                     "/docs in website address. "
            }
models.Base.metadata.create_all(engine)
app.mount("/images", StaticFiles(directory="images"), name="images")