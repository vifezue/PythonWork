class Book:
    
    def __init__(self, bookAuthor, ISBN, numPurchased, bookTitle, numCheckedOut = 0, retailPrice = 0):
        """Creates the book class
        
        Arguments:
            author {string} -- the name of the creator of the book
            ISBN {int} -- ISBN
            numPurchased {int} -- number of book purchased total
            bookTitle {string} -- the name of the book title
            numCheckedOut {int} -- number of checked out book total
        
        Keyword Arguments:
            retailPrice {int} -- retail price (default: {0})
        """

        self.bookAuthor = bookAuthor
        self.bookISBN = ISBN
        self.numberPurchased = numPurchased
        self.numberCheckedOut = numCheckedOut
        self.price = retailPrice
        self.title = bookTitle        
    
    def addSetAuthor(self,val):
        """[set the book Author]
        
        Arguments:
            val {string} -- [new passed in author]
        """
        self.bookAuthor = val
         
    def getAuthor(self):
        """gets the author name
        
        Returns:
            [string] -- [returns the book author name]
        """
        return self.bookAuthor
    
    def setISBN(self, val):
        """[sets the ISBN]
        
        Arguments:
            val {int} -- [sets the ISBN]
        """
        self.bookISBN = val
        
    def getISBN(self):
        """[gets the ISBN of the book object]
        
        Returns:
            [int] -- [the ISBN of the book object]
        """
        return self.bookISBN
    
    def setNumPurchased(self, val):
        """sets the number of books purchased in the book object
        
        Arguments:
            val {int} -- [new number of purchased object]
        """
        self.numberPurchased = val
        
    def getNumPurchased(self):
        """gets the number of purchased books
        
        Returns:
            [int] -- number of books purchased
        """
        return self.numberPurchased
    
    def setNumCheckedOut(self, val):
        """set the number checkout of the book object
        
        Arguments:
            val {int} -- [new number value]
        """
        self.numberCheckedOut = val
        
    def getNumCheckout(self):
        """gets the number checked out of the book value
        
        Returns:
            [int] -- [returns the number checked out of the book object]
        """
        return self.numberCheckedOut
    
    def setPrice(self, val):
        """sets the price of the Book Object
        
        Arguments:
            val {int} -- [new price value]
        """
        self.price = val
        
    def getPrice(self):
        """gets the price value
        
        Returns:
            [int] -- [returns the price]
        """
        return self.price

    def getTitle(self):
        return self.title

    def setBookTitle(self, val):
        self.title = val

     

    
    
    