from db.repositories import RepositoriesFactory
from db.models import User


class UserService:
    def __init__(self, repositories: RepositoriesFactory) -> None:
        self.repositories = repositories

    async def get(self, username: str) -> User:
        user, created = await self.repositories.user_repo.get_or_create(
            username=username
        )
        if created:
            await self.repositories.session.commit()
            await self.repositories.session.refresh(user)
        return user
