from flask import Blueprint
from app.controllers import product_controller
from app.middleware.auth import login_required

products = Blueprint('products', __name__)


@products.route('/products', methods=['GET'])
@login_required
def index():
    return product_controller.index()

@products.route('/products/new', methods=['GET'])
@login_required
def new():
    return product_controller.new()

@products.route('/products', methods=['POST'])
@login_required
def create():
    return product_controller.create()

@products.route('/products/<int:id>/edit', methods=['GET'])
@login_required
def edit(id):
    return product_controller.edit(id)

@products.route('/products/<int:id>',  methods=['PUT', 'PATCH'])
@login_required
def update(id):
    return product_controller.update(id)

@products.route('/products/<int:id>', methods=['DELETE'])
@login_required
def delete(id):
    return product_controller.delete(id)