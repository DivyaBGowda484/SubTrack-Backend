# app/api/expense.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db  # Correct import for the DB session
from app.schemas.expense_schemas import ExpenseCreate, ExpenseOut
from app.services.expense_service import ExpenseService

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

@router.post("/", response_model=ExpenseOut, summary="Add a new expense")
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    """
    Add a new expense entry to the database.
    """
    try:
        return ExpenseService.add_expense(db, expense)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
