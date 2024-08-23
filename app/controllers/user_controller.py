from flask import request, redirect, url_for, render_template, flash
from app.models import User
from app import db

def index():
    data = User.query.all()
    return render_template('users/index.html', data=data)

def new():
    return render_template('users/new.html')

def create():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        flash('User created successfully!')
        return redirect(url_for('user.index'))