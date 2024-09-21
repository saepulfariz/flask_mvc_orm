from flask import Blueprint
from app.controllers import auth_controller

auth = Blueprint('auth', __name__)


@auth.route('/')
def index():
    return auth_controller.index()

@auth.route('/',  methods=['POST'])
def verify():
    return auth_controller.verify()

@auth.route('/register')
def register():
    return auth_controller.register()

@auth.route('/logout',  methods=['GET'])
def logout():
    return auth_controller.logout()