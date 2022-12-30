from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class DbLeague(Base):
    __tablename__ = "leagues"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    country = Column(String)
    img = Column(String)
    teams = relationship("DbTeam", back_populates="league")


class DbTeam(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city = Column(String)
    img = Column(String)
    manager = Column(String)
    year_of_creation = Column(Integer)
    league_id= Column(Integer, ForeignKey("leagues.id"))
    league = relationship("DbLeague", back_populates="teams")
    # players = relationship()

# class DbPlayer(Base):
#     __tablename__ = "players"
#     name = Column(String)
#     surname = Column(String)
#     date_of_birth = Column(DateTime)
#     nationality = Column(String)
#     position = Column(String)
#     number = Column(Integer)
#     # team = relationship()
