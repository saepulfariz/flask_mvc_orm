from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from app.config.config import Config

from flask_migrate import Migrate

import os
from dotenv import load_dotenv
load_dotenv()


from app.middleware.method_spoofer import CustomRequest, MethodSpooferMiddleware

csrf = CSRFProtect()

db = SQLAlchemy()

app = Flask(__name__,static_url_path='/static', static_folder='../static',template_folder='views')

# app = Flask(__name__)
csrf.init_app(app)

app.request_class = CustomRequest
app.wsgi_app = MethodSpooferMiddleware(app.wsgi_app)

app.config.from_object(Config)
    
db.init_app(app)


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

app_host = os.getenv('FLASK_RUN_HOST')
app_port = os.getenv('FLASK_RUN_PORT')
app_debug = os.getenv('FLASK_DEBUG')
app_name = os.getenv('FLASK_APP')
app_reverse_proxy = os.getenv('FLASK_REVERSE_PROXY')

migrate = Migrate() #define migration

migrate.init_app(app,db) #initiate migration

# app.register_blueprint(main, url_prefix='/')

if __name__ == '__main__':
    # with app.app_context():
    #     # Inisialisasi database atau tugas lain yang membutuhkan app context
    #     db.create_all()

    app.run(app_host, app_port, app_debug)


