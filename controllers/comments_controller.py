from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from main import db

from models.projects import Project
from models.comments import Comment

from schemas.comment_schema import comment_schema, comments_schema


comments = Blueprint("comments", __name__)


@comments.route('/projects/<int:project_id>/comments', methods=['GET'])
def get_all_project_comments(project_id: int):
	project = Project.query.filter_by(id=project_id).first()
	
	return jsonify(comments_schema.dump(project.comments))


@comments.route('/projects/<int:project_id>/comments', methods=['POST'])
def create_comment(project_id: int):

 
	# user_id = get_jwt_identity()
	user_id = 1
	
	project = Project.query.filter_by(id=project_id).first()
  
	message = request.json['message']
 
	comment = Comment(
     	message=message, 
		user_id=user_id,
		project=project
	)
 
	db.session.add(comment)
	db.session.commit()
 
	return jsonify(message="Comment added")