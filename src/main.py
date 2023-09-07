from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import api


def get_application() -> FastAPI:
    application = FastAPI()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    application.include_router(api.router)

    return application


app = get_application()
