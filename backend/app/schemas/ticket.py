from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TicketResponse(BaseModel):
    id: int
    booking_id: int
    ticket_number: str
    qr_code: str | None = None
    pdf_path: str | None = None
    issued_at: datetime
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)