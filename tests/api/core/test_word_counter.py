import unittest

from app.api.core.word_counter import WordCounter

class WordCounterTests(unittest.TestCase):
    def setUp(self):
        self.word_counter = WordCounter()

    def test_count_words_when_text_is_empty(self):
        assert self.word_counter.count_words("") == 0

    def test_count_words_when_text_has_unique_word(self):
        assert self.word_counter.count_words("foo") == 1

    def test_count_words_when_text_is_present(self):
        assert self.word_counter.count_words("some text") == 2
