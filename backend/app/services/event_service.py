from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.event import Event
from app.schemas.event import EventCreate

from app.models.seat import Seat

from app.models.booking import Booking
from app.models.booking_seat import BookingSeat
from app.enums.booking_status import BookingStatus

def create_event(db: Session, event: EventCreate):
    db_event = Event(
        title=event.title,
        description=event.description,
        event_type=event.event_type,
        event_date=event.event_date,
        event_time=event.event_time,
        venue_id=event.venue_id,
        organizer_id=event.organizer_id,
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


def get_events(db: Session):
    return db.query(Event).all()


def get_event(db: Session, event_id: int):
    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return event


def update_event(db: Session, event_id: int, data: EventCreate):
    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    event.venue_id = data.venue_id
    event.title = data.title
    event.event_time = data.event_time
    event.organizer_id = data.organizer_id
    event.description = data.description
    event.event_type = data.event_type
    event.event_date = data.event_date

    db.commit()
    db.refresh(event)

    return event


def delete_event(db: Session, event_id: int):
    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(event)
    db.commit()

    return {"message": "Event deleted successfully"}

def get_event_seats(
    db: Session,
    event_id: int,
):
    event = get_event(db, event_id)

    seats = (
        db.query(Seat)
        .filter(
            Seat.venue_id == event.venue_id
        )
        .order_by(
            Seat.row,
            Seat.seat_number,
        )
        .all()
    )

    booked_seat_ids = {
        seat_id
        for (seat_id,) in (
            db.query(BookingSeat.seat_id)
            .join(
                Booking,
                Booking.id == BookingSeat.booking_id,
            )
            .filter(
                Booking.event_id == event_id,
                Booking.status != BookingStatus.CANCELLED,
            )
            .all()
        )
    }

    result = []

    for seat in seats:
        result.append(
            {
                "id": seat.id,
                "row": seat.row,
                "seat_number": seat.seat_number,
                "category": seat.category,
                "is_booked": seat.id in booked_seat_ids,
            }
        )

    return result