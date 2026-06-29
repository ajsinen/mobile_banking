from fastapi import HTTPException, status
from app.core.security import hash_password
from app.modules.auth.repository import (AuthRepository)


class AuthService:
    def __init__(self):
        self.repo = AuthRepository()

    async def register_user(self, username: str, password: str, name: str, address: str, age: int) -> dict:

        existing_user = await self.repo.get_user_by_username(username)

        if existing_user:
            raise HTTPException(detail="User already exists", status_code=status.HTTP_400_BAD_REQUEST)

        hashed_password = hash_password(password)

        user = await self.repo.register_user(name, address, hashed_password, age, username)
        return dict(user)
