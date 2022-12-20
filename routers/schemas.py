from datetime import datetime
from typing import List
from pydantic import BaseModel


class LeagueBase(BaseModel):
    name: str
    country: str
    img: str
    # teams : List[team]


class LeagueDisplay(BaseModel):
    name: str
    country: str
    img: str

    class Config():
        orm_mode = True
