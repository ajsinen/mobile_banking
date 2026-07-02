from fastapi import APIRouter
from app.modules.users.schema import UserListResponse
from starlette import status
from typing import List

from app.modules.users.service import UserService

router = APIRouter(tags=["users"])

user_service = UserService()

@router.get("/users", response_model=List[UserListResponse], status_code=status.HTTP_200_OK)
async def get_all_users():
    return await user_service.get_all_users()