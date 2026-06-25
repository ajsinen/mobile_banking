import asyncpg
from dotenv import load_dotenv
import os
_pool: asyncpg.Pool | None = None

load_dotenv()


async def connect_db():
    db_password = os.getenv("DB_PASSWORD")
    db_user = os.getenv("DB_USER")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    print(db_url)
    global _pool

    _pool = await asyncpg.create_pool(
        dsn= db_url,
        min_size=5,
        max_size=20,
        command_timeout=60,
    )


async def disconnect_db():
    if _pool:
        await _pool.close()


def get_pool() -> asyncpg.Pool:
    if _pool is None:
        raise RuntimeError("Database pool not initialized")

    return _pool