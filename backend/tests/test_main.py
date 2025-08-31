import time

from fastapi.testclient import TestClient

from app.main import app
from app.tasks import compute_keys


client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {}


def test_compute_dfa(celery_worker):
    response = client.post(
        url="/tasks",
        json={
            "normalCipherText": "00000000000000000000000000000000",
            "faultyCipherText": "00000000000000000000000000000000",
        },
    )
    assert response.status_code == 201
    assert list(response.json()) == ["taskId"]


def test_get_result_invalid_task_id(celery_worker):
    response = client.get(url="/tasks/invalid")
    assert response.status_code == 422


def test_get_result_unknown_task_id(celery_worker):
    response = client.get(url="/tasks/123e4567-e89b-12d3-a456-426655440000")
    assert response.status_code == 200
    assert response.json() == {
        "taskId": "123e4567-e89b-12d3-a456-426655440000",
        "taskResult": None,
        "taskStatus": "PENDING",
    }


def test_get_result(celery_worker):
    task = compute_keys.delay(
        "00000000000000000000000000000000", "00000000000000000000000000000000"
    )
    time.sleep(1)
    response = client.get(url=f"/tasks/{task.id}")
    assert response.status_code == 200
    assert response.json() == {
        "taskId": task.id,
        "taskResult": [],
        "taskStatus": "SUCCESS",
    }
