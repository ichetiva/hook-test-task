from db.repositories.factory import RepositoriesFactory


class UserService:
    def __init__(self, repositories: RepositoriesFactory) -> None:
        self.repositories = repositories
