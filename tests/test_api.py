from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_api_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "service running"


def test_valid_prediction():
    response = client.post(
        "/predict-risk",
        json={"customer_id": "6467-CHFZW"}
    )
    assert response.status_code == 200
    assert "risk_category" in response.json()


def test_invalid_customer():
    response = client.post(
        "/predict-risk",
        json={"customer_id": "INVALID"}
    )
    assert response.status_code == 404