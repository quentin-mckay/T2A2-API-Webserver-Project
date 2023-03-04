from flask import Blueprint, abort, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from main import db

from models.users import User
from models.notes import Note
from schemas.user_schema import user_schema, users_schema
from schemas.note_schema import note_schema, notes_schema


notes = Blueprint("notes", __name__, url_prefix="/notes")


@notes.get('/')
def get_users():
    note_list = Note.query.all() # User.all() did not work (flask-marshmallow docs are wrong)
    return notes_schema.dump(note_list) # 


@notes.get('/<int:id>')
def get_user_notes(id: int):
    note = Note.query.filter_by(id=id).first()
    return note_schema.dump(note)

# @users.get('/<int:id>')
# def get_user(id: int):
#     user = User.query.filter_by(id=id).first() # User.get(id) did not work (flask-marshmallow docs are wrong)
#     return user_schema.dump(user)


@notes.route('/', methods=['POST'])
@jwt_required() # planetary led to error without the parentheses
def create_note():
    note_fields = note_schema.load(request.json)

    # extract id of user from the JWT token
    request_id = get_jwt_identity()
    
    new_note = Note(
        content=note_fields['content'],
        user_id=request_id # link the new note to the correct user
    )
    
    db.session.add(new_note)
    db.session.commit()
    
    
    return jsonify(message="Note added")