from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to LedgerPilot",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}