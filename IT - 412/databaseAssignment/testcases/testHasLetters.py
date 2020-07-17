import unittest
from functions.funtionLibrary import *

class TestHasLetters(unittest.TestCase):
    def testHasLettersTrue(self):
        """This a True test to see if the string has a letter"""
        val = hasLetters("Trueval")     
        self.assertTrue(val)
        
    def testHasLettersFalse(self):
        """This a False test to see if the string has a letter"""
        val = hasLetters("545454")     
        self.assertFalse(val)
        
    def testHasNumbersTrue(self):
        """This a False test to see if the string has a letter"""
        val = hasLetters(str(545345345454))     
        self.assertFalse(val)