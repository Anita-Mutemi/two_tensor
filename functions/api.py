import json
from packages.public_api.app import app
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class RequestHandler(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        scope = request.scope
        # Adjust the scope to match the ASGI interface
        scope["type"] = "http"
        scope["path"] = "/"

        # Handle the request
        response = await app(scope, receive, send)
        return JSONResponse(content=response["body"])


async def handler(event, context):
    request = Request(scope=event, receive=None)
    response = await RequestHandler(request)
    return {
        "statusCode": response.status_code,
        "body": response.body.decode("utf-8"),
        "headers": {"Content-Type": "application/json"},
    }
