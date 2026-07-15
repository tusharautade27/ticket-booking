from app.models.booking_seat import BookingSeat
from app.models.seat import Seat

from datetime import datetime, UTC

from sqlalchemy.orm import Session

from app.enums.booking_status import BookingStatus
from app.models.booking import Booking

from app.models.seat_hold import SeatHold
from app.schemas.booking import BookingCreate

from app.services.ticket_service import TicketService

def create_booking(
    db: Session,
    booking: BookingCreate,
    user_id: int,
):
    # Validate seats
    seats = (
        db.query(Seat)
        .filter(
            Seat.id.in_(booking.seat_ids)
        )
        .all()
    )

    if len(seats) != len(booking.seat_ids):
        raise ValueError("One or more seats do not exist")

    # Check if any seat is actively held by another user
    for seat_id in booking.seat_ids:
        active_hold = (
            db.query(SeatHold)
            .filter(
                SeatHold.event_id == booking.event_id,
                SeatHold.seat_id == seat_id,
                SeatHold.expires_at > datetime.now(UTC),
                SeatHold.user_id != user_id,
            )
            .first()
        )

        if active_hold:
            raise ValueError(
                f"Seat {seat_id} is currently on hold."
            )

    # Check if seat is already booked
    for seat_id in booking.seat_ids:
        booked = (
            db.query(BookingSeat)
            .join(Booking)
            .filter(
                Booking.event_id == booking.event_id,
                BookingSeat.seat_id == seat_id,
                Booking.status != BookingStatus.CANCELLED,
            )
            .first()
        )

        if booked:
            raise ValueError(
                f"Seat {seat_id} is already booked."
            )

    # Create booking
    db_booking = Booking(
        user_id=user_id,
        event_id=booking.event_id,
        status=BookingStatus.PENDING,
    )

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)

    # Create booking-seat mappings
    for seat_id in booking.seat_ids:
        booking_seat = BookingSeat(
            booking_id=db_booking.id,
            seat_id=seat_id,
        )
        db.add(booking_seat)

    db.commit()
    db.refresh(db_booking)

    # Generate ticket immediately after booking
    TicketService.create_ticket(
        db=db,
        booking=db_booking,
    )

    return db_booking

def get_my_bookings(
    db: Session,
    user_id: int,
):
    return (
        db.query(Booking)
        .filter(Booking.user_id == user_id)
        .all()
    )