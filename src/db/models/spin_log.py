from sqlalchemy import Column, Integer, Boolean, ForeignKey

from db.models import Base


class SpinLog(Base):
    __tablename__ = "spins_log"

    user_id = Column(Integer, ForeignKey("users.id"))
    round_id = Column(Integer, ForeignKey("rounds.id"))
    cell_id = Column(Integer, ForeignKey("cells.id"))
    is_jackpot = Column(Boolean, nullable=False)
