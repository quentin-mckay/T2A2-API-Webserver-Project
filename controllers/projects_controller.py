from flask import Blueprint, request, jsonify, abort
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


@projects.route('/', methods=['GET'])
def get_all_projects():
    project_list = Project.query.all() # User.all() did not work (flask-marshmallow docs are wrong)

    return jsonify(projects_schema.dump(project_list)), 200 # OK


@projects.route('/<int:project_id>', methods=['GET'])
def get_project_by_id(project_id: int):
    # project = Project.query.filter_by(id=project_id).first() # alternative way
    project = Project.query.get(project_id) # shorthand for querying by primary_key
    
    if not project:
        return jsonify(message="Project not found"), 404 # Not Found

    return jsonify(project_schema.dump(project)), 200 # OK


# @jwt_required() # projectary led to error without the parentheses
@projects.route('/', methods=['POST'])
def create_project():
    project_fields = request.json
    # project_fields = project_schema.load(request.json)
    
    # print(request.json)
    # print(project_fields)
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

    try:
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
        
        
        db.session.add(new_project)
        db.session.commit()
        
        return jsonify(message="Project added", id=new_project.id), 201 # Created

    except Exception as e:
        return jsonify(message="Error while creating new Project"), 500 # Internal Server Error
    
    
@projects.route('/<int:project_id>', methods=['PUT'])
# @jwt_required()
def update_project(project_id: int):
    # project_fields = project_schema.load(request.json)
    project_fields = request.json

    # user_id = get_jwt_identity()
    user_id = 3
    
    user = User.query.get(user_id)
    if not user:
        return abort(401, message="Invalid user")


    project = Project.query.get(project_id)
    
    if not project:
        return abort(404, message="Project not found")

    project.title = project_fields.get('title')
    project.description = project_fields.get('description')
    project.github_url = project_fields.get('githubURL')
    project.demo_url = project_fields.get('demoURL')
    project.image_url = project_fields.get('imageURL')
    
    db.session.commit()
    
    return jsonify(message="Updated project", project=project_schema.dump(project)), 202 # Accepted


@projects.route('/<int:project_id>', methods=['DELETE'])
# @jwt_required()
def delete_project(project_id: int):
    # user_id = get_jwt_identity()
    # user_id = 3
    
    # # #Find it in the db
    # user = User.query.get(user_id)
    # if not user:
    #     return abort(401, description="Invalid user")
    
    
    project = Project.query.get(project_id)
    if not project:
        return jsonify(message="That project does not exist"), 404
    
    db.session.delete(project)
    db.session.commit()
    
    return jsonify(message="You deleted a project", id=project_id), 202 # Accepted