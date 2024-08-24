from flask import request, redirect, url_for, render_template, flash
from app.models import Product
from app import db

def index():
    data = Product.query.all()
    return render_template('products/index.html', data=data)

def new():
    return render_template('products/new.html')

def create():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']
        product = Product(name=name, price=price, stock=stock)
        db.session.add(product)
        db.session.commit()
        flash('Product created successfully!')
        return redirect(url_for('product.index'))
    
def edit(id):
    data = Product.query.get_or_404(id)
    return render_template('products/edit.html', data=data)

def update(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = request.form['price']
        product.stock = request.form['stock']
        db.session.commit()
        flash('Product updated successfully!')
        return redirect(url_for('product.index'))