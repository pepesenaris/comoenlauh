from config import db, ma
from marshmallow_sqlalchemy import fields
from models import Note, Person


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_fk = True


note_schema = NoteSchema()


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    notes = fields.Nested(NoteSchema, many=True)


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)
