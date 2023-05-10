import unittest
import new_main


class TestMainFunctions(unittest.TestCase):
    def test_sum_of_numbers(self):
        self.assertEqual(new_main.sum_of_numbers(2, 6, 4, 78, 1, 454, 30, 68), 643)
        self.assertEqual(new_main.sum_of_numbers(-458, 458), 0)
        self.assertEqual(
            new_main.sum_of_numbers(9, -13, -14, 95, 320, -1001, 15, 0), -589
        )

    def test_sum_of_list_of_numbers(self):
        self.assertEqual(
            new_main.sum_of_list_of_numbers([2, 6, 4, 78, 1, 454, 30, 68]), 643
        )
        self.assertEqual(new_main.sum_of_list_of_numbers([-458, 458]), 0)
        self.assertEqual(
            new_main.sum_of_list_of_numbers([9, -13, -14, 95, 320, -1001, 15, 0]), -589
        )

    def test_max_numbers(self):
        self.assertEqual(new_main.max_number(2, 6, 4, 78, 1), 78)
        self.assertEqual(new_main.max_number(-25, -456, 0, 151, 41), 151)
        self.assertEqual(new_main.max_number(-558, -299, -356), -299)

    def test_reversed_sentence_order(self):
        self.assertEqual(
            new_main.reversed_sentence_order("There is a House of the Rising Sun"),
            "Sun Rising the of House a is There",
        )
        self.assertEqual(
            new_main.reversed_sentence_order("God was never on your side"),
            "side your on never was God",
        )
        self.assertEqual(
            new_main.reversed_sentence_order(
                "With the lights out, it's less dangerous"
            ),
            "dangerous less it's out, lights the With",
        )

    # def test_is_number_in_list(self):
    #     self.assertTrue(main.is_number_in_list(5, [2, 6, 5, 25, -65, 45]))
    #     self.assertFalse(main.is_number_in_list(5, [2, 6, 8, 25, -65, 45]))
    #     self.assertTrue(main.is_number_in_list(-25, [2, 6, 5, 25, -25, 45]))

    # def test_count_sentence_elements(self):
    #     self.assertEqual(
    #         main.count_sentence_elements("You load 16 tons, what do you get?"),
    #         "Number of words: 8, Number of digits: 2, Number of upper letters: 1, Number of lower letters: 22",
    #     )

    # def test_even_numbers(self):
    #     self.assertEqual(
    #         main.even_numbers(-15, 25),
    #         [
    #             -14,
    #             -12,
    #             -10,
    #             -8,
    #             -6,
    #             -4,
    #             -2,
    #             0,
    #             2,
    #             4,
    #             6,
    #             8,
    #             10,
    #             12,
    #             14,
    #             16,
    #             18,
    #             20,
    #             22,
    #             24,
    #         ],
    #     )
