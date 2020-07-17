from functions.regex_functions import *
import unittest


class testFunctions(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def testValidCreditCards(self):
        creditCardList = ['4556799984114',
                          '4024007190958',
                          '4485 417 07 4720']
        for card in creditCardList:
            value = isValidCreditCard(card)
            self.assertTrue(value)

    def testBadCreditCards(self):
        value = None
        badCreditCardList = ['55556799984114',
                             '09024007190958',
                             '12485 417 07 4720',
                             'victor',
                             'unit@test.com']
        for badCard in badCreditCardList:
            value = isValidCreditCard(badCard)
            self.assertFalse(value)

    def testValidAmounts(self):
        value = None
        amounts = ['$5,160',
                   '$7,949',
                   '$7,902',
                   '$8,134']
        for amount in amounts:
            value = isValidAmount(amount)
            self.assertTrue(value)

    def testInvalidAmounts(self):
        value = None
        badAmounts = ['$5160',
                      '$7,949,975',
                      '$902',
                      '$8',
                      'Victor',
                      'test@example.com']
        for badAmount in badAmounts:
            value = isValidAmount(badAmount)
            self.assertFalse(value)

    def testValidCoordinates(self):
        value = None
        amounts = ['-24.97415, -94.2243',
                   '-2.32626, 7.11829',
                   '70.37374, 88.5683',
                   '-56.23146, -12.22482']
        for amount in amounts:
            value = isValidCoordinates(amount)
            self.assertTrue(value)
            
    
    def testBadCoordinates(self):
        value = None
        amounts = ['-24.apple, -94.2243',
                   '-2.32626 7.11829',
                   '70.37374 and 88.5683',
                   '-56.23146 && -12.22482',
                   'Maple Tree',
                   'test@example.com']
        for amount in amounts:
            value = isValidCoordinates(amount)
            self.assertTrue(value)
