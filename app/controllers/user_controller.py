from flask import request, redirect, url_for, render_template, flash
from app.models import User
from app import db

def index():
    data = User.query.all()
    print(data)
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
        flash('User created successfully!', 'message')
        return redirect(url_for('users.index'))
    
def edit(id):
    data = User.query.get_or_404(id)
    return render_template('users/edit.html', data=data)

def update(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        flash('User updated successfully!', 'message')
        return redirect(url_for('users.index'))
    
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'message')
    return redirect(url_for('users.index'))