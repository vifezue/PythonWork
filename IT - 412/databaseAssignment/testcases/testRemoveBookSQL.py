import unittest
from functions.funtionLibrary import *

class testRemoveSQLString(unittest.TestCase):
    def testRemoveSQLString(self):
        """This test should build the Delete command for SQL"""      
        val = removeBookSQLStr(2)
        self.assertEqual(val,"DELETE from bookStore WHERE bookID ='2'")
        
    
            
        