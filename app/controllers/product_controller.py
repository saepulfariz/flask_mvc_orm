from flask import request, redirect, url_for, render_template, flash
from app.models import Product, User
from app import db
from sqlalchemy import text 
from app.helpers.custom_helper import setAlert

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField, FloatField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length

class ProductForm(FlaskForm):
    name = StringField('Name', 
                           validators=[DataRequired(message="Name tidak boleh kosong."), Length(min=3, max=50,message="Name harus antara 3 sampai 50 karakter.")], 
                           render_kw={"class": "form-control", "placeholder": "Enter your Name"})
    price = DecimalField('Price', 
                        validators=[DataRequired()], 
                        render_kw={"class": "form-control", "placeholder": "Enter your price"})
    stock = IntegerField('Stock', 
                        validators=[DataRequired()], 
                        render_kw={"class": "form-control", "placeholder": "Enter your stock"})
    user_id = SelectField('Pilih User', choices=[], coerce=int, validate_choice=False, validators=[DataRequired()])
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})

    def validate_user_id(self, field):
        user = User.query.get(field.data)
        if not user:
            raise ValidationError('User tidak valid. Silakan pilih user yang benar.')

def index():
    form = FlaskForm()
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

    # query native in model
    data = Product.get_products_with_owners()

    data = Product.query.all()

    data = {
        'title' : 'View products',
        'data' : data
    }

    return render_template('products/index.html', data=data, form=form)

def new():
    form = ProductForm()
    data = {
        'title' : 'New product',
        'users' : User.query.all()
    }
    # Isi pilihan SelectField dengan user.id dan user.username
    form.user_id.choices = [(user.id, user.username) for user in data['users']]
    return render_template('products/new.html', data=data, form=form)

def create():
    form = ProductForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form['name']
            price = request.form['price']
            stock = request.form['stock']
            user_id = request.form['user_id']
            product = Product(name=name, price=price, stock=stock,user_id=user_id )
            db.session.add(product)
            db.session.commit()
            # flash('Product created successfully!', 'message')
            setAlert('success', 'Success', 'Add Success')
            return redirect(url_for('products.index'))
        else:
            data = {
                'users' : User.query.all()
            }
            # Isi pilihan SelectField dengan user.id dan user.username
            form.user_id.choices = [(user.id, user.username) for user in data['users']]
            return render_template('products/new.html', data=data, form=form)
    
def edit(id):
    result = Product.query.get_or_404(id)
    form = ProductForm()
    data = {
        'title' : 'Edit product',
        'users' : User.query.all(),
        'data' : result
    }
    form.user_id.choices = [(user.id, user.username) for user in data['users']]
    form.user_id.data = result.user_id  # Pre-select pilihan dropdown
    return render_template('products/edit.html', data=data, form=form)

def update(id):
    product = Product.query.get_or_404(id)
    form = ProductForm()
    if form.validate_on_submit():
        product.name = request.form['name']
        product.price = request.form['price']
        product.stock = request.form['stock']
        product.user_id = request.form['user_id']
        db.session.commit()
        # flash('Product updated successfully!', 'message')
        setAlert('success', 'Success', 'Edit Success')
        return redirect(url_for('products.index'))
    else:
        result = Product.query.get_or_404(id)
        data = {
            'users' : User.query.all(),
            'data' : result
        }
        return render_template('products/edit.html', data=data, form=form)
    
def delete(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    # flash('Product deleted successfully!', 'message')
    setAlert('success', 'Success', 'Delete Success')
    return redirect(url_for('products.index'))