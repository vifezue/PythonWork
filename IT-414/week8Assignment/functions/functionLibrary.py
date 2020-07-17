
import platform
import json
import os.path
from database_access import *
from datetime import *
from xlsxwriter import workbook
import ezsheets


def addHeadersGoogleDocs(rows):
    rows[0][0] = "Parent Education Level"
    rows[0][1] = "Test Preparation Course"
    rows[0][2] = "Math Score"
    rows[0][3] = "Reading Score"
    rows[0][4] = "Writing Score"


def createTextFile():
    textFilePath = os.path.join("text_files", "script_log.txt")
    logFile = open(str(textFilePath), "w")
    return logFile


def loadGoogleTableData(worksheet, workbook, data):
    row = 1
# Iterate over the data and write it out row by row.
    for item in (data):
        col = 0
        row[row][col] = str(item['parental level of education'])
        col += 1
        row[row][col] = str(item['test preparation course'])
        col += 1
        row[row][col] = str(item['math score'])
        col += 1
        row[row][col] = str(item['reading score'])
        col += 1
        row[row][col] = str(item['writing score'])
        row += 1


def logAction(logFile, action):
    today = datetime.today()
    strDate = today.strftime("%b %d,%Y")

    now = datetime.now()
    strTime = now.strftime("%H:%M:%S")
    cleanDateTime = strDate + " " + strTime

    with open(logFile.name, "a") as textFile:
        textFile.write(cleanDateTime + " "+action+"\n")
        textFile.close()


def getPath():
    try:
        my_system = platform.system()

        if my_system == "Windows":
            root_fs = "C:\\IT414-VictorIfezue\week8Assignment"
        else:
            root_fs = "/IT414-VictorIfezue/week8Assignment"

        final_filepath = os.path.join(root_fs, "text_files")
        return final_filepath
    except Exception as error:
        print(error)


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


def validate_string(val):
    """Validates string"""
    if val != None:
        if type(val) is int:
            return str(val).encode('utf-8')
        else:
            return val


def addGradesToDatabase(item, my_db):
    """Adds the Json Item to the CRM_Grades   
    Arguments:
        item -- dictionary Item
    """
    educationLevel = noQuotes(validate_string(
        item.get('parental level of education', None)))
    testPrepCourse = noQuotes(validate_string(
        item.get("test preparation course", None)))
    mathScore = noQuotes(validate_string(item.get("math score", None)))
    readingScore = noQuotes(validate_string(item.get("reading score", None)))
    writingScore = noQuotes(validate_string(
        item.get("writing score", None)).upper())

    sqlOutput = ("INSERT INTO crm_grades (parentEducationLevel,testPreparationCourse, mathScore,readingScore,writingScore) VALUES ('{0}','{1}','{2}','{3}','{4}')").format(
        educationLevel, testPrepCourse, mathScore, readingScore, writingScore)
    try:
        my_db.executeQuery(sqlOutput)

    except Exception as error:
        print("The command " + sqlOutput +
              " failed to write to the crm_grades database.")
        print(error)


def createGradesTable():
    my_db = DB_Connect('root', '', 'python_projects')

    try:
        sqlDropTable = 'DROP TABLE `crm_grades`;'
        my_db.executeQuery(sqlDropTable)
    except:
        pass

    try:
        sqlCreateTable = '''CREATE TABLE `crm_grades` (
                    `id` int(11) NOT NULL,
                    `parentEducationLevel` varchar(50) NOT NULL,
                    `testPreparationCourse` varchar(50) NOT NULL,
                    `mathScore` varchar(5) NOT NULL,
                    `readingScore` varchar(5) NOT NULL,
                    `writingScore` varchar(5) NOT NULL
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'''
        my_db.executeQuery(sqlCreateTable)
    except Exception as error:
        print(error)

    try:
        sqlAlter1 = 'ALTER TABLE `crm_grades` ADD PRIMARY KEY (`id`);'
        my_db.executeQuery(sqlAlter1)
        sqlAlter2 = 'ALTER TABLE `crm_grades` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;'
        my_db.executeQuery(sqlAlter2)
    except Exception as error:
        print(error)


def writeSpreadsheet(worksheet, workbook, dataSet):
    row = 0
    col = 0
    worksheet.write(row, col, "Parent Education Level")
    col += 1
    worksheet.write(row, col, "Test Preparation Course")
    col += 1
    worksheet.write(row, col, "Math Score")
    col += 1
    worksheet.write(row, col, "Reading Score")
    col += 1
    worksheet.write(row, col, "Writing Score")
    col += 1
    loadExcelTableData(worksheet, workbook, dataSet)
    workbook.close()


def loadExcelTableData(worksheet, workbook, reader):
    row = 1
# Iterate over the data and write it out row by row.
    for item in (reader):
        col = 0
        worksheet.write(row, col, str(item['parental level of education']))
        col += 1
        worksheet.write(row, col, str(item['test preparation course']))
        col += 1
        worksheet.write(row, col, str(item['math score']))
        col += 1
        worksheet.write(row, col, str(item['reading score']))
        col += 1
        worksheet.write(row, col, str(item['writing score']))
        col += 1
        row += 1
