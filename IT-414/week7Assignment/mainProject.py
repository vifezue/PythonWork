import sys
import pymysql
import os
import os.path
from database_access import DB_Connect
from functions.functionLibrary import *
import json
from bs4 import BeautifulSoup

"""
    Victor Ifezue
    IT 414 - Tom Petz
    Week 7 - Database Automation Assignment
    
    This project cleans data from files like XML , JSON, CSV,
    and stores them into the crm_address database. The database has been 
    configured to autocommit upon connection. 
    Once the data is stored on crm_address table is renames it to
    crm_address_working.
"""

my_path = getPath()
xmlPath = os.path.join(my_path, "address_data.xml")
jsonPath = os.path.join(my_path, "address_data.json")
csvPath = os.path.join(my_path, "address_data.csv")

#create Address table
createAddressTable()

hasCompleted = False
while not hasCompleted:
    #Logic to determine which route based on user selection
    actionType = getAction()
    print(actionType + " selected!")

    if str(actionType).upper() == 'ADDRESS JSON DATA':
        if os.path.exists(jsonPath):
            addJsonFileToDatabase(jsonPath)
            print("JSON data imported successfully.")
        else:
            print("The JSON file does not exist.")

    if str(actionType).upper() == 'ADDRESS CSV DATA':
        if os.path.exists(csvPath):
            addCSVFileToDatabase(csvPath)
            hasCompleted = True
            print("CSV data imported successfully.")
        else:
            print("The CSV file does not exist.")

    if str(actionType).upper() == 'ADDRESS XML DATA':
        if os.path.exists(xmlPath):
            addXMLFileToDatabase(xmlPath)
            hasCompleted = True
            print("XML data imported successfully.")
        else:
            print("The XML file does not exist.")

    hasCompleted = True
    
#renames the database and adds "_working"
renameDatabase()
