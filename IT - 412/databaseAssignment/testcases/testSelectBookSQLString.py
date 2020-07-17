import unittest
from functions.funtionLibrary import *

class testBookSQLString(unittest.TestCase):
    def testBookSQLString(self):
        """This test should build the select command for SQL"""     
        val = selectBookSQLStr("Mark Twain")
        self.assertEqual(val,"SELECT * FROM bookStore where bookTitle = 'Mark Twain'")