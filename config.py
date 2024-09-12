import os

class Config:
    # Konfigurasi untuk MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask_mvc_orm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SECRET_KEY = os.urandom(32)
    SECRET_KEY = 'APP_FLASK'

    # Konfigurasi untuk SQL Server
    SQLALCHEMY_BINDS = {
        'sqlserver': 'mssql+pyodbc://Traceability:ability@172.21.202.142/PCS?driver=ODBC+Driver+17+for+SQL+Server',
        'sqlite': 'sqlite:///app.db'
    }