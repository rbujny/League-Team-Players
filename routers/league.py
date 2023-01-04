from typing import List

from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db import db_league
from db.database import get_db
from routers import image
from routers.schemas import LeagueDisplay, LeagueBase, UserAuth

router = APIRouter(
    prefix="/league",
    tags=["league"]
)


@router.post("/", response_model=LeagueDisplay)
def add(request: LeagueBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_league.add_team(db, request)


@router.get("/all", response_model=List[LeagueDisplay])
def get_all(db: Session = Depends(get_db)):
    return db_league.get_all_teams(db)

@router.get("/{league_id}", response_model=LeagueDisplay)
def get_league_by_id(league_id: int, db:Session = Depends(get_db)):
    return db_league.get_team_id(db, league_id)


@router.post("/image")
def upload_league_image(img: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    return image.upload_image("leagues", img)
