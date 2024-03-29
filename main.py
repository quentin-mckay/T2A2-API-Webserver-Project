from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS


db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
cors = CORS()


def create_app():
    
    app = Flask(__name__)
    
    CORS(app)
    
    app.config.from_object('config.app_config')
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    from commands import db_commands
    app.register_blueprint(db_commands)

    # Import the controllers and register the blueprints
    from controllers import registerable_controllers
    
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    return app