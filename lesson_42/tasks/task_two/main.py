class StringTricks:
    def __init__(self, sentence: str) -> None:
        self.sentence = sentence

    def first_word(self) -> str:
        words = self.sentence.split()
        return words[0]

    def last_word(self) -> str:
        words = self.sentence.split()
        return words[-1]

    def reversed_sentence(self) -> str:
        return self.sentence[::-1]

    def reversed_words(self) -> str:
        words = self.sentence.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

    def upper_letters(self) -> str:
        return self.sentence.upper()

    def lower_letters(self) -> str:
        return self.sentence.lower()

    def info(self) -> str:
        words = len(self.sentence.split())
        numbers = sum(char.isdigit() for char in self.sentence)
        upper_letters = sum(char.isupper() for char in self.sentence)
        lower_letters = sum(char.islower() for char in self.sentence)
        return f"Number of words: {words}, Number of digits: {numbers}, Number of upper letters: {upper_letters}, Number of lower letters: {lower_letters}"


if __name__ == "__main__":
    sentence = StringTricks("")

    test = sentence.first_word()

    print(test)
    # print(sentence.last_word())
    # print(sentence.reversed_sentence())
    # print(sentence.reversed_words())
    # print(sentence.upper_letters())
    # print(sentence.lower_letters())
    # print(sentence.info())
