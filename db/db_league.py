from fastapi import HTTPException, status
from db.models import DbLeague
from routers.schemas import LeagueBase
from routers.slug import name_to_slug
from sqlalchemy.orm import Session


def add_team(db: Session, request: LeagueBase):
    league = DbLeague(
        name=request.name,
        country=request.country,
        img=f"images/leagues/{request.img}",
        slug=name_to_slug(request.name)
    )
    db.add(league)
    db.commit()
    db.refresh(league)
    return league


def get_all_teams(db: Session):
    return db.query(DbLeague).all()


def get_team_id(db: Session, league_id: int):
    league = db.query(DbLeague).filter(DbLeague.id == league_id).first()
    if not league:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="League has not been found!")
    return league