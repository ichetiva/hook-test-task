from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.base import BaseRepository
from db.models import Cell
from db.models import SpinLog


class CellRepository(BaseRepository[Cell]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Cell, session)

    async def get_available_for_round(self, round_id: int) -> list[Cell]:
        subq = select(SpinLog.cell_id).where(SpinLog.round_id == round_id).subquery()
        stmt = (
            select(Cell)
            .where(Cell.is_jackpot == False)
            .join(subq, Cell.id.not_in(subq))
        )
        result = await self.session.scalars(stmt)
        return result.all()
