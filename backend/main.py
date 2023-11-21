from backend.api.api import api_router
from backend.core.config import settings
from backend.middleware.db_session_middleware import DBSessionMiddleware
from backend.middleware.health_check_middleware import HealthCheckMiddleware
from backend.schemas.resp import CommonResponse
from fastapi import FastAPI
from starlette.exceptions import HTTPException

app = FastAPI(title=settings.PROJECT_NAME)


# Add the middleware to the app
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return CommonResponse(status_code=exc.status_code, message=exc.detail, data=None)


@app.exception_handler(Exception)
async def http_internal_server_error_handler(request, exc):
    return CommonResponse(status_code=500, message="Internal Server Error", data=None)


app.add_middleware(DBSessionMiddleware)
app.add_middleware(HealthCheckMiddleware)

app.include_router(api_router)
