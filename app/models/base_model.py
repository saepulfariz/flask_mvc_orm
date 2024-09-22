from datetime import datetime
from pytz import timezone
from app import db

# Zona waktu GMT+7
tz = timezone('Asia/Jakarta')

class BaseModel(db.Model):
    __abstract__ = True  # Ini membuat SQLAlchemy tidak membuat tabel untuk BaseModel

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(tz))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(tz), onupdate=lambda: datetime.now(tz))

    def __repr__(self):
        return f"<{self.__class__.__name__} created_at={self.created_at} updated_at={self.updated_at}>"
