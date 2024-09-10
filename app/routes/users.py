from flask import Blueprint
from app.controllers import product_controller,home_controller,user_controller

users = Blueprint('users', __name__)



# User routes
@users.route('/users', methods=['GET'])
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

@users.route('/users/<int:id>', methods=['POST'])
def update(id):
    return user_controller.update(id)

@users.route('/users/<int:id>/delete', methods=['POST'])
def delete(id):
    return user_controller.delete(id)