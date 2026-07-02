from fastapi import HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.params import Depends
from uuid import UUID
from starlette import status
from app.modules.auth.repository import AuthRepository
from app.core.security import decode_token


class UserDepends:
    def __init__(self):
        self.auth_repo = AuthRepository()

    async def get_user_from_jwt(self, request: Request) -> dict:

        token = request.headers.get('authorization', None)
        if not token:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

        print(token[7:])
        decoded_token = decode_token(token[7:])

        print("DECODED TOKEN",decoded_token)
        user_info = await self.auth_repo.get_user_by_id(UUID(decoded_token["sub"]))

        return user_info
