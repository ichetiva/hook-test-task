from sqlalchemy import Column, Boolean

from db.models import Base


class Round(Base):
    __tablename__ = "rounds"

    is_finished = Column(Boolean, default=False)
