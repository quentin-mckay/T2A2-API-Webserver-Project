from main import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    
    projects = db.relationship('ProjectTag', back_populates='tag')
    
    def __repr__(self):
        return f'<Tag {self.id} {self.title}>'