from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    
    with app.app_context():
        from . import models, routes

        # from app.views import main

        app.register_blueprint(routes.main, url_prefix='/')
        app.register_blueprint(routes.user, url_prefix='/')
        app.register_blueprint(routes.products, url_prefix='/')
        # app.register_blueprint(views.main, url_prefix='/')
        # app.register_blueprint(views.user, url_prefix='/')
        # app.register_blueprint(views.product, url_prefix='/')

        db.create_all()
    
    return app
