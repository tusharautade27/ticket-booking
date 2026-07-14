from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.seat_generator import generate_seats

from app.database.dependencies import get_db
from app.schemas.venue import (
    VenueCreate,
    VenueUpdate,
    VenueResponse,
)
from app.services.venue_service import (
    create_venue,
    get_all_venues,
    get_venue_by_id,
    update_venue,
    delete_venue,
)

router = APIRouter(
    prefix="/venues",
    tags=["Venues"],
)


@router.post(
    "",
    response_model=VenueResponse,
)
def create(
    venue: VenueCreate,
    db: Session = Depends(get_db),
):
    return create_venue(db, venue)


@router.get(
    "",
    response_model=list[VenueResponse],
)
def get_all(
    db: Session = Depends(get_db),
):
    return get_all_venues(db)


@router.get(
    "/{venue_id}",
    response_model=VenueResponse,
)
def get_one(
    venue_id: int,
    db: Session = Depends(get_db),
):
    venue = get_venue_by_id(db, venue_id)

    if not venue:
        raise HTTPException(
            status_code=404,
            detail="Venue not found",
        )

    return venue


@router.put(
    "/{venue_id}",
    response_model=VenueResponse,
)
def update(
    venue_id: int,
    venue: VenueUpdate,
    db: Session = Depends(get_db),
):
    updated = update_venue(
        db,
        venue_id,
        venue,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Venue not found",
        )

    return updated


@router.delete(
    "/{venue_id}",
)
def delete(
    venue_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_venue(
        db,
        venue_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Venue not found",
        )

    return {
        "message": "Venue deleted successfully"
    }


@router.post(
    "/{venue_id}/generate-seats",
)
def generate_all_seats(
    venue_id: int,
    db: Session = Depends(get_db),
):
    result = generate_seats(
        db,
        venue_id,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Venue not found",
        )

    return result