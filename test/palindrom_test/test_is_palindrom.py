import unittest
from palindroms.palindrom_slicing import is_palindrom


class isPalindromTest(unittest.TestCase):

    def test_palindrom_True(self):
        self.assertTrue(is_palindrom(545))
        self.assertTrue(is_palindrom("Kayak"))
        self.assertTrue(is_palindrom(121))
        self.assertTrue(is_palindrom("Level"))

    def test_palindrom_False(self):
        self.assertFalse(is_palindrom("test"))
        self.assertFalse(is_palindrom(123))
        self.assertFalse(is_palindrom("google"))
        self.assertFalse(is_palindrom(332))

    def test_multiple_word_palindrom_True(self):
        self.assertTrue(is_palindrom("Don't nod."))
        self.assertTrue(is_palindrom("Red rum, sir, is murder"))
        self.assertTrue(is_palindrom("Eva, can I see bees in a cave?"))
        self.assertTrue(is_palindrom("No lemon, no melon"))