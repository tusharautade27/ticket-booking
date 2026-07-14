from datetime import datetime
from pathlib import Path

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.database.dependencies import get_db
from app.models.ticket import Ticket
from app.models.user import User

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"],
)


@router.get("/download/{booking_id}")
def download_ticket(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ticket = (
        db.query(Ticket)
        .filter(
            Ticket.booking_id == booking_id,
        )
        .first()
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found",
        )

    # Only the owner can download the ticket
    if ticket.booking.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized",
        )

    if not ticket.pdf_path:
        raise HTTPException(
            status_code=404,
            detail="PDF not generated",
        )

    pdf = Path(ticket.pdf_path)

    if not pdf.exists():
        raise HTTPException(
            status_code=404,
            detail="PDF file missing",
        )

    return FileResponse(
        path=pdf,
        media_type="application/pdf",
        filename=pdf.name,
    )


@router.post("/validate/{ticket_number}")
def validate_ticket(
    ticket_number: str,
    db: Session = Depends(get_db),
):
    """
    Validate a ticket at event entry.
    """

    ticket = (
        db.query(Ticket)
        .filter(
            Ticket.ticket_number == ticket_number,
        )
        .first()
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found",
        )

    if ticket.is_used:
        raise HTTPException(
            status_code=400,
            detail="Ticket has already been used",
        )

    ticket.is_used = True
    ticket.used_at = datetime.utcnow()

    db.commit()
    db.refresh(ticket)

    return {
        "message": "Ticket validated successfully",
        "ticket_number": ticket.ticket_number,
        "booking_id": ticket.booking_id,
        "validated_at": ticket.used_at,
    }