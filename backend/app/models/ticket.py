from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    __table_args__ = (
        UniqueConstraint(
            "booking_id",
            name="uq_ticket_booking",
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id", ondelete="CASCADE"),
        nullable=False,
    )

    ticket_number = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    qr_code = Column(
        String,
        nullable=True,
    )

    pdf_path = Column(
        String,
        nullable=True,
    )

    # ------------------------
    # Validation
    # ------------------------

    is_used = Column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
    )

    used_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )

    issued_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    booking = relationship(
        "Booking",
        back_populates="ticket",
    )