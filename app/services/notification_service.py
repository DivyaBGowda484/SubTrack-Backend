from sqlalchemy.orm import Session
from app.models.notification_model import Notification

class NotificationService:
    @staticmethod
    def get_all(db: Session):
        return db.query(Notification).all()