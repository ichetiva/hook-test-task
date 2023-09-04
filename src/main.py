from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_application() -> FastAPI:
    application = FastAPI()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    return application
