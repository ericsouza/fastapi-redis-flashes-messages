import os
from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import AnyUrl

class Settings(BaseSettings):
    redis_url: AnyUrl = os.environ.get("REDIS_URL", "redis://localhost")
    redis_db: int = int(os.getenv("REDIS_DB", "0"))


@lru_cache()
def get_settings() -> BaseSettings:
    return Settings()