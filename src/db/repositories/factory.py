from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.user import UserRepository
from db.repositories.cell import CellRepository
from db.repositories.round import RoundRepository
from db.repositories.spin_log import SpinLogRepository


class RepositoriesFactory:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @property
    def user_repo(self) -> UserRepository:
        return UserRepository(self.session)

    @property
    def cell_repo(self) -> CellRepository:
        return CellRepository(self.session)

    @property
    def round_repo(self) -> RoundRepository:
        return RoundRepository(self.session)

    @property
    def spin_log_repo(self) -> SpinLogRepository:
        return SpinLogRepository(self.session)
