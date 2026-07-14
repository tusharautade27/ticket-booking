from pathlib import Path

from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
)
from reportlab.lib.styles import getSampleStyleSheet


class PDFService:

    PDF_DIRECTORY = Path("storage/pdf_tickets")

    @staticmethod
    def generate(
        ticket,
        booking,
        event,
    ) -> str:
        """
        Generate a PDF ticket.
        """

        PDFService.PDF_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True,
        )

        pdf_path = (
            PDFService.PDF_DIRECTORY /
            f"{ticket.ticket_number}.pdf"
        )

        styles = getSampleStyleSheet()

        document = SimpleDocTemplate(
            str(pdf_path),
            rightMargin=0.5 * inch,
            leftMargin=0.5 * inch,
            topMargin=0.5 * inch,
            bottomMargin=0.5 * inch,
        )

        story = []

        story.append(
            Paragraph(
                "<b>🎫 Ticket Booking System</b>",
                styles["Title"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Ticket Number:</b> {ticket.ticket_number}",
                styles["BodyText"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Event:</b> {event.title}",
                styles["BodyText"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Date:</b> {event.event_date}",
                styles["BodyText"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Time:</b> {event.event_time}",
                styles["BodyText"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Booking ID:</b> {booking.id}",
                styles["BodyText"],
            )
        )

        document.build(story)

        return str(pdf_path)