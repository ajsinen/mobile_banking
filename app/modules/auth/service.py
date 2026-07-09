from fastapi import HTTPException, status
from app.core.security import hash_password, verify_password, create_access_token
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


    async def login_user(self, username: str, password: str) -> dict:
        # GET USER BY USERNAME
        user = await self.repo.get_user_by_username(username)
        if not user:
            raise HTTPException(detail="User not found", status_code=status.HTTP_404_NOT_FOUND)

        # CHECK IF VALID PASSWORD FOR USERNAME
        if not verify_password(password, user['password']):
            raise HTTPException(detail="Incorrect username or password", status_code=status.HTTP_404_NOT_FOUND)

        # CREATE ACCESS TOKEN
        access_token = create_access_token(str(user['id']), user['role'])
        print("ACCESS_TOKEN: ", access_token)

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }
