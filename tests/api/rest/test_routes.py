import json
import unittest

from app import app

class RoutesTests(unittest.TestCase):
    def setUp(self):
        self.url = "/api/wc"
        self.api = app

    def test_count_word_when_text_is_valid(self):
        valid_input = dict(text="foo bar")
        with self.api.test_client() as c:
            response = c.post(self.url, data=json.dumps(valid_input), content_type='application/json')
            body = json.loads(response.data)
            assert response.status_code == 200
            assert body['given_text'] == valid_input['text']
            assert body['words_counted'] == 2

    def test_count_word_when_text_is_not_present(self):
        valid_input = dict()
        with self.api.test_client() as c:
            response = c.post(self.url, data=json.dumps(valid_input), content_type='application/json')
            body = json.loads(response.data)
            assert response.status_code == 400
            assert body['message']['text']
