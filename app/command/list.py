from flask.cli import AppGroup
import click
from flask import current_app as app

from colorama import Fore, Back, Style

# Membuat AppGroup untuk perintah 'list'
list_cli = AppGroup('list',short_help="List Command (flask list app)")

@list_cli.command('default')
def list_default():
    """Menampilkan default command"""
    print('Default command list')

@list_cli.command('app')
# @app.cli.command('list')
def list_app():
    # kalau single nampil, kalau pake AppGroup Pake short_help
    """Menampilkan list command"""
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')

@list_cli.command('data')
@click.argument("name", required=False)
def list_data(name = None):
    """Menampilkan data"""
    name = "None" if (name is None) else name
    print('data '+ name)