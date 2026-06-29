from fastapi import APIRouter
from starlette import status
from app.modules.auth.schema import (
    RegisterRequest,
    RegisterResponse
)
from app.modules.auth.service import (AuthService)
router = APIRouter(tags=["authentication"])

service = AuthService()

@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(payload: RegisterRequest):
    return await service.register_user(payload.username, payload.password, payload.name, payload.address, payload.age)


# @router.get("/login")
# async def login():
#     return {"message": "Hello World"}