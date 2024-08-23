from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    
    with app.app_context():
        from . import models, views

        # from app.views import main

        app.register_blueprint(views.main, url_prefix='/')

        db.create_all()
    
    return app
