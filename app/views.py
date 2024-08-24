from flask import Blueprint
from app.controllers import product_controller,home_controller,user_controller

main = Blueprint('main', __name__)
user = Blueprint('user', __name__)
product = Blueprint('product', __name__)

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

@user.route('/users/<int:id>/delete', methods=['POST'])
def delete(id):
    return user_controller.delete(id)


@product.route('/products', methods=['GET'])
def index():
    return product_controller.index()

@product.route('/products/new', methods=['GET'])
def new():
    return product_controller.new()

@product.route('/products', methods=['POST'])
def create():
    return product_controller.create()

@product.route('/products/<int:id>/edit', methods=['GET'])
def edit(id):
    return product_controller.edit(id)

@product.route('/products/<int:id>', methods=['POST'])
def update(id):
    return product_controller.update(id)

@product.route('/products/<int:id>/delete', methods=['POST'])
def delete(id):
    return product_controller.delete(id)