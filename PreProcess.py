from __future__ import unicode_literals
from hazm import *


class PunctuationMarkRemover:
    def __init__(self):
        self._punctuation_marks = {'،', '.', '!', '?', '؟', '(', ')', '[', ']', '"', '/', '\\', '؛', ':', ',', '{', '}'}

    def remove_punctuation_marks(self, word):
        result = ''
        for character in word:
            if character not in self._punctuation_marks:
                result += character
        return result


class PreProcessor:
    def __init__(self):
        self.normalizer = Normalizer()
        self.stemmer = Stemmer()
        self.dictionary = {}
        self.punctuation_mark_remover = PunctuationMarkRemover()

    def pre_process(self, word):
        normalized = self.normalizer.normalize(word)
        tokens = word_tokenize(normalized)

        for i in range(len(tokens)):
            tokens[i] = self.punctuation_mark_remover.remove_punctuation_marks(tokens[i])
            tokens[i] = self.stemmer.stem(tokens[i])

        # TODO Remove stopwords

        while '' in tokens:
            tokens.remove('')

        return tokens
