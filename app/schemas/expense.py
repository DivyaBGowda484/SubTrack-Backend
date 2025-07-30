from pydantic import BaseModel
from typing import Optional
from datetime import date


class ExpenseBase(BaseModel):
    name: str
    amount: float
    date: date
    category: Optional[str] = None
    payment_method: Optional[str] = None


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[date] = None
    category: Optional[str] = None
    payment_method: Optional[str] = None


class ExpenseOut(ExpenseBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
