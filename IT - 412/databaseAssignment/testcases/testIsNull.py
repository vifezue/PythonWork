import unittest
from functions.funtionLibrary import *

class testIsNull(unittest.TestCase):
    def testIsNullFalse(self):
        """This a False test to see if the string is NULL"""
        val = is_null("False")     
        self.assertFalse(val)
        
    def testIsNullTrue(self):
        """This a True test to see if the string is NULL"""
        val = is_null("")      
        self.assertTrue(val)
        
    def testIsNullTrueAgain(self):
        """This a True test to see if the string is NULL"""
        val = is_null('')      
        self.assertTrue(val)
        
    def testIsNullFalseAgain(self):
        """This a False test to see if the string is NULL"""
        val = is_null(5)      
        self.assertFalse(val)
        
    
            
        