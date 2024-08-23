from app import create_app
from config import MySQLConfig

# from app.views import main

app = create_app(MySQLConfig)

# app.register_blueprint(main, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
