import fastapi
from .routes.search import search_router


backend_app: fastapi.FastAPI = fastapi.FastAPI()

backend_app.include_router(search_router, prefix="/search", tags=["search"])


__all__ = ["backend_app"]
