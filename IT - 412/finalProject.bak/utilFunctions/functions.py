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
from utilFunctions.functions import *
from classes.database_access import DB_Connect
from shutil import copyfile

# from classes.clsDataSet import *

my_db = DB_Connect('root', '', 'python_projects')

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
    invalidChars = ["!", "@", "#", "$", "%", "^", "&", "*",
                    "(", ")", "_", "=", "+", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\", ")"]
    for char in invalidChars:
        if char in string:
            return False
    return True


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
        return strString.replace("'", "''")
    else:
        return strString


def validate_str(self, passedStr):
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


def showActionOptions():
    """Prints user statement for input
    """
    print("What would you like to do? \n"
          + "Please type in your selection by the number" +
          "\n 1 - Import A New Data File " +
          "\n 2 - Show records in a database" +
            "\n 3 - Add a record" +
            "\n 4 - Edit a record" +
            "\n 5 - Quit the program")


def convert_csv(data):
    header = data[0][:-2] + ['type', 'date']
    with open('customers.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for count, pro in enumerate(data):
            if count == 0:
                print(pro)
                continue
            writer.writerow(pro)


def convert_json(data):
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

    with open('customers.json', 'w') as json_file:
        json.dump(total_dict, json_file)
            
    return json_file


def getAction():
    """Gets the user input and provides validation"""
    isValidAction = False
    while not isValidAction:
        showActionOptions()
        userAction = input()
        userAction = userAction.strip()
        if is_null(userAction) == False:
            if hasLetters(userAction) == False:
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


def getDatabaseName(val):
    """Gets the type of Action the user wants to do    
    Arguments:
        val {int} -- [user input]

    Returns:
        [string] -- [the action the user wants to do]
    """
    switch = {
        1: 'crm',
        2: 'mailings'
    }
    if val in switch:
        return switch.get(val)
    else:
        return False


def showDatabaseOptions():
    """Shows the database options for selection
    """
    print("Which database would you like to use? \n"
          + "Please type in your selection by the number" +
          "\n 1 - CRM " +
          "\n 2 - Mailings")


def getDataFile():
    """ Allows the user to select a file from their computer"""
    root = tk.Tk()
    root.withdraw()

    try:
        file_path = filedialog.askopenfilename()
        if not file_path == '' or file_path.__contains__('.txt') == True:
            return file_path
    except:
        return False


def validate_string(val):
    if val != None:
        if type(val) is int:
            return str(val).encode('utf-8')
        else:
            return val


def readDataFile(filepath):
    fileName = os.path.basename(filepath)
    fileObject = open(fileName, "r")
    return fileObject


def loadJsonToDatabase(file):

    json_data = open(file).read()
    json_obj = json.loads(json_data)

    for i, item in enumerate(json_obj):
        firstName = validate_string(item.get("firstName", None))
        lastName = validate_string(item.get("lastName", None))
        companyName = validate_string(item.get("companyName", None))
        address = validate_string(item.get("address", None))
        city = validate_string(item.get("city", None))
        county = validate_string(item.get("county", None))
        state = validate_string(item.get("state", None))
        zipcode = validate_string(item.get("zipCode", None))
        phone1 = validate_string(item.get("phone1", None))
        phone2 = validate_string(item.get("phone2", None))
        email = validate_string(item.get("email", None))
        customertype = validate_string(item.get("type", None))
        date = validate_string(item.get("date", None))
        sqlData = "INSERT INTO `crm_data` (fName,lName,address,city,state,zipcode,company,primaryPhone,secondaryPhone,emailAddress) VALUES (" + \
            firstName, lastName, companyName, address, city, county, state, zipcode, phone1, phone2, email, customertype, date + ")"
        print(sqlData)
        
def addItemToDatabase(item):
    firstName = NoQuotes(validate_string(item.get("firstName", None)))
    lastName = NoQuotes(validate_string(item.get("lastName", None)))
    companyName = NoQuotes(validate_string(item.get("companyName", None)))
    address = NoQuotes(validate_string(item.get("address", None)))
    city = NoQuotes(validate_string(item.get("city", None)))
    county = NoQuotes(validate_string(item.get("county", None)))
    state = NoQuotes(validate_string(item.get("state", None)))
    zipcode = NoQuotes(validate_string(item.get("zipCode", None)))
    phone1 = NoQuotes(validate_string(item.get("phone1", None)))
    phone2 = NoQuotes(validate_string(item.get("phone2", None)))
    email = NoQuotes(validate_string(item.get("email", None)))
    customertype = NoQuotes(validate_string(item.get("type", None)))
    date = NoQuotes(validate_string(item.get("date", None)))
    sqlData = "INSERT INTO `crm_data` (fName,lName,address,city,state,zipcode,company,primaryPhone,secondaryPhone,emailAddress) VALUES (" + \
        firstName, lastName, companyName, address, city, county, state, zipcode, phone1, phone2, email, customertype, date + ")"
    my_db.executeQuery(sqlData)
    

def importJsonFileCRMToDataBase(file):    
    addedCustomers = []
    
    json_data = open(file).read()
    json_obj = json.loads(json_data)
    
    for i, item in enumerate(json_obj):
        if len(addedCustomers) > 0: 
            for customer in addedCustomers:
                a = json.dumps(item)                   
                b = json.dumps(customer)
                if a == b == False:
                    addedCustomers.append(item)
                    addItemToDatabase(item)
                else:
                    continue
        else:
            addedCustomers.append(item)
            addItemToDatabase(item)
    else:
        print("Invalid File Type - Please select a text file and try again.")
                
def backUpFile(filepath):
    """Backs up selected file with datetime stamp
    
    Arguments:
        filepath {fileObject} -- the file selected
    """
    timestr = time.strftime("%Y%m%d-%H%M%S")
    today = str(datetime.date.today())
    
    if path.exists(filepath):
        src = path.realpath(filepath)
        dst = src+timestr
        shutil.copy(src,dst) 

    
def clean_data(passedFile):
    if passedFile == None:
        with open(passedFile, 'r') as file:
            file = file.readlines()
        newFile = []
        for count, line in enumerate(file):
            if count == 0:
                header = line.split('|')
                lin = [li.replace('#', '').strip() for li in header]
                newFile.append(lin)
            else:
                lin = [li.replace('#', '').strip()
                        for li in line.split('|')]
                newFile.append(lin)
        return newFile
    else:
        with open(passedFile, 'r') as file:
            file = file.readlines()
        newFile = []
        for count, line in enumerate(file):
            if count == 0:
                header = line.split('|')
                lin = [li.replace('#', '').strip() for li in header]
                newFile.append(lin)
            else:
                lin = [li.replace('#', '').strip()
                        for li in line.split('|')]
                newFile.append(lin)
        return newFile
    
def parseFile(file):
    backUpFile(file)
    cleanFile = clean_data(file)
    return file
    
    
    
