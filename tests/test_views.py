import unittest

from app import app

class ViewsTests(unittest.TestCase):

    def setUp(self):
        self.url = "/api/"
        self.api = app
        with app.test_client() as c:
            self.response = c.get(self.url)

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        response_str = self.response.data.decode('utf-8')
        lines = str(response_str).splitlines()
        content = "".join(lines)
        self.assertIn('<title>Word Counter</title>', content)
        self.assertIn('<h1>Word Counter</h1>', content)
        self.assertIn('<label for="text">Please enter input text:</label>', content)
