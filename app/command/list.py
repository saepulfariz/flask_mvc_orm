from flask.cli import AppGroup

# Membuat AppGroup untuk perintah 'list'
list_cli = AppGroup('list')

@list_cli.command('app')
def list_command():
    print('LIST COMMAND')