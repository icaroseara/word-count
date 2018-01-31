from flask import request

from app.api.core.word_counter import WordCounter
from app.api.rest.base import BaseResource, rest_resource
from app.api.rest.schemas.text_schema import TextSchema

@rest_resource
class WordCount(BaseResource):
    endpoints = ['/wc']

    def post(self):
        data, errors = TextSchema().load(request.json)
        if errors: return errors
        given_text = data.get('text')
        word_count = WordCounter(given_text).count_words()
        return {'given_text': given_text, 'words_counted': word_count }
