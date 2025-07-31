from sqlalchemy.orm import Session
from app.db.models.subscription import Subscription
from app.schemas.subscription import SubscriptionCreate, SubscriptionUpdate


def create_subscription(db: Session, subscription: SubscriptionCreate, user_id: int):
    db_subscription = Subscription(**subscription.dict(), user_id=user_id)
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription


def get_user_subscriptions(db: Session, user_id: int):
    return db.query(Subscription).filter(Subscription.user_id == user_id).all()


def get_subscription_by_id(db: Session, subscription_id: int, user_id: int):
    return db.query(Subscription).filter(
        Subscription.id == subscription_id,
        Subscription.user_id == user_id
    ).first()


def update_subscription(db: Session, db_subscription: Subscription, updates: SubscriptionUpdate):
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(db_subscription, key, value)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription


def delete_subscription(db: Session, db_subscription: Subscription):
    db.delete(db_subscription)
    db.commit()
