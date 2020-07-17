import tkinter as tk
from tkinter import filedialog
from utilFunctions.functions import *
import os
import datetime
import io

import time


my_db = DB_Connect('root', '', 'python_projects')

def importFile():
    
    addedCustomers = []   
    file = getDataFile()
    if not file == '':
        # backUpFile(file)
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
        
        
        
        



def getDataFile():
    
    root = tk.Tk()
    root.withdraw()

    try:
        file_path = filedialog.askopenfilename()
        if not file_path == '':
            return file_path
    except:
        return ''

def validate_string(val):
    if val != None:
        if type(val) is int:
            return str(val).encode('utf-8')
        else:
            return val
        
        
def backUpFile(filepath):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    today = str(datetime.date.today())
    targetfile = filepath
    os.rename(os.path.realpath(targetfile), os.path.realpath(targetfile)+"."+timestr)
   
    
importFile()