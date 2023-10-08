from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    VERSION: str = Field("")

    # POSTGRES
    DB_USERNAME: str = Field("postgres")
    DB_PASSWORD: str = Field("password")
    DB_HOST: str = Field("localhost")
    DB_DATABASE: str = Field("tasty_delivery")

    # TOKEN
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(1440)
    SECRET_KEY: str = Field('')
    ALGORITHM: str = Field('HS256')


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
