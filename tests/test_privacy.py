from app.security.privacy import sanitize_log


def test_sanitize_log_removes_sensitive_fields():
    event = {
        "service": "backend-api",
        "status": "healthy",
        "response_time_ms": 45,
        "email": "test@example.com",
        "ip_address": "192.0.2.10",
        "token": "FAKE_TOKEN"
    }

    sanitized = sanitize_log(event)

    assert sanitized == {
        "service": "backend-api",
        "status": "healthy",
        "response_time_ms": 45
    }


def test_sanitize_log_rejects_unknown_fields():
    event = {
        "service": "backend-api",
        "password": "FAKE_PASSWORD",
        "api_key": "FAKE_API_KEY"
    }

    sanitized = sanitize_log(event)

    assert sanitized == {
        "service": "backend-api"
    }
