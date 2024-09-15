from app import create_app, db
from config import Config
from flask_migrate import Migrate

# from app.views import main

app = create_app(Config)

import os
from dotenv import load_dotenv
load_dotenv()

app_host = os.environ['FLASK_RUN_HOST']
app_port = os.environ['FLASK_RUN_PORT']
app_debug = os.environ['FLASK_DEBUG']
app_name = os.environ['FLASK_APP']
app_reverse_proxy = os.environ['FLASK_REVERSE_PROXY']

migrate = Migrate() #define migration

migrate.init_app(app,db) #initiate migration

# app.register_blueprint(main, url_prefix='/')

if __name__ == '__main__':
    # with app.app_context():
    #     # Inisialisasi database atau tugas lain yang membutuhkan app context
    #     db.create_all()

    app.run(app_host, app_port, app_debug)
