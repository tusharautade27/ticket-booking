from datetime import datetime

from pydantic import BaseModel


class PaymentCreate(BaseModel):
    booking_id: int
    amount: int


class PaymentResponse(BaseModel):
    id: int
    booking_id: int
    amount: int
    provider: str
    status: str
    transaction_id: str | None
    paid_at: datetime | None

    model_config = {
        "from_attributes": True
    }