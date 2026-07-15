from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.event import EventCreate, EventResponse
from app.services.event_service import (
    create_event,
    get_events,
    get_event,
    get_event_seats,
    update_event,
    delete_event,
)

router = APIRouter(
    prefix="/events",
    tags=["Events"],
)


@router.post(
    "",
    response_model=EventResponse,
)
def create(
    event: EventCreate,
    db: Session = Depends(get_db),
):
    return create_event(db, event)


@router.get(
    "",
    response_model=list[EventResponse],
)
def get_all(
    db: Session = Depends(get_db),
):
    return get_events(db)


@router.get(
    "/{event_id}",
    response_model=EventResponse,
)
def get_one(
    event_id: int,
    db: Session = Depends(get_db),
):
    return get_event(db, event_id)

@router.get(
    "/{event_id}/seats",
)
def get_seats(
    event_id: int,
    db: Session = Depends(get_db),
):
    return get_event_seats(
        db,
        event_id,
    )


@router.put(
    "/{event_id}",
    response_model=EventResponse,
)
def update(
    event_id: int,
    event: EventCreate,
    db: Session = Depends(get_db),
):
    return update_event(db, event_id, event)


@router.delete(
    "/{event_id}",
)
def delete(
    event_id: int,
    db: Session = Depends(get_db),
):
    return delete_event(db, event_id)