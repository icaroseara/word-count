from marshmallow import Schema, fields

class TextSchema(Schema):
    text = fields.Str(required=True)
