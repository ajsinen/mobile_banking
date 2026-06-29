from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import connect_db
from app.core.database import disconnect_db
from app.core.config import settings

# from app.modules.users.router import router as users_router
from app.modules.auth.router import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # connect to database
    await connect_db()

    yield
    # disconnect db connection when application shuts down
    await disconnect_db()

print(settings.APP_NAME)
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

# app.include_router(auth_router)
app.include_router(auth_router)