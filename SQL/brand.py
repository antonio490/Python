# coding=utf-8

from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

from ..common.base import Base

association_table = Table(
    'association', Base.metadata,
    Column('brand_id', Integer, ForeignKey('brand.id')),
    Column('car_id', Integer, ForeignKey('car.id'))
)

class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cars = relationship("Car", secondary=association_table)

    def __init__(self, name, cars):
        self.name = name
        self.cars = cars
