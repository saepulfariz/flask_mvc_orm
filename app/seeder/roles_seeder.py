from app import db
from app.models import Role

def run():
    role1 = Role(title="Administrator")
    db.session.add(role1)

    role2 = Role(title="Member")
    db.session.add(role2)
    db.session.commit()

    print("Roles seeder executed successfully!")    
