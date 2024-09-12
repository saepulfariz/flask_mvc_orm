from flask import request, redirect, url_for, render_template, flash
from app.models import User, Student, PcsModel
from app import db

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])

def index():
    data = User.query.all()
    print(Student.query.all())
    print(Student.get_student())
    print(PcsModel.getProductionData('V01'))
    students = Student.get_student()
    return render_template('users/index.html', data=data, students = students)

def new():
    form = UserForm()
    return render_template('users/new.html', form=form)

def create():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form['username']
            email = request.form['email']
            user = User(username=username, email=email)
            db.session.add(user)
            db.session.commit()
            flash('User created successfully!', 'message')
            return redirect(url_for('users.index'))
        else:
            return render_template('users/new.html', form=form)
    
def edit(id):
    form = UserForm()
    data = User.query.get_or_404(id)
    return render_template('users/edit.html', data=data, form=form)

def update(id):
    form = UserForm()
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        if form.validate_on_submit():
            user.username = request.form['username']
            user.email = request.form['email']
            db.session.commit()
            flash('User updated successfully!', 'message')
            return redirect(url_for('users.index'))
        else:
            data = User.query.get_or_404(id)
            return render_template('users/edit.html', data=data, form=form)
    
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'message')
    return redirect(url_for('users.index'))