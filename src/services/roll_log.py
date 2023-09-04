from db.repositories.factory import RepositoriesFactory


class RollLogService:
    def __init__(self, repositories: RepositoriesFactory) -> None:
        self.repositories = repositories
