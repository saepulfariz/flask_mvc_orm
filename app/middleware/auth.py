from functools import wraps
from flask import Flask, request, redirect, url_for, session, abort
from app.models import User

def login_required(role=None):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'id' not in session:
                return redirect(url_for('auth.index'))
            
            id = session['id']
            
            user_data = User.query.get_or_404(id)
            if user_data is None:
                return redirect(url_for('auth.index'))
            
            if role and user_data.role_id != role:
                return abort(403)  # Forbidden access
            
            return f(*args, **kwargs)
        return decorated_function
    return wrapper