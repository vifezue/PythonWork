import unittest
from functions.funtionLibrary import *

class TestNoQuotes(unittest.TestCase):
    """Test for removal of quotes"""
    
    def testNoQuotes(self):
        """This a test to see if the single quotes are removed"""
        
        wordlist = ["Mike's", "Mike''s", "Mick''''s"]
        self.assertEqual(NoQuotes("Mike's"), "Mikes")
        
    def testBadNoQuotes(self):
        """This a test to see if the test fails"""        
        wordlist = [str(65464), "Victors", "Victor''''s"]
        for word in wordlist:
            self.assertNotEqual(NoQuotes(word), "Victor")
        