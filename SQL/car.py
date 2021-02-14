
# coding=utf-8

from sqlalchemy import Column, String, Integer, Enum

from ..common.base import Base

class Engine(enum.Enum):
    diesel = 1
    fuel = 2
    electric = 3
    hybrid = 4


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    horsepower = Column(Integer)
    engine = Column(Enum(Engine))
    year = Column(Integer)


    def __init__(self, name):
        self.name = name
