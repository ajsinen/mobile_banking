from starlette import status

from app.modules.accounts.repository import AccountRepository
from fastapi import HTTPException

class AccountService:
    def __init__(self):
        self.account_repository = AccountRepository()

    async def create_savings(self, customer_id: str, account_number: str) -> dict:

        user_account = await self.account_repository.create_account(customer_id, account_number)

        if user_account is None:
            raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)

        return dict(user_account)