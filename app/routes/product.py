from flask import Blueprint
from app.controllers import product_controller,home_controller,user_controller

product = Blueprint('product', __name__)


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