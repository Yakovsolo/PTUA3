import unittest
import calculator


class CalculatorTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.add(-2, 2), 0)
        self.assertEqual(calculator.add(10, 100), 110)

    def test_subtraction(self):
        self.assertEqual(calculator.subtract(10, 100), -90)

    def test_division(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertRaises(ZeroDivisionError, calculator.divide, 1, 0)

    def test_mutipication(self):
        self.assertEqual(calculator.multiply(10, 2), 20)
