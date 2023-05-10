import unittest
from main import StringTricks


class TestStringTricks(unittest.TestCase):
    def setUp(self) -> None:
        self.string_tricks_one = StringTricks("What a wonderful world!")
        self.string_tricks_two = StringTricks("")
        self.string_tricks_three = StringTricks("123456789")

    def test_first_word(self):
        self.assertEqual(self.string_tricks_one.first_word(), "What")
        self.assertEqual(self.string_tricks_three.first_word(), "123456789")

    def test_first_word_with_empty_string(self):
        self.assertRaises(IndexError, self.string_tricks_two.first_word)

    def test_last_word(self):
        self.assertEqual(self.string_tricks_one.last_word(), "world!")
        self.assertEqual(self.string_tricks_three.last_word(), "123456789")

    def test_last_word_with_empty_string(self):
        self.assertRaises(IndexError, self.string_tricks_two.last_word)

    def test_reversed_sentence(self):
        self.assertEqual(
            self.string_tricks_one.reversed_sentence(),
            "!dlrow lufrednow a tahW",
        )
        self.assertEqual(
            self.string_tricks_two.reversed_sentence(),
            "",
        )
        self.assertEqual(
            self.string_tricks_three.reversed_sentence(),
            "987654321",
        )

    def test_reversed_words(self):
        self.assertEqual(
            self.string_tricks_one.reversed_words(),
            "world! wonderful a What",
        )
        self.assertEqual(
            self.string_tricks_two.reversed_words(),
            "",
        )
        self.assertEqual(
            self.string_tricks_three.reversed_words(),
            "123456789",
        )

    def test_upper_letters(self):
        self.assertEqual(
            self.string_tricks_one.upper_letters(),
            "WHAT A WONDERFUL WORLD!",
        )
        self.assertEqual(
            self.string_tricks_two.upper_letters(),
            "",
        )
        self.assertEqual(
            self.string_tricks_three.upper_letters(),
            "123456789",
        )

    def test_lower_letters(self):
        self.assertEqual(
            self.string_tricks_one.lower_letters(),
            "what a wonderful world!",
        )
        self.assertEqual(
            self.string_tricks_two.lower_letters(),
            "",
        )
        self.assertEqual(
            self.string_tricks_three.lower_letters(),
            "123456789",
        )

    def test_info_method(self):
        self.assertEqual(
            self.string_tricks_one.info(),
            "Number of words: 4, Number of digits: 0, Number of upper letters: 1, Number of lower letters: 18",
        )
        self.assertEqual(
            self.string_tricks_two.info(),
            "Number of words: 0, Number of digits: 0, Number of upper letters: 0, Number of lower letters: 0",
        )
        self.assertEqual(
            self.string_tricks_three.info(),
            "Number of words: 1, Number of digits: 9, Number of upper letters: 0, Number of lower letters: 0",
        )
