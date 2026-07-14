from datetime import date, time
from pydantic import BaseModel

from app.enums.event_type import EventType


class EventCreate(BaseModel):
    title: str
    description: str
    event_type: EventType
    event_date: date
    event_time: time
    venue_id: int
    organizer_id: int


class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    event_type: EventType
    event_date: date
    event_time: time
    venue_id: int
    organizer_id: int

    model_config = {
        "from_attributes": True
    }