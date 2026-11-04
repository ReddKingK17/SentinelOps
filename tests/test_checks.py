
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_check_valid():
    response = client.post(
        "/checks",
        json={
            "service": "backend-api",
            "status": "healthy",
            "response_time_ms": 45
        }
    )

    assert response.status_code == 201
    assert response.json()["message"] == "Check accepted"


def test_create_check_negative_response_time():
    response = client.post(
        "/checks",
        json={
            "service": "backend-api",
            "status": "healthy",
            "response_time_ms": -50
        }
    )

    assert response.status_code == 422


def test_create_check_rejects_extra_fields():
    response = client.post(
        "/checks",
        json={
            "service": "backend-api",
            "status": "healthy",
            "response_time_ms": 45,
            "email": "test@example.com"
        }
    )

    assert response.status_code == 422
