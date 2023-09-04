from sqlalchemy import Column, Integer, Boolean

from db.models.base import Base


class Cell(Base):
    __tablename__ = "cells"

    number = Column(Integer, unique=True, nullable=False)
    weight = Column(Integer, nullable=False)
    is_jackpot = Column(Boolean, default=False)
