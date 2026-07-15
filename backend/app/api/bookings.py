from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.booking import BookingCreate, BookingResponse
from app.services.booking_service import (
    create_booking,
    get_my_bookings,
)

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.post("/", response_model=BookingResponse)
def create(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return create_booking(db, booking, current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/me",
    response_model=List[BookingResponse],
)
def my_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_my_bookings(
        db,
        current_user.id,
    )