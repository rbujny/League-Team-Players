from fastapi import HTTPException, status

from db.models import DbLeague
from routers.schemas import LeagueBase
from sqlalchemy.orm import Session


def add_team(db: Session, request: LeagueBase):
    league = DbLeague(
        name=request.name,
        country=request.country,
        img=f"images/{request.img}",
    )
    db.add(league)
    db.commit()
    db.refresh(league)
    return league


def get_all_teams(db: Session):
    return db.query(DbLeague).all()
