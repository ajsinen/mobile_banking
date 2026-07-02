from fastapi import HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.params import Depends
from uuid import UUID
from starlette import status
from app.modules.auth.repository import AuthRepository


auth_repository = AuthRepository()

async def get_user_from_jwt(headers: Request) -> dict:
    token: str = headers.get('Authorization')
    user = await  auth_repository.get_user_by_id(UUID(token["user_id"]))

    if user is None:
        raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)

    return dict(user)
