from db.repositories.factory import RepositoriesFactory
from db.models.round import Round


class RoundService:
    def __init__(self, repositories: RepositoriesFactory) -> None:
        self.repositories = repositories

    async def get(self) -> Round:
        round_, _ = await self.repositories.round_repo.get_or_create(is_finished=False)
        return round_
