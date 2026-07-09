from pydantic import BaseModel

class CreateSavingsRequest(BaseModel):
    account_number: str


class CreateSavingsResponse(BaseModel):
    customer_id: str
    account_number: str
    message: str | None = "Savings created Successfully"