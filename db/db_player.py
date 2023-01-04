from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db.models import DbPlayer, DbTeam
from routers.schemas import PlayerBase
from routers.slug import name_to_slug


def get_age(date_of_birth):
    d1 = datetime.strptime(str(date_of_birth), "%Y-%m-%d")
    d2 = datetime.strptime(str(datetime.date(datetime.today())), "%Y-%m-%d")
    delta = d2 - d1
    return (delta.days + 1) // 365.25


def create(db: Session, request: PlayerBase):
    player = DbPlayer(
        name=request.name,
        last_name=request.last_name,
        img=f"images/players/{request.img}",
        date_of_birth=request.date_of_birth,
        age=get_age(request.date_of_birth),
        nationality=request.nationality.capitalize(),
        position=request.position.capitalize(),
        number=request.number,
        slug=name_to_slug(request.name+" "+request.last_name),
        team_id=request.team_id
    )
    db.add(player)
    db.commit()
    db.refresh(player)
    return player


def transfer(db: Session, id: int, team_id: int):
    player = db.query(DbPlayer).filter(DbPlayer.id == id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player has not been found!")
    team = db.query(DbTeam).filter(DbTeam.id == team_id).first()
    if not team:
        if not player:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team has not been found!")
    player.team_id = team_id
    db.add(player)
    db.commit()
    db.refresh(player)
    return f"{player.name} {player.last_name} has been transferred to {team.name}."


def get_players_team(db: Session, team_id: int):
    players = db.query(DbPlayer).filter(DbPlayer.team_id == team_id).all()
    if not players:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="This team doesn't exsists or has not any players!")
    return players


def get_player_id(db: Session, player_id: int):
    player = db.query(DbPlayer).filter(DbPlayer.id == player_id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player has not been found!")
    return player


def delete(db: Session, id: int):
    player = db.query(DbPlayer).filter(DbPlayer.id == id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Not found a player")
    db.delete(player)
    db.commit()
    return "ok"
