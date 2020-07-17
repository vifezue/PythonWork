import unittest
from classes.clsBook import Book

class TestBookClass(unittest.TestCase):
    """ Test the Book Class """    
    def setUp(self):
        """Create an instance of the Book class for testing all class functions"""
        self.my_book = Book("Leyla Ali",9999999999999,9,"The Greatest",1, 14.99)

        
    def testGetAuthor(self):
        """Tests getting the book Author"""
        val = self.my_book.getAuthor()
        print(val)
        self.assertEqual("Leyla Ali",str(val))

    def testGetISBN(self):
        """Test getiing the ISBN"""
        val = self.my_book.getISBN()
        self.assertEqual(9999999999999,val)
    
    def testGetNumberPurchased(self):
        """Test Getting the number Purchased"""
        val = self.my_book.getNumPurchased()
        self.assertEqual(9,val)

    def testGetNumberCheckedout(self):
        """Test Getting the number checked out"""
        val = self.my_book.getNumCheckout()
        self.assertEqual(1,val)

    def testGetPrice(self):
        """Test getting the book price"""
        val = self.my_book.getPrice()
        self.assertEqual(14.99,val)
    
    def testGetTitle(self):
        """Test getting the book title"""
        val = self.my_book.getTitle()
        self.assertEqual("The Greatest",val)
    
    def testSetISBN(self):
        """Testing setting the ISBN"""
        self.my_book.setISBN("8888888888888")
        self.assertEqual("8888888888888",self.my_book.bookISBN)

    def testSetNumPurchased(self):
        """Testing setting the Number Purchased"""
        self.my_book.setNumPurchased(2)
        self.assertEqual(2,self.my_book.numberPurchased)
        
    def testSetPrice(self):
        """Testing setting the Price"""
        self.my_book.setPrice("8888888888888")
        self.assertEqual("8888888888888",self.my_book.price)

    def testSetBookTitle(self):
        """Testing setting the Book Title"""
        self.my_book.setBookTitle("Book Title")
        self.assertEqual("Book Title",self.my_book.title)
    