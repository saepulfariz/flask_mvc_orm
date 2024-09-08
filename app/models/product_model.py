from app import db
from .base_model import BaseModel
from sqlalchemy import text 

class Product(BaseModel):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    
    # Foreign key to associate product with user
    # default onupdate and ondelete RESTRICT
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # ForeignKey dengan onupdate CASCADE dan ondelete SET NULL
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', onupdate='CASCADE', ondelete='SET NULL'), nullable=True)
    
    user = db.relationship('Users', backref=db.backref('products', lazy=True))

    def __repr__(self):
        return f'<Product {self.name}>'
    
    @staticmethod
    def get_products_with_owners():
        sql_query = """
        SELECT products.id, products.name, products.price, products.stock, users.username 
        FROM products 
        JOIN users ON products.user_id = users.id
        """

        sql_query = text(sql_query)
        
        result = db.session.execute(sql_query)
        return result.fetchall()
