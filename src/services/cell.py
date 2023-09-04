from db.repositories.factory import RepositoriesFactory


class CellService:
    def __init__(self, repositories: RepositoriesFactory) -> None:
        self.repositories = repositories
