from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.base import BaseRepository
from db.models.cell import Cell


class CellRepository(BaseRepository[Cell]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Cell, session)
