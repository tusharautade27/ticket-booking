from sqlalchemy import (
    Column,
    Integer,
    Enum,
    DateTime,
    ForeignKey,
    Index,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base
from app.enums import BookingStatus


class Booking(Base):
    __tablename__ = "bookings"

    __table_args__ = (
        Index("idx_booking_user", "user_id"),
        Index("idx_booking_event", "event_id"),
    )

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    event_id = Column(
        Integer,
        ForeignKey("events.id", ondelete="CASCADE"),
        nullable=False,
    )

    status = Column(
        Enum(BookingStatus),
        nullable=False,
        default=BookingStatus.PENDING,
    )

    booked_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # ------------------------
    # Relationships
    # ------------------------

    user = relationship(
        "User",
        back_populates="bookings",
    )

    event = relationship(
        "Event",
        back_populates="bookings",
    )

    booking_seats = relationship(
        "BookingSeat",
        back_populates="booking",
        cascade="all, delete-orphan",
    )

    seats = relationship(
        "Seat",
        secondary="booking_seats",
        back_populates="bookings",
    )

    payments = relationship(
        "Payment",
        back_populates="booking",
    )

    # ✅ NEW: One booking has one ticket
    ticket = relationship(
        "Ticket",
        back_populates="booking",
        uselist=False,
        cascade="all, delete-orphan",
    )

    # ------------------------
    # Audit Fields
    # ------------------------

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

    def __repr__(self):
        return (
            f"<Booking(id={self.id}, "
            f"user={self.user_id}, "
            f"event={self.event_id}, "
            f"status='{self.status.value}')>"
        )