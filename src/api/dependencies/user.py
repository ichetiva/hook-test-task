from typing import Annotated

from fastapi import Depends, Body

from db.schemes.roulette import SpinRouletteIn
from db.models import User
from services import ServicesFactory
from api.dependencies.services import get_services


async def get_user(
    data: Annotated[SpinRouletteIn, Body()],
    services: Annotated[ServicesFactory, Depends(get_services)],
) -> User:
    user = await services.user_service.get(data.username)
    return user
