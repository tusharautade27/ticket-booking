from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.event import Event
from app.schemas.event import EventCreate


def create_event(db: Session, event: EventCreate):
    db_event = Event(
        title=event.title,
        description=event.description,
        event_type=event.event_type,
        event_date=event.event_date,
        event_time=event.event_time,
        venue_id=event.venue_id,
        organizer_id=event.organizer_id,
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


def get_events(db: Session):
    return db.query(Event).all()


def get_event(db: Session, event_id: int):
    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return event


def update_event(db: Session, event_id: int, data: EventCreate):
    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    event.venue_id = data.venue_id
    event.title = data.title
    event.event_time = data.event_time
    event.organizer_id = data.organizer_id
    event.description = data.description
    event.event_type = data.event_type
    event.event_date = data.event_date

    db.commit()
    db.refresh(event)

    return event


def delete_event(db: Session, event_id: int):
    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(event)
    db.commit()

    return {"message": "Event deleted successfully"}