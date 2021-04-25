import unittest
from palindroms.palindrom_slicing import is_palindrom


class isPalindromTest(unittest.TestCase):

    def test_short_palindrom(self):
        self.assertTrue(is_palindrom("Anna"), "Anna is a palindrom")
        self.assertTrue(is_palindrom("Kayak"), "Kayak is a palindrom")
        self.assertTrue(is_palindrom("Level"), "Level is a palindrom")
        self.assertTrue(is_palindrom("Level"), "Level is a palindrom")
