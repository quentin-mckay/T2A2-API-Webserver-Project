from main import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    
    def __repr__(self):
        return f'<Tag {self.id} {self.title}>'