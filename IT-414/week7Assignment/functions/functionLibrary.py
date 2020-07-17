import sys
import platform
import os
import json
from bs4 import BeautifulSoup
import csv
from database_access import *
import xmltodict


def getAction():
    """Gets the user input and provides validation"""
    isValidAction = False
    while not isValidAction:
        # SHOWS THE ACTIONS TO THE CHOSEN METHOD
        showActionOptions()
        userAction = input()
        userAction = userAction.strip()
        if is_null(userAction) == False and userAction != None:
            # MAKES SURE THE CORRECT VALUE WAS ENTERED
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
        1: 'ADDRESS CSV DATA',
        2: 'ADDRESS JSON DATA',
        3: 'ADDRESS XML DATA'
    }
    if val in switch:
        return switch.get(val)
    else:
        return False


def getPath():
    try:
        my_system = platform.system()

        if my_system == "Windows":
            root_fs = "C:\\IT414-VictorIfezue\week7Assignment"
        else:
            root_fs = "/IT414-VictorIfezue/week7Assignment"

        final_filepath = os.path.join(root_fs, "textFiles")
        return final_filepath
    except Exception as error:
        print(error)


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


def noQuotes(strString):
    """Fixes Quoted string

    Arguments:
        strString {string} -- [passed in string]

    Returns:
        [string] -- [returns string with formatted quotes]
    """
    if is_null(strString) == True:
        strString = ''
    if ('\'') in strString:
        return strString.replace("'", "")
    else:
        return strString


def showActionOptions():
    """Prints user statement for input
    """
    print("What data would you like to import? \n"
          + "Please type in your selection by the number" +
            "\n 1 - ADDRESS CSV DATA" +
            "\n 2 - ADDRESS JSON DATA" +
            "\n 3 - ADDRESS XML DATA")


def validate_string(val):
    """Validates string"""
    if val != None:
        if type(val) is int:
            return str(val).encode('utf-8')
        else:
            return val


def addDictToDatabase(item):
    """Adds the Json Item to the CRM_Address   
    Arguments:
        item -- dictionary Item
    """
    my_db = DB_Connect('root', '', 'python_projects')

    firstName = noQuotes(validate_string(item.get('first_name', None)))
    lastName = noQuotes(validate_string(item.get("last_name", None)))
    street = noQuotes(validate_string(item.get("street", None)))
    city = noQuotes(validate_string(item.get("city", None)))
    state = noQuotes(validate_string(item.get("state", None)).upper())
    zipCode = noQuotes(validate_string(item.get("zip", None)))

    sqlOutput = ("INSERT INTO crm_address (first_name,last_name, street,city,state,zip) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')").format(
        firstName, lastName, street, city, state, zipCode)
    try:
        my_db.executeQuery(sqlOutput)

    except Exception as error:
        print("The command " + sqlOutput +
              " failed to write to the crm_address database.")
        print(error)


def addJsonFileToDatabase(jsonFile):
    json_data = open(jsonFile).read()
    json_list = json.loads(json_data)

    for value, customer in enumerate(json_list):
        addDictToDatabase(customer)


def addXMLFileToDatabase(xmlFile):
    xmlData = open(xmlFile, encoding="utf-8")
    xmlText = xmlData.read()
    myXML = BeautifulSoup(xmlText, "lxml")
    address = myXML.find_all("entry")

    for item in address:
        info = item.get_text()
        addressArray = str(info).split("\n")
        addressArray.remove('')
        addressArray.remove('')

        dictAddress = {
            'first_name': str(addressArray[0]),
            'last_name': str(addressArray[1]),
            'street': str(addressArray[2]),
            'city': str(addressArray[3]),
            'state': str(addressArray[4]),
            'zip': str(addressArray[5])
        }

        addDictToDatabase(dictAddress)


def addCSVFileToDatabase(csvFile):
    with open(csvFile, newline='') as csvData:
        reader = csv.DictReader(csvData)
        for row in reader:
            addDictToDatabase(row)


def renameDatabase():
    my_db = DB_Connect('root', '', 'python_projects')
    
    sqlDropTable = 'DROP TABLE `crm_address_working`;'
    my_db.executeQuery(sqlDropTable)
    
    my_db.executeQuery("START TRANSACTION")

    my_db.executeQuery(
        "RENAME TABLE python_projects.crm_address TO python_projects.crm_address_working")

    my_db.executeQuery("COMMIT")


def createAddressTable():
    my_db = DB_Connect('root', '', 'python_projects')    

    try:
        sqlDropTable = 'DROP TABLE `crm_address`;'
        my_db.executeQuery(sqlDropTable)
    except:
        pass
    

    sqlCreateTable = '''CREATE TABLE `crm_address` (
                `id` int(11) NOT NULL,
                `first_name` varchar(50) NOT NULL,
                `last_name` varchar(50) NOT NULL,
                `street` varchar(250) NOT NULL,
                `state` varchar(50) NOT NULL,
                `city` varchar(100) NOT NULL,
                `zip` varchar(5) NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'''
    my_db.executeQuery(sqlCreateTable)

    sqlAlter1 = 'ALTER TABLE `crm_address` ADD PRIMARY KEY (`id`);'
    my_db.executeQuery(sqlAlter1)

    sqlAlter2 = 'ALTER TABLE `crm_address` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;'
    my_db.executeQuery(sqlAlter2)
