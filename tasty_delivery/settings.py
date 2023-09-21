from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    VERSION: str = Field("")

    DB_USERNAME: str = Field("postgres")
    DB_PASSWORD: str = Field("password")
    DB_HOST: str = Field("localhost")
    DB_DATABASE: str = Field("tasty_delivery")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
