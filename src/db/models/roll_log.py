from sqlalchemy import Column, Integer, ForeignKey

from db.models.base import Base


class RollLog(Base):
    __tablename__ = "roll_logs"

    user_id = Column(Integer, ForeignKey("users.id"))
    round_id = Column(Integer, ForeignKey("rounds.id"))
    cell_id = Column(Integer, ForeignKey("cells.id"))
