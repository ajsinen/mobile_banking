from app.core.base_repository import BaseRepository

class UserRepository(BaseRepository):

    async def get_all_users(self) :
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(
                "SELECT username, name, address, customer_id, age, role FROM users"
            )

            return [dict(row) for row in rows]
