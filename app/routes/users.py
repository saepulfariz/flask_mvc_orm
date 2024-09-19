from flask import Blueprint
from app.controllers import product_controller,home_controller,user_controller
from app.middleware.auth import login_required

users = Blueprint('users', __name__)



# User routes
@users.route('/users', methods=['GET'])
@login_required
def index():
    return user_controller.index()

@users.route('/users/new', methods=['GET'])
def new():
    return user_controller.new()

@users.route('/users', methods=['POST'])
def create():
    return user_controller.create()

@users.route('/users/<int:id>/edit', methods=['GET'])
def edit(id):
    return user_controller.edit(id)

@users.route('/users/<int:id>', methods=['PUT', 'PATCH'])
def update(id):
    return user_controller.update(id)

@users.route('/users/<int:id>', methods=['DELETE'])
def delete(id):
    return user_controller.delete(id)