import unittest

from helper import (is_prime,
                    is_odd,
                    is_even,)

NUMBERS = list(range(0, 10))

class HelperTest(unittest.TestCase):
    def test_even(self):
        input_data = NUMBERS
        outcome_data = [True, False, True, False, True, False, True, False, True, False]
        for variant, (input_data, outcome_data) in enumerate(zip(input_data, outcome_data)):
            self.assertEqual(is_even(input_data), outcome_data)


    def test_odd(self):
        input_data = NUMBERS
        outcome_data = [False, True, False, True, False, True, False, True, False, True]
        for variant, (input_data, outcome_data) in enumerate(zip(input_data, outcome_data)):
            self.assertEqual(is_odd(input_data), outcome_data)


    def test_prime(self):
        input_data = NUMBERS
        outcome_data = [False, False, True, True, False, True, False, True, False, False]
        for variant, (input_data, outcome_data) in enumerate(zip(input_data, outcome_data)):
            self.assertEqual(is_prime(input_data), outcome_data)