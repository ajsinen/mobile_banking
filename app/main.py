from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from app.core.database import connect_db
from app.core.database import disconnect_db
from app.core.config import settings
import fastapi_swagger_dark as fsd

# from app.modules.users.router import router as users_router
from app.modules.auth.router import router as auth_router
from app.modules.accounts.router import router as account_router
from app.modules.healthcheck.router import router as healthcheck_router
from app.modules.users.router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # connect to database
    await connect_db()

    yield
    # disconnect db connection when application shuts down
    await disconnect_db()

print(settings.APP_NAME)

# 1. Turn off native white Swagger UI docs
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
    docs_url=None
)

# 2. Setup a dedicated router for the dark theme docs
swagger_router = APIRouter()
fsd.install(swagger_router)
app.include_router(swagger_router)

# Include your application business routes
app.include_router(auth_router)
app.include_router(account_router)
app.include_router(healthcheck_router)
app.include_router(user_router)
