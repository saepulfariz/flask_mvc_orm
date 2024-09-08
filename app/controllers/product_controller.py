from flask import request, redirect, url_for, render_template, flash
from app.models import Product, User
from app import db
from sqlalchemy import text 

def index():
    # data = Product.query.all()
   
    # data = db.session.query(User.username, Product).join(Product).all()
    # data = db.session.query(User, Product).join(Product).filter(User.id == user_id).all()
    # data = db.session.query(Product.id, Product.name,Product.price, Product.stock,User.username).join(User).all()

    # sql_query = """SELECT * FROM products"""
    sql_query = """ SELECT products.id, products.name, products.price, products.stock, users.username FROM products JOIN users ON products.user_id = users.id """
    sql_query = text(sql_query)
    
    # Execute the raw SQL query
    result = db.session.execute(sql_query)
    
    # Fetch all rows from the result
    data = result.fetchall()

    return render_template('products/index.html', data=data)

def new():
    data = {
        'users' : User.query.all()
    }
    return render_template('products/new.html', data=data)

def create():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']
        user_id = request.form['user_id']
        product = Product(name=name, price=price, stock=stock,user_id=user_id )
        db.session.add(product)
        db.session.commit()
        flash('Product created successfully!')
        return redirect(url_for('product.index'))
    
def edit(id):
    result = Product.query.get_or_404(id)
    data = {
        'users' : User.query.all(),
        'data' : result
    }
    return render_template('products/edit.html', data=data)

def update(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = request.form['price']
        product.stock = request.form['stock']
        product.user_id = request.form['user_id']
        db.session.commit()
        flash('Product updated successfully!')
        return redirect(url_for('product.index'))
    
def delete(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!')
    return redirect(url_for('product.index'))