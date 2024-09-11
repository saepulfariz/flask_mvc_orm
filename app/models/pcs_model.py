from app import db, db_sqlserver
from .base_model import BaseModel
from sqlalchemy import text 
from sqlalchemy.orm import sessionmaker

class PcsModel(BaseModel):
    __abstract__ = True  # Ini membuat SQLAlchemy tidak membuat tabel untuk PcsModel
    __bind_key__ = 'sqlserver'  # Bind model ini ke koneksi SQL Server
    __tablename__ = 'DC_PRODUCTION_DATA'

    @staticmethod
    def getProductionData(pp_code ='B02'):
        sql_query = """ SELECT TOP 10 * FROM DC_PRODUCTION_DATA WHERE PP_CODE = '"""+pp_code+"""'
        """

        sql_query = text(sql_query)

        engine = db.get_engine(bind='sqlserver')

        Session = sessionmaker(bind=engine)
        session = Session()

        result = session.execute(sql_query)
        result = result.fetchall()
        
        return result