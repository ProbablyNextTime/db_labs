from os import abort

import requests

APP_DEV_URL = "http://localhost:5000/api"


def handle_creating_company(name: str, capitalisation: int):
    try:
        response = requests.post(
            f"{APP_DEV_URL}/company", json=dict(name=name, capitalisation=capitalisation)
        )

    except Exception:
        print("An error occurred while trying to reach the API.")
        return abort()

    if response.status_code != 200:
        print("An error occurred during the API request.")
        return abort()

    return response


def handle_updating_company(id: int, name: str, capitalisation: int):
    try:
        response = requests.patch(
            f"{APP_DEV_URL}/company/{id}",
            json=dict(name=name, capitalisation=capitalisation),
        )
    except Exception:
        print("An error occurred while trying to reach the API.")
        return abort()

    if response.status_code != 200:
        print("An error occurred during the API request.")
        return abort()

    return response


def handle_searching_for_companies(query_string: str):
    try:
        response = requests.get(f"{APP_DEV_URL}/company?query={query_string}")
    except Exception:
        print("An error occurred while trying to reach the API.")
        return abort()

    if response.status_code != 200:
        print("An error occurred during the API request.")
        return abort()

    if not response.json():
        print(f"No results found for the keyword: {query_string}")
        return abort()

    return response


def handle_getting_companies():
    try:
        response = requests.get(f"{APP_DEV_URL}/company")
    except Exception:
        print("An error occurred while trying to reach the API.")
        return abort()

    if response.status_code != 200:
        print("An error occurred during the API request.")
        return abort()

    if not response.json():
        print(f"No results found")
        return abort()

    return response
