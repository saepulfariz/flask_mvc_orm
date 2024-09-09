from flask import Blueprint
from app.controllers import product_controller,home_controller,user_controller

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return home_controller.index()