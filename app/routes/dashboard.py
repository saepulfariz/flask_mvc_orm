from flask import Blueprint
from app.controllers import dashboard_controller

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def index():
    return dashboard_controller.index()