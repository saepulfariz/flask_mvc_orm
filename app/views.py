from flask import Blueprint
from app.controllers import home_controller,user_controller

main = Blueprint('main', __name__)
user = Blueprint('user', __name__)

@main.route('/')
def index():
    return home_controller.index()

# User routes
@user.route('/users', methods=['GET'])
def index():
    return user_controller.index()

@user.route('/users/new', methods=['GET'])
def new():
    return user_controller.new()

@user.route('/users', methods=['POST'])
def create():
    return user_controller.create()

@user.route('/users/<int:id>/edit', methods=['GET'])
def edit(id):
    return user_controller.edit(id)

@user.route('/users/<int:id>', methods=['POST'])
def update(id):
    return user_controller.update(id)