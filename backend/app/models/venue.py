from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)

    address = Column(String(255), nullable=False)

    city = Column(String(100), nullable=False)

    total_rows = Column(Integer, nullable=False)

    total_columns = Column(Integer, nullable=False)

    # ------------------------
    # Relationships
    # ------------------------

    seats = relationship(
        "Seat",
        back_populates="venue",
        cascade="all, delete-orphan",
    )

    events = relationship(
        "Event",
        back_populates="venue",
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
        return f"<Venue(id={self.id}, name='{self.name}', city='{self.city}')>"