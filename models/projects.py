from main import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        project_content = self.content[:10] + '...'
        return f'<Project {self.id} {project_content}>'