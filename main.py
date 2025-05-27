"""
Main entry point for the FastAPI application.
Creates the FastAPI app with all configurations and middleware.
Routes are imported from a separate module.
"""
import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.responses import RedirectResponse
from contextlib import asynccontextmanager

# from api.routes import api_router

from shared.core.config.settings import settings
from shared.core.config.events import startup_event, shutdown_event

# Add the project root to Python's module search path
# This solves the 'ModuleNotFoundError: No module named 'backend'' issue
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup logging from dedicated config module
from shared.core.config.logging import setup_logging
from api.v1.routes import api_router_v1
logger = setup_logging()

# Import API router after adding project root to path



@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handle application lifecycle events (startup and shutdown)
    """
    await startup_event()
    logger.info("Application startup complete")
    yield
    await shutdown_event()
    logger.info("Application shutdown complete")


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    # Set up CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Add security middleware
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)
    app.add_middleware(GZipMiddleware, minimum_size=1000)

    # Include API router
    # app.include_router(api_router, prefix=settings.API_V1_STR)
    app.include_router(api_router_v1, prefix="/api/v1")
    @app.get("/", include_in_schema=False)
    async def root():
        """Redirect root to API documentation"""
        return RedirectResponse(url="/docs")

    return app


app = create_application()


if __name__ == "__main__":
    import uvicorn
    logger.info(f"Documentation available at http://{settings.HOST}:{settings.PORT}/docs")
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )