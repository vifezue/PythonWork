import unittest
from functions.funtionLibrary import *

class testSQLString(unittest.TestCase):
    def testSQLString(self):
        """This test should build the SELECT * command for SQL"""      
        val = selectAllSQLStr()
        self.assertEqual(val,"SELECT * FROM bookStore")
        
        
        
    