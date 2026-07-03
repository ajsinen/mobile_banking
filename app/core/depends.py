from fastapi import HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.params import Depends
from uuid import UUID
from starlette import status
from app.modules.auth.repository import AuthRepository
from app.core.security import decode_token, oauth2_scheme


class UserDepends:
    def __init__(self):
        self.auth_repo = AuthRepository()

    async def get_current_user(self, token: str = Depends(oauth2_scheme)) -> dict:

        decoded_token = decode_token(token)

        print("DECODED TOKEN",decoded_token)
        user_info = await self.auth_repo.get_user_by_id(UUID(decoded_token["sub"]))

        return user_info
