from models import Author, Book
from marshmallow import Schema, fields

class AuthorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()

class BookSchema(Schema):
    id = fields.Integer(dump_only=True) #significa que nao pode ser postado
    name = fields.Str()
    edition = fields.Str()
    year_published = fields.Integer()
    authors = fields.List(fields.Integer(), required=True)
    # criando uma lista para receber multiplos autoes, para ficar como o post exemplo.
