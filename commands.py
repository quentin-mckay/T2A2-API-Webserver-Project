from flask import Blueprint

from main import db

from models.users import User
from models.projects import Project


db_commands = Blueprint("db", __name__)


@db_commands.cli.command("create")
def create_db():
	db.create_all()
	print("Tables created")
 
 

@db_commands.cli.command("seed")
def seed_db():
    #Create the users first
    # admin_user = User(
    #     email = "admin@email.com",
    #     # password = bcrypt.generate_password_hash("password123").decode("utf-8"),
    #     password = '1234',
    #     admin = True
    # )
    # db.session.add(admin_user)

    user1 = User(
        username = "Quentin",
        # password = bcrypt.generate_password_hash("123456").decode("utf-8")
        password = '5678',
        admin = True
    )
    db.session.add(user1)
    
    user2 = User(
        username = "Laura",
        # password = bcrypt.generate_password_hash("123456").decode("utf-8")
        password = 'ghjk'
    )
    db.session.add(user2)
    
    user3 = User(
        username = "Tino",
        # password = bcrypt.generate_password_hash("123456").decode("utf-8")
        password = 'fgjthdf'
    )
    db.session.add(user3)
    
    
    # This extra commit will end the transaction and generate the ids for the user
    db.session.commit()
    print("Tables seeded")
    
    
    
    project1 = Project(
        content = "This is the very first project",
        user = user1
    )
    project2 = Project(
        content = "This is the second project",
        user = user1
    )
    
    project3 = Project(
        content = "This is the second project",
        user = user2
    )
    db.session.add_all([project1, project2, project3])
    db.session.commit()


@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")