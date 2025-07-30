from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.subscription_schemas import SubscriptionCreate
from app.services.subscription_service import SubscriptionService

router = APIRouter()

@router.post("/subscriptions")
def create_subscription(data: SubscriptionCreate, db: Session = Depends(get_db)):
    return SubscriptionService.create(db, data)