import unittest
from palindroms.palindrom_slicing import is_palindrome


class isPalindromTest(unittest.TestCase):

    def test_palindrom_True(self):
        self.assertTrue(is_palindrome(545))
        self.assertTrue(is_palindrome("Kayak"))
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome("Level"))

    def test_palindrom_False(self):
        self.assertFalse(is_palindrome("test"))
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome("google"))
        self.assertFalse(is_palindrome(332))

    def test_multiple_word_palindrom_True(self):
        self.assertTrue(is_palindrome("Don't nod."))
        self.assertTrue(is_palindrome("Red rum, sir, is murder"))
        self.assertTrue(is_palindrome("Eva, can I see bees in a cave?"))
        self.assertTrue(is_palindrome("No lemon, no melon"))

    def test_multiple_word_palindrom_False(self):
        self.assertFalse(is_palindrome("Some unnecessary sentence."))
        self.assertFalse(is_palindrome("This, Sentence is not a Palindrom."))
        self.assertFalse(is_palindrome("Is this sentence a Palindrom?"))
        self.assertFalse(is_palindrome("This sentece Also is not a Palindrom!!!!"))


    def test_value_Error_when_incorrect_value_is_provided(self):
        with self.assertRaises(ValueError) as context:
            is_palindrome([1, 2, 3, 4, 5, 6])
        self.assertEqual(str(context.exception), "Provided argument is not int or string")
        with self.assertRaises(ValueError) as context:
            is_palindrome({1: 4, "test": "no"})
        self.assertEqual(str(context.exception), "Provided argument is not int or string")
        with self.assertRaises(ValueError) as context:
            is_palindrome((1, 2, 5, 223, 565))
        self.assertEqual(str(context.exception), "Provided argument is not int or string")
        with self.assertRaises(ValueError) as context:
            is_palindrome({1, 2, 3, 45, 5})
        self.assertEqual(str(context.exception), "Provided argument is not int or string")