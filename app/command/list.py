from flask.cli import AppGroup
from flask import current_app as app

from colorama import Fore, Back, Style

# Membuat AppGroup untuk perintah 'list'
list_cli = AppGroup('list',short_help="List Command (flask list app)")

@list_cli.command('app')
# @app.cli.command('list')
def list_command():
    # kalau single nampil, kalau pake AppGroup Pake short_help
    """Menampilkan list command"""
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')