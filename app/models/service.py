from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ServiceCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")

    service: Literal[
        "backend-api",
        "worker",
        "database"
    ]

    status: Literal["healthy", "degraded", "down"]

    response_time_ms: float = Field(
        ge=0,
        le=60000
    )
