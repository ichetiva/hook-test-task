import random
from typing import TYPE_CHECKING

from db.repositories import RepositoriesFactory
from db.models import Round, User, SpinLog
from db.schemes.roulette import RouletteStatisticsOut, ActiveMember

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
            for_update=True, is_finished=False
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
            cell_number = random.choices(numbers, weights=weights, k=1)[0]
            cell = await self.services.repositories.cell_repo.get(number=cell_number)
        spin_log = await self.services.spin_log_service.create(cell, user, round_)
        return spin_log

    async def get_statistics(self) -> RouletteStatisticsOut:
        members_count = await self.repositories.spin_log_repo.get_members_count()
        most_active_members = (
            await self.repositories.spin_log_repo.get_most_active_members()
        )
        return RouletteStatisticsOut(
            members_count=members_count,
            most_active_members=[
                ActiveMember(
                    user_id=member[0], rounds_count=member[1], avg_spins_count=member[2]
                )
                for member in most_active_members
            ],
        )
