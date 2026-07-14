from datetime import datetime, timedelta, UTC

from sqlalchemy.orm import Session

from app.models.seat_hold import SeatHold


HOLD_MINUTES = 10


def release_expired_holds(db: Session):
    expired_holds = (
        db.query(SeatHold)
        .filter(SeatHold.expires_at < datetime.now(UTC))
        .all()
    )

    for hold in expired_holds:
        db.delete(hold)

    db.commit()


def hold_seat(
    db: Session,
    user_id: int,
    event_id: int,
    seat_id: int,
):
    # Remove expired holds first
    release_expired_holds(db)

    # Check whether the seat is already held
    existing = (
        db.query(SeatHold)
        .filter(
            SeatHold.event_id == event_id,
            SeatHold.seat_id == seat_id,
            SeatHold.expires_at > datetime.now(UTC),
        )
        .first()
    )

    if existing:
        return None

    hold = SeatHold(
        user_id=user_id,
        event_id=event_id,
        seat_id=seat_id,
        expires_at=datetime.now(UTC) + timedelta(minutes=HOLD_MINUTES),
    )

    db.add(hold)
    db.commit()
    db.refresh(hold)

    return hold