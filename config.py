from pydantic import BaseSettings

from functools import lru_cache

class Settings(BaseSettings):
    # database_url: str = "postgresql://postgres:root@127.0.0.1/websocket"
    redis_host: str = "redis://localhost"
    redis_password: str = ""
    redis_port: int = 6379
    redis_db: int = 1
    telegram_api_key: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    return settings
