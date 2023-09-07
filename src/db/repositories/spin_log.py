from sqlalchemy import select
from sqlalchemy.sql import func
from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.base import BaseRepository
from db.models import SpinLog


class SpinLogRepository(BaseRepository[SpinLog]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(SpinLog, session)

    async def get_members_count(self) -> list[int, int]:
        stmt = select(
            SpinLog.round_id,
            func.count(SpinLog.user_id),
        ).group_by(SpinLog.round_id)
        result = await self.session.execute(stmt)
        return result.fetchmany()

    async def get_avg_spins_per_round(self) -> dict[int, float]:
        subq = (
            select(
                SpinLog.user_id, SpinLog.round_id, func.count(SpinLog.id).label("spr")
            )
            .group_by(SpinLog.user_id, SpinLog.round_id)
            .subquery()
        )
        stmt = (
            select(subq.c.user_id, func.avg(subq.c.spr).label("avg_spr"))
            .select_from(subq)
            .group_by(subq.c.user_id)
        )
        result = (await self.session.execute(stmt)).fetchmany()
        return {entry[0]: float(entry[1]) for entry in result}

    async def get_most_active_members(self) -> list[tuple[int, int, float]]:
        stmt = select(
            SpinLog.user_id, func.count(SpinLog.round_id.distinct()).label("rc")
        ).group_by(SpinLog.user_id)
        result = (await self.session.execute(stmt)).fetchmany()
        avg_spins_per_round = await self.get_avg_spins_per_round()
        return [(entry[0], entry[1], avg_spins_per_round[entry[0]]) for entry in result]
