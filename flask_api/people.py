from config import db
from flask import abort, make_response
from models import Person
from schemas import people_schema, person_schema


def read_all():
    people = Person.query.all()
    return people_schema.dump(people)


def _get_by_lastname(lname):
    return Person.query.filter(Person.lname == lname).one_or_none()


def create(person):
    lname = person.get("lname")

    existing_person = _get_by_lastname(lname)

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()

        return person_schema.dump(new_person), 201
    else:
        abort(
            406,
            f"Person with last name {lname} already exists",
        )


def read_one(lname):
    person = _get_by_lastname(lname)

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404, f"Person with last name {lname} not found")


def update(lname, person):
    the_person = _get_by_lastname(lname)

    if the_person is not None:
        updated_person = person_schema.load(person, session=db.session)
        the_person.fname = updated_person.fname

        db.session.merge(the_person)
        db.session.commit()

        return person_schema.dump(the_person), 201
    else:
        abort(404, f"Person with last name {lname} not found")


def delete(lname):
    existing_person = _get_by_lastname(lname)

    if existing_person is not None:
        db.session.delete(existing_person)
        db.session.commit()

        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(404, f"Person with last name {lname} not found")


def test():
    return make_response("test ok", 200)
