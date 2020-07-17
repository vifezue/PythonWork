import unittest
from functions.functionLibrary import *
from classes.clsPhoneBook import *

class PhoneBookFunctionsTest(unittest.TestCase):
    """Test for functions in the function_library.py file"""

    def testStrValidation(self):
        """Here is a test I think should work to test first Name"""
        nameList = ["Victor", "victor", " victor","victor ", "victor   ", "MichEAL","McDaniels"]
        for name in nameList:
            self.assertTrue(validate_str(name))

    def testBadStrValidation(self):
        """Here is a test I think should work to test first Name"""
        nameList = ["Victor32", "3623", "","16", "victor   3", "34", "M@tt"]
        for name in nameList:
            self.assertFalse(validate_str(name))
            
    def testCheckPhoneType(self):
        """Test to see if the Phone Type is allowed
        """
        phoneTypeList = ["Cell", "Home","Office"]
        for phoneType in phoneTypeList:
            self.assertTrue(checkPhoneType(phoneType))
            
    def testBadCheckPhoneType(self):
        """Test Failure test to see if it is in the list of accepted Phone Types
        """
        phoneTypeList = ["Cell Phone", "Home Office","", 1, "2Phones","@%#%^"]
        for phoneType in phoneTypeList:
            self.assertFalse(checkPhoneType(phoneType))
            
    def testValidatePhoneNumber(self):
        """Test to see if the method accepts a valid phone number
        """
        phoneNumberList = ["5865633934","5869899584","2485847455","8108475487"]
        for phoneNumber in phoneNumberList:
            self.assertTrue(validatePhoneNumber(phoneNumber))
            
    def testValidatePhoneNumberbyRange(self):
        """Passes a range of 9 digit numbers to validate
        """
        for i in range(1000000000,9999999999):
            self.assertTrue(validatePhoneNumber(str(i))) 
    
    def testBadValidatePhoneNumber(self):
        """Failure Test to see if the method accepts a valid phone number
        """
        phoneNumberList = ["","58698995846","2485847455","8108475487","America","@#$%^&*"]
        for phoneNumber in phoneNumberList:
            self.assertFalse(validatePhoneNumber(phoneNumberList))
            
    def testBadValidatePhoneNumberbyRange(self):
        """Failure test to see if the passed in range is accepted
        """
        for i in range(0,1000000000):
            self.assertFalse(validatePhoneNumber(i))
            
    def testBadValidatePhoneNumberByLargeRange(self):
        """Failure test to see if the passed in range is accepted
        """
        for i in range(9999999999,100000000000):
            self.assertFalse(validatePhoneNumber(i))   
        
    def testCheckFirstName1(self):
        """Test to see if name is not the same as the passed in value
        """
        firstName = checkFirstName("Victor")
        self.assertEqual(firstName,"Victor")
    
    def testCheckFirstName2(self):
        """Test to see if name is not the same as the passed in value
        """
        firstName = checkFirstName("Victor")
        self.assertIs(firstName,"Victor")
    
    def testCheckFirstName3(self):
        """Failure Test to see if name is not the same as the passed in value
        """
        firstName = checkFirstName("Mike")
        self.assertNotEqual(firstName,"Victor")
    
    def testCheckLastName1(self):
        """Failure Test to see if name is not the same as the passed in value
        """
        lastName = checklastName("Victor")
        self.assertEqual(lastName,"Victor")
    
    def testCheckLastName2(self):
        """Test to see if name is not the same as the passed in value
        """
        lastName = checkLastName("Victor")
        self.assertIs(lastName,"Victor")
    
    def testCheckLastName3(self):
        """Failure Test to see if name is not the same as the passed in value
        """
        lastName = checkLastName("Mike")
        self.assertNotEqual(lastName,"Victor")
            
    def testCheckPhoneNumber(self):
        """Test to see the passed in phone number is valid and returns formatted
        """
        phoneNumber = checkPhoneNumber("5865633934")
        self.assertIs("586-563-3934",phoneNumber)
        
    def testCheckBadPhoneNumber(self):
        """Failure Test to see if the phone number is valid and formatted when returning
        """
        phoneNumber = checkPhoneNumber("5865633934")
        self.assertIsNot("586-563-3999",phoneNumber)

    def testFormatPhoneNumberbyList(self):
        """Test to see if the number list returns formatted with for loop
        """
        formattedNumberList = ["5865633934","2489584847","18002489898"]
        expectedformattedNumberList = ["586-563-3934","248-958-4847","1-800-248-9898"]
        numberList = []
        for number in formattedNumberList:
            val = phone_format(number)
            numberList.append(val)
        
        for val in numberList:
            self.assertIn(val,expectedformattedNumberList)
        
    def testHasNumbers(self):
        """Test to see if the range of numbers is numbers
        """
        for i in range(0,1000000000):
            self.assertTrue(hasNumbers(str(i)))

    def testHasBadNumbers(self):
        """Test to see if the range of numbers is numbers
        """
        letterList = ["a","b","c","d","e","f","g","h",
                      "i","j","k","l","m","n","o","p",
                      "q","r","s","t","u","v","w","x",
                      "x","y","z"]
        for i in letterList:
            self.assertFalse(hasNumbers(str(i)))
    
    def testHasLetters(self):
        """Test to see if the the passed in list of letters has letters
        """
        letterList = ["a","b","c","d","e","f","g","h",
                      "i","j","k","l","m","n","o","p",
                      "q","r","s","t","u","v","w","x",
                      "x","y","z"]
        for letter in letterList:
            self.assertTrue(hasLetters(str(letter)))
            
    def testHasBadLetters(self):
        """Test to see if the the passed in list of numbers has letters
        """
 
        for i in range(0,11):
            self.assertFalse(hasLetters(str(i)))
    
    def testDictionaryValuesReturned(self):
        """Test to see if the return value is a dictionary
        """
        fName = "Victor"
        lName = "Ifezue"
        phoneNumber = "586-563-3934"
        phoneType = "Cell"
        val = createDictionary(fName,lName,phoneNumber,phoneType)
        self.assertDictEqual({"firstName": "Victor", "lastName": "Ifezue", "phoneNumber": "586-563-3934", "phoneType": "Cell"},val)
        
    def testIsDictionary(self):
        """Test to see if the dictionary contains the same values
        """
        fName = "Victor"
        lName = "Ifezue"
        phoneNumber = "586-563-3934"
        phoneType = "Cell"
        dictionary = {"firstName": "Victor", "lastName": "Ifezue", "phoneNumber": "586-563-3934", "phoneType": "Cell"}
        val = createDictionary(fName,lName,phoneNumber,phoneType)
        self.assertIsInstance(val,dict)
    