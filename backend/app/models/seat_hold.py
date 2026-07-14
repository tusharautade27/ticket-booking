from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    Index,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class SeatHold(Base):
    __tablename__ = "seat_holds"

    __table_args__ = (
        Index(
            "idx_hold_expiry",
            "expires_at",
        ),
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

    seat_id = Column(
        Integer,
        ForeignKey("seats.id", ondelete="CASCADE"),
        nullable=False,
    )

    expires_at = Column(
        DateTime(timezone=True),
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

    user = relationship(
        "User",
        back_populates="seat_holds",
    )

    event = relationship(
        "Event",
        back_populates="seat_holds",
    )

    seat = relationship(
        "Seat",
        back_populates="seat_holds",
    )