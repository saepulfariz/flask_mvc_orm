from flask_sqlalchemy import SQLAlchemy
from Model import BaseModel
db = SQLAlchemy()

class Product(BaseModel):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    price = db.Column(db.Float(13))

    # Foreign key to associate product with user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }