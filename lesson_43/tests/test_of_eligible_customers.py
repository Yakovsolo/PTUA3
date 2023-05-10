import unittest
import main


class TestEligiblesCustomers(unittest.TestCase):
    def test_eligible_customers(self):
        customers = {
            "Ann": [12.5, 8.8, 15.45, 5, 22.5],
            "Ben": [13.4, 57.5, 32.4],
            "John": [11.4, 35.5, 22.6, 18.5],
        }

        eligible = main.eligible_customers(customers, 3, 50.0)
        self.assertEqual(eligible, ["Ann", "Ben", "John"])

    def test_no_eligible_customers(self):
        customers = {
            "Ann": [12.5, 11.0, 14.0, 20.0],
            "Ben": [9.4, 4.5, 9.8],
            "John": [25.0, 30.0, 35.0, 40.0],
            "Steve": [10.0, 10.0, 10.0, 10.0, 10.0],
        }

        eligible = main.eligible_customers(customers, 5, 100.0)
        self.assertEqual(eligible, [])
