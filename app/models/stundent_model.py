from app import db
from .base_model import BaseModel

class Student(BaseModel):
    __tablename__ = 'students'
    __bind_key__ = 'sqlite'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    

    def __repr__(self):
        return f'<User {self.name}>'
