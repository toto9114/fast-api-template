from fastapi import Request
from fastapi.responses import Response, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.concurrency import iterate_in_threadpool


class CommonResponseMiddleware(BaseHTTPMiddleware):
    async def dispatch(
            self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        response = await call_next(request)
        response_body = [chunk async for chunk in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body))
        response_body = response_body[0].decode()
        # Customize the response
        custom_response = {
            "meta": {
                "status_code": response.status_code,
                "message": "Ok"
            },
            "data": response_body
        }

        # Return the customized response
        return JSONResponse(content=custom_response)
