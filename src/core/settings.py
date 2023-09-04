from functools import lru_cache

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_db: str

    @property
    def postgres_url(self) -> str:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            path="/" + self.POSTGRES_DB,
        )

    model_config = SettingsConfigDict()


@lru_cache
def get_settings() -> Settings:
    return Settings()
