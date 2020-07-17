from classes.database_access import DB_Connect
from functions.funtionLibrary import *
from classes.clsBook import *


class clsTestLibrary(unittest.TestCase):
    
    def setUp(self):
        bookName = "Twilight"
        bookAuthor = "Victor Ifezue"
        bookID = 1
        ISBN = "9789610007258-9999"
        numPurchased = 10
        numCheckedOut = 2       
        self.my_Book = Book(bookAuthor,ISBN,numPurchased,numCheckedOut)