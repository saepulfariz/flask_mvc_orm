from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from app.middleware.method_spoofer import CustomRequest, MethodSpooferMiddleware

csrf = CSRFProtect()

db = SQLAlchemy()
db_sqlserver = SQLAlchemy()

def create_app(config_class):

    app = Flask(__name__,static_url_path='/static', static_folder='../static')

    # app = Flask(__name__)
    csrf.init_app(app)

    app.request_class = CustomRequest
    app.wsgi_app = MethodSpooferMiddleware(app.wsgi_app)

    app.config.from_object(config_class)
    
    db.init_app(app)

    # Inisialisasi SQL Server dengan bind
    # db_sqlserver.init_app(app)
    
    with app.app_context():
        from . import models, routes

        # from app.views import main

        app.register_blueprint(routes.main, url_prefix='/')
        app.register_blueprint(routes.users, url_prefix='/')
        app.register_blueprint(routes.products, url_prefix='/')
        # app.register_blueprint(views.main, url_prefix='/')
        # app.register_blueprint(views.user, url_prefix='/')
        # app.register_blueprint(views.product, url_prefix='/')

        db.create_all()
    
    return app
