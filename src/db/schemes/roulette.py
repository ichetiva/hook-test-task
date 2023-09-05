from pydantic import BaseModel


class SpinRouletteIn(BaseModel):
    username: str


class SpinRouletteOut(BaseModel):
    user_id: int
    round_id: int
    cell_id: int
    is_jackpot: bool
