from fastapi import APIRouter

from api.routes import roulette

router = APIRouter(prefix="/api")

router.include_router(roulette.router)
