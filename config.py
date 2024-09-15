import os

import os
from dotenv import load_dotenv
load_dotenv()

default_hostname = os.environ['database.default.hostname']
default_database = os.environ['database.default.database']
default_username = os.environ['database.default.username']
default_password = os.environ['database.default.password']

class Config:
    # Konfigurasi untuk MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+default_username+':'+default_password+'@'+default_hostname+'/'+default_database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SECRET_KEY = os.urandom(32)
    SECRET_KEY = 'APP_FLASK'

    # Random data for generating secure tokens. If this is not set then SECRET_KEY is used.
    WTF_CSRF_SECRET_KEY= 'APP_FLASK'

    # Set to False to disable all CSRF protection. Default is True.
    WTF_CSRF_ENABLED = True

    # When using the CSRF protection extension, this controls whether every view is protected by default. Default is True.
    WTF_CSRF_CHECK_DEFAULT = True

    # HTTP methods to protect from CSRF. Default is {'POST', 'PUT', 'PATCH', 'DELETE'}.
    WTF_CSRF_METHODS = {'POST', 'PUT', 'PATCH', 'DELETE'}

    # Name of the form field and session key that holds the CSRF token. Default is csrf_token.
    # call default {{ form.csrf_token }}
    # call custom field {{ form.csrf_token_sae }}
    # WTF_CSRF_FIELD_NAME = 'csrf_token_sae'
    WTF_CSRF_FIELD_NAME = 'csrf_token'

    # HTTP headers to search for CSRF token when it is not provided in the form. Default is ['X-CSRFToken', 'X-CSRF-Token'].
    WTF_CSRF_HEADERS = ['X-CSRFToken', 'X-CSRF-Token']

    # Max age in seconds for CSRF tokens. Default is 3600. If set to None, the CSRF token is valid for the life of the session.
    WTF_CSRF_TIME_LIMIT = 3600

    # Whether to enforce the same origin policy by checking that the referrer matches the host. Only applies to HTTPS requests. Default is True.
    WTF_CSRF_SSL_STRICT = True

    # Set to False to disable Flask-Babel I18N support. Also set to False if you want to use WTForms’s built-in messages directly, see more info here. Default is True.
    WTF_I18N_ENABLED = True

    # Konfigurasi untuk SQL Server
    SQLALCHEMY_BINDS = {
        # 'sqlserver': 'mssql+pyodbc://Traceability:ability@172.21.202.142/PCS?driver=ODBC+Driver+17+for+SQL+Server',
        'sqlserver': 'sqlite:///app.db',
        'sqlite': 'sqlite:///app.db'
    }