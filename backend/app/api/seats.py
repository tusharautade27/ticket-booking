from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.seat import (
    SeatCreate,
    SeatResponse,
)
from app.services.seat_service import (
    create_seat,
    get_all_seats,
    get_seat,
    update_seat,
    delete_seat,
)

router = APIRouter(
    prefix="/seats",
    tags=["Seats"],
)


@router.post(
    "",
    response_model=SeatResponse,
)
def create(
    seat: SeatCreate,
    db: Session = Depends(get_db),
):
    return create_seat(db, seat)


@router.get(
    "",
    response_model=list[SeatResponse],
)
def get_all(
    db: Session = Depends(get_db),
):
    return get_all_seats(db)


@router.get(
    "/{seat_id}",
    response_model=SeatResponse,
)
def get_one(
    seat_id: int,
    db: Session = Depends(get_db),
):
    seat = get_seat(db, seat_id)

    if not seat:
        raise HTTPException(
            status_code=404,
            detail="Seat not found",
        )

    return seat


@router.put(
    "/{seat_id}",
    response_model=SeatResponse,
)
def update(
    seat_id: int,
    seat: SeatCreate,
    db: Session = Depends(get_db),
):
    updated = update_seat(
        db,
        seat_id,
        seat,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Seat not found",
        )

    return updated


@router.delete(
    "/{seat_id}",
)
def delete(
    seat_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_seat(
        db,
        seat_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Seat not found",
        )

    return {
        "message": "Seat deleted successfully"
    }