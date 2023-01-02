from typing import List

from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from db import db_league
from db.database import get_db
from routers import image
from routers.schemas import LeagueDisplay, LeagueBase

router = APIRouter(
    prefix="/league",
    tags=["league"]
)


@router.post("/", response_model=LeagueDisplay)
def add(request: LeagueBase, db: Session = Depends(get_db)):
    return db_league.add_team(db, request)


@router.get("/all", response_model=List[LeagueDisplay])
def get_all(db: Session = Depends(get_db)):
    return db_league.get_all_teams(db)


@router.post("/image")
def upload_league_image(img: UploadFile = File(...)):
    return image.upload_image("leagues", img)
