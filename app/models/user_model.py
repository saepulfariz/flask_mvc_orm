from app import db
from .base_model import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Relationship: One user can have many products
    # products = db.relationship('Product', backref='owner', lazy=True)
    products = db.relationship('Product', backref='User', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
