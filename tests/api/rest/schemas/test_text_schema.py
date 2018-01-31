import unittest

from app.api.rest.schemas.text_schema import TextSchema

class TextSchemaTests(unittest.TestCase):
    def setUp(self):
        self.text_schema = TextSchema()

    def test_validates_a_valid_input(self):
        given_input = {"text": "some text"}
        data, errors = self.text_schema.load(given_input)
        assert data == given_input
        assert not errors

    def test_validates_an_invalid_input(self):
        given_input = {"text": 1}
        data, errors = self.text_schema.load(given_input)
        assert not data
        assert errors == {'text': ['Not a valid string.']}

    def test_validates_an_empty_input(self):
        given_input = {}
        data, errors = self.text_schema.load(given_input)
        assert not data
        assert errors == {'text': ['Missing data for required field.']}
