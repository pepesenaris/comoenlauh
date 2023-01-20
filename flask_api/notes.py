from config import db
from flask import abort, make_response
from models import Note
from schemas import note_schema


def read_all():
    note = Note.query.all()
    return note_schema.dump(note)


def _get_by_id(note_id):
    return Note.query.get(note_id)


def read_one(note_id):
    note = _get_by_id(note_id)

    if note is not None:
        return note_schema.dump(note)
    else:
        abort(404, f"Note with id {note_id} not found")


def update(note_id, note):
    existing_note = _get_by_id(note_id)

    if existing_note:
        update_note = note_schema.load(note, session=db.session)
        existing_note.content = update_note.content
        db.session.merge(existing_note)
        db.session.commit()
        return note_schema.dump(existing_note), 201
    else:
        abort(404, f"Note with ID {note_id} not found")


def delete(note_id):
    existing_note = _get_by_id(note_id)

    if existing_note:
        db.session.delete(existing_note)
        db.session.commit()
        return make_response(f"{note_id} successfully deleted", 204)
    else:
        abort(404, f"Note with ID {note_id} not found")
