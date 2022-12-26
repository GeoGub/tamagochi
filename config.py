from pydantic import BaseSettings

from functools import lru_cache

class Settings(BaseSettings):
    # database_url: str = "postgresql://postgres:root@127.0.0.1/websocket"
    redis_host: str = "redis://localhost"
    redis_password: str | None = ""
    redis_port: int = 6379
    redis_db: int = 1

@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    return settings
