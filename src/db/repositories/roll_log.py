from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.base import BaseRepository
from db.models.roll_log import RollLog


class RollLogRepository(BaseRepository[RollLog]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(RollLog, session)
