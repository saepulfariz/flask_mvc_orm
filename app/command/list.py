from flask.cli import AppGroup
from flask import current_app as app

# Membuat AppGroup untuk perintah 'list'
list_cli = AppGroup('list',short_help="List Command")

@list_cli.command('app')
# @app.cli.command('list')
def list_command():
    # kalau single nampil, kalau pake AppGroup Pake short_help
    """Menampilkan list command"""
    print('LIST COMMAND')