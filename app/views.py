from flask import Blueprint
from .controllers import get_users

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return get_users()
