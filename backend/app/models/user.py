from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base
from app.enums import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, nullable=False, index=True)

    password = Column(String(255), nullable=False)

    role = Column(
        Enum(UserRole),
        nullable=False,
        default=UserRole.CUSTOMER,
    )

    # ------------------------
    # Relationships
    # ------------------------

    events = relationship(
        "Event",
        back_populates="organizer",
        cascade="all, delete-orphan",
    )

    bookings = relationship(
        "Booking",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    seat_holds = relationship(
        "SeatHold",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    waitlists = relationship(
        "Waitlist",
        back_populates="user",
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
        return f"<User(id={self.id}, email='{self.email}', role='{self.role.value}')>"