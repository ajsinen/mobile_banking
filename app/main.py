from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import connect_db
from app.core.database import disconnect_db

from app.modules.users.router import router as users_router
# from app.modules.auth.router import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # connect to database
    await connect_db()

    yield
    # disconnect db connection when application shuts down
    await disconnect_db()


app = FastAPI(
    title="My API",
    lifespan=lifespan,
)

# app.include_router(auth_router)
app.include_router(users_router)