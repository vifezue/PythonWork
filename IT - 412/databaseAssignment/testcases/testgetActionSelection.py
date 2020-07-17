import unittest
from functions.funtionLibrary import *

class TestGetActionSelection(unittest.TestCase):
    """Test for getting action solution"""
    
    def testGetActionSolution(self):
        """This a True test to see if the action is selected""" 
        actionlist = [1,2,3,4,5]
        for action in actionlist:
            if action == 1:
                val = getActionSelection(action)
                self.assertEqual(val,"Show All Books")
            if action == 2:
                val = getActionSelection(action)
                self.assertEqual(val,"Add a book")
            if action == 3:
                val = getActionSelection(action)
                self.assertEqual(val,"Edit a book")
            if action == 4:
                val = getActionSelection(action)
                self.assertEqual(val,"Remove a book")
            if action == 5:
                val = getActionSelection(action)
                self.assertEqual(val,"Exit Program")        
        
    def testBadGetActionSolution(self):
        """This a False test to see if the action is selected""" 
        actionlist = ["Add a book",7,8,100,"5","","@1"]
        for action in actionlist:
            val = getActionSelection(action)
            self.assertFalse(val)