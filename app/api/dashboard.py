# app/api/dashboard.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db  # Ensure this points correctly to your DB session
from app.services.dashboard_service import get_dashboard_data

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/", summary="Get dashboard data", response_model=dict)
def dashboard(db: Session = Depends(get_db)):
    """
    Endpoint to fetch dashboard data.
    """
    return get_dashboard_data(db)
