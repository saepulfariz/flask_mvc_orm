from flask_sqlalchemy import SQLAlchemy
from Model import BaseModel
db = SQLAlchemy()


class User(BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Float(13))
    address = db.Column(db.String(120))

    # Relationship: One user can have many products
    products = db.relationship('Products', backref='owner', lazy=True)


    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'address': self.address,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }