from flask import Blueprint

from main import db

from models.users import User
from models.projects import Project
from models.comments import Comment
from models.tags import Tag

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

    # password = bcrypt.generate_password_hash("123456").decode("utf-8")
    user1 = User(username = "Quentin", password = '5678', admin = True)
    user2 = User(username = "Laura", password = 'ghjk')
    user3 = User(username = "Tino", password = 'fgjthdf')
    
    db.session.add_all([user1, user2, user3])
    db.session.commit() # This extra commit will end the transaction and generate the ids for the user
    
    
    
    project1 = Project(content = "This is the very first project", user = user1) # user field comes from User model backref
    project2 = Project(content = "This is the second project", user = user1)
    project3 = Project(content = "This is the second project", user = user2)
    
    db.session.add_all([project1, project2, project3])
    db.session.commit()



    comment1 = Comment(message='Comment for the first project', user_id=2, project=project1) # project field from backref defined in Project model
    comment2 = Comment(message='Comment for the second project', user_id=3, project=project2)
    comment3 = Comment(message='Another comment for the second project', user_id=3, project=project2)
    comment4 = Comment(message='A comment for the third project', user_id=1, project_id=3) # another way to do it
    
    db.session.add_all([comment1, comment2, comment3, comment4])
    db.session.commit()



    print("Tables seeded")




@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")