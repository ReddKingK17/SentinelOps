
from collections.abc import Mapping


ALLOWED_LOG_FIELDS = (
    "service",
    "status",
    "response_time_ms",
)


def sanitize_log(event: Mapping[str, object]) -> dict[str, object]:
    """Keep only fields approved for application logging."""

    return {
        key: event[key]
        for key in ALLOWED_LOG_FIELDS
        if key in event
    }
