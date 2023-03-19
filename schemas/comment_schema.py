from main import ma
from models.comments import Comment
from marshmallow import fields



class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        
    user =  fields.Nested("UserSchema", only=("username",))  
      
      
      
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)