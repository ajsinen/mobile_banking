from app.core.base_repository import BaseRepository


class AuthRepository(BaseRepository):

    async def get_user_by_username(self, username: str):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(
                "SELECT * FROM users WHERE username = $1", username
            )




    async def register_user(self, name: str, address: str, password: str , age: int, username: str) -> dict:

        async with self.pool.acquire() as conn:
            return await conn.fetchrow(
                "INSERT INTO users (name, username, password, age, address) "
                "VALUES ($1, $2, $3, $4, $5) RETURNING id, username, name",
                name, username, password, age, address
            )


