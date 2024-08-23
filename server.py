from app import create_app, db
from config import MySQLConfig
from flask_migrate import Migrate

# from app.views import main

app = create_app(MySQLConfig)

migrate = Migrate() #define migration

migrate.init_app(app,db) #initiate migration

# app.register_blueprint(main, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
