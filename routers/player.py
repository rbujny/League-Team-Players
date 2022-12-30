from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_player
from db.database import get_db
from routers.schemas import PlayerDisplay, PlayerBase

router = APIRouter(
    prefix="/player",
    tags=["player"]
)

@router.post("/", response_model=PlayerDisplay)
def create_player(request: PlayerBase, db:Session = Depends(get_db)):
    return db_player.create(db,request)


@router.post("/transfer/{id}/{team_id}")
def transfer_player(id: int, team_id: int, db:Session = Depends(get_db)):
    return db_player.transfer(db, id, team_id)

@router.get("/{team_id}/players", response_model=List[PlayerDisplay])
def get_players_by_team(team_id: int, db:Session = Depends(get_db)):
    return db_player.get_players_team(db,team_id)

@router.get("/{player_id}", response_model=PlayerDisplay)
def get_player_by_id(player_id: int, db:Session = Depends(get_db)):
    return db_player.get_player_id(db,player_id)

@router.delete("/delete/{id}")
def delete_player(id:int, db:Session = Depends(get_db)):
    return db_player.delete(db, id)
