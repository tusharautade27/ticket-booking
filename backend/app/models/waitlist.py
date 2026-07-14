from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    UniqueConstraint,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Waitlist(Base):
    __tablename__ = "waitlists"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "event_id",
            name="uq_waitlist_user",
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

    joined_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="waitlists",
    )

    event = relationship(
        "Event",
        back_populates="waitlists",
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