from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.seat_hold import (
    SeatHoldCreate,
    SeatHoldResponse,
)
from app.services.seat_hold_service import hold_seat

router = APIRouter(
    prefix="/seat-holds",
    tags=["Seat Holds"],
)


@router.post(
    "",
    response_model=SeatHoldResponse,
)
def create_hold(
    request: SeatHoldCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    hold = hold_seat(
        db=db,
        user_id=current_user.id,
        event_id=request.event_id,
        seat_id=request.seat_id,
    )

    if hold is None:
        raise HTTPException(
            status_code=400,
            detail="Seat is already on hold",
        )

    return hold