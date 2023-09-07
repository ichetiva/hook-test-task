from typing import Annotated

from fastapi import APIRouter, Depends

from db.schemes.roulette import SpinRouletteOut, RouletteStatisticsOut
from db.models import User
from api.dependencies.services import get_services
from api.dependencies.user import get_user
from services import ServicesFactory

router = APIRouter(prefix="/roulette", tags=["roulette"])


@router.post("/", response_model=SpinRouletteOut)
async def spin_roulette_view(
    services: Annotated[ServicesFactory, Depends(get_services)],
    user: Annotated[User, Depends(get_user)],
):
    spin_log = await services.round_service.spin(user)
    return spin_log


@router.get("/", response_model=RouletteStatisticsOut)
async def get_roulette_statistics_view(
    services: Annotated[ServicesFactory, Depends(get_services)],
):
    statistics = await services.round_service.get_statistics()
    return statistics
