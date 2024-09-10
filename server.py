from app import create_app, db
from config import Config
from flask_migrate import Migrate

# from app.views import main

app = create_app(Config)

migrate = Migrate() #define migration

migrate.init_app(app,db) #initiate migration

# app.register_blueprint(main, url_prefix='/')

if __name__ == '__main__':
    # with app.app_context():
    #     # Inisialisasi database atau tugas lain yang membutuhkan app context
    #     db.create_all()
    app.run(debug=True)
