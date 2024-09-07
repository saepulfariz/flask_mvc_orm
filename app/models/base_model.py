from datetime import datetime
from app import db

class BaseModel(db.Model):
    __abstract__ = True  # Ini membuat SQLAlchemy tidak membuat tabel untuk BaseModel

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<{self.__class__.__name__} created_at={self.created_at} updated_at={self.updated_at}>"
