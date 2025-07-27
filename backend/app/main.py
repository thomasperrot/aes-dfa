from celery import Celery
from fastapi import FastAPI

from .settings import settings
from .schemas import CipherTexts
from .tasks import compute_key

app = FastAPI()
celery = Celery(
    __name__,
    broker_url=settings.celery_broker_url,
    result_backend=settings.celery_result_backend,
    pool="solo",
)


@app.get("/")
def read_root():
    return {}


@app.post("/aes-dfa")
def compute_dfa(cipher_texts: CipherTexts):
    return compute_key(cipher_texts.normal_cipher_text, cipher_texts.faulty_cipher_text)
