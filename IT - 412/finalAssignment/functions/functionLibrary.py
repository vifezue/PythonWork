import pymysql
import io
import json
import csv
import re
import time
import json
import os.path
import tkinter as tk
import datetime
import shutil
import os
from os import path
from tkinter import filedialog
from shutil import copyfile
from classes.database_access import DB_Connect

my_db = DB_Connect('root', '', 'python_projects')

def addItemToCRMDatabase(item):
    """Service Controller to add data to the database by either a manual process or import        
    Arguments:
        item -- json
    """             
    firstName = NoQuotes(validate_string(item.get("firstName", None)))
    lastName = NoQuotes(validate_string(item.get("lastName", None)))
    companyName = NoQuotes(validate_string(item.get("companyName", None)))
    address = NoQuotes(validate_string(item.get("address", None)))
    city = NoQuotes(validate_string(item.get("city", None)))
    state = NoQuotes(validate_string(item.get("state", None)))
    zipcode = NoQuotes(validate_string(item.get("zipCode", None)))
    phone1 = NoQuotes(validate_string(item.get("phoneNumber", None)))
    phone2 = NoQuotes(validate_string(item.get("secondaryPhone", None)))
    email = NoQuotes(validate_string(item.get("email", None)))
    
    if is_null(item.get("type")) == True or len(item.get("type")) == 0 or item.get("type") == None:
        customerType = "New"
    else: pass
    
    if is_null(item.get("date")) == True or len(item.get("date"))== 0 or item.get("date") == None:
        date = str(datetime.date.today())
    else: pass
            
    state = state.capitalize()
    
    """ADD TO CRM_DATA DATABASE"""
    try:
        sqlOutput = ("INSERT INTO crm_data (fName,lName,address,city,state,zipcode,company, primaryPhone,secondaryPhone,emailAddress, customerType, emtryDate) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')").format(
            firstName, lastName, address, city, state, zipcode, companyName, phone1, phone2, email, customerType, date)
        my_db.executeQuery(sqlOutput)
    except Exception as error:
        print("The command " + sqlOutput + " failed to write to the crm_data database.")
        print(error)
        
def addItemToAllDatabases(item):
    """Adds the Json Item to the database"""
    
    """ADD TO CRM_DATA DATABASE"""
    
    try:
        addToCRMDatabase(item)   
    except Exception as error:
        print(error)
    
    """ADD TO MAILING DATABASE"""    
    try:
        addItemToMailingDatabase(item)
    except Exception as error:
        print(error)        
    
def addToCRMDatabase(item):    
    """Adds the Json Item to the CRM_Database    
    Arguments:
        item -- json
    """    
    firstName = NoQuotes(validate_string(item.get('first_name', None)))
    lastName = NoQuotes(validate_string(item.get("last_name", None)))
    companyName = NoQuotes(validate_string(item.get("company_name", None)))
    address = NoQuotes(validate_string(item.get("address", None)))
    city = NoQuotes(validate_string(item.get("city", None)))
    county = NoQuotes(validate_string(item.get("county", None)))
    state = NoQuotes(validate_string(item.get("state", None)).upper())
    zipcode = NoQuotes(validate_string(item.get("zip", None)))
    phone1 = NoQuotes(validate_string(item.get("phone1", None)))
    phone2 = NoQuotes(validate_string(item.get("phone2", None)))
    
    if hasLetters(zipcode) == True:
        zipcode = "00000"        
    
    if phone2 == None:
        phone2 = "None"
        
    email = NoQuotes(validate_string(item.get("email", None)))
    
    # customertype = NoQuotes(validate_string(item.get("type", None)))
    # date = NoQuotes(validate_string(item.get("date", None)))
    
    if is_null(item.get("type")) == True or len(item.get("type")) == 0 or item.get("type") == None:
        customerType = "New"
    else:
        customerType = NoQuotes(validate_string(item.get("type", None)))
    
    if is_null(item.get("date")) == True or len(item.get("date"))== 0 or item.get("date") == None:
        date = str(datetime.date.today())
    else:
        date = NoQuotes(validate_string(item.get("date", None)))
    
    """ADD TO CRM_DATA DATABASE"""
    
    sqlOutput = ("INSERT INTO crm_data (fName,lName,address,city,state,zipcode,company, primaryPhone,secondaryPhone,emailAddress, customerType, entryDate) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')").format(firstName, lastName, address, city, state, zipcode, companyName, phone1, phone2, email, customerType, date)    
    try:
        my_db.executeQuery(sqlOutput)
        
    except Exception as error:
        print("The command " + sqlOutput + " failed to write to the crm_data database.")
        print(error)

def addItemToMailingDatabase(item, insertFlag = 0):
    """Adds the Json Item to the database    
    Arguments:
        item -- json
    """ 
    if insertFlag == 0:
        firstName = NoQuotes(validate_string(item.get('first_name', None)))
        lastName = NoQuotes(validate_string(item.get("last_name", None)))
        companyName = NoQuotes(validate_string(item.get("company_name", None)))
        address = NoQuotes(validate_string(item.get("address", None)))
        city = NoQuotes(validate_string(item.get("city", None)))
        state = NoQuotes(validate_string(item.get("state", None)).upper())
        zipcode = NoQuotes(validate_string(item.get("zip", None)))
        name = firstName.title() +" "+ lastName.title()
        fulladdress = str(address) + " "+ str(city)+ " " + str(state) + " " + str(zipcode)
    else:
        name = NoQuotes(validate_string(item.get('name', None)))
        companyName = NoQuotes(validate_string(item.get("company", None)))
        fulladdress = NoQuotes(validate_string(item.get("address", None)))

    """ADD TO MAILING DATABASE"""    
    try:
        sqlMailOutput = ("INSERT INTO MAILINGS (name,company,address) VALUES ('{0}','{1}','{2}')").format(name, companyName, fulladdress)
        my_db.executeQuery(sqlMailOutput)
    except Exception as error:
        print("The command " + sqlMailOutput + " failed to write to the mailing database.")
        print(error)

def backUpFile(filepath):
    """Backs up selected file with datetime stamp    
    Arguments:
        filepath {fileObject} -- the file selected
    """
    timestr = time.strftime("%Y%m%d-%H%M%S")
    today = str(datetime.date.today())
    
    try:
        if path.exists(filepath):
            src = path.realpath(filepath)
            dst = src+timestr
            shutil.copy(src, dst)
    except Exception as error:
        print(error)    


def convert_csv(data):
    """Converts the passed in file to a CSV File    
    Arguments:
        data {txtFile} -- [passed in text file]
    """
    
    if data != None:
        header = data[0][:-2] +  ['customerType', 'entryDate']
        with open('textfiles\customers.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for count, pro in enumerate(data):
                if count == 0:
                    continue
                writer.writerow(pro)
    else:
        print("Please enter a valid file.")


def convert_json(data):
    """ Converts the data into a Json """

    if data != None:
        total_dict = []
        keys = [d for d in data[0]]
        all_keys = keys[:-2] + ['type', 'date']
        index_dict = {}
        for index, key in zip(range(13), all_keys):
            index_dict[str(index)] = key
        for count, line in enumerate(data):
            dict_now = {}
            for coun, lin in enumerate(line):
                coun = str(coun)
                dict_now[index_dict[coun]] = lin
            total_dict.append(dict_now)

    with open('textfiles\customers.json', 'w') as json_file:
        json.dump(total_dict, json_file)
        
def enterMailingInfo():
    """Data Collection for the Mailing Information Database
       Collects the data for entry
    
    Returns:
        Nothing
    """
    isCollecting = True
    while isCollecting:
        firstName = getFirstName()
        if firstName == False:
            print('The customer record was not entered.')
            break
        
        lastName = getLastName()
        if lastName == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        
        companyName = getCompanyName()
        if companyName == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        
        address = getAddress()
        if address == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        
        city = getCity()
        if city ==  False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        
        state = getState()
        if state == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        
        zipCode = getZipCode()
        if zipCode == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break        
        
        Name = NoQuotes(firstName.title()) + " " + NoQuotes(lastName.title())
        companyName = NoQuotes(companyName.title())
        fulladdress = NoQuotes(str(address) + " "+ str(city)+ " " + str(state) + " " + str(zipCode))

        mailingDetails = {'name': Name,'company': companyName, 'address': fulladdress}
        return mailingDetails   
        
def getAction():
    """Gets the user input and provides validation"""
    isValidAction = False
    while not isValidAction:
        #SHOWS THE ACTIONS TO THE CHOSEN METHOD
        showActionOptions()
        userAction = input()
        userAction = userAction.strip()
        if is_null(userAction) == False and userAction != None:
            #MAKES SURE THE CORRECT VALUE WAS ENTERED
            if hasLetters(userAction) == False:
                if getActionSelection(int(userAction)) == False:
                    print("Invalid Entry - Please Try Again")
                    continue
                else:
                    if hasNumbers(userAction) == True:
                        val = getActionSelection(int(userAction))
                        return val
            else:
                print("Invalid Entry - Please Try Again")
                continue
        else:
            print("Invalid Entry - Please Try Again")
            continue
        
def getActionSelection(val):
    """Gets the type of Action the user wants to do

    Arguments:
        val {int} -- [user input]

    Returns:
        [string] -- [the action the user wants to do]
    """
    switch = {
        1: 'Import A New Data File',
        2: 'Show records in a database',
        3: 'Add a record',
        4: 'Edit a record',
        5: 'Quit the program'
    }
    if val in switch:
        return switch.get(val)
    else:
        return False
    
def getAddress():
    """Get the address information
    
    Returns:
        string -- address information
    """
    address_not = '!"\\@$%^&*_=+<>?;[]{\}\''
    print('To Exit, enter "EXIT"')
    while True:
        flagged = 0
        address = input('Please enter the Street Address: ').replace("'","\\")
        if address.strip().lower() == 'exit':
            print('Your are now exiting the application service.')
            return False
        
        if len(address.strip()) != 0 and address != None and is_null(address) == False:                
            for val in address:
                if val.lower() in address_not:
                    message = str(val)
                    print("Invalid character + (" + message + ") | Please try again.")
                    flagged += 1
                    break            
        else:
            print('Please enter a value for address.')
            continue
        
        if flagged == 0:
            return address
        else:
            continue
        
def getCompanyName():
    """Gets the company information
    
    Returns:
        string -- company information
    """
    print('To Exit, enter "EXIT"')
    while True:
        flagged = 0
        companyName = input('Please enter the Company name: ').replace("'","\\")
        if companyName.strip().lower() == 'exit':
            print('Your are now exiting the application service.')
            return False
            break
        
        if len(companyName.strip()) != 0 and companyName != None and is_null(companyName) == False:                
            flagged = 0
        else:
            print('Please enter a value for last name.')
            flagged += 1
            continue
        
        if flagged == 0:
            return companyName
        else:
            continue
        
def getCRMColumnSelection(val):
    """Gets the type of Columns the user wants to do

    Arguments:
        val {int} -- [user input]

    Returns:
        [string] -- [the action the user wants to do]
    """
    switch = {
        1: 'fName',
        2: 'lName',
        3: 'address',
        4: 'city',
        5: 'state',
        6: 'zipcode',
        7: 'company',
        8: 'primaryPhone',
        9: 'secondaryPhone',
        10: 'emailAddress',
        11: 'all'
    }
    if val in switch:
        return switch.get(val)
    else:
        return False
    
def editSQLStr(column, newValue, GUID, database):
    """Build the UPDATE SQL query for the database
    
    Returns:
        [type] -- [description]
    """ 
    try:
        if database.upper() == "CRM_DATA":
            sqlStr = "UPDATE crm_data SET " + column + " = "+"'"+ newValue +"' WHERE crmID =" +"'"+str(GUID)+"'"
            return sqlStr 
            
        if database.upper() =="MAILINGS":
            sqlStr = "UPDATE mailings SET " + column + " = "+"'"+ newValue +"' WHERE mailID =" +"'"+str(GUID)+"'"
            return sqlStr
    except Exception as error:
        print(error)
    
def getMailColumnSelection(val):
    """Gets the type of Action the user wants to do

    Arguments:
        val {int} -- [user input]

    Returns:
        [string] -- [the action the user wants to do]
    """
    switch = {
        1: 'name',
        2: 'address',
        3: 'company',
        4: 'All'
    }
    if val in switch:
        return switch.get(val)
    else:
        return False
        

def getCustomerData():
    """Gathers the Data to enter and new Customer Record
    
    Returns:
        dict -- customerDetails
    """
    customerCollectionRunning = True
    while customerCollectionRunning:
        firstName = getFirstName()
        if firstName == False:
            print('The customer record was not entered.')
            break
        
        lastName = getLastName()
        if lastName == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        
        companyName = getCompanyName()
        if companyName == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        
        address = getAddress()
        if address == False:
            break
        
        city = getCity()
        if city ==  False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        
        state = getState()
        if state == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        
        zipCode = getZipCode()
        if zipCode == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        
        primaryPhoneNumber = getPhone()
        if primaryPhoneNumber == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        else:
            primaryPhoneNumber = phone_format(primaryPhoneNumber)
        
        print("Do you want to enter a secondary phone number? \n")
        val = input("Enter Y for Yes ONLY!: ")
        if val.lower() == "YES":
            secondaryPhoneNumber = getPhone()
            if secondaryPhoneNumber == False:
                print('The customer record was not entered. Returning to the Main Menu.')
                break
            else:
                secondaryPhoneNumber = phone_format(secondaryPhoneNumber)
        else:
            secondaryPhoneNumber = ""
        
        emailAddress = getEmailAddress()
        if emailAddress == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        
        state = NoQuotes(validate_string(state.capitalize()))
        firstName = NoQuotes(firstName.title())
        lastName = NoQuotes(lastName.title())
        companyName = NoQuotes(companyName.title())
        
        customerData = {'firstName': firstName, 'lastName': lastName, 'email': emailAddress, 'phoneNumber': primaryPhoneNumber, 'secondaryPhone': secondaryPhoneNumber,
                'address': address, 'zip': zipCode, 'state': state, 'city': city, 'companyName': companyName}        
        return customerData 
        
def getEmailAddress():
    """Gets the customers Email address from user entry
    
    Returns:
        [string] -- [emailadress]
    """
    email_not = '! " \' # $ % ^ & * ( )  = + , < > / ? ; : [ ] { } \\'
    print('To Exit, enter "EXIT"')
    while True:
        flagged = 0
        email = input('Please enter the email: ').replace("'","\\")
        if email.strip().lower() == 'exit':
            print('Your are now exiting the application service.')
            return False
        
        if len(email.strip()) != 0 and email != None and len(email) > 9 and len(email) < 12:                
            for val in email:
                if val.lower() not in email_not:
                    message = str(val)
                    print("Invalid character + (" + message + ") | Please try again.")
                    flagged += 1
                    break
                else:
                    pass             
        else:
            print('Please enter a value for Phone Number.')
            flagged += 1
            continue
        
        if flagged == 0:
            return email
        else:
            continue


def getDataFile():
    """Gets the data file from user input
    
    Returns:
        file -- returns a selected file
    """
    root = tk.Tk()
    root.withdraw()

    try:
        file_path = filedialog.askopenfilename()
        """UPLOAD FILE MAY APPEAR BEHIND OTHER SCREENS"""
        if file_path != None:
            if not file_path == '' or file_path.__contains__('.txt') == True:
                return file_path
    except Exception as error:
        print(error)
        return False
    

def getDatabaseName(val):
    """Gets the type of Action the user wants to do    
    Arguments:
        val {int} -- [user input]

    Returns:
        [string] -- [the action the user wants to do]
    """
    if val != None or is_null(val) == False:
        try: 
            switch = {
                1: 'crm_data',
                2: 'mailings'
            }
            
            if val in switch:
                return switch.get(val)
            else:
                return False
        except Exception as e:
            print(e)
    else:
        return False
    
def getCity():
    """Gets the City for customer 
    
    Returns:
        string -- City 
    """
    city_allowed = "abcdefghijklmnopqrstuvwxyz' "
    print('To Exit, enter "EXIT"')
    while True:
        flagged = 0
        city = input('Please enter the City name: ').replace("'","\\")
        if city.strip().lower() == 'exit':
            print('Your are now exiting the application service.')
            return False
        
        if len(city.strip()) != 0 and city != None:                
            for val in city:
                if val.lower() not in city_allowed:
                    message = str(val)
                    print("Invalid character + (" + message + ") | Please try again.")
                    flagged += 1
                    break
                else:
                    pass             
        else:
            print('Please enter a value for city.')
            continue
        
        if flagged == 0:
            return city
        else:
            continue
        
def getEmailAddress():
    
    """Gets the email address from user entry
    
    Returns:
        string -- email address
    """
    email_not = '! " \' # $ % ^ & * ( )  = + , < > / ? ; : [ ] { } \\'
    print('To Exit, enter "EXIT"')
    while True:
        flagged = 0
        email = input('Please enter the email: ').replace("'","\\")
        if email.strip().lower() == 'exit':
            print('Your are now exiting the application service.')
            return False
        
        if len(email.strip()) != 0 and email != None and len(email) > 4 and len(email) < 50 and email.__contains__("@"):                
            for val in email:
                if val.lower() in email_not:
                    message = str(val)
                    print("Invalid character + (" + message + ") | Please try again.")
                    flagged += 1
                    break
                else:
                    pass             
        else:
            print('Please enter a value for Phone Number.')
            flagged += 1
            continue
        
        if flagged == 0:
            return email
        else:
            continue    

def getFirstName():
    """Gets the first name
    
    Returns:
        string -- firstName
    """
    name = "abcdefghijklmnopqrstuvwxyz1234567890- '"
    print('To Exit, enter "EXIT"')
    while True:
        flagged = 0
        firstName = input('Please enter the first name: ').replace("'","\\")
        firstName = validate_string(firstName)
        if firstName.strip().lower() == 'exit':
            print('Your are now exiting the application service.')
            return False
        
        if len(firstName.strip()) != 0 and hasLetters(firstName) == True and is_null(firstName) == False:                
            for val in firstName:
                if val.lower() not in name:
                    message = str(val)
                    print("Invalid character + (" + message + ") | Please try again.")
                    flagged += 1
                    break
                else:
                    pass             
        else:
            print('Please enter a value for first name.')
            flagged += 1
            continue
        
        if flagged == 0:
            return firstName
        else:
            continue
        
def getLastName():
    """Gets the last name
    
    Returns:
        string -- lastName
    """
    name = "abcdefghijklmnopqrstuvwxyz1234567890- \'"
    print('To Exit, enter "EXIT"')
    while True:
        flagged = 0
        lastName = input('Please enter the last name: ').replace("'","\\")
        lastName = validate_string(lastName)
        if lastName.strip().lower() == 'exit':
            print('Your are now exiting the application service.')
            return False        
        if len(lastName.strip()) != 0 and hasLetters(lastName) == True and is_null(lastName) == False:                
            for val in lastName:
                if val.lower() not in name:
                    message = str(val)
                    print("Invalid character + (" + message + ") | Please try again.")
                    flagged += 1
                    break
                else:
                    pass             
        else:
            print('Please enter a value for last name.')
            flagged += 1
            continue
        
        if flagged == 0:
            return lastName
        else:
            continue
        
def getPhone():
    """Gets the Phone Numer
    
    Returns:
        string -- phoneNumber or secondaryPhone
    """
    charsAllowed = "1234567890"
    print('To Exit, enter "EXIT"')
    while True:
        flagged = 0
        phoneNumber = input('Please enter the Phone Number [with no dashes(-)]: ').replace("'","\\")
        phoneNumber = validate_string(phoneNumber)
        if phoneNumber.strip().lower() == 'exit':
            print('Your are now exiting the application service.')
            return False        
        if len(phoneNumber.strip()) != 0 and phoneNumber != None and len(phoneNumber) > 9 and len(phoneNumber) < 12:                
            for val in phoneNumber:
                if val.lower() not in charsAllowed:
                    message = str(val)
                    print("Invalid character + (" + message + ") | Please try again.")
                    flagged += 1
                    break
                else:
                    pass             
        else:
            print('Please enter a value for Phone Number.')
            continue
        
        if flagged == 0:
            return phoneNumber
        else:
            continue
        
def getState():
    """Gets the state by user entry
    
    Returns:
        string -- state
    """
    charsAllowed = "abcdefghijklmnopqrstuvwxyz"
    print('To Exit, enter "EXIT"')
    while True:
        flagged = 0
        state = input('Please enter the State (ex. Enter "MI" for Michigan) : ').replace("'","\\")
        state = validate_string(state)  
        if state.strip().lower() == 'exit':
            print('Your are now exiting the application service.')
            return False                      
        if len(state.strip()) != 0 and state != None and len(state) == 2:                
            for val in state:
                if val.lower() not in charsAllowed:
                    message = str(val)
                    print("Invalid character + (" + message + ") | Please try again.")
                    flagged += 1
                    break
                else:
                    pass             
        else:
            print('Please enter a value for state.')
            continue
        
        if flagged == 0:
            return state
        else:
            continue
        
def getZipCode():
    """Gets the ZipCode by user entry
    
    Returns:
        string -- zip
    """
    charsAllowed = "1234567890-"
    print('To Exit, enter "EXIT"')
    while True:
        flagged = 0
        zipCode = input('Please enter the ZIP Code name: ').replace("'","\\")
        zipCode = validate_string(zipCode)
        if zipCode.strip().lower() == 'exit':
            print('Your are now exiting the application service.')
            return False
        
        if len(zipCode.strip()) != 0 and zipCode != None and len(zipCode) > 4 and len(zipCode) < 11:                
            for val in zipCode:
                if val.lower() not in charsAllowed:
                    message = str(val)
                    print("Invalid character + (" + message + ") | Please try again.")
                    flagged += 1
                    break
                else:
                    pass             
        else:
            print('Please enter a value for zipCode.')
            continue
        
        if flagged == 0:
            return zipCode
        else:
            continue
    
def hasLetters(inputString):
    """Checks if the string has numbers and returns boolean

    Arguments:
        inputString str -- passed in string

    Returns:
        boolean -- True if exist and False if number does not exist
    """
    return any(char.isalpha() for char in inputString)


def hasNumbers(inputString):
    """Checks if the string has numbers and returns boolean

    Arguments:
        inputString str -- passed in string

    Returns:
        boolean -- True if exist and False is str does not exist
    """
    return any(char.isdigit() for char in inputString)
    
def is_null(val):
    """Checks for a Null Value and returns Boolean

    Arguments:
        val {any} -- [passed in value]

    Returns:
        [boolean] -- True or False
    """
    if val != None or is_null(val) == False:
        try:
            if val == "":
                return True
            else:
                return False
        except Exception as error:
            print(error)
            return False
    else:
        return False
    
def NoQuotes(strString):
    """Fixes Quoted string

    Arguments:
        strString {string} -- [passed in string]

    Returns:
        [string] -- [returns string with formatted quotes]
    """
    if strString != None or is_null(strString) == False:
        if is_null(strString) == True:
            strString = ''
        if ('\'') in strString:
            return strString.replace("'", "''")
        else:
            return strString
    else:
        pass     
                
def phone_format(number):
    """Formats the phone number entered
    
    Arguments:
        n {string} -- unformatted phone number
    
    Returns:
        [string] -- formatted phone number
    """
    number = validate_string(number)
    if number != None and is_null(number) == False and hasLetters(number) == True and str(number) != 'phone1' and str(number) != 'phone2':
        if is_null(number) == False:
            if number.count("-") == 0:
                try:
                    return format(int(number[:-1]), ",").replace(",", "-") + number[-1] 
                except Exception as error:
                    print(error)
                    return number
            else:
                return number
    else:
        "000-000-0000"
        
        
def serviceController(jsonFile):
    """
    DATA IMPORT SERVICE CONTROLLER
    """            
    json_data = open(jsonFile).read()
    json_list = json.loads(json_data)    
    
    """Adds each item to the databases"""
    for value, customer in enumerate(json_list):
        addItemToAllDatabases(customer)
        
def selectCRMSQLStr(firstName, lastName):
    """Build the Select the Customer Query

    Returns:
        [Name] -- Select All SQL String
    """
    
    if firstName != None or lastName != None:
        firstName = NoQuotes(firstName)
        lastName = NoQuotes(lastName)
        sqlData = "SELECT"+" crmID FROM CRM_DATA where fName = '" + firstName.strip()  + "' and lName = '" + lastName.strip()+"'"
        return sqlData

def selectMailingSQLStr(firstName, lastName):
    """Build the Select the Customer Query
    Returns:
        [Name] -- Select All SQL String
    """
    if firstName != None or lastName != None:
        firstName = NoQuotes(firstName)
        lastName = NoQuotes(lastName)
        sqlData = "SELECT"+" mailID FROM MAILINGS where name = '" + firstName.strip()  + " " + lastName.strip()+"'"
        return sqlData   
                
def showDatabaseOptions():
    """Shows the database options for selection
    """
    print("Which database would you like to use? \n"
          + "Please type in your selection by the number" +
          "\n 1 - CRM " +
          "\n 2 - Mailings")
    
def showActionOptions():
    """Prints user statement for input
    """
    print("------------------------------------------------------------")
    print("What would you like to do? \n"
          + "Please type in your selection by the number" +
            "\n 1 - Import A New Data File " +
            "\n 2 - Show records in a database" +
            "\n 3 - Add a record" +
            "\n 4 - Edit a record" +
            "\n 5 - Quit the program")
    
def showOptions():
    """Prints user statement for input
    """
    print("What would you like to do? \n"
          + "Please type in your selection by the number" +
            "\n 1 - Change First Name " +
            "\n 2 - Change Last Name" +
            "\n 3 - Change Address" +
            "\n 4 - Change City" +
            "\n 5 - Change State"+
            "\n 6 - Change ZipCode " +
            "\n 7 - Change Company Name" +
            "\n 8 - Change Primary Phone" +
            "\n 9 - Change Secondary Phone"+
            "\n 10 - Change Email Address"+
            "\n 11 - Change All Customer Record"
)

def showMailDataOptions():
    """Prints user statement for input
    """
    print("What would you like to do? \n"
          + "Please type in your selection by the number" +
            "\n 1 - Change Name " +
            "\n 2 - Change Address" +
            "\n 3 - Change Company Name" +
            "\n 4 - Change All Customers Record"
)

def showRecords(database):
    """Shows the database records"""    
    if database != None:
        sqlString = "SELECT * FROM " + database
        if database == "crm_data":
            try:
                results = my_db.executeSelectQuery(sqlString)
                for customer in results:
                    print("-------------------------------------------------------")
                    for item in customer:
                        print(str(item).upper() + " : "+ str(customer[item]).upper())
            except Exception as error:
                print(error)
        else:
            try:
                results = my_db.executeSelectQuery(sqlString)
                for customer in results:
                    print("-------------------------------------------------------")
                    for item in customer:
                        print(str(item).upper() + " : "+ str(customer[item]).upper())
            except Exception as error:
                print(error)

def updateCRMRecord():
    
    """Collects user entry and selects the GUID from the crm_data database by
        selecting the first and last name and returning the ID
        Allows the user to update the record by the ID

    Returns:
        Nothing
    """
    database = "CRM_DATA"
    print("Please select the customer to update!")
    isCollecting = True
    while isCollecting:     
        #COLLECTS DATA BY USER ENTRY TO QUERY THE DATABASE FOR THE RECORD TO UPDATE 
        firstName = getFirstName()
        if firstName == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        
        lastName = getLastName()
        if lastName == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break

        #QUERIES THE DATABASE
        selectNameQuery = selectCRMSQLStr(firstName, lastName)
        crmGUID = my_db.executeSelectQuery(selectNameQuery)

        #RETURNS THE GUID
        count = len(crmGUID)
        if count == 0:
            #CHECKS IF A CUSTOMER RECORD WAS RETURNED
            print('There is no such customer record based on your search.')
            val = input("Do you want to search again? Please enter Y for YES or any other key to EXIT")
            if val.lower() == "y":
                continue
            else:
                break   

        if count != 0:
            #PARSES OUT THE JUNK
            crmGUID = str(crmGUID)
            crmGUID = crmGUID.replace("[","")
            crmGUID = crmGUID.replace("]","")
            crmGUID = crmGUID.replace("crmID","")
            crmGUID = crmGUID.replace(":","")
            crmGUID = crmGUID.replace("{","")
            crmGUID = crmGUID.replace("}","")
            crmGUID = crmGUID.replace("''","")
            crmGUID = crmGUID.strip()
            
            #PRINTS THE SELECTED USER TO THE SCREEN
            query = ("SELECT * FROM CRM_DATA WHERE CRMID = '{0}'").format(str(crmGUID))
            results = my_db.executeSelectQuery(query)
            for customer in results:
                for item in customer:
                    print(str(item).upper() + " : "+ str(customer[item]))
            #CONFIRMATION OF THE UPDATE TO THE SELECTED RECORD
            confirmation = input("Are you sure you want to update this customer? \n" +
                                        "Please enter Y for Yes and N for No:   ")
            if confirmation.lower() == "y":
                #LOGIC FOR THE USER TO ENTER THE INFORMATION
                print('Enter the new updates for the customer')
                enteredCorrect = True
                while enteredCorrect:
                    showOptions()
                    inputNumber = input().replace("'","\\")
                    try:
                        selectedChoice = getCRMColumnSelection(int(inputNumber))
                    except:
                        selectedChoice =  False
                    
                    if selectedChoice == False:
                        print("Invalid Selection. Please Try again!")
                        continue
                    else:
                        break
                
                strSQL = ""
                if selectedChoice == "fName":
                    newFirstName = getFirstName()
                    sqlStr = editSQLStr(selectedChoice,newFirstName,crmGUID,database)
                    try:
                        my_db.executeQuery(sqlStr)
                        print('First Name updated successfully')
                        break
                    except Exception as error:
                        print(sqlStr + " failed.")
                        print(error)
                        break
                        
                if selectedChoice == "lName":
                    newLastName = getLastName()
                    sqlStr = editSQLStr(selectedChoice,newLastName,crmGUID,database)
                    try:
                        my_db.executeQuery(sqlStr)
                        print('Last Name updated successfully')
                        break
                    except Exception as error:
                        print(sqlStr + " failed.")
                        print(error)
                        break
                    
                if selectedChoice == "address":
                    newAddress = getAddress()
                    sqlStr = editSQLStr(selectedChoice,newAddress,crmGUID,database)
                    try:
                        my_db.executeQuery(sqlStr)
                        print('Address updated successfully')
                        break
                    except Exception as error:
                        print(sqlStr + " failed.")
                        print(error)
                        break
                if selectedChoice == "city":
                    newCity = getCity()
                    sqlStr = editSQLStr(selectedChoice,newCity,crmGUID,database)
                    try:
                        my_db.executeQuery(sqlStr)
                        print('City updated successfully')
                        break
                    except Exception as error:
                        print(sqlStr + " failed.")
                        print(error)
                        break
                if selectedChoice == "state":
                    newState = getState()
                    sqlStr = editSQLStr(selectedChoice,newState,crmGUID,database)
                    try:
                        my_db.executeQuery(sqlStr)
                        print('State updated successfully')
                        break
                    except Exception as error:
                        print(sqlStr + " failed.")
                        print(error)
                        break
                if selectedChoice == "zipcode":
                    newZipCode = getZipCode()
                    sqlStr = editSQLStr(selectedChoice,newZipCode,crmGUID,database)
                    try:
                        my_db.executeQuery(sqlStr)
                        print('ZipCode updated successfully')
                        break
                    except Exception as error:
                        print(sqlStr + " failed.")
                        print(error)
                        break
                if selectedChoice == "company":
                    newCompany = getCompanyName()
                    sqlStr = editSQLStr(selectedChoice,newCompany,crmGUID,database)
                    try:
                        my_db.executeQuery(sqlStr)
                        print('Company updated successfully')
                        break
                    except Exception as error:
                        print(sqlStr + " failed.")
                        print(error)
                        break
                if selectedChoice == "primaryPhone":
                    newPrimaryPhone = getPhone()
                    sqlStr = editSQLStr(selectedChoice,newPrimaryPhone,crmGUID,database)
                    try:
                        my_db.executeQuery(sqlStr)
                        print('Primary Phone updated successfully')
                        break
                    except Exception as error:
                        print(sqlStr + " failed.")
                        print(error)
                        break
                if selectedChoice == "secondaryPhone":
                    newSecondaryPhone = getPhone()
                    sqlStr = editSQLStr(selectedChoice,newSecondaryPhone,crmGUID,database)
                    try:
                        my_db.executeQuery(sqlStr)
                        print('Secondary Phone updated successfully')
                        break
                    except Exception as error:
                        print(sqlStr + " failed.")
                        print(error)
                        break
                if selectedChoice == "emailAddress":
                    newEmail = getEmailAddress()
                    sqlStr = editSQLStr(selectedChoice,newEmail,crmGUID,database)
                    try:
                        my_db.executeQuery(sqlStr)
                        print('Email Address updated successfully')
                        break
                    except Exception as error:
                        print(sqlStr + " failed.")
                        print(error)
                        break
                    
                if selectedChoice.upper() == "ALL":
                    updatedCustomer = getCustomerData()
                    
            #INSERTS INTO THE DATABASE                    
            if updatedCustomer == 1 and updatedCustomer != None and selectedChoice == "All":
                today = str(datetime.date.today())
                sqlUpdateCustomer = ('UPDATE `crm_data` SET fName={0},lName={1},address={2}, city={3}, state={4},zipcode={5},company={6},primaryPhone={7}\
                    ,secondaryPhone= {8},emailAddress={9}, customerType ={10} , entryDate ={11} WHERE `crmID` ={12}').format(
                                                                                            updatedCustomer['firstName'],
                                                                                            updatedCustomer['lastName'],
                                                                                            updatedCustomer['address'],
                                                                                            updatedCustomer['city'],
                                                                                            updatedCustomer['state'],
                                                                                            updatedCustomer['zip'],
                                                                                            updatedCustomer['companyName'],
                                                                                            updatedCustomer['phoneNumber'],
                                                                                            updatedCustomer['secondaryPhone'],
                                                                                            updatedCustomer['email'],
                                                                                            "Updated Recorded",
                                                                                            today,                                                                                                
                                                                                            str(crmGUID)
                                                                                            )
                try:
                    my_db.executeQuery(sqlUpdateCustomer)
                    print('All Records updated successfully')
                    break
                except Exception as error:
                    print(sqlUpdateCustomer + " failed.")
                    print(error)
            else:
                #IF MORE THEN ONE RECORD WAS FOUND
                print("Update failed to return a valid customer to update. Please try again!")
                value = input("Do you want to search again? Please enter Y for YES or any other key to EXIT")
                if value.lower() == "y":
                    continue
                else:
                    break   

def updateMailingsRecord():
    
    """Collects user entry and selects the GUID from the mailing database by
       selecting the first and last name and returning the ID
       Allows the user to update the record by the ID
    
    Returns:
        Nothing
    """
    database = "MAILINGS"
    isCollecting = True
    while isCollecting:
        #GETS FIRST NAME
        firstName = getFirstName()
        if firstName == False:
            print('The customer record was not entered.')
            break
        #GETS LAST NAME
        lastName = getLastName()
        if lastName == False:
            print('The customer record was not entered. Returning to the Main Menu')
            break
        #QUERYS THE DATABASE FOR THE NAME ENTERED
        selectNameQuery = selectMailingSQLStr(firstName, lastName)
        #GRABS THE GUID
        mailGUID = my_db.executeSelectQuery(selectNameQuery)
        #MAKE SURE A GUID WAS GRABBED
        count = len(mailGUID)       
        if count == 0:
            #NO CUSTOMER RECORD WAS FOUND
            print('There is no such customer record based on your search.\n')
            val = input("Do you want to search again? Please enter Y for YES or any other key to EXIT.\n")
            if val.lower() == "y":
                continue
            else:
                break
             
        if count == 1 and count < 2 and count != 0:
            #IF FOUND PARSES OUT THE DATA AND GET THE ID  IF ONLY 1 IS FOUND
            mailGUID = str(mailGUID)
            mailGUID = mailGUID.replace("[","")
            mailGUID = mailGUID.replace("]","")
            mailGUID = mailGUID.replace("mailID","")
            mailGUID = mailGUID.replace(":","")
            mailGUID = mailGUID.replace("{","")
            mailGUID = mailGUID.replace("}","")
            mailGUID = mailGUID.replace("''","")
            mailGUID = mailGUID.strip()            
            
            #PRINTS THE SELECTED USER TO THE SCREEN FOR DISPLAY
            query = ("SELECT * FROM MAILINGS WHERE mailID= {0}").format(mailGUID)
            results = my_db.executeSelectQuery(query)
            for customer in results:
                    for item in customer:
                        print(str(item).upper() + " : "+ str(customer[item]))
                        #CONFIRMATION OF THE UPDATE
            confirmation = input("Are you sure you want to update this customer? \n" +
                                    "Please enter Y for Yes and N for No:   \n")
            if confirmation.lower() == "y":
                enteredCorrect = True
                while enteredCorrect:
                    #SHOWS COLUMN LIST TO UPDATE FOR THE USERS SELECTION
                    showMailDataOptions()
                    inputNumber = input().replace("'","\\")
                    #MAKES SURE AN INTEGER WAS ENTERED
                    try:
                        #BUILDS SQL STRING
                        selectedChoice = getMailColumnSelection(int(inputNumber))
                    except:
                        selectedChoice =  False
                    
                    if selectedChoice == False:
                        print("Invalid Selection. Please Try again!")
                        continue
                    else:
                        break       
                print('Enter the new updates for the customer')
                #BUILD THE SQL STRING FOR THE EXEC PROC AND THE LOGIC FOR THE REQUIRED FIELD
                strSQL =""
                if selectedChoice.lower() == "name":
                    firstName = getFirstName()
                    
                    if firstName != False:
                        lastName = getLastName()
                    else: 
                        break
                        if lastName != False:                    
                            name = firstName + " "+ lastName
                        else:
                            break
                        #BUILD SQL STRING
                    strSQL = editSQLStr(selectedChoice,name,mailGUID,database)
                    try:
                        my_db.executeQuery(strSQL)
                        print('Name updated successfully') 
                        break
                    except Exception as error:
                        print(strSQL + " failed.")
                        print(error)
                        break
                 
                if selectedChoice.lower() == "address":
                    newAddress = getAddress()
                    newCity = getCity()
                    newState = getState()
                    newZipCode = getZipCode()
                    
                    fulladdress = str(newAddress + " "+ newCity+ " "+ newState.title()+" "+newZipCode)
                    strSQL = editSQLStr(selectedChoice,fulladdress,mailGUID,database)
                    try:
                        my_db.executeQuery(strSQL)
                        print('Address updated successfully') 
                        break
                    except Exception as error:
                        print(strSQL + " failed.")
                        print(error)
                        break
                    
                if selectedChoice.lower() == "company":
                    newCompany = getCompanyName()
                    strSQL = editSQLStr(selectedChoice,newCompany,mailGUID,database)
                    try:
                        my_db.executeQuery(strSQL)
                        print('Company Name updated successfully')
                        break
                    except Exception as error:
                        print(strSQL + " failed.")
                        print(error)
                        break     
                if selectedChoice.lower() == "all":
                    updatedMailInfo = enterMailingInfo()
            #ADDS TO THE DATABASE SQL USING A FORMATTED STRING AFTER VALIDATION
                if len(updatedMailInfo) == 3 and updatedMailInfo != None:
                    sqlUpdateMailInfo = ("UPDATE mailings SET name='{0}', address='{1}', company='{2}' WHERE mailID ='{3}'").format(
                                                                                    updatedMailInfo['name'],
                                                                                    updatedMailInfo['address'],
                                                                                    updatedMailInfo['company'],
                                                                                    mailGUID)
                    try:
                        my_db.executeQuery(sqlUpdateMailInfo)
                        print('All Records updated successfully')
                        return
                    except Exception as error:
                        print(sqlUpdateMailInfo + " failed.")
                        print(error) 
        else:
            #IF MORE THEN ONE RECORD IS FOUND IT GIVES ERROR THEN RETRY DIALOG
            print("Update failed to return a valid customer. Please try again!\n")
            value = input("Do you want to search again? Please enter Y for YES or any other key to EXIT")
            if value.lower() == "y":
                continue
            else:
                break
            
def validate_string(val):
    """Validates string"""
    if val != None:
        if type(val) is int:
            return str(val).encode('utf-8')
        else:
            return val  
