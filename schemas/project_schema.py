from main import ma
from models.projects import Project
from marshmallow import fields



class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project
        
    user = fields.Nested("UserSchema", only=("username", "id")) 
    tags = fields.List(fields.Nested("TagSchema"))
    comments = fields.List(fields.Nested("CommentSchema"))
    
    
    
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)