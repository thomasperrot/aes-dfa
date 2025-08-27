from uuid import UUID

from celery import Celery
from celery.result import AsyncResult
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .settings import settings
from .schemas import CipherTexts, TaskStatus
from .tasks import compute_keys

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
celery = Celery(
    __name__,
    broker_url=settings.celery_broker_url,
    result_backend=settings.celery_result_backend,
    pool="solo",
    task_track_started=True,
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
        "taskId": str(task_id),
        "taskStatus": task_result.status,
        "taskResult": task_result.result if task_result.status == "SUCCESS" else None,
    }
