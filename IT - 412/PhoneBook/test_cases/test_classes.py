import unittest
from functions.functionLibrary import *
from classes.clsPhoneBook import *

class clsTestPhoneBook(unittest.TestCase):

    def setUp(self):
        """Create an instance of the Phone Book Class for testing"""
        firstName = checkFirstName("Mark")
        lastName = checkLastName("Cuban")
        phoneNumber = checkPhoneNumber("5865633934")
        phoneType = "Cell"
        self.my_contact = PhoneBook(firstName,lastName,phoneNumber,phoneType)
        
    def test_CreatePhoneBookRecord(self):
        """Test to see if the dictionary is an instance of a dictionary and with the same values
        """
        test_dictionary = self.my_contact.createPhoneBookRecord()
        dictionary = {"firstName": "Mark", "lastName": "Cuban", "phoneNumber": "586-563-3934", "phoneType": "Cell"}
        self.assertEqual(dictionary,test_dictionary)
    
    def test_SavePhoneBookContact(self):
        """Tests to see if the dictionary saves in the list
        """
        
        testResult = False
        test_dictionary = self.my_contact.createPhoneBookRecord()
        testList = [] 
        self.my_contact.savePhoneBookContact(testList)
        
        dictionary = {"firstName": "Mark", "lastName": "Cuban", "phoneNumber": "586-563-3934", "phoneType": "Cell"}
        realList =[]
        realList.append(dictionary)

        if len(realList) == 1 and len(testList) == 1:
            testResult = True
        
        self.assertTrue(testResult)
            

