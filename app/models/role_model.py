from app import db
from .base_model import BaseModel

class Role(BaseModel):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    
    # Relationship: One user can have many products
    # products = db.relationship('Product', backref='owner', lazy=True)
    # users = db.relationship('User', backref='Role', lazy=True)
    users = db.relationship('User',
                            backref='role', lazy='dynamic')

    def __repr__(self):
        return f'<Role {self.title}>'
