from flask import Blueprint, jsonify, request, abort
from main import db

from models.users import User
from schemas.user_schema import user_schema

from datetime import timedelta
from flask_jwt_extended import create_access_token



auth = Blueprint('auth', __name__, url_prefix='/auth')



@auth.route('/register', methods=['POST'])
def register():
    # load() converts from serialized format (JSON) to python dict 
    # AND also validates (makes sure data is in expected format and free of errors)
    user_fields = user_schema.load(request.json)
    
    
    # both of these are <class 'dict'>
    # print(type(request.json))
    # print(type(user_fields))
    
    username = user_fields['username']
    user = User.query.filter_by(username=username).first() # returns None if didn't find anything
    
    if user:
        print('Username already exists. Aborting.')
        
        # this is CA example
        # return abort(400, description="username alread registered") # sends Content-Type: text/html
        
        # planetary does following (sends json)
        return jsonify(message="That username already exists."), 409 # Conflict

    new_user = User(
        username=user_fields['username'],
        password=user_fields['password']
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    # print(type(new_user)) # <class 'models.users.User'>
    # print(new_user) # <User 5>

    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(new_user.id), expires_delta=expiry)


    # can't just jsonify(new_user)
    # return user_schema.dump(new_user) # dump converts Python -> JSON (I don't need to wrap in jsonify())
    # planetary does
    return jsonify(message="User registered successfully!", access_token=access_token), 201 # Created



@auth.route("/login", methods=['POST'])
def login():
    
    # Extract POST data
    if request.is_json:
        user_fields = user_schema.load(request.json)
        # could then do ?
        # username, password = user_fields.values()
    else: # if it's a POST from a <form>
        user_fields = user_schema.load(request.form)
        
        
    print(user_fields)
        
        
    # See if user already exists
    user = User.query.filter_by(username=user_fields["username"]).first()
    if not user or user.password != user_fields['password']:
        return jsonify(message="You entered a bad username or password"), 401 # Permission Denied
        # CA does
        # return abort(401, description="Incorrect username and password")
        
    
    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    
    # from planetary
    return jsonify(message="Login succeeded!", access_token=access_token), 200

@auth.route('/test', methods=['POST'])
def test():
    print(request)
    return jsonify(message= 'hello', access_token=1234)