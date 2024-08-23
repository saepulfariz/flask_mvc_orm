from flask import Blueprint
from app.controllers import home_controller

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return home_controller.index()
