from app import db
from app.models import Role

def run():
    role1 = Role(title="aku")
    role2 = Role(title="tas")

    db.session.add(role1)
    db.session.add(role2)
    db.session.commit()

    print("Roles seeder executed successfully!")
