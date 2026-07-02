from pydantic import BaseModel


class UserListResponse(BaseModel):
    username: str
    name: str
    address: str
    customer_id: str
    age: int
    role: int
