from sqlalchemy.orm import Session

from app.models.event import Event
from app.models.waitlist import Waitlist


class WaitlistService:
    @staticmethod
    def join_waitlist(
        db: Session,
        user_id: int,
        event_id: int,
    ) -> Waitlist:

        event = db.query(Event).filter(Event.id == event_id).first()

        if not event:
            raise ValueError("Event not found.")

        existing = (
            db.query(Waitlist)
            .filter(
                Waitlist.user_id == user_id,
                Waitlist.event_id == event_id,
            )
            .first()
        )

        if existing:
            raise ValueError("You are already on the waitlist.")

        waitlist = Waitlist(
            user_id=user_id,
            event_id=event_id,
        )

        db.add(waitlist)
        db.commit()
        db.refresh(waitlist)

        print("Inserted Waitlist ID:", waitlist.id)

        rows = db.query(Waitlist).all()
        print("Rows after commit:", len(rows))
        print(rows)

        return waitlist

    @staticmethod
    def leave_waitlist(
        db: Session,
        user_id: int,
        event_id: int,
    ) -> None:
        """
        Remove a user from an event waitlist.
        """

        waitlist = (
            db.query(Waitlist)
            .filter(
                Waitlist.user_id == user_id,
                Waitlist.event_id == event_id,
            )
            .first()
        )

        if not waitlist:
            raise ValueError("You are not on the waitlist.")

        db.delete(waitlist)
        db.commit()

    @staticmethod
    def get_waitlist(
        db: Session,
        event_id: int,
    ) -> list[Waitlist]:
        """
        Return the waitlist ordered by join time (FIFO).
        """

        return (
            db.query(Waitlist)
            .filter(Waitlist.event_id == event_id)
            .order_by(Waitlist.joined_at.asc())
            .all()
        )

    @staticmethod
    def get_first_user(
        db: Session,
        event_id: int,
    ) -> Waitlist | None:
        """
        Return the first user in the waitlist.
        """

        return (
            db.query(Waitlist)
            .filter(Waitlist.event_id == event_id)
            .order_by(Waitlist.joined_at.asc())
            .first()
        )