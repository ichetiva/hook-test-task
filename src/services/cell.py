from db.repositories import RepositoriesFactory
from db.models import Cell


class CellService:
    def __init__(self, repositories: RepositoriesFactory) -> None:
        self.repositories = repositories

    async def get_available_for_round(self, round_id: int) -> list[Cell]:
        return await self.repositories.cell_repo.get_available_for_round(round_id)

    async def get_jackpot(self) -> Cell:
        return await self.repositories.cell_repo.get(is_jackpot=True)
