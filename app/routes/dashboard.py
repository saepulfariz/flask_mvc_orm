from flask import Blueprint
from app.controllers import dashboard_controller
from app.middleware.auth import login_required

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
@login_required()
def index():
    return dashboard_controller.index()