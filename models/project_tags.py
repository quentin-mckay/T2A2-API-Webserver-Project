from main import db

class ProjectTags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), nullable=False)
    
    project = db.relationship('project', back_populates='tags')
    tag = db.relationship('tag', back_populates='projects')