from flask import request, redirect, url_for, render_template, flash

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
