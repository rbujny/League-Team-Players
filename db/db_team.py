from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db.models import DbTeam
from routers.schemas import TeamBase


def create(db: Session, request: TeamBase):
    team = DbTeam(
        name=request.name,
        city=request.city,
        img=request.img,
        manager=request.manager,
        year_of_creation=request.year_of_creation,
        league_id=request.league_id
    )
    db.add(team)
    db.commit()
    db.refresh(team)
    return team


def get_teams_league(db: Session, leauge_id: int):
    teams = db.query(DbTeam).filter(DbTeam.league_id == leauge_id).all()
    if not teams:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This league doesn't exsists or has not any "
                                                                          "teams!")
    return teams
def get_team_id(db: Session, team_id: int):
    team = db.query(DbTeam).filter(DbTeam.id == team_id).first()
    if not team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team has not been found!")
    return team