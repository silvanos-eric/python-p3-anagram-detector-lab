class Anagram:

    def __init__(self, word: str) -> None:
        self.word = word

    def match(self, word_list: list):
        return [
            possible_word for possible_word in word_list
            if Anagram.checker(possible_word, self.word)
        ]

    @staticmethod
    def checker(possible_word: str, word: str):
        possible_word_sorted = sorted(possible_word)
        word_sorted = sorted(word)
        return True if possible_word_sorted == word_sorted else False
