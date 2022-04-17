import unittest

from helper import (is_prime,
                    is_odd,
                    is_even,)


class HelperTest(unittest.TestCase):
    def test_even(self):
        self.assertEqual(
            is_even(4), True
        )


    def test_odd(self):
        self.assertEqual(
            is_odd(3), True
        )


    def test_prime(self):
        self.assertEqual(
        is_prime(7), True
        )