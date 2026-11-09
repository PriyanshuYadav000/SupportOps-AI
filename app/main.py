from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.tickets import router as tickets_router
from app.core.config import get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_logging

settings = get_settings()
configure_logging()

app = FastAPI(
    title=settings.app_name,
    description="AI-powered customer support ticket triage and knowledge assistant",
    version=settings.app_version,
    debug=settings.debug,
)

app.include_router(health_router)
app.include_router(tickets_router)
register_exception_handlers(app)
