import sys
from functions.funtionLibrary import *

def buildInsertBookSQL(bookAuthor, ISBN, title, numCheckOut, numPurchased, price =0):
    """Build the Insert SQL query for execution
    
    Arguments:
        author {string} -- [the name of the author]
        ISBN {string} -- [ISBN]
        title {string} -- [Book Title]
    
    Keyword Arguments:
        numCheckOut {int} -- [number of books checked out] (default: {0})
        price {int} -- [the price of the book] (default: {0})
        numPurchased {int} -- [number of books purchased] (default: {0})
    
    Returns:
        [string] -- [SQL Insert Statement for a new Book record]
    """
    bookAuthor = NoQuotes(bookAuthor.strip())
    title = NoQuotes(title)
    
    sqlStr = "INSERT INTO bookStore (bookAuthor, ISBN, numPurchased, numCheckedOut, bookTitle, bookPrice) VALUES ("+ "'"+bookAuthor+"',"+"'"+str(ISBN).strip()+"',"+"'"+str(numPurchased).strip()+"',"+"'"+str(numCheckOut).strip()+"',"+"'"+title+"',"+"'"+str(price).strip()+"')"
    return sqlStr

def capTitles(value):
    """Capatalizes and returns the passed in string
    
    Arguments:
        value {string} -- passed in string
    
    Returns:
        [string] -- [string in caps]
    """
    return str(value).title()

def checkInvalidChars(string):
    """Checks if passed in string has an invalid character
    
    Arguments:
        string {string} -- string
    
    Returns:
        Boolean -- True or false based on the condition
    """
    isValid = True
    invalidChars = ["!","@","#","$","%","^","&","*","(",")","_","=","+","<",">","/","?",";",":","[","]","{","}","\\",")"]
    for char in invalidChars:
        if char in string:
            return False
    return True

def editSQLStr(column, newValue, bookID):
    """Build the UPDATE SQL query for the database
    
    Arguments:
        column {string} -- [the column needing an update]
        newValue {string} -- [the new value]
        bookID {string} -- [the books ID]
    
    Returns:
        [type] -- [description]
    """ 
    newValue = NoQuotes(newValue)
    sqlStr = "UPDATE bookStore SET " +column+ " = "+"'"+newValue+"' WHERE bookID =" +"'"+str(bookID)+"'"
    return sqlStr

def format_isbn(isbn):
    """Formated the ISBN
    
    Arguments:
        isbn {string} -- [passed in ISBN]
    
    Returns:
        [string] -- [returns the ISBN in proper format]
    """
    try:
        return "-".join([isbn[0:3], isbn[3], isbn[4:7], isbn[7:12], isbn[12]])
    except:
        return False    

def getAction():
    """Gets the user input and provides validation"""
    isValidAction = False
    while not isValidAction:
        showActionOptions()
        userAction = input()
        userAction = userAction.strip()
        if is_null(userAction) == False: 
            if hasLetters(userAction)== False:
                if getActionSelection(int(userAction)) == False:
                    print("Invalid Entry - Please Try Again")
                else:
                    if hasNumbers(userAction) == True:
                        val = getActionSelection(int(userAction))
                        return val
            else:
                print("Invalid Entry - Please Try Again")
        else:
            print("Invalid Entry - Please Try Again")

def getActionSelection(val):
    """Gets the type of Action the user wants to do
    
    Arguments:
        val {int} -- [user input]
    
    Returns:
        [string] -- [the action the user wants to do]
    """
    switch={
                1:'Show All Books',
                2:'Add a book',
                3:'Edit a book',
                4:'Remove a book',
                5:'Exit Program'
    }
    if val in switch:
        return switch.get(val)
    else:
        return False

def getColumnSelection(val):
    """Gets the column by user selection
    
    Arguments:
        val {int} -- the number entered in by the user for selection
    
    Returns:
        [string] -- [the column name]
    """
    switch={
                1:'bookID',
                2:'bookAuthor',
                3:'ISBN',
                4:'numPurchased',
                5:'numCheckedOut',
                6:'bookTitle',
                7:'bookPrice'
    }
    if val in switch:
        return switch.get(val)
    else:
        return False
    
def hasNumbers(inputString):
    """Checks if the string has numbers and returns boolean
        
    Arguments:
        inputString str -- passed in string
        
    Returns:
        boolean -- True if exist and False is str does not exist
    """
    return any(char.isdigit() for char in inputString)

def hasLetters(inputString):
    """Checks if the string has numbers and returns boolean
      
    Arguments:
        inputString str -- passed in string
        
    Returns:
        boolean -- True if exist and False if number does not exist
    """
    return any(char.isalpha() for char in inputString)

    
def is_null(val):
    """Checks for a Null Value and returns Boolean
    
    Arguments:
        val {any} -- [passed in value]
    
    Returns:
        [boolean] -- True or False
    """
    try:            
        if val == "":
            return True
        else:
            return False 
    except:
        return False

def NoQuotes(strString):
    """Fixes Quoted string
    
    Arguments:
        strString {string} -- [passed in string]
    
    Returns:
        [string] -- [returns string with formatted quotes]
    """
    if is_null(strString) == True:
        strString = ''
    if ('\'') in strString:
        return strString.replace("'","")
    else:
         return strString

def removeBookSQLStr(bookID):
    """Build SQL String to remove the book from the database
    
    Arguments:
        bookID {string} -- Passed in Book unique identifier
    
    Returns:
        [string] -- [return formatted SQL String for execution to delete a record]
    """
    sqlStr = "DELETE from bookStore WHERE bookID =" +"'"+str(bookID).strip()+"'"
    return sqlStr

def showActionOptions():
    """Prints user statement for input
    """
    print("What would you like to do? \n"
            +"Please type in your selection by the number"+
            "\n 1 - Show All Books "+
            "\n 2 - Add a book "+
            "\n 3 - Edit a book "+
            "\n 4 - Remove a book"+
            "\n 5 - Exit Program")

def showColumnOptions():
    """Prints user statement for input
    """
    print("What would you like to do? \n"
            +"Please type in your selection by the number"+
            "\n 1 - Book ID "+
            "\n 2 - Book Author "+
            "\n 3 - ISBN "+
            "\n 4 - Number Purchased"+
            "\n 5 - Number Checked Out"+
            "\n 6 - Book Title"+
            "\n 7 - Book Price")    

def selectAllSQLStr():
    """Build the Select All SQL String
    
    Returns:
        [string] -- Select All SQL String
    """
    sqlData = "SELECT "+" * FROM bookStore"
    return sqlData

def selectBookSQLStr(bookTitle):
    """Build the Select the book
    
    Returns:
        [Book] -- Select All SQL String
    """
    bookTitle = NoQuotes(bookTitle)
    sqlData = "SELECT"+" * FROM bookStore where bookTitle = '" + bookTitle.strip()  + "'"
    return sqlData

def showAllBooks(data):
    """Shows all book title in the database and prints them out
    
    Arguments:
        data {collection} -- passed in collection of data
    """
    for item in data:
        print(item[0]),
        print(item[1]),
        print(item[2]),
        print(item[3]),
        print(item[4]),
        print(item[5]),
        print(item[6])

def validate_str(self,passedStr):
    """Validates the string and make sure its only a string and returns boolean
            
    Arguments:
        passedStr {string} -- user entry entered string
        
    Returns:
        boolean -- True or False
    """
    if passedStr == "" or hasNumbers(passedStr):
        return False
    else:
        try:
            string_ok = isinstance(passedStr, str)
            if string_ok == True:
                passedStr = passedStr.strip()
                return True
            else:
                return False
        except:
            return True

# def progress(count, total, status=''):
#     bar_len = 60
#     filled_len = int(round(bar_len * count / float(total)))

#     percents = round(100.0 * count / float(total), 1)
#     bar = '=' * filled_len + '-' * (bar_len - filled_len)

#     sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
#     sys.stdout.flush()

            
