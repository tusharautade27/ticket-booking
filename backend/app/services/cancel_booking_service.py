from pathlib import Path

from sqlalchemy.orm import Session

from app.enums.booking_status import BookingStatus
from app.models.booking import Booking
from app.models.booking_seat import BookingSeat
from app.models.ticket import Ticket


def cancel_booking(
    db: Session,
    booking_id: int,
    user_id: int,
):
    booking = (
        db.query(Booking)
        .filter(Booking.id == booking_id)
        .first()
    )

    if not booking:
        raise ValueError("Booking not found")

    if booking.user_id != user_id:
        raise ValueError(
            "You are not authorized to cancel this booking"
        )

    if booking.status == BookingStatus.CANCELLED:
        raise ValueError("Booking already cancelled")

    # -----------------------------
    # Delete generated ticket
    # -----------------------------
    ticket = (
        db.query(Ticket)
        .filter(
            Ticket.booking_id == booking.id
        )
        .first()
    )

    if ticket:

        # Delete QR image
        if ticket.qr_code:
            qr = Path(ticket.qr_code)

            if qr.exists():
                qr.unlink()

        # Delete PDF
        if ticket.pdf_path:
            pdf = Path(ticket.pdf_path)

            if pdf.exists():
                pdf.unlink()

        db.delete(ticket)

    # -----------------------------
    # Remove booked seats
    # -----------------------------
    (
        db.query(BookingSeat)
        .filter(
            BookingSeat.booking_id == booking.id
        )
        .delete()
    )

    # -----------------------------
    # Cancel booking
    # -----------------------------
    booking.status = BookingStatus.CANCELLED

    db.commit()
    db.refresh(booking)

    return {
        "message": "Booking cancelled successfully"
    }