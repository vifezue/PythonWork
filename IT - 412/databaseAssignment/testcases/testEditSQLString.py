import unittest
from functions.funtionLibrary import *

class testEditSQLString(unittest.TestCase):
    def testEditSQLString(self):
        """This checks to see if the EDIT sQL string is built"""      
        val = editSQLStr("BookTitle","New Book Title",2)
        self.assertEqual(val,"UPDATE bookStore SET BookTitle = 'New Book Title' WHERE bookID ='2'")
        
    
            
        