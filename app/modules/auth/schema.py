from pydantic import BaseModel, Field
from uuid import UUID


class RegisterRequest(BaseModel):
    name: str
    address: str | None = "None"
    username: str
    password: str = Field(min_length=8)
    age: int = Field(gt=18)


class RegisterResponse(BaseModel):
    id: UUID
    username: str
    name: str
    customerId: str


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    accessToken: str
    tokenType: str = "bearer"