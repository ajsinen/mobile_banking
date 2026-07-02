from fastapi import APIRouter, Depends
from app.modules.accounts.service import AccountService
from app.modules.accounts.schema import (
    CreateSavingsRequest, CreateSavingsResponse)
from starlette import status
from app.modules.auth.depends import get_user_from_jwt

account_service = AccountService()

router = APIRouter(
    tags=["accounts"],
)

@router.post("/savings", response_model=CreateSavingsResponse, status_code=status.HTTP_201_CREATED)
async def create_savings(payload: CreateSavingsRequest, user: dict = Depends(get_user_from_jwt)):

    return user

    return await account_service.create_savings(payload.customer_id, payload.account_number)
