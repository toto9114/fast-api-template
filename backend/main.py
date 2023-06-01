from fastapi import FastAPI
from starlette.exceptions import HTTPException

from backend.api.api import api_router
from backend.core.config import settings
from backend.schemas.resp import CommonResponse

app = FastAPI(
    title=settings.PROJECT_NAME
)


# Add the middleware to the app
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return CommonResponse(status_code=exc.status_code, message=exc.detail, data=None)


@app.exception_handler(Exception)
async def http_internal_server_error_handler(request, exc):
    return CommonResponse(status_code=500, message="Internal Server Error", data=None)


app.include_router(api_router)
