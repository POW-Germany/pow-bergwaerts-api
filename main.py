from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from modules.config import Config
from modules.logger import Logger

Logger = Logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager."""
    Logger.info("Application startup")
    yield
    Logger.info("Application shutdown")


app = FastAPI(title=Config.APP_NAME, version=Config.APP_VERSION, lifespan=lifespan)


@app.get("/health")
async def health_check(request: Request):
    """Health check endpoint."""
    Logger.info("Health check requested")
    return JSONResponse(content={"status": "ok"})


if __name__ == "__main__":
    import uvicorn

    Logger.info("Starting FastAPI application")
    uvicorn.run(app, host="0.0.0.0", port=8080)
