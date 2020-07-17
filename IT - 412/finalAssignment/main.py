import pymysql, io, json, csv, re, time, os.path, datetime, sys
from functions.functionLibrary import *
from classes.database_access import DB_Connect
from classes.clsDataSet import *

#DATABASE CONNECTION
my_db = DB_Connect('root', '', 'python_projects')

print("Welcome to the Customer Collection")

appRunning = True
while appRunning:
    
    #GETS THE ACTION SELECTED BY THE USER"""
    actionType = getAction()
    
    #PRINTS THE SELECTED ACTION TO THE SCREEN FOR VERIFICATION
    print(actionType.upper() + " IS NOW RUNNING!")
    
    #LOGIC TO EXECUTE USERS DESIRED ACTION TYPE    
    if str(actionType).upper() == "IMPORT A NEW DATA FILE":
        """IMPORTS THE NEW FILE INTO THE DATABASES SERVICE"""
        
        importFile = True
        while importFile:
            print("PLEASE SELECT THE NEW FILE")
            
            #GETS THE DATA FILE FROM A OPEN FILE DIALOG
            dataFile = getDataFile()
            
            #CHECKS TO SEE IF FILE IS A TXT FILE
            if not dataFile == False and dataFile.endswith( ".txt"):
                    try:
                        #PARSES THE SELECTED FILE AND CHECKS FOR DUPLICATES
                        newData = validateData(dataFile)
                        #BACKS UP THE FILE IN THE SAME FILE DIRECTORY
                        backUpFile(dataFile)
                        #CONVERTS THE FILE TO JSON
                        newData.convert_json()
                        #CONVERTS THE FILE TO CSV
                        newData.convert_csv()
                        #TRUNCATES THE DATABASE TABLES
                        my_db.executeQuery('TRUNCATE TABLE crm_data')
                        my_db.executeQuery('TRUNCATE TABLE mailings')
                        #IMPORT THE DATA INTO THE DATABASE CONTROLLER
                        serviceController('textfiles\customers.json')
                        print("CRM and Mailings Databases Records have been loaded successfully!")
                        break                
                    except Exception as error:
                        print(error)
                        print("The import process failed. Please try this step again.")
                        break
            else:
                print("The file for the import process is not accepted. Please upload a valid .txt file!")
                break
                    
    if str(actionType).upper() == "ADD A RECORD":
        """ADDS A NEW RECORD TO THE SELECTED DATABASE SERVICE"""
        
        AddingToDatabase = True
        while AddingToDatabase:
            #SHOWS THE NAME OF DATABASE FOR SELECTION
            showDatabaseOptions()      
            try:
                #VALIDATION TO MAKE SURE THE NUMBER PASSED IN IS A INTEGER
                databaseSelection = int(input().replace("'","\\"))
            except ValueError:
                print("Invalid Database Selection. Please Try Again")
                break
                #GETS THE DATABASE SELECTION FOR THE COLLECTION AND INPUT
                selectedDatabase = getDatabaseName(int(databaseSelection))
                #CHECK TO SEE IF ITS A VALID DATABASE CHOSE
            if not selectedDatabase == False:
                #LOGIC TO INPUT DATA IN THE SELECTED DATABASE
                if selectedDatabase.upper() == "CRM_DATA":
                    try:
                        newCustomer = getCustomerData()
                        if newCustomer != None:
                            addItemToCRMDatabase(newCustomer)
                            print("Record Added Successfully!")
                        break
                    except Exception as error:
                        print(error)
                        print("The update process failed. Please try again.")
                        break
                        
                if selectedDatabase.upper() == "MAILINGS":
                    try:
                        newMalingInfo = enterMailingInfo()
                        if newMalingInfo != None:
                            addItemToMailingDatabase(newMalingInfo,1)
                            print("Record Added Successfully!")
                        break
                    except Exception as error:
                        print(error)
                        print("The update process failed for the MAILINGS DATABASE. Please try again.")
                        break
            else: 
                print("Invalid Database Selection. Please try again!")
                break
                    
    if str(actionType).upper() == "EDIT A RECORD":
        """EDITS A RECORD IN THE DATABASE SERVICE"""
        
        edittingDatabase = True
        while edittingDatabase:
            #SHOWS THE DATABASES THAT WERE SELECTED TO BE EDITED
            showDatabaseOptions()  
            #ENSURES THE USER HAS ENTERED AN INTEGER VALUE          
            try:
                databaseSelection = int(input().replace("'","\\"))
            except ValueError:
                print("Invalid Database Selection. Please Try Again")
                break
            #GETS THE DATABASE SELECTION FOR THE USER INPUT USING A COLLECTION
            selectedDatabase = getDatabaseName(int(databaseSelection))
            if not selectedDatabase == False:
                #LOGIC TO DECIDE WHAT DATABASE TO ADD ANY UPDATES
                if selectedDatabase.upper() == "CRM_DATA":
                    try:
                        updateCRMRecord()
                        break
                    except Exception as error:
                        print(error)
                        print("The update process failed. Please try again.")
                        break                       
                if selectedDatabase.upper() == "MAILINGS":
                    try:
                        updateMailingsRecord()
                        break
                    except Exception as error:
                        print("The update process failed for the MAILINGS DATABASE. Please try again.")
                        print(error)
                        break
            else: 
                print("Invalid Database Selection. Please try again!")
                break
                            
    if str(actionType).upper() == "SHOW RECORDS IN A DATABASE":
        showData = True
        """SHOWS THE RECORDS IN THE SELECTED DATABASE SERVICE"""
        while showData:
            #SHOWS DATABASE OPTIONS FOR THE USER TO SELECT
            showDatabaseOptions()     
            #VALIDATION TO MAKE SURE AN INT VALUE HAS BEEN ENTERED
            try:
                databaseSelection = int(input().replace("'","\\"))
            except ValueError:
                print("Invalid Database Selection. Please Try Again")
                break
            #GETS THE DATABASE NAME FROM A COLLECTION BY USER ENTRY
            selectedDatabase = getDatabaseName(int(databaseSelection))            
            if not selectedDatabase == False:
                #LOGIC TO DECIDE WHAT DATABASE TO SHOW AND LOOPS THROUGH ALL VALUES FOR DISPLAY
                if selectedDatabase.upper() == "CRM_DATA":
                    try:
                        showRecords(selectedDatabase)
                        break
                    except Exception as error:
                        print("Something didnt go as expected. Please try again.")
                        print(error)
                        break
                        
                if selectedDatabase.upper() == "MAILINGS":
                    try:
                        showRecords(selectedDatabase)
                        break
                    except Exception as error:
                        print("Something didnt go as expected. Please try again.")
                        print(error)
                        break
            else: 
                print("Invalid Database Selection. Please try again!")
                break                    
                        
    if str(actionType).upper() == "QUIT THE PROGRAM":
        #EXITS THE PROGRAM
        """QUITS THE PROGRAM"""
        sys.exit()