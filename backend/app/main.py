from fastapi import FastAPI
from sqlalchemy import text

from app.database.database import engine

# Routers
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.venues import router as venue_router
from app.api.events import router as event_router
from app.api.bookings import router as booking_router
from app.api.seats import router as seat_router
from app.api.seat_holds import router as seat_hold_router
from app.api.waitlist import router as waitlist_router
from app.api.tickets import router as ticket_router
from app.api import payments
from app.api import cancel_booking

# Import models so SQLAlchemy registers them
from app.models import User

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Ticket Booking API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(venue_router)
app.include_router(event_router)
app.include_router(booking_router)
app.include_router(seat_router)
app.include_router(seat_hold_router)
app.include_router(payments.router)
app.include_router(cancel_booking.router)
app.include_router(waitlist_router)
app.include_router(ticket_router)


@app.get("/")
def root():
    return {"message": "Ticket Booking API is running 🚀"}


@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        version = connection.execute(text("SELECT version();")).scalar()

    return {
        "status": "Connected",
        "database": version,
    }


@app.get("/debug-db")
def debug_db():
    with engine.connect() as conn:
        db_name = conn.execute(
            text("SELECT current_database();")
        ).scalar()

        tables = conn.execute(
            text(
                """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema='public'
                ORDER BY table_name;
                """
            )
        ).fetchall()

    return {
        "database": db_name,
        "tables": [t[0] for t in tables],
    }

from fastapi import Depends
from app.core.dependencies import get_current_user
from app.models.user import User


@app.get("/me-test")
def me_test(
    current_user: User = Depends(get_current_user),
):
    return {
        "id": current_user.id,
        "email": current_user.email,
    }