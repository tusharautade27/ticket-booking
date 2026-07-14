from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    DateTime,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base
from app.enums import SeatCategory


class Seat(Base):
    __tablename__ = "seats"

    __table_args__ = (
        UniqueConstraint(
            "venue_id",
            "row",
            "seat_number",
            name="uq_seat_position",
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    venue_id = Column(
        Integer,
        ForeignKey("venues.id", ondelete="CASCADE"),
        nullable=False,
    )

    row = Column(String(5), nullable=False)

    seat_number = Column(Integer, nullable=False)

    category = Column(
        Enum(SeatCategory),
        nullable=False,
        default=SeatCategory.STANDARD,
    )

    # ------------------------
    # Relationships
    # ------------------------

    venue = relationship(
        "Venue",
        back_populates="seats",
    )

    booking_seats = relationship(
        "BookingSeat",
        back_populates="seat",
        cascade="all, delete-orphan",
    )

    seat_holds = relationship(
        "SeatHold",
        back_populates="seat",
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
            f"<Seat(id={self.id}, "
            f"row='{self.row}', "
            f"seat={self.seat_number}, "
            f"category='{self.category.value}')>"
        )
    
    bookings = relationship(
        "Booking",
        secondary="booking_seats",
        back_populates="seats",
    )