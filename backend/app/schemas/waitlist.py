from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WaitlistResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    joined_at: datetime
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)