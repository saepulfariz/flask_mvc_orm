import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class MySQLConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask_mvc_orm'

class SQLServerConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://username:password@localhost/db_name?driver=SQL+Server'
