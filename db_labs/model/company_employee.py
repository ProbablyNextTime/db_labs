from sqlalchemy import ForeignKey, Integer

from db_labs.db import db


class CompanyEmployee(db.Model):
    years_worked = db.Column(Integer)
    company_id = db.Column(
        Integer, ForeignKey("company.id", ondelete="CASCADE"), nullable=False
    )
    company = db.relationship('Company')
    employee_id = db.Column(
        Integer, ForeignKey("employee.id", ondelete="CASCADE"), nullable=False
    )
    employee = db.relationship('Employee')

