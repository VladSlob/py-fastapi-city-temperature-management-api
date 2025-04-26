from sqlalchemy import Column, Integer, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Weather(Base):
    __tablename__ = 'weather'


    temperature = Column(Float, nullable=False)
