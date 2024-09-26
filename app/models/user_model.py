from app import db
from .base_model import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.String(100), default='user.png') 
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', onupdate='CASCADE', ondelete='SET NULL'), nullable=True)
    
    # Relationship: One user can have many products
    # products = db.relationship('Product', backref='owner', lazy=True)
    products = db.relationship('Product', backref='User', lazy=True)
    roles = db.relationship('Role', backref='User', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
