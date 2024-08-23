from flask import Blueprint
from app.controllers import home_controller,user_controller

main = Blueprint('main', __name__)
user = Blueprint('user', __name__)

@main.route('/')
def index():
    return home_controller.index()

# User routes
@user.route('/users')
def get_users():
    return user_controller.index()
