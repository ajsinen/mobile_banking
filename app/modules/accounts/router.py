from fastapi import APIRouter, Depends
from app.modules.accounts.service import AccountService
from app.modules.accounts.schema import (
    CreateSavingsRequest)
from starlette import status
from app.core.depends import UserDepends

account_service = AccountService()
user_depends = UserDepends()
router = APIRouter(
    tags=["accounts"],
)

@router.post("/savings", status_code=status.HTTP_201_CREATED)
async def create_savings(payload:CreateSavingsRequest, current_user: dict = Depends(user_depends.get_current_user)):

    return await account_service.create_savings(current_user['customer_id'], payload.account_number)
