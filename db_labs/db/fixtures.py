"""Create fake models for tests and seeding dev DB."""
from faker import Factory as FakerFactory
import factory
import random

from db_labs.model import CompanyEmployee
from db_labs.model.company import Company
from db_labs.model.country import Country
from db_labs.model.employee import Employee
from db_labs.model.user import User
from db_labs.db import db
from jetkit.db import Session

faker: FakerFactory = FakerFactory.create()
DEFAULT_NORMAL_USER_EMAIL = "test@test.test"
DEFAULT_PASSWORD = "testo"


def seed_db():
    # seed DB with factories here
    # https://pytest-factoryboy.readthedocs.io/en/latest/#model-fixture


    # default normal user
    if not User.query.filter_by(email=DEFAULT_NORMAL_USER_EMAIL).one_or_none():
        # add default user for testing
        db.session.add(
            UserFactory.create(
                email=DEFAULT_NORMAL_USER_EMAIL, password=DEFAULT_PASSWORD
            )
        )
        print(
            f"Created default user with email {DEFAULT_NORMAL_USER_EMAIL} "
            f"with password '{DEFAULT_PASSWORD}'"
        )

    CompanyEmployeeFactory.create_batch(10)  # Developers and skills will be created as well

    db.session.commit()
    print("Database seeded.")


class SQLAFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Use a scoped session when creating factory models."""
    class Meta:
        abstract = True
        sqlalchemy_session = Session


class UserFactory(SQLAFactory):
    class Meta:
        model = User

    name = factory.LazyAttribute(lambda x: faker.name())
    email = factory.LazyAttribute(lambda x: faker.email())
    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    password = factory.Sequence(lambda x: f"{faker.word()}-{x}")


class CountryFactory(SQLAFactory):
    class Meta:
        model = Country

    name = factory.Sequence(lambda x: f"{x}-{faker.word()}")
    population = factory.LazyAttribute(lambda x: faker.random_int(min=0, max=9999, step=1))
    president_full_name = factory.Sequence(lambda x: f"{faker.first_name()}_{faker.last_name()}")


class EmployeeFactory(SQLAFactory):
    class Meta:
        model = Employee

    first_name = factory.LazyFunction(faker.first_name)
    last_name = factory.LazyFunction(faker.last_name)
    position = factory.LazyFunction(faker.word)
    blog_url = factory.Sequence(lambda x: f"https:/localhost:3000/blog-{x}")
    age = factory.Sequence(lambda x: faker.random_int(min=20, max=55, step=1))


class CompanyFactory(SQLAFactory):
    class Meta:
        model = Company

    name = factory.Sequence(lambda x: f"{faker.word()}-{x}")
    website_url = factory.LazyAttribute(lambda x: f"https:/localhost:3000/website-{faker.word()}")
    capitalisation = factory.LazyFunction(faker.random_int)
    founder = factory.LazyFunction(faker.last_name)
    origin_country = factory.SubFactory(CountryFactory)


class CompanyEmployeeFactory(SQLAFactory):
    class Meta:
        model = CompanyEmployee

    years_worked = factory.LazyFunction(faker.random_int)
    employee = factory.SubFactory(EmployeeFactory)
    company = factory.SubFactory(CompanyFactory)
