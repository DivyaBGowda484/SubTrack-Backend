from sqlalchemy.orm import Session
from app.db.models.expense import Expense
from app.schemas.expense import ExpenseCreate

class ExpenseService:
    @staticmethod
    def add_expense(db: Session, data: ExpenseCreate):
        new_expense = Expense(**data.dict())
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)
        return new_expense