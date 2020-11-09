from marshmallow import fields as f

from db_labs.api.schemas import BaseSchema

class CountrySchema(BaseSchema):
   name = f.Str()
   population = f.Integer()
   president_full_name = f.Str()

class CompanySchema(BaseSchema):
   name = f.Str()
   capitalisation = f.Number()
   founder = f.Str()
   website_url = f.Str()
   country = f.Nested(CountrySchema)

