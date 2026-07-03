from fastapi import APIRouter, Depends

from app.core.permissions import require_roles
from app.modules.users.schema import UserListResponse
from starlette import status
from typing import List

from app.modules.users.service import UserService

router = APIRouter(tags=["users"])

user_service = UserService()

@router.get("/users", response_model=List[UserListResponse], status_code=status.HTTP_200_OK)
async def get_all_users(current_user=Depends(require_roles(1))):
    print(current_user)
    return await user_service.get_all_users()