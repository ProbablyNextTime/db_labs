# Lab 2:

## Variant 22:

### Report: [БД_КП81_ЛР2_Янковський_Дмитро.pdf](lab_reports/БД_КП81_ЛР2_Янковський_Дмитро.pdf)

### Screenshots:

![](lab_reports/db_schema.png)

### CLI commands(lab2 specific):
Get developers - `python3 db_labs/cli/__init__.py --option get_developers`

Search for developers - `python3 db_labs/cli/__init__.py --option search_developers`

Create developer - `python3 db_labs/cli/__init__.py --option create_developer`

Update developer by id - ` python3 db_labs/cli/__init__.py --option update_developer `
### Prerequisites:

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python  # poetry
```

## Useful Commands:

### Python Virtual Environment:

```
poetry shell  # activate python virtual environment
poetry install  # install dependencies
```

### Run Dev Server:

```
flask  # CLI commands
make idb # Setup and seed database
make run  # run flask dev server
```


### Database:
Using Postgresql.
```
createdb db_labs  # create DB
flask db upgrade  # run migrations
flask seed  # populate with sample data
flask db migrate  # generate new migration
flask db  # more migration commands
```

### API Documentation:

Once your flask dev server is running:

- [OpenAPI JSON](http://localhost:5000/api/openapi.json) (http://localhost:5000/api/openapi.json)
- [Swagger UI](http://localhost:5000/api/swagger) (http://localhost:5000/api/swagger)
