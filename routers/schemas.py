from datetime import datetime
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


# for League display
class Team(BaseModel):
    name: str

    class Config():
        orm_mode = True


class LeagueDisplay(BaseModel):
    name: str
    country: str
    img: str
    teams : List[Team]

    class Config():
        orm_mode = True


class League(BaseModel):
    name: str

    class Config():
        orm_mode = True


class TeamDisplay(BaseModel):
    name: str
    city: str
    img: str
    manager: str
    league: League

    class Config():
        orm_mode = True
