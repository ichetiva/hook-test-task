from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    id: int = Column(Integer, primary_key=True)
