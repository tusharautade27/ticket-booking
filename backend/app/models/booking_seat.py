from sqlalchemy import DateTime
from sqlalchemy.sql import func

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class BookingSeat(Base):
    __tablename__ = "booking_seats"

    __table_args__ = (
        UniqueConstraint(
            "booking_id",
            "seat_id",
            name="uq_booking_seat",
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id", ondelete="CASCADE"),
        nullable=False,
    )

    seat_id = Column(
        Integer,
        ForeignKey("seats.id", ondelete="CASCADE"),
        nullable=False,
    )

    booking = relationship(
        "Booking",
        back_populates="booking_seats",
    )

    seat = relationship(
        "Seat",
        back_populates="booking_seats",
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )