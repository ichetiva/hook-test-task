from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.base import BaseRepository
from db.models.round import Round


class RoundRepository(BaseRepository[Round]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Round, session)
