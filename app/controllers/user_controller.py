from flask import request, redirect, url_for, render_template, flash
from app.models import User
from app import db

def index():
    data = User.query.all()
    return render_template('users/index.html', data=data)