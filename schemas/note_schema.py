from main import ma
from models.notes import Note


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        
        
note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)