from flask import Blueprint
from app.controllers import product_controller,home_controller,user_controller

products = Blueprint('products', __name__)


@products.route('/products', methods=['GET'])
def index():
    return product_controller.index()

@products.route('/products/new', methods=['GET'])
def new():
    return product_controller.new()

@products.route('/products', methods=['POST'])
def create():
    return product_controller.create()

@products.route('/products/<int:id>/edit', methods=['GET'])
def edit(id):
    return product_controller.edit(id)

@products.route('/products/<int:id>',  methods=['PUT', 'PATCH'])
def update(id):
    return product_controller.update(id)

@products.route('/products/<int:id>', methods=['DELETE'])
def delete(id):
    return product_controller.delete(id)