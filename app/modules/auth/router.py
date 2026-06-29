from fastapi import APIRouter
from starlette import status
from app.modules.auth.schema import (
    RegisterRequest,
    RegisterResponse, LoginRequest, LoginResponse
)
from app.modules.auth.service import (AuthService)
router = APIRouter(tags=["Authentication"])

service = AuthService()

@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(payload: RegisterRequest):
    return await service.register_user(payload.username, payload.password, payload.name, payload.address, payload.age)


@router.post("/login", response_model= LoginResponse, status_code=status.HTTP_200_OK)
async def login(payload: LoginRequest):
    return await service.login_user(payload.username, payload.password)
