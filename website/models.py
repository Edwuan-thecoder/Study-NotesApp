# importing from the current package
from . import db
# import class to help keep track of current User
from flask_login import UserMixin
# import func so that every time a note is created it will add the date
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # This field will be the field that create a relationship with the User table ((One to Many relationship))
    user_ID = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Store all notes(NoteId) for specific User here
    notes = db.relationship('Note')
