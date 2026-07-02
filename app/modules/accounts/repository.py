from app.core.base_repository import BaseRepository

class AccountRepository(BaseRepository):

    async def create_account(self, customer_id: str, account_number: str):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow("INSERT INTO accounts (customer_id, account_number) "
                                       "VALUES ($1, $2) RETURNING customer_id, account_number",
                                       customer_id, account_number)
