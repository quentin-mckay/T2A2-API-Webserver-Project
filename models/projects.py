from main import db
from .project_tag import project_tag


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    github_url = db.Column(db.String, nullable=False)
    demo_url = db.Column(db.String)
    image_url = db.Column(db.String)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    comments = db.relationship('Comment', backref='project', cascade='all, delete')
    
    tags = db.relationship('Tag', secondary=project_tag, backref='projects')
    
    def __repr__(self):
        return f'<Project {self.id} {self.title}>'
