from sqlalchemy.orm import Session

from app.models.seat import Seat
from app.models.venue import Venue
from app.enums.seat_category import SeatCategory


def generate_seats(
    db: Session,
    venue_id: int,
):
    venue = (
        db.query(Venue)
        .filter(Venue.id == venue_id)
        .first()
    )

    if not venue:
        return None

    existing = (
        db.query(Seat)
        .filter(Seat.venue_id == venue_id)
        .first()
    )

    if existing:
        return {
            "message": "Seats already generated"
        }

    seats = []

    for r in range(venue.total_rows):

        row_letter = chr(65 + r)

        for c in range(1, venue.total_columns + 1):

            category = (
                SeatCategory.VIP
                if r < 2
                else SeatCategory.STANDARD
            )

            seat = Seat(
                venue_id=venue.id,
                row=row_letter,
                seat_number=c,
                category=category,
            )

            seats.append(seat)

    db.add_all(seats)
    db.commit()

    return {
        "message": f"{len(seats)} seats generated successfully"
    }