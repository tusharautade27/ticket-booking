from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Time,
    Enum,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base
from app.enums import EventType


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    description = Column(String(1000))

    event_type = Column(
        Enum(EventType),
        nullable=False,
    )

    event_date = Column(Date, nullable=False)

    event_time = Column(Time, nullable=False)

    venue_id = Column(
        Integer,
        ForeignKey("venues.id", ondelete="CASCADE"),
        nullable=False,
    )

    organizer_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    # ------------------------
    # Relationships
    # ------------------------

    venue = relationship(
        "Venue",
        back_populates="events",
    )

    organizer = relationship(
        "User",
        back_populates="events",
    )

    bookings = relationship(
        "Booking",
        back_populates="event",
        cascade="all, delete-orphan",
    )

    seat_holds = relationship(
        "SeatHold",
        back_populates="event",
        cascade="all, delete-orphan",
    )

    waitlists = relationship(
        "Waitlist",
        back_populates="event",
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
            f"<Event(id={self.id}, "
            f"title='{self.title}', "
            f"type='{self.event_type.value}')>"
        )