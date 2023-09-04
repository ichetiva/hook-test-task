from db.repositories.factory import RepositoriesFactory

from services.user import UserService
from services.cell import CellService
from services.round import RoundService
from services.spin_log import SpinLogService


class ServicesFactory:
    def __init__(self, repositories: RepositoriesFactory) -> None:
        self.repositories = repositories

    @property
    def user_service(self) -> UserService:
        return UserService(self.repositories)

    @property
    def cell_service(self) -> CellService:
        return CellService(self.repositories)

    @property
    def round_service(self) -> RoundService:
        return RoundService(self.repositories)

    @property
    def spin_log_service(self) -> SpinLogService:
        return SpinLogService(self.repositories)
