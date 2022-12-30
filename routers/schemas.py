from datetime import date as date_type
from typing import List
from pydantic import BaseModel


class TeamBase(BaseModel):
    name: str
    city: str
    img: str
    manager: str
    year_of_creation: int
    league_id: int


class LeagueBase(BaseModel):
    name: str
    country: str
    img: str

class PlayerBase(BaseModel):
    name: str
    last_name: str
    img: str
    date_of_birth: date_type
    nationality : str
    position : str
    number : int
    team_id: int

# for League display
class Team(BaseModel):
    name: str

    class Config():
        orm_mode = True
class League(BaseModel):
    name: str

    class Config():
        orm_mode = True
class Player(BaseModel):
    name: str
    last_name: str

    class Config():
        orm_mode = True


class LeagueDisplay(BaseModel):
    name: str
    country: str
    img: str
    teams : List[Team]

    class Config():
        orm_mode = True

class TeamDisplay(BaseModel):
    name: str
    city: str
    img: str
    manager: str
    league: League
    players: List[Player]

    class Config():
        orm_mode = True

class PlayerDisplay(BaseModel):
    name: str
    last_name: str
    img: str
    age: int
    nationality : str
    position : str
    number : int
    team_id: int

    class Config():
        orm_mode = True