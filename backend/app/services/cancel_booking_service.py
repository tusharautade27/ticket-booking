from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.models.booking_seat import BookingSeat
from app.enums.booking_status import BookingStatus


def cancel_booking(
    db: Session,
    booking_id: int,
):
    booking = (
        db.query(Booking)
        .filter(Booking.id == booking_id)
        .first()
    )

    if not booking:
        raise ValueError("Booking not found")

    if booking.status == BookingStatus.CANCELLED:
        raise ValueError("Booking already cancelled")

    (
        db.query(BookingSeat)
        .filter(BookingSeat.booking_id == booking_id)
        .delete()
    )

    booking.status = BookingStatus.CANCELLED

    db.commit()
    db.refresh(booking)

    return booking