from flask import Blueprint
from app.controllers import auth_controller

auth = Blueprint('auth', __name__)


@auth.route('/')
def index():
    return auth_controller.index()