from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask.cli import with_appcontext, AppGroup
import click

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
    app.register_blueprint(routes.auth, url_prefix='/auth')

    db.create_all()


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    data = {
        'title' : 'Token is required'
    }
    return render_template('errors/csrf.html', reason=e.description, data=data), 400

app_host = os.getenv('FLASK_RUN_HOST')
app_port = os.getenv('FLASK_RUN_PORT')
app_debug = os.getenv('FLASK_DEBUG')
app_name = os.getenv('FLASK_APP')
app_reverse_proxy = os.getenv('FLASK_REVERSE_PROXY')

migrate = Migrate() #define migration

migrate.init_app(app,db) #initiate migration

# app.register_blueprint(main, url_prefix='/')

import importlib

def register_commands(app):
    """Fungsi untuk memuat semua file di folder 'command'"""
    command_folder = os.path.join(os.path.dirname(__file__), 'command')

    # Loop melalui semua file di folder 'command'
    for filename in os.listdir(command_folder):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            module = importlib.import_module(f'app.command.{module_name}')

            # Cari semua command di file tersebut
            for attr in dir(module):
                command = getattr(module, attr)
                # Periksa apakah atribut adalah instance dari AppGroup (CLI command)
                if isinstance(command, AppGroup):
                    # Tambahkan command ke Flask app
                    app.cli.add_command(command)

# Panggil fungsi untuk register semua command
register_commands(app)

@app.cli.command("create-user")
@click.argument("name")
def create_user(name):
    print('Nama : '+name)

@app.cli.command("migrate:refresh")
def migrate_refresh():
    # Hapus semua data dari tabel (opsional)
    print(f"Migrate Rollback Success.")
    db.drop_all()

    # Buat ulang tabel-tabel (opsional)
    print(f"Migrate All Success.")
    db.create_all()

@app.cli.command("migrate")
def migrate():
    print(f"Migrate All Success.")
    db.create_all()

@app.cli.command("migrate:rollback")
def migrate_rollback():
    print(f"Migrate Rollback Success.")
    db.drop_all()

@app.cli.command("db:seed")
@click.argument("name", required=False)
def seed_all(name = None):
    """Menjalankan semua seeder"""
    seeder_folder = os.path.join(os.path.dirname(__file__), 'seeder')

    # Memuat semua file seeder
    for filename in os.listdir(seeder_folder):
        if filename.endswith('_seeder.py'):
            module_name = filename[:-3]  # Menghilangkan .py dari nama file
            module = __import__(f'app.seeder.{module_name}', fromlist=['run'])
            
            if name is None :
                # Menjalankan fungsi `run` dari setiap file seeder
                if hasattr(module, 'run'):
                    print(f"Running seeder: {module_name}")
                    module.run()
                else:
                    print(f"Seeder {module_name} does not have a 'run' function")
            elif (name == module_name) : 
                # Menjalankan fungsi `run` dari setiap file seeder
                if hasattr(module, 'run'):
                    print(f"Running seeder: {module_name}")
                    module.run()
                else:
                    print(f"Seeder {module_name} does not have a 'run' function")


if __name__ == '__main__':
    # with app.app_context():
    #     # Inisialisasi database atau tugas lain yang membutuhkan app context
    #     db.create_all()

    app.run(app_host, app_port, app_debug)


