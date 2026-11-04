
from fastapi import FastAPI

from app.models.service import ServiceCheck

app = FastAPI(
    title="SentinelOps API",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/checks", status_code=201)
def create_check(check: ServiceCheck):
    return {
        "message": "Check accepted",
        "check": check.model_dump()
    }
