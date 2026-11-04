
from unittest.mock import patch

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_valid_check_logs_only_allowed_fields():
    with patch("app.main.logger.info") as mock_log:
        response = client.post(
            "/checks",
            json={
                "service": "backend-api",
                "status": "healthy",
                "response_time_ms": 45
            }
        )

    assert response.status_code == 201

    mock_log.assert_called_once_with(
        "Service check received: %s",
        {
            "service": "backend-api",
            "status": "healthy",
            "response_time_ms": 45.0
        }
    )


def test_invalid_check_is_not_logged():
    with patch("app.main.logger.info") as mock_log:
        response = client.post(
            "/checks",
            json={
                "service": "backend-api",
                "status": "healthy",
                "response_time_ms": 45,
                "email": "test@example.com",
                "token": "FAKE_SECRET"
            }
        )

    assert response.status_code == 422
    mock_log.assert_not_called()
