class WordCounter:
    @classmethod
    def count_words(cls, text):
        words = str(text).split()
        return len(words)
