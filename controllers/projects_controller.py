from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from main import db

from models.users import User
from models.projects import Project
# from schemas.user_schema import user_schema, users_schema
from schemas.project_schema import project_schema, projects_schema
# from schemas.comment_schema import comment_schema, comments_schema


projects = Blueprint("projects", __name__, url_prefix="/projects")


@projects.get('/')
def get_all_projects():
    project_list = Project.query.all() # User.all() did not work (flask-marshmallow docs are wrong)
    return projects_schema.dump(project_list) # 


@projects.get('/<int:id>')
def get_project(id: int):
    project = Project.query.filter_by(id=id).first()
    return project_schema.dump(project)
    

# @users.get('/<int:id>')
# def get_user(id: int):
#     user = User.query.filter_by(id=id).first() # User.get(id) did not work (flask-marshmallow docs are wrong)
#     return user_schema.dump(user)


@projects.route('/', methods=['POST'])
# @jwt_required() # planetary led to error without the parentheses
def create_project():
    project_fields = request.json
    # print(request.json)
    # print(project_fields)
    # extract id of user from the JWT token
    # request_id = get_jwt_identity()
    user_id = 3
    
    title = project_fields['title']
    description = project_fields['description']
    github_url = project_fields['githubURL']
    demo_url = project_fields['demoURL']
    image_url = project_fields['imageURL']

    new_project = Project(
        title=title,
        description=description,
        github_url=github_url,
        demo_url=demo_url,
        image_url=image_url,
        user_id=user_id # link the new project to the correct user
    )
    
    db.session.add(new_project)
    db.session.commit()
    
    
    return jsonify(message="Project added")