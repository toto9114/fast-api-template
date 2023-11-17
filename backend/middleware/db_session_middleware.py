from uuid import uuid4

from backend.db.session import set_session_context, reset_session_context
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class DBSessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(
            self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        session_id = str(uuid4())
        context = set_session_context(session_id)
        try:
            response = await call_next(request)
        finally:
            reset_session_context(context)
        return response
