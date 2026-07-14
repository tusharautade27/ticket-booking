from sqlalchemy.orm import Session

from app.models.venue import Venue
from app.schemas.venue import VenueCreate, VenueUpdate


def create_venue(db: Session, venue: VenueCreate):
    db_venue = Venue(
        name=venue.name,
        city=venue.city,
        address=venue.address,
        total_rows=venue.total_rows,
        total_columns=venue.total_columns,
    )

    db.add(db_venue)
    db.commit()
    db.refresh(db_venue)

    return db_venue


def get_all_venues(db: Session):
    return db.query(Venue).all()


def get_venue_by_id(db: Session, venue_id: int):
    return (
        db.query(Venue)
        .filter(Venue.id == venue_id)
        .first()
    )


def update_venue(
    db: Session,
    venue_id: int,
    venue: VenueUpdate,
):
    db_venue = get_venue_by_id(db, venue_id)

    if not db_venue:
        return None

    db_venue.name = venue.name
    db_venue.city = venue.city
    db_venue.address = venue.address
    db_venue.total_rows = venue.total_rows
    db_venue.total_columns = venue.total_columns
    
    db.commit()
    db.refresh(db_venue)

    return db_venue


def delete_venue(
    db: Session,
    venue_id: int,
):
    db_venue = get_venue_by_id(db, venue_id)

    if not db_venue:
        return None

    db.delete(db_venue)
    db.commit()

    return db_venue