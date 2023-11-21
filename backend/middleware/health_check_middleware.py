from fastapi import Request
from fastapi.responses import Response, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.concurrency import iterate_in_threadpool


class HealthCheckMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if request.url.path == "/health":
            return JSONResponse(content={"status": "ok"})
        response = await call_next(request)

        return response
