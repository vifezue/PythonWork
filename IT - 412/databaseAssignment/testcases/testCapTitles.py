import unittest
from functions.funtionLibrary import *

class testCapTitle(unittest.TestCase):
    def testCapTitle(self):
        """This a positive test to Cap Titles"""
        val = capTitles("false true")     
        self.assertEqual(val, "False True")

    def testCapTitleAgain(self):
        """This a positive test to Cap Titles"""
        val = capTitles("victor")     
        self.assertEqual(val, "Victor")

    def testFalseCapTitle(self):
        """This a false test to Cap Titles"""
        val = capTitles("victor Ifezue")     
        self.assertNotEqual(val, "victor Ifezue")
