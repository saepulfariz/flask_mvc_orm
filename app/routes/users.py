from flask import Blueprint
from app.controllers import product_controller,home_controller,user_controller
from app.middleware.auth import login_required

users = Blueprint('users', __name__)



# User routes
@users.route('/users', methods=['GET'])
@login_required(role=1)
def index():
    return user_controller.index()

@users.route('/users/new', methods=['GET'])
@login_required(role=1)
def new():
    return user_controller.new()

@users.route('/users', methods=['POST'])
@login_required(role=1)
def create():
    return user_controller.create()

@users.route('/users/<int:id>/edit', methods=['GET'])
@login_required(role=1)
def edit(id):
    return user_controller.edit(id)

@users.route('/users/<int:id>', methods=['PUT', 'PATCH'])
@login_required(role=1)
def update(id):
    return user_controller.update(id)

@users.route('/users/<int:id>', methods=['DELETE'])
@login_required(role=1)
def delete(id):
    return user_controller.delete(id)

@users.route('/change-password', methods=['GET'])
@login_required()
def change_password():
    return user_controller.change_password()

@users.route('/change-password', methods=['PUT'])
@login_required()
def update_password():
    return user_controller.update_password()

@users.route('/profile', methods=['GET'])
@login_required()
def profile():
    return user_controller.profile()

@users.route('/profile/edit', methods=['GET'])
@login_required()
def edit_profile():
    return user_controller.edit_profile()

@users.route('/profile', methods=['PUT'])
@login_required()
def update_profile():
    return user_controller.update_profile()