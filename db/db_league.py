from fastapi import HTTPException, status
from db.models import DbLeague
from routers.schemas import LeagueBase
from routers.slug import name_to_slug
from sqlalchemy.orm import Session


def add_team(db: Session, request: LeagueBase):
    league = DbLeague(
        name=request.name.capitalize(),
        country=request.country.capitalize(),
        img=f"images/{request.img}",
        slug=name_to_slug(request.name)
    )
    db.add(league)
    db.commit()
    db.refresh(league)
    return league


def get_all_teams(db: Session):
    return db.query(DbLeague).all()
