from flask import request, redirect, url_for, render_template, flash, session
from app.models import User
from app import db
from app.helpers.custom_helper import setAlert

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo

from passlib.hash import pbkdf2_sha256

class LoginFrom(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(message="Username tidak boleh kosong."), Length(min=3, max=50,message="Username harus antara 3 sampai 50 karakter.")], 
                           render_kw={"class": "form-control", "placeholder": "Enter your username/Email"})
    password = PasswordField('Password',
                        render_kw={"class": "form-control", "placeholder": "Enter your password"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})

class RegisterForm(FlaskForm):
    name = StringField('Name', 
                        validators=[DataRequired()], 
                        render_kw={"class": "form-control", "placeholder": "Enter your name"})
    username = StringField('Username', 
                           validators=[DataRequired(message="Username tidak boleh kosong."), Length(min=3, max=50,message="Username harus antara 3 sampai 50 karakter.")], 
                           render_kw={"class": "form-control", "placeholder": "Enter your username/Email"})
    password = PasswordField('Password',
                             validators=[ Length(min=3,message="Password min 3")],
                        render_kw={"class": "form-control", "placeholder": "Enter your password"})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[EqualTo(fieldname="password", message="Password harus sama"), Length(min=3,message="Password min 3")],
                        render_kw={"class": "form-control", "placeholder": "Confirm your password"})
    email = StringField('Email', 
                        validators=[DataRequired(), Email()], 
                        render_kw={"class": "form-control", "placeholder": "Enter your email"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email sudah digunakan. Silakan pilih email lain.')
        
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username sudah digunakan. Silakan pilih username lain.')

def index() :
    form = LoginFrom()
    data = {
        'title' : 'Login'
    }
    return render_template('auth/login.html', data=data, form=form) 

def verify() : 
    form = LoginFrom()
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']

        # data = User.query.filter_by(username=username).first()
        data = User.query.filter(
            (User.username ==username) | (User.email== username)
        ).first()
        if data : 
            hash = data.password

            if (pbkdf2_sha256.verify(password, hash)) :
                session['id'] = data.id
                session['username'] = username
                session['role_id'] = data.role_id
                # flash('User valid', 'message')
                setAlert('success', 'Success', 'User login')
                return redirect(url_for('dashboard.index'))
            else:
                # flash('Password wrong', 'message')
                setAlert('warning', 'Warning', 'Password wrong')
                return redirect(url_for('auth.index'))
                                 
        else: 
            # flash('User not found', 'message')
            setAlert('warning', 'Warning', 'User not found')
            return redirect(url_for('auth.index'))
    else:
        data = {
            'title' : 'Login'
        }
        return render_template('auth/login.html', data=data, form=form) 
    
def register() :
    form = RegisterForm()
    data = {
        'title' : 'Register'
    }
    return render_template('auth/register.html', data=data, form=form) 

def registered() : 
    form = RegisterForm()
    if form.validate_on_submit():
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role_id = 2
        password = pbkdf2_sha256.hash(password)
        user = User(name=name,username=username, email=email, password=password, role_id=role_id)
        db.session.add(user)
        db.session.commit()
        # flash('User created successfully!, please login.', 'message')
        setAlert('success', 'Success', 'User created successfully!, please login.')
        return redirect(url_for('auth.index'))
    else: 
        data = {
            'title' : 'Register'
        }
        return render_template('auth/register.html', data=data, form=form) 
    
def logout() : 
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('auth.index'))
