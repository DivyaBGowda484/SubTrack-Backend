from pydantic import BaseModel
from typing import Optional
from datetime import date


class SubscriptionBase(BaseModel):
    name: str
    amount: float
    billing_cycle: str  # e.g., monthly, yearly
    next_billing_date: date
    category: Optional[str] = None
    payment_method: Optional[str] = None


class SubscriptionCreate(SubscriptionBase):
    pass


class SubscriptionUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[float] = None
    billing_cycle: Optional[str] = None
    next_billing_date: Optional[date] = None
    category: Optional[str] = None
    payment_method: Optional[str] = None


class SubscriptionOut(SubscriptionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
