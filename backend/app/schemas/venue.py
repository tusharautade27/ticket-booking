from pydantic import BaseModel


class VenueBase(BaseModel):
    name: str
    city: str
    address: str
    total_rows: int
    total_columns: int


class VenueCreate(VenueBase):
    pass


class VenueUpdate(VenueBase):
    pass


class VenueResponse(VenueBase):
    id: int

    model_config = {
        "from_attributes": True
    }