from db.repositories.factory import RepositoriesFactory

from services.user import UserService


class ServicesFactory:
    def __init__(self, repositories: RepositoriesFactory) -> None:
        self.repositories = repositories

    @property
    def user_service(self) -> UserService:
        return UserService(self.repositories)
