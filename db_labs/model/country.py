from sqlalchemy import Integer, ForeignKey, Text
from db_labs.db import db

class Country(db.Model):
    name = db.Column(Text, unique=True, nullable=False)
    population = db.Column(Integer)
    president_full_name = db.Column(Text, unique=True)