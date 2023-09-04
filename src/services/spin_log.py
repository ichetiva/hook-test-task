from db.repositories.factory import RepositoriesFactory


class SpinLogService:
    def __init__(self, repositories: RepositoriesFactory) -> None:
        self.repositories = repositories
