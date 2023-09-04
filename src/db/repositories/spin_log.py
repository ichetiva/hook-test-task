from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.base import BaseRepository
from db.models.roll_log import SpinLog


class SpinLogRepository(BaseRepository[SpinLog]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(SpinLog, session)
