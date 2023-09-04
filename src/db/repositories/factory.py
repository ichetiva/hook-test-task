from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.user import UserRepository


class RepositoriesFactory:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @property
    def user_repo(self) -> UserRepository:
        return UserRepository(self.session)
