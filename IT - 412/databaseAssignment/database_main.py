import sys
import pymysql
from functions.funtionLibrary import *
from classes.database_access import DB_Connect
from classes.clsBook import *


my_db = DB_Connect('root', '', 'python_projects')
   

print("Welcome To The Library Database!\n")


hasCompleted = False
while not hasCompleted:
    actionType = getAction()
    print(actionType)

    if actionType == "Show All Books":

        """Show All Book is selected"""

        sqlStrSelect = selectAllSQLStr()
        results = my_db.executeSelectQuery(sqlStrSelect)
        count = len(results)
        if count > 0:
            for book in results:
                print("--------------------------------")
                for item in book:
                    print(str(item).upper() + " : "+ str(book[item]))
                    
        else:
            print("No books are in the database.")
            continue
            
    if actionType == "Add a book":

        """Add all Book is selected"""
                
        isValidBookTitle = False
        while not isValidBookTitle:
            bookTitle = input("Please enter the name of the book title: ")
            if is_null(bookTitle) == False:
                if checkInvalidChars(bookTitle) == True:
                    bookTitle = capTitles(bookTitle)
                    break
                else:
                    print("Invalid Book Title")
            else:
                print("Please try again and dont leave Book Title blank.")
                
        isValidBookAuthor = False
        while not isValidBookAuthor:
            author = input("Please enter the name of the book author: ")
            if is_null(author) == False:
                if hasNumbers(author) == False and checkInvalidChars(author) == True and hasNumbers(author) == False:
                    bookAuthor = capTitles(author)
                    break
                else:
                    print("Invalid Book Author")
            else:
                print("Please try again and dont leave Book Name blank.")

        isValidBookISBN = False
        while not isValidBookISBN:
            ISBN = input("Please enter the name of the book ISBN: ")
            if hasNumbers(ISBN) == True and len(str(ISBN)) == 13:
                print(len(ISBN))
                ISBN = format_isbn(str(ISBN))
                break
            else:
                print("Invalid Book ISBN\n")
                
        isValidNumPurchased = False
        while not isValidNumPurchased:
            numPurchased = input("Please enter the number of the books purchased: ")
            if hasNumbers(numPurchased) == True:
                break
            else:
                print("Invalid Number Purchased")
        
        my_book = Book(bookAuthor, ISBN, numPurchased, bookTitle, numCheckedOut = 0, retailPrice= 0)
        strSQLAddBook = buildInsertBookSQL(bookAuthor, str(ISBN), bookTitle, 0, numPurchased)
        my_db.executeQuery(strSQLAddBook)
        print("Book Added Successfully")

    if actionType == "Edit a book":
        
        """Edit a books value in the database"""
        isDone = False
        while not isDone:
            bookNameSTR = ""
            bookNameSTR = input("What is the name of the book that you would like to edit? ")
            if is_null(bookNameSTR) == False:
                strSql = selectBookSQLStr(bookNameSTR)
                bookVal = ""
                bookVal = my_db.executeSelectQuery(strSql)
                if len(bookVal) == 1:
                    for item in bookVal:
                        ID                  = item['bookID']
                        bookTitle           = item['bookTitle']
                        bookAuthor          = item['bookAuthor']
                        bookISBN            = item['ISBN']
                        numberCheckedOut    = item['numCheckedOut']
                        numberPurchased     = item['numPurchased']
                        bookPrice           = item['bookPrice']
                else:
                    print("Sorry but the book you are searching for is not in our database")
                    continue
                    
                actionBook = Book(bookAuthor,bookISBN, numberPurchased, bookTitle, numberCheckedOut, bookPrice)
                print("The book was found.")
                showColumnOptions()
                selAction = input("Please select the column to change by the number associated with the action: ") 
                if is_null(selAction) == False and hasLetters(selAction) == False:
                    columnToChange = getColumnSelection(int(selAction))
                    if not columnToChange == False:
                        newValueColumn = input("Please enter the new value for the column: ")
                        if is_null(newValueColumn) == False:
                            
                            if columnToChange == "bookAuthor" and selAction == 2:
                                """ book author"""
                                newValueColumn = capTitles(newValueColumn)
                            else:
                                print("Invalid Author value! Please try this step again.")
                                continue
                                
                            if columnToChange == "ISBN" and hasLetters(newValueColumn) == False and selAction == 3:
                                """ ISBN and formatting"""
                                newValueColumn = format_isbn(str(newValueColumn))
                            else:
                                print("Invalid ISBN value! Please try this step again.")
                                continue
                                
                            if columnToChange == "numPurchased" and hasLetters(newValueColumn)== False and selAction == 4:
                                """ Number Purchased"""
                                newValueColumn = int(newValueColumn)
                            else:
                                print("Invalid number purchased value! Please try this step again.")
                                continue
                                
                            if columnToChange == "numCheckedOut" and hasLetters(newValueColumn) == False and selAction == 5:
                                """Number Checked Out"""
                                newValueColumn = int(newValueColumn)
                            else:
                                print("Invalid Number checked out value! Please try this step again.")
                                continue
                            
                            if columnToChange == "bookTitle" and checkInvalidChars(newValueColumn) == False and selAction == 6:
                                """Book Title"""
                                newValueColumn = NoQuotes(newValueColumn)
                                continue
                            else:
                                print("Invalid book title value! Please try this step again.")
                            
                            if columnToChange == "bookPrice" and selAction == 7:
                                """Book Price"""
                                newValueColumn = float(newValueColumn)
                            else:
                                print("Invalid Number purchased value! Please try this step again.")
                                continue
        
                            editSQL = editSQLStr(columnToChange,newValueColumn,ID)
                            my_db.executeQuery(editSQL)
                            print("The change was successful.")
                            break
                        else:
                            print("Invalid entry. We cannot change the value to NULL. Please try this step again.")
                            continue
                    else:
                        print("The column you selected is invalid.Please try this step again")
                        continue
                else:
                    print("Invalid selection! Please try this step again.")
                    continue
            else:
                print("Invalid Book Name. Please verify your selected and try again.")
                continue                        
        
    if actionType == "Remove a book":
        
        """Delete a book from the database"""
        
        bookNameSTR = ""
        bookNameSTR = input("What is the name of the book that you would like to delete? ")
        if is_null(bookNameSTR) == False:
            strSql = selectBookSQLStr(bookNameSTR)
            bookVal = ""
            bookVal = my_db.executeSelectQuery(strSql)
            if len(bookVal) == 1:
                for item in bookVal:
                    ID = item['bookID']
                delSQLStr = removeBookSQLStr(ID)
                confirmation = input("Are you sure you want to remove this book? \n"+
                                    "Please enter Y for Yes and N for No:   ")
                if confirmation.lower() == "y":
                    my_db.executeQuery(delSQLStr)
                    print("The book was removed.")
                    continue
                else:
                    print("We aborted the deletion as requested.")
                    continue
            else:
                print("We could not find the specified book in the system.")
                continue
        else:
            print("The value you entered is invalid.")
            continue
            
    if actionType == "Exit Program":
        exit()
    