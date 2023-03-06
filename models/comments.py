from main import db

class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    message= db.Column(db.String())
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)