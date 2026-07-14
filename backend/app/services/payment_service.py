from sqlalchemy.orm import Session

from app.enums.booking_status import BookingStatus
from app.models.booking import Booking
from app.models.seat_hold import SeatHold
from app.services.ticket_service import TicketService


def confirm_booking(
    db: Session,
    booking_id: int,
    user_id: int,
):
    # Find booking
    booking = (
        db.query(Booking)
        .filter(
            Booking.id == booking_id,
            Booking.user_id == user_id,
        )
        .first()
    )

    if not booking:
        return None

    # Prevent confirming an already confirmed booking
    if booking.status == BookingStatus.CONFIRMED:
        return booking

    # Update booking status
    booking.status = BookingStatus.CONFIRMED

    # Remove seat holds
    db.query(SeatHold).filter(
        SeatHold.user_id == user_id,
        SeatHold.event_id == booking.event_id,
    ).delete()

    db.commit()
    db.refresh(booking)

    # Create ticket if it doesn't already exist
    TicketService.create_ticket(
        db=db,
        booking=booking,
    )

    return booking