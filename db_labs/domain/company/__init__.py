from typing import Dict, Union
from flask_smorest import abort

from db_labs.db import db


import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)
log = logging.getLogger(__name__)


def handle_getting_and_searching_for_companies(query_string: str):
    if query_string:
        query_string = f"%{query_string}%"

        query = """SELECT country_1.id as country_id, company.id as id, country_1.name as country_name, *
        FROM company LEFT OUTER JOIN company_employee ON company.id = company_employee.company_id LEFT OUTER JOIN employee ON employee.id = company_employee.employee_id LEFT OUTER JOIN country as country_1 on country_1.id = company.origin_country_id
        WHERE CAST(company.name AS VARCHAR) ILIKE :query_string ESCAPE '~' OR CAST(company.capitalisation AS VARCHAR) ILIKE :query_string ESCAPE '~' UNION SELECT  country_1.id as country_id, company.id as id, country_1.name as country_name, *
        FROM company LEFT OUTER JOIN company_employee ON company.id = company_employee.company_id LEFT OUTER JOIN employee ON employee.id = company_employee.employee_id LEFT OUTER JOIN country as country_1 on country_1.id = company.origin_country_id
        WHERE CAST(employee.first_name AS VARCHAR) ILIKE :query_string ESCAPE '~' LIMIT 20;"""

        result = db.session.execute(query, dict(query_string=query_string))
    else:
        query = """SELECT country_1.id as country_id, company.id as id, country_1.name as country_name, * FROM company LEFT OUTER JOIN country as country_1 on country_1.id = company.origin_country_id LIMIT 20;"""
        result = db.session.execute(query)

    companies = []
    for entry in result:
        country = dict(id=entry['country_id'], name=entry['country_name'])
        company = dict(id=entry['id'], name=entry['name'], country=country, capitalisation=entry['capitalisation'], founder=entry['founder'], website_url=entry['website_url'])
        companies.append(company)


    return companies


def handle_creating_company(args: Dict[str, str]):

    create_company_query = """INSERT INTO company (name, capitalisation, origin_country_id) VALUES (:name, :capitalisation, 1) RETURNING company.id, company.name, company.capitalisation """
    update_relations = """INSERT INTO company_employee (company_id, employee_id) VALUES (:company_id, 1)"""
    result = db.session.execute(create_company_query, args)
    company = {}
    for entry in result:
        company = entry
    db.session.execute(update_relations, dict(company_id=company['id'], employee_id=1))
    db.session.commit()



    return company


def handle_updating_company(args: Dict[str, Union[str, int]], company_id: int):
    values = {key: value for key, value in args.items() if value is not None}

    update_developer_query = """UPDATE company SET updated_at=NOW(), name=:name, capitalisation=:capitalisation WHERE id=:id RETURNING company.id, company.name, company.capitalisation"""
    values["id"] = company_id
    result = db.session.execute(update_developer_query, values)

    db.session.commit()

    company = {}
    for entry in result:
        company = entry

    if not company:
        abort(404, message=f"No company with id: ${company_id} found.")

    return company