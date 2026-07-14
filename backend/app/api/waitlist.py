from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.waitlist import WaitlistResponse
from app.services.waitlist_service import WaitlistService

router = APIRouter(
    prefix="/waitlist",
    tags=["Waitlist"],
)


@router.post(
    "/{event_id}",
    response_model=WaitlistResponse,
    status_code=status.HTTP_201_CREATED,
)
def join_waitlist(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return WaitlistService.join_waitlist(
            db=db,
            user_id=current_user.id,
            event_id=event_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.delete("/{event_id}")
def leave_waitlist(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        WaitlistService.leave_waitlist(
            db=db,
            user_id=current_user.id,
            event_id=event_id,
        )
        return {"message": "Removed from waitlist successfully."}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "/{event_id}",
    response_model=list[WaitlistResponse],
)
def get_waitlist(
    event_id: int,
    db: Session = Depends(get_db),
):
    return WaitlistService.get_waitlist(
        db=db,
        event_id=event_id,
    )