from app import db
from app.models import User
from passlib.hash import pbkdf2_sha256

def run():
    name = 'admin'
    username = 'admin'
    email = 'admin@gmail.com'
    role_id = 1
    password = '123'
    password = pbkdf2_sha256.hash(password)
    user = User(name=name,username=username, email=email, password=password, role_id=role_id)
    
    db.session.add(user)

    name = 'member'
    username = 'member'
    email = 'member@gmail.com'
    role_id = 2
    password = '123'
    password = pbkdf2_sha256.hash(password)
    user = User(name=name,username=username, email=email, password=password, role_id=role_id)
    
    db.session.add(user)
    db.session.commit()

    print("Users seeder executed successfully!")
