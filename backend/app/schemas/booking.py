from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.enums.booking_status import BookingStatus


class BookingCreate(BaseModel):
    event_id: int
    seat_ids: List[int]


class BookingResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    status: BookingStatus
    booked_at: datetime

    model_config = {
        "from_attributes": True
    }