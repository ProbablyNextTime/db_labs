from sqlalchemy import Integer, ForeignKey, Text
from db_labs.db import db

class Company(db.Model):
    name = db.Column(Text, unique=True, nullable=False)
    website_url = db.Column(Text, unique=True)
    capitalisation = db.Column(Integer)
    founder = db.Column(Text)
    origin_country_id = db.Column(Integer, ForeignKey('country.id', ondelete='CASCADE'), nullable=False)
    origin_country = db.relationship('Country')

    employees = db.relationship("Employee", secondary="company_employee", back_populates='companies')

