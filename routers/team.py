from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_team
from db.database import get_db
from routers.schemas import TeamDisplay, TeamBase

router = APIRouter(
    prefix="/team",
    tags=["team"]
)

@router.post("/", response_model=TeamDisplay)
def create_team(request: TeamBase, db:Session = Depends(get_db)):
    return db_team.create(db,request)


@router.get("/{league_id}/teams", response_model=List[TeamDisplay])
def get_teams_by_league(league_id: int, db:Session = Depends(get_db)):
    return db_team.get_teams_league(db, league_id)

@router.get("/{team_id}", response_model=TeamDisplay)
def get_team_by_id(team_id: int, db:Session = Depends(get_db)):
    return db_team.get_team_id(db, team_id)