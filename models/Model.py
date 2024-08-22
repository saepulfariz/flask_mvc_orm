from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True  # Ini membuat SQLAlchemy tidak membuat tabel untuk BaseModel
    cid = db.Column(db.Integer, nullable=True, default=1, onupdate=2)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now(pytz.timezone('Asia/Jakarta')))
    updated_at = db.Column(
        db.DateTime(), nullable=False,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )
    # created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    # updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<{self.__class__.__name__} created_at={self.created_at} updated_at={self.updated_at}>"
    
    def creatId():
        return 88