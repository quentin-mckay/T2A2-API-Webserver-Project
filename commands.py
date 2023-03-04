from flask import Blueprint

from main import db

from models.users import User
from models.notes import Note


db_commands = Blueprint("db", __name__)


@db_commands.cli.command("create")
def create_db():
	db.create_all()
	print("Tables created")
 
 

@db_commands.cli.command("seed")
def seed_db():
    #Create the users first
    admin_user = User(
        email = "admin@email.com",
        # password = bcrypt.generate_password_hash("password123").decode("utf-8"),
        password = '1234',
        admin = True
    )
    db.session.add(admin_user)

    user1 = User(
        email = "user1@email.com",
        # password = bcrypt.generate_password_hash("123456").decode("utf-8")
        password = '5678'
    )
    db.session.add(user1)
    
    user2 = User(
        email = "user2@email.com",
        # password = bcrypt.generate_password_hash("123456").decode("utf-8")
        password = 'ghjk'
    )
    db.session.add(user2)
    
    
    
    
    # This extra commit will end the transaction and generate the ids for the user
    db.session.commit()
    print("Tables seeded")
    
    
    
    note1 = Note(
        content = "This is the very first note",
        user = user1
    )
    note2 = Note(
        content = "This is the second note",
        user = user1
    )
    note3 = Note(
        content = "This is the second note",
        user = user2
    )
    db.session.add_all([note1, note2, note3])
    db.session.commit()


@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")