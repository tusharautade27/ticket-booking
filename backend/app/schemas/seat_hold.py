from datetime import datetime

from pydantic import BaseModel


class SeatHoldCreate(BaseModel):
    event_id: int
    seat_id: int


class SeatHoldResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    seat_id: int
    expires_at: datetime

    model_config = {
        "from_attributes": True
    }