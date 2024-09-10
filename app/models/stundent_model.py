from app import db
from .base_model import BaseModel
from sqlalchemy import text 
from sqlalchemy.orm import sessionmaker

class Student(BaseModel):
    __tablename__ = 'students'
    __bind_key__ = 'sqlite'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    

    def __repr__(self):
        return f'<User {self.name}>'
    
    @staticmethod
    def get_student():
        sql_query = """ SELECT * FROM students
        """
        sql_query = text(sql_query)
        
        # ini ngambil ke koneksi database mysql pasti gak ada table students nya
        # result = db.session.execute(sql_query)
        # result = db.session.execute(sql_query, None, bind=db.get_engine(app, 'bind_name'))
        # result = db.session.execute(sql_query, None, bind='sqlite')
        # result = db.session.execute(query, params, bind=db.get_engine(app, 'bind_name'))
        # result = db.get_session('sqlite').execute(sql_query, params)
        # result = db.get_session('sqlite').execute(sql_query)

        # result = db.session.execute(text("SELECT * FROM students"), bind=db.get_engine(bind='sqlite'))
        engine = db.get_engine(bind='sqlite')

        Session = sessionmaker(bind=engine)
        session = Session()

        # try:
        #     # Eksekusi query menggunakan session.execute()
        #     result = session.execute(sql_query)
        #     for row in result:
        #         print(row)
        # finally:
        #     session.close()

        # params = None
        # result = db.session.execute(text("SELECT * FROM students"),bind_arguments='sqlserver')
        # result = db.session.execute(sql_query, params=params,bind=db.get_engine(bind='sqlite'))
        # return result.fetchall()
        result = session.execute(sql_query)
        result = result.fetchall()
        return result
