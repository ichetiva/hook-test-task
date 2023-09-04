from sqlalchemy import Column, Integer, ForeignKey

from db.models.base import Base


class SpinLog(Base):
    __tablename__ = "spins_log"

    user_id = Column(Integer, ForeignKey("users.id"))
    round_id = Column(Integer, ForeignKey("rounds.id"))
    cell_id = Column(Integer, ForeignKey("cells.id"))
