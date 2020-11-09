from typing import Dict, Union

from flask import request
from flask_smorest import Blueprint
from db_labs.api.company.schema import CompanySchema
from db_labs.domain.company import (
    handle_creating_company,
    handle_updating_company,
    handle_getting_and_searching_for_companies
)

blp = Blueprint("Company", __name__, url_prefix=f"/api/company")


@blp.route("", methods=["GET"])
@blp.response(CompanySchema(many=True))
def get_companies():
    query_string = request.args.get("query")

    companies = handle_getting_and_searching_for_companies(query_string)

    return companies


@blp.route("", methods=["POST"])
@blp.response(CompanySchema)
@blp.arguments(CompanySchema)
def create_company(args: Dict[str, str]):
    """Create a company entry."""
    company = handle_creating_company(args)

    return company


@blp.route("/<string:company_id>", methods=["PATCH"])
@blp.response(CompanySchema)
@blp.arguments(CompanySchema)
def update_company(args: Dict[str, Union[str, int]], company_id: int):
    """Check if company with given id exists, then update the entry."""
    company = handle_updating_company(args, company_id)

    return company
