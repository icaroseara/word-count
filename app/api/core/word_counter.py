class WordCounter:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        words = str(self.text).split()
        return len(words)
