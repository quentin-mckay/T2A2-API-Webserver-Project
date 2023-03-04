from main import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    
    # backref='user' creates column in the Note model used for querying
	# ex: quentin = User(email="asdf@gmail.com", password="1234")
    # ex: note = Note(content="I am a note", owner=quentin)
    notes = db.relationship('Note', backref='user')
    
    def __repr__(self):
        return f'<User {self.id} {self.email}>'