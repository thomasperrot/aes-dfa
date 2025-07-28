from uuid import UUID

from celery import Celery
from celery.result import AsyncResult
from fastapi import FastAPI

from .settings import settings
from .schemas import CipherTexts, TaskStatus
from .tasks import compute_keys

app = FastAPI()
celery = Celery(
    __name__,
    broker_url=settings.celery_broker_url,
    result_backend=settings.celery_result_backend,
    pool="solo",
)


@app.get("/")
async def read_root():
    return {}


@app.post("/tasks", status_code=201)
def compute_dfa(cipher_texts: CipherTexts):
    task = compute_keys.delay(
        cipher_texts.normal_cipher_text, cipher_texts.faulty_cipher_text
    )
    return {"taskId": task.id}


@app.get("/tasks/{task_id}", response_model=TaskStatus)
def get_status(task_id: UUID):
    task_result = AsyncResult(str(task_id))
    return {
        "task_id": str(task_id),
        "taskStatus": task_result.status,
        "taskResult": task_result.result,
    }
