from main import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    
    # backref='user' creates column in the Project model used for querying
	# ex: quentin = User(username="Quentin", password="1234")
    # ex: project = Project(content="I am a project", owner=quentin)
    projects = db.relationship(
        'Project', 
        backref='user', 
        lazy=True,
        cascade="all, delete"
    )
    
    # comments = db.relationship(
    #     "Comment",
    #     backref="user",
    #     cascade="all, delete"
    # )
    
    
    def __repr__(self):
        return f'<User {self.id} {self.email}>'