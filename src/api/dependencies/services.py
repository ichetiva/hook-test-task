from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services import ServicesFactory
from db.repositories import RepositoriesFactory
from api.dependencies.database import get_session


async def get_services(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> ServicesFactory:
    repositories = RepositoriesFactory(session)
    return ServicesFactory(repositories)
