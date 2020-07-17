import unittest
from functions.funtionLibrary import *

class TestValidateString(unittest.TestCase):

    def testStrValidation(self):
        """Here is a test I think should work to test a string"""
        nameList = ["Victor", "victor", " victor","victor ", "victor   ", "MichEAL","McDaniels"]
        for name in nameList:
            self.assertTrue(validate_str(name))

    def testBadStrValidation(self):
        """Here is a test I think should work to test a string"""
        nameList = ["Victor32", "3623", "","16", "victor   3", "34", "M@tt"]
        for name in nameList:
            self.assertFalse(validate_str(name))