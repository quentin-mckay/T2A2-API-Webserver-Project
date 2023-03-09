from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from main import db

from models.users import User
from models.projects import Project
from models.tags import Tag
# from schemas.user_schema import user_schema, users_schema
from schemas.project_schema import project_schema, projects_schema
# from schemas.comment_schema import comment_schema, comments_schema

# from flask_cors import cross_origin
import os
import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name = os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key = os.environ.get("CLOUDINARY_API_KEY"),
    api_secret = os.environ.get("CLOUDINARY_API_SECRET")
)


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


# @jwt_required() # planetary led to error without the parentheses
@projects.route('/', methods=['POST'])
def create_project():
    project_fields = request.json
    # print(request.json)
    print(project_fields)
    # extract id of user from the JWT token
    # request_id = get_jwt_identity()
    user_id = 3
    
    title = project_fields.get('title')
    description = project_fields.get('description')
    github_url = project_fields.get('githubURL')
    demo_url = project_fields.get('demoURL')
    image_url = project_fields.get('imageURL')
    
    print(project_fields.get('tags'))
    tags = project_fields.get('tags')

    image = project_fields.get('image')
    
    if image:
        response = cloudinary.uploader.upload(image, folder='projectshare')
        image_url = response.get('url')


    new_project = Project(
        title=title,
        description=description,
        github_url=github_url,
        demo_url=demo_url,
        image_url=image_url,
        user_id=user_id, # link the new project to the correct user,
        # tags=tags
    )
    
    for tag in tags:
        new_tag = Tag(name=tag)
        new_project.tags.append(new_tag)
    # new_project.tags.append(tags[0])
    
    db.session.add(new_project)
    db.session.commit()
    
    
    return jsonify(message="Project added"), 201