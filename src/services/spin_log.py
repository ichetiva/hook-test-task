from db.repositories import RepositoriesFactory
from db.models import Cell, User, Round, SpinLog


class SpinLogService:
    def __init__(self, repositories: RepositoriesFactory) -> None:
        self.repositories = repositories

    async def create(self, cell: Cell, user: User, round_: Round) -> SpinLog:
        spin_log, created = await self.repositories.spin_log_repo.get_or_create(
            user_id=user.id,
            round_id=round_.id,
            cell_id=cell.id,
            is_jackpot=cell.is_jackpot,
        )
        if created:
            await self.repositories.session.commit()
            await self.repositories.session.refresh(spin_log)
        return spin_log
