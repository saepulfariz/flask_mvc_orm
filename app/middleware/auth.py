from functools import wraps
from flask import Flask, request, redirect, url_for, session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'id' not in session:
            return redirect(url_for('auth.index'))
        return f(*args, **kwargs)
    return decorated_function