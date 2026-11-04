
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ServiceCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")

    service: str = Field(
        min_length=1,
        max_length=50,
        pattern=r"^[a-zA-Z0-9_-]+$"
    )

    status: Literal["healthy", "degraded", "down"]

    response_time_ms: float = Field(
        ge=0,
        le=60000
    )
