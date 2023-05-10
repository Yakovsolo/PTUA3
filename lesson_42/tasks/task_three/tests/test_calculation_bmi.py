import unittest
from calculation_bmi import bmi


class TestCalculationBMI(unittest.TestCase):
    def test_bmi(self):
        self.assertEqual(23.54788069073783, bmi(78, 1.82))
        self.assertEqual(20.5456936226167, bmi(50, 1.56))
        self.assertEqual(27.70083102493075, bmi(100, 1.90))
        with self.assertRaises(ValueError):
            bmi(20, 1.40)
        with self.assertRaises(ValueError):
            bmi(240, 1.40)
        with self.assertRaises(ValueError):
            bmi(80, 0.40)
        with self.assertRaises(ValueError):
            bmi(80, 3.40)
