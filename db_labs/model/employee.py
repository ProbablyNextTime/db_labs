from sqlalchemy import Integer, ForeignKey, Text
from db_labs.db import db

class Employee(db.Model):
    position = db.Column(Text)
    blog_url = db.Column(Text, unique=True)
    first_name = db.Column(Text)
    last_name = db.Column(Text)
    age = db.Column(Integer)

    companies = db.relationship("Company", secondary="company_employee", back_populates="employees")