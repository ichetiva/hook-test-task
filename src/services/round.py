from db.repositories.factory import RepositoriesFactory


class RoundService:
    def __init__(self, repositories: RepositoriesFactory) -> None:
        self.repositories = repositories
