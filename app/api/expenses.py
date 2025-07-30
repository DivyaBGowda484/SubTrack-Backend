from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.expense_schemas import ExpenseCreate, ExpenseOut
from app.services.expense_service import ExpenseService

router = APIRouter()

@router.post("/expenses", response_model=ExpenseOut)
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return ExpenseService.add_expense(db, expense)