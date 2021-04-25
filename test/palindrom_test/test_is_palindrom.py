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

    def test_multiple_word_palindrom_False(self):
        self.assertFalse(is_palindrom("Some unnecessary sentence."))
        self.assertFalse(is_palindrom("This, Sentence is not a Palindrom."))
        self.assertFalse(is_palindrom("Is this sentence a Palindrom?"))
        self.assertFalse(is_palindrom("This sentece Also is not a Palindrom!!!!"))


    def test_value_Error_when_incorrect_value_is_provided(self):
        with self.assertRaises(ValueError) as context:
            is_palindrom([1, 2, 3, 4, 5, 6])
        self.assertEqual(str(context.exception), "Provided argument is not int or string")
        with self.assertRaises(ValueError) as context:
            is_palindrom({1: 4, "test": "no"})
        self.assertEqual(str(context.exception), "Provided argument is not int or string")
        with self.assertRaises(ValueError) as context:
            is_palindrom((1, 2, 5, 223, 565))
        self.assertEqual(str(context.exception), "Provided argument is not int or string")
        with self.assertRaises(ValueError) as context:
            is_palindrom({1, 2, 3, 45, 5})
        self.assertEqual(str(context.exception), "Provided argument is not int or string")