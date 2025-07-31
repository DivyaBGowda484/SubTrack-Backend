# app/api/subscription.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db  # or adjust if you're using app.dependencies
from app.schemas.subscription import SubscriptionCreate, SubscriptionOut
from app.services.subscription_service import SubscriptionService

router = APIRouter(
    prefix="/subscriptions",
    tags=["Subscriptions"]
)

@router.post("/", response_model=SubscriptionOut, summary="Create a new subscription")
def create_subscription(
    data: SubscriptionCreate, db: Session = Depends(get_db)
):
    """
    Create a new subscription entry in the database.
    """
    try:
        return SubscriptionService.create(db, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
