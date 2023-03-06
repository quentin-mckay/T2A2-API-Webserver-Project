from flask import Blueprint, abort, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from main import db

from models.users import User
from schemas.user_schema import user_schema, users_schema
from schemas.project_schema import project_schema, projects_schema


users = Blueprint("users", __name__, url_prefix="/users")


@users.get("/")
def get_users():
    users_list = User.query.all() # User.all() did not work (flask-marshmallow docs are wrong)
    response = jsonify(users_schema.dump(users_list))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # return users_schema.dump(users_list) # 


@users.get('/<int:id>')
def get_user(id: int):
    user = User.query.filter_by(id=id).first() # User.get(id) did not work (flask-marshmallow docs are wrong)
    return user_schema.dump(user)


@users.get('/<int:id>/projects')
def get_user_projects(id: int):
    user = User.query.filter_by(id=id).first()
    projects = user.projects
    return projects_schema.dump(projects)