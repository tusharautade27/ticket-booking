from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    DateTime,
    func,
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id", ondelete="CASCADE"),
        nullable=False,
    )

    amount = Column(Integer, nullable=False)

    provider = Column(
        String,
        nullable=False,
        default="MOCK",
    )

    status = Column(
        String,
        nullable=False,
        default="PENDING",
    )

    transaction_id = Column(
        String,
        nullable=True,
    )

    paid_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    booking = relationship(
        "Booking",
        back_populates="payments",
    )