import unittest
from classes.clsDataSet import *

class testFunctions(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def testGetActionSolution(self):
        actionlist = [1,2,3,4,5]
        for action in actionlist:
            if action == 1:
                val = getActionSelection(action)
                self.assertEqual(val,"Import A New Data File")
            if action == 2:
                val = getActionSelection(action)
                self.assertEqual(val,"Show records in a database")
            if action == 3:
                val = getActionSelection(action)
                self.assertEqual(val,"Add a record")
            if action == 4:
                val = getActionSelection(action)
                self.assertEqual(val,"Edit a record")
            if action == 5:
                val = getActionSelection(action)
                self.assertEqual(val,"Quit the program")
                   
    def testBadGetActionSolution(self):
        """This a False test to see if the action is selected""" 
        actionlist = ["Delete a File",7,8,100,"5","","@1"]
        for action in actionlist:
            val = getActionSelection(action)
            self.assertFalse(val)
            
    def testEditSQLString(self):
        """This checks to see if the EDIT SQL string is built""" 
        database = "CRM_DATA"     
        val = editSQLStr("fName","George",2, database)
        self.assertEqual(val,"UPDATE CRM_DATA SET fName = 'George' WHERE crmID ='2'")
        
    def testEditSQLString(self):
        """This checks to see if the EDIT SQL string is built""" 
        database = "MAILINGS"     
        val = editSQLStr("fName","Mark",12, database)
        self.assertEqual(val,"UPDATE MAILINGS SET fName = 'Mark' WHERE crmID ='12'")

    def testGetColumnSolution(self):
        """This a True test to see if the column is selected""" 
        actionlist = [1,2,3,4,5]
        for action in actionlist:
            if action == 1:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"fName")
            if action == 2:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"lName")
            if action == 3:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"address")
            if action == 4:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"city")
            if action == 5:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"state")
            if action == 6:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"zipcode")
            if action == 7:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"company")
            if action == 8:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"primaryPhone")
            if action == 9:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"secondaryPhone")
            if action == 10:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"emailAddress")
            if action == 10:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"all")

    def testGetMailColumnSolution(self):
        """This a True test to see if the column is selected""" 
        actionlist = [1,2,3,4,5]
        for action in actionlist:
            if action == 1:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"name")
            if action == 2:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"address")
            if action == 3:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"company")
            if action == 4:
                val = getCRMColumnSelection(action)
                self.assertEqual(val,"All")

    def testBadCRMColumnSolution(self):
        """This a False test to see if the column is selected"""
        actionlist = ["firstName",19,18,110,"15","","1@"]
        for action in actionlist:
            val = getCRMColumnSelection(action)
            self.assertFalse(val)
            
    def testBadMailColumnSolution(self):
        """This a False test to see if the column is selected"""
        actionlist = ["firstName",19,18,110,"15","","1@"]
        for action in actionlist:
            val = getMailColumnSelection(action)
            self.assertFalse(val)
            
    def testHasLettersTrue(self):
        """This a True test to see if the string has a letter"""
        val = hasLetters("Trueval")     
        self.assertTrue(val)
        
    def testHasLettersFalse(self):
        """This a False test to see if the string has a letter"""
        val = hasLetters("545454")     
        self.assertFalse(val)
        
    def testHasNumbersTrue(self):
        """This a False test to see if the string has a letter"""
        val = hasLetters(str(545345345454))     
        self.assertFalse(val)
        
    def testGetDatabaseName(self):
        """This is a Positive test to see if it returns the database name"""
        actionlist = [1,2]
        for action in actionlist:
            if action == 1:
                val = getDatabaseName(action)
                self.assertEqual(val,"crm_data")
            if action == 2:
                val = getDatabaseName(action)
                self.assertEqual(val,"mailings")
                
    def testGetFalseDatabaseName(self):
        """This is a FALSE test to see if it returns the database name"""
        actionlist = [3,4,5,"","6",100]
        for action in actionlist:
            val = getDatabaseName(action)
            self.assertFalse(val)
            
    def testValidateString(self):
        strL = "Run"
        validate_string(strL)
        self.assertEqual("Run")
        
    def testValidateNumberToString(self):
        number = 9
        validate_string(number)
        self.assertEqual('9')  
        
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
    
    def testNoQuotes(self):
        """This a test to see if the single quotes are removed"""                
        wordlist = "Mike's"
        self.assertEqual(NoQuotes("Mike''s"))

    def testBadNoQuotes(self):
        """This a test to see if the test fails"""        
        wordlist = [str(65464), "Victors", "Victor''''s"]
        for word in wordlist:
            self.assertNotEqual(NoQuotes(word), "Victor")
    
    def testHasLettersTrue8(self):
        """This a True test to see if the string has a letter"""
        val = hasLetters("Trueval")     
        self.assertTrue(val)
        
    def testHasLettersFalse9(self):
        """This a False test to see if the string has a letter"""
        val = hasLetters("545454")     
        self.assertFalse(val)
        
    def testHasNumbersTrue3(self):
        """This a False test to see if the string has a letter"""
        val = hasLetters(str(545345345454))     
        self.assertFalse(val)
        
    def testHasNumbersFalse1(self):
        """This a False test to see if the string has a number"""
        val = hasNumbers("False")     
        self.assertFalse(val)
        
    def testHasNumbersTrue2(self):
        """This a True test to see if the string has a number"""
        val = hasNumbers("545454")     
        self.assertTrue(val)
        
    def testHasNumbersTrue4(self):
        """This a True test to see if the string has a number"""
        val = hasNumbers(str(545345345454))     
        self.assertTrue(val)       