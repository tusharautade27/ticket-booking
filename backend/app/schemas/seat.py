from pydantic import BaseModel

from app.enums import SeatCategory


class SeatCreate(BaseModel):
    venue_id: int
    row: str
    seat_number: int
    category: SeatCategory


class SeatResponse(BaseModel):
    id: int
    venue_id: int
    row: str
    seat_number: int
    category: SeatCategory

    model_config = {
        "from_attributes": True
    }