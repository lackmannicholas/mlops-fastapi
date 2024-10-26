from typing import Optional

from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param
from starlette.requests import Request


class CustomHTTPBearer(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        auth_header = request.headers.get("Authorization") or request.headers.get(
            "X-Internal-Authorization"
        )

        if not auth_header:
            error_message = (
                f"Failed to authenticate with missing auth header "
                f"request={str(request.url)} method:{request.method}"
            )
            raise HTTPException(status_code=401, detail=error_message)

        scheme, credentials = get_authorization_scheme_param(auth_header)

        if scheme != "Bearer":
            error_message = (
                f"Failed to authenticate with improperly formatted auth header "
                f"request={str(request.url)} method:{request.method}"
            )
            raise HTTPException(status_code=401, detail=error_message)

        return HTTPAuthorizationCredentials(scheme=scheme, credentials=credentials)
