from flask import request, redirect, url_for, render_template, flash
from app.models import User

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

class LoginFrom(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(message="Username tidak boleh kosong."), Length(min=3, max=50,message="Username harus antara 3 sampai 50 karakter.")], 
                           render_kw={"class": "form-control", "placeholder": "Enter your username/Email"})
    password = PasswordField('Password',
                        render_kw={"class": "form-control", "placeholder": "Enter your password"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})

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
            flash('User valid', 'message')
            return redirect(url_for('auth.index'))
        else: 
            flash('User not found', 'message')
            return redirect(url_for('auth.index'))
    else:
        data = {
            'title' : 'Login'
        }
        return render_template('auth/login.html', data=data, form=form) 
