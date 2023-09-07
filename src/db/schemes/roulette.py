from typing import List, Tuple
from decimal import Decimal

from pydantic import BaseModel


class SpinRouletteIn(BaseModel):
    username: str


class SpinRouletteOut(BaseModel):
    user_id: int
    round_id: int
    cell_id: int
    is_jackpot: bool

    class Config:
        from_attributes = True


class ActiveMember(BaseModel):
    user_id: int
    rounds_count: int
    avg_spins_count: float


class RouletteStatisticsOut(BaseModel):
    members_count: List[Tuple[int, int]]
    most_active_members: List[ActiveMember]
