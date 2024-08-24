from flask import request, redirect, url_for, render_template, flash
from app.models import Product
from app import db

def index():
    data = Product.query.all()
    return render_template('products/index.html', data=data)