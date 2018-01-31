from flask import request
from app.api.rest.base import BaseResource, rest_resource

@rest_resource
class WordCounter(BaseResource):
    endpoints = ['/wc']

    def post(self):
        json_payload = request.json
        return {'given_text': '', 'word_count': 0 }
