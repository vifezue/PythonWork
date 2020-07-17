import unittest
from functions.funtionLibrary import *

class testFormatISBN(unittest.TestCase):
    def testFormatISBN(self):
        """This is a positive test to see if the ISBN comes back formatted"""      
        val = format_isbn("1234567894123")
        self.assertEqual(val,"123-4-567-89412-3")
        
    def testBadFormatISBN(self):
        """This is a negative test to see if the ISBN comes back formatted"""    
        val = format_isbn("1234567843534594123")
        self.assertFalse(val)
        
    def testBadFormatISBNAgain(self):
        """This is a negative test to see if the ISBN comes back formatted"""      
        val = format_isbn("12345678")
        self.assertFalse(val)
