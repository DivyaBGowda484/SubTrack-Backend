from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.dashboard_service import get_dashboard_data

router = APIRouter()

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    return get_dashboard_data(db)