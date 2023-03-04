from main import ma
from models.users import User
from marshmallow import fields


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        
    notes = fields.List(fields.Nested("NoteSchema"))
        

user_schema = UserSchema()
users_schema = UserSchema(many=True)