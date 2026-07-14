from sqlalchemy.orm import Session

from app.models.seat import Seat
from app.schemas.seat import SeatCreate


def create_seat(db: Session, seat: SeatCreate):
    db_seat = Seat(
        venue_id=seat.venue_id,
        row=seat.row,
        seat_number=seat.seat_number,
        category=seat.category,
    )

    db.add(db_seat)
    db.commit()
    db.refresh(db_seat)

    return db_seat


def get_all_seats(db: Session):
    return db.query(Seat).all()


def get_seat(db: Session, seat_id: int):
    return db.query(Seat).filter(
        Seat.id == seat_id
    ).first()


def update_seat(
    db: Session,
    seat_id: int,
    seat: SeatCreate,
):
    db_seat = get_seat(db, seat_id)

    if not db_seat:
        return None

    db_seat.venue_id = seat.venue_id
    db_seat.row = seat.row
    db_seat.seat_number = seat.seat_number
    db_seat.category = seat.category

    db.commit()
    db.refresh(db_seat)

    return db_seat


def delete_seat(
    db: Session,
    seat_id: int,
):
    db_seat = get_seat(db, seat_id)

    if not db_seat:
        return None

    db.delete(db_seat)
    db.commit()

    return db_seat