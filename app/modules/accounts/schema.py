from pydantic import BaseModel, Field

class CreateSavingsRequest(BaseModel):
    accountNumber: str


class CreateSavingsResponse(BaseModel):
    customerId: str
    accountNumber: str
    message: str | None = "Savings created Successfully"