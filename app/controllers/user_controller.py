from flask import request, redirect, url_for, render_template, flash
from app.models import User, Student, PcsModel
from app import db

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, PasswordField
from wtforms.validators import DataRequired, Length, Email

from passlib.hash import pbkdf2_sha256

class UserForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(message="Username tidak boleh kosong."), Length(min=3, max=50,message="Username harus antara 3 sampai 50 karakter.")], 
                           render_kw={"class": "form-control", "placeholder": "Enter your username"})
    email = StringField('Email', 
                        validators=[DataRequired(), Email()], 
                        render_kw={"class": "form-control", "placeholder": "Enter your email"})
    password = PasswordField('Password', 
                        validators=[DataRequired(), Length(min=3, max=50,message="Password harus antara 3 sampai 50 karakter.")], 
                        render_kw={"class": "form-control", "placeholder": "Enter your password"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})

    def __init__(self, original_username=None, original_email=None, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email

    # Custom validator untuk memastikan username unik
    def validate_username(self, username):
        # Jika mode edit dan username tidak berubah, tidak perlu validasi unik
        if self.original_username and self.original_username == username.data:
            return
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username sudah digunakan. Silakan pilih username lain.')

    # Custom validator untuk memastikan email unik
    def validate_email(self, email):
        # Jika mode edit dan email tidak berubah, tidak perlu validasi unik
        if self.original_email and self.original_email == email.data:
            return
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email sudah digunakan. Silakan pilih email lain.')

def index():
    form = FlaskForm()
    data = User.query.all()
    print(Student.query.all())
    print(Student.get_student())
    # print(PcsModel.getProductionData('V01'))
    students = Student.get_student()
    return render_template('users/index.html', data=data, students = students, form=form)

def new():
    form = UserForm()
    return render_template('users/new.html', form=form)

def create():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            password = pbkdf2_sha256.hash(password)
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            flash('User created successfully!', 'message')
            return redirect(url_for('users.index'))
        else:
            return render_template('users/new.html', form=form)
    
def edit(id):
    data = User.query.get_or_404(id)
    form = UserForm(original_username=data.username, original_email=data.email)
    return render_template('users/edit.html', data=data, form=form)

def update(id):
    user = User.query.get_or_404(id)
    form = UserForm(original_username=user.username, original_email=user.email)
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