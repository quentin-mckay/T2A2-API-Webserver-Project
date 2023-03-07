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
    seed()

def seed():
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
    
    
    
    project1 = Project(
        title="Syntax Highlighter",
        description="Syntax highlighter for code blocks in the Ed platform",
        github_url="https://github.com/quentin-mckay/Code-Syntax-Highlighter-Ed",
        image_url="https://github.com/quentin-mckay/Code-Syntax-Highlighter-Ed/blob/master/images/screenshot.png",
        user=user1
    ) # user field comes from User model backref
    project2 = Project(
        title="Text-to-Image Generator",
        description="Create images from text",
        github_url="https://github.com/quentin-mckay/OpenAI-Image-Generator-React-Frontend",
        demo_url="https://openai-image-generator-react-frontend.onrender.com/",
        image_url="https://github.com/quentin-mckay/OpenAI-Image-Generator-React-Flask/blob/master/app-image.jpg",
        user=user1
    )
    project3 = Project(
        title="Third project",
        github_url="https://github.com/quentin-mckay/Base-Converter-PyScript",
        user=user2
    )
    
    db.session.add_all([project1, project2, project3])
    db.session.commit()



    comment1 = Comment(message='Comment for the first project', user_id=2, project=project1) # project field from backref defined in Project model
    comment2 = Comment(message='Comment for the second project', user_id=3, project=project2)
    comment3 = Comment(message='Another comment for the second project', user_id=3, project=project2)
    comment4 = Comment(message='A comment for the third project', user_id=1, project_id=3) # another way to do it
    
    db.session.add_all([comment1, comment2, comment3, comment4])
    db.session.commit()


    tag1 = Tag(name='React')
    tag2 = Tag(name='Tailwind')
    tag3 = Tag(name='Flask')

    project1.tags.append(tag1)
    project1.tags.append(tag2)
    project2.tags.append(tag3)


    db.session.add_all([tag1, tag2, tag3])
    db.session.commit()


    print("Tables seeded")




@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")
    
    
@db_commands.cli.command('reset')
def drop_db():
    
    db.drop_all()
    print("Tables dropped")
    
    db.create_all()
    print("Tables created")
    
    seed()