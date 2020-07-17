import unittest
from functions.funtionLibrary import *

class test_checkInvalidChars(unittest.TestCase):
    def test_checkInvalidChars(self):
        """This a true test for checking for bad characters"""
        namelist = ["Victor", "Sam", "Mike Lowry"]        
        for name in namelist:
            self.assertTrue(checkInvalidChars(name))
            
    def test_checkBadInvalidChars(self):
        """This is a bad test for checking for invalid characters"""
        namelist = ["Greg!", "S@m", "Mike & Frank"]        
        for name in namelist:
            self.assertTrue(checkInvalidChars(name))
        