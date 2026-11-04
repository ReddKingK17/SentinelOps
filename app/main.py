import logging

from fastapi import FastAPI
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.models.service import ServiceCheck
from app.security.privacy import sanitize_log

logger = logging.getLogger("sentinelops")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(levelname)s: %(message)s")
    )
    logger.addHandler(handler)

logger.propagate = False

app = FastAPI(
    title="SentinelOps API",
    version="0.1.0"
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Invalid request data"
        }
    )


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/checks", status_code=201)
def create_check(check: ServiceCheck):
    safe_event = sanitize_log(check.model_dump())

    logger.info("Service check received: %s", safe_event)

    return {
        "message": "Check accepted",
        "check": check.model_dump()
    }
