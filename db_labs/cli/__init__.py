from pprint import pprint
import click
from db_labs.domain.cli import (
    handle_creating_company,
    handle_updating_company,
    handle_getting_companies,
    handle_searching_for_companies
)

APP_DEV_URL = "http://localhost:5000/api"


@click.command()
@click.option(
    "--option",
    prompt="Your name",
    help="Options: create_company\nupdate_company\nsearch_company",
)
def main(option):
    if option == "create_company":
        email = click.prompt("Please enter a name", type=str)
        first_name = click.prompt("Please enter a capitalisation of the company", type=int)

        response = handle_creating_company(email, first_name)

        print("New company created.")
        return pprint(response.json())

    if option == "update_company":
        company_id = click.prompt("Please enter a company id", type=int)
        name = click.prompt("Please enter a name", type=str)
        capitalisation = click.prompt("Please enter a capitalization", type=str)

        response = handle_updating_company(company_id, name, capitalisation)

        print(f"Company with id: {company_id} was updated.")
        return pprint(response.json())

    if option == "search_companies":
        query_string = click.prompt(
            "Please enter a search keyword(employee/company name)", type=str
        )

        response = handle_searching_for_companies(query_string)

        print(
            f"{len(response.json())} companies found for the keyword: {query_string}"
        )
        return pprint(response.json())
    #
    if option == "get_companies":
        response = handle_getting_companies()

        print(f"{len(response.json())} companies fetched")
        return pprint(response.json())


if __name__ == "__main__":
    main()
