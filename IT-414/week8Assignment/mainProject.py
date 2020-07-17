import requests
from functions.functionLibrary import *
import os.path
import csv
import openpyxl
import ezsheets
from datetime import date
import openpyxl
from openpyxl.utils import *
import xlsxwriter
import threading
import ezsheets


sourceSystemURL = "https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week08/WI20-Assignment/exam_data.csv"

systemfilePath = getPath()

LogFile = createTextFile()

logAction(LogFile, "Automation Job Started.")

requestObj = requests.get(sourceSystemURL)

open(os.path.join(systemfilePath, 'dataImport.csv'),
     'wb').write(requestObj.content)

csvPath = os.path.join(systemfilePath, 'dataImport.csv')

# UNCOMMENT WHEN GOING LIVE
createGradesTable()
with open(csvPath, newline='') as csvData:
    reader = csv.DictReader(csvData)
    my_db = DB_Connect('root', '', 'python_projects')
    for row in reader:
        addGradesToDatabase(row, my_db)
    logAction(LogFile, "Loaded Database Tables.")
    my_db.conn.close()

workbook = xlsxwriter.Workbook(os.path.join(systemfilePath, "gradesWorkbook.xlsx"))
worksheet = workbook.add_worksheet("Grades")
with open(csvPath, newline='') as csvData:
    dataSet = csv.DictReader(csvData)
    writeSpreadsheet(worksheet, workbook, dataSet)
logAction(LogFile, "Created Spreadsheet.")

my_spreadsheet = ezsheets.createSpreadsheet("My Spreadsheet")
curr_sheet = my_spreadsheet[0]
rows = curr_sheet.getRows()
addHeadersGoogleDocs(rows)
curr_sheet.updateRows(rows)
with open(csvPath, newline='') as csvData:
    data = csv.DictReader(csvData)
    loadGoogleTableData(curr_sheet,my_spreadsheet,data)
curr_sheet.updateRows(rows)
logAction(LogFile, "Created Google Spreadsheet.")
