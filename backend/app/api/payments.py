from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.booking import BookingResponse
from app.services.payment_service import confirm_booking

router = APIRouter(
    prefix="/payments",
    tags=["Payments"],
)


@router.post(
    "/confirm/{booking_id}",
    response_model=BookingResponse,
)
def confirm_payment(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    booking = confirm_booking(
        db=db,
        booking_id=booking_id,
        user_id=current_user.id,
    )

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found",
        )

    return booking