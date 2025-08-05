from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    celery_broker_url: str
    celery_result_backend: str
    nb_threads: Optional[int] = 3


settings = Settings()
