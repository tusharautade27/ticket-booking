from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.database.dependencies import get_db
from app.models.user import User
from app.services.cancel_booking_service import cancel_booking

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.post("/{booking_id}/cancel")
def cancel(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return cancel_booking(
            db=db,
            booking_id=booking_id,
            user_id=current_user.id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )