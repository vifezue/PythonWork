import unittest
from functions.funtionLibrary import *

class TestgetColumnSelection(unittest.TestCase):
    """Test for getting action solution"""
    
    def testGetColumnSolution(self):
        """This a True test to see if the column is selected""" 
        actionlist = [1,2,3,4,5]
        for action in actionlist:
            if action == 1:
                val = getColumnSelection(action)
                self.assertEqual(val,"bookID")
            if action == 2:
                val = getColumnSelection(action)
                self.assertEqual(val,"bookAuthor")
            if action == 3:
                val = getColumnSelection(action)
                self.assertEqual(val,"ISBN")
            if action == 4:
                val = getColumnSelection(action)
                self.assertEqual(val,"numPurchased")
            if action == 5:
                val = getColumnSelection(action)
                self.assertEqual(val,"numCheckedOut")
            if action == 6:
                val = getColumnSelection(action)
                self.assertEqual(val,"bookTitle")
            if action == 7:
                val = getColumnSelection(action)
                self.assertEqual(val,"bookPrice")          
        
    def testBadGetColumnSolution(self):
        """This a False test to see if the column is selected"""
        actionlist = ["ISBN",9,8,10,"5","","1"]
        for action in actionlist:
            val = getColumnSelection(action)
            self.assertFalse(val)