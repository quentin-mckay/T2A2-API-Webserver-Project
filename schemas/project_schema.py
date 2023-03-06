from main import ma
from models.projects import Project


class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project
        
        
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)