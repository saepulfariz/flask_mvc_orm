from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
db = SQLAlchemy()

class BaseTable(db.Model):
    __abstract__ = True
    cid = db.Column(db.Integer, nullable=True, default=1, onupdate=2)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now(pytz.timezone('Asia/Jakarta')))
    updated_at = db.Column(
        db.DateTime(), nullable=False,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )
    # created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    # updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    def creatId():
        return 88
    
class User(BaseTable):
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
    
class Product(BaseTable):
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