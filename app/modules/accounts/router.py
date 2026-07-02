from uuid import UUID
from fastapi import APIRouter, Depends
from app.modules.accounts.service import AccountService
from app.modules.accounts.schema import (
    CreateSavingsRequest, CreateSavingsResponse)
from starlette import status
from app.modules.auth.depends import UserDepends

account_service = AccountService()
user_depends = UserDepends()
router = APIRouter(
    tags=["accounts"],
)

@router.post("/savings", status_code=status.HTTP_201_CREATED)
async def create_savings(payload:CreateSavingsRequest, user_info: dict = Depends(user_depends.get_user_from_jwt)):

    return await account_service.create_savings(user_info.get('customer_id'), payload.accountNumber)
