from datetime import datetime

from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.models.ticket import Ticket
from app.services.pdf_service import PDFService
from app.services.qr_service import QRService


class TicketService:

    @staticmethod
    def generate_ticket_number() -> str:
        """
        Example:
        TKT-20260713-143012
        """
        return f"TKT-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

    @staticmethod
    def create_ticket(
        db: Session,
        booking: Booking,
    ) -> Ticket:
        """
        Create a ticket for a confirmed booking.
        """

        existing = (
            db.query(Ticket)
            .filter(Ticket.booking_id == booking.id)
            .first()
        )

        if existing:
            return existing

        ticket_number = TicketService.generate_ticket_number()

        ticket = Ticket(
            booking_id=booking.id,
            ticket_number=ticket_number,
        )

        db.add(ticket)
        db.commit()
        db.refresh(ticket)

        # -----------------------------
        # Generate QR Code
        # -----------------------------
        qr_path = QRService.generate(ticket.ticket_number)
        ticket.qr_code = qr_path

        # -----------------------------
        # Generate PDF
        # -----------------------------
        pdf_path = PDFService.generate(
            ticket=ticket,
            booking=booking,
            event=booking.event,
        )

        ticket.pdf_path = pdf_path

        db.commit()
        db.refresh(ticket)

        return ticket