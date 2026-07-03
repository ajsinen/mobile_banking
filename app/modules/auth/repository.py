from app.core.base_repository import BaseRepository
from app.modules.accounts.schema import CreateSavingsRequest
from uuid import UUID


class AuthRepository(BaseRepository):
    async def get_user_by_id(self, user_id: UUID) -> dict:
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(
                "SELECT customer_id, username, name, role FROM users WHERE id = $1", user_id
            )


    async def get_user_by_username(self, username: str) -> dict:
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(
                "SELECT * FROM users WHERE username = $1", username
            )




    async def register_user(self, name: str, address: str, password: str , age: int, username: str) -> dict:

        async with self.pool.acquire() as conn:
            return await conn.fetchrow(
                "INSERT INTO users (name, username, password, age, address) "
                "VALUES ($1, $2, $3, $4, $5) RETURNING id, username, name, customer_id",
                name, username, password, age, address
            )
