import unittest
from functions.funtionLibrary import *

class testBuildInsertSQL(unittest.TestCase):
    def testBuildInsertSQL(self):
        """Builds the Insert SQL String"""      
        val = buildInsertBookSQL("Mike Tyson","84-84845-584844","The Greatest Boxer",0,0,2)
        self.assertEqual(val,"INSERT INTO bookStore (bookAuthor, ISBN, numPurchased, numCheckedOut, bookTitle, bookPrice) VALUES ('Mike Tyson','84-84845-584844','0','0','The Greatest Boxer','2')")
        
    
            
        