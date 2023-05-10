import unittest
from main import is_leap


class TestIsLeap(unittest.TestCase):
    def test_returns_true_when_leap_year(self):
        result = is_leap(2000)
        self.assertTrue(result)
