from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

def test_compute_dfa():
    response = client.post(url="/aes-dfa", json={"normalCipherText": "00000000000000000000000000000000", "faultyCipherText": "00000000000000000000000000000000"})
    assert response.status_code == 200
    assert response.json() == "00000000000000000000000000000000"
