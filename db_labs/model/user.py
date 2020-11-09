from sqlalchemy import Integer, ForeignKey, Text
from db_labs.db import db

class User(db.Model):
    name = db.Column(Text, unique=True, nullable=False)
    email = db.Column(Text, unique=True)
    first_name = db.Column(Text)
    last_name = db.Column(Text)
    password = db.Column(Text, nullable=False)
