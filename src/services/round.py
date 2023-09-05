import random
from typing import TYPE_CHECKING

from db.repositories import RepositoriesFactory
from db.models import Round, User, SpinLog

if TYPE_CHECKING:
    from services import ServicesFactory


class RoundService:
    def __init__(
        self, repositories: RepositoriesFactory, services: "ServicesFactory"
    ) -> None:
        self.repositories = repositories
        self.services = services

    async def get(self) -> Round:
        round_, created = await self.repositories.round_repo.get_or_create(
            is_finished=False
        )
        if created:
            await self.repositories.session.commit()
            await self.repositories.session.refresh(round_)
        return round_

    async def spin(self, user: User) -> SpinLog:
        round_ = await self.get()
        round_available_cells = (
            await self.services.cell_service.get_available_for_round(round_.id)
        )
        if len(round_available_cells) == 0:
            cell = await self.services.cell_service.get_jackpot()
        else:
            numbers = [cell.number for cell in round_available_cells]
            weights = [cell.weight for cell in round_available_cells]
            cell = random.choices(numbers, weights=weights, k=len(numbers))
        spin_log = await self.services.spin_log_service.create(cell, user, round_)
        return spin_log
