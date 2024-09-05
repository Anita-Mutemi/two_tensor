import json
from packages.public_api.app import app
from fastapi import Request # type: ignore
from fastapi.responses import JSONResponse  # type: ignore
from starlette.middleware.base import BaseHTTPMiddleware  # type: ignore


class RequestHandler(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        scope = request.scope
        # Adjust the scope to match the ASGI interface
        scope["type"] = "http"
        scope["path"] = "/"

        # Handle the request
        response = await app(scope, receive, send) # type: ignore
        return JSONResponse(content=response["body"])


async def handler(event, context):
    request = Request(scope=event, receive=None)
    response = await RequestHandler(request)
    return {
        "statusCode": response.status_code,
        "body": response.body.decode("utf-8"),
        "headers": {"Content-Type": "application/json"},
    }
