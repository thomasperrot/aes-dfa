from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    celery_broker_url: str
    celery_result_backend: str
    nb_threads: int


settings = Settings()
