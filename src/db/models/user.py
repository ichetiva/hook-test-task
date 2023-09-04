from sqlalchemy import Column, String

from db.models.base import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String(50), unique=True)
