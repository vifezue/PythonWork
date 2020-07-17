import unittest
from functions.funtionLibrary import *

class TestHasNumbers(unittest.TestCase):
    def testHasNumbersFalse(self):
        """This a False test to see if the string has a number"""
        val = hasNumbers("False")     
        self.assertFalse(val)
        
    def testHasNumbersTrue(self):
        """This a True test to see if the string has a number"""
        val = hasNumbers("545454")     
        self.assertTrue(val)
        
    def testHasNumbersTrue(self):
        """This a True test to see if the string has a number"""
        val = hasNumbers(str(545345345454))     
        self.assertTrue(val)