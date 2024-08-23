from flask import render_template
from .models import User

def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)
