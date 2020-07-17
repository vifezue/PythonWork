import ezsheets
import openpyxl
import requests
from bs4 import BeautifulSoup
from functions.functionLibrary import *

"""
    Week 5 - Spreadsheets Assignment
    Google Spreadsheet Assignment
    Victor Ifezue
    Professor Tom Petz
    
    I did all the average calculation with a 
    method instead of Excel Formulas
    
"""
request = startBrowser()

# check for a sucessful response or exit app
if request.status_code != 200:
    exit()

my_workbook = ezsheets.Spreadsheet(
    "1g6ZObgUf7D_F3tZBgBseXUETTpF_0HN-IpatQ4YgKsM")

requestText = request.text
beautifulSoupText = BeautifulSoup(requestText, "html.parser")
my_data = beautifulSoupText.findAll("tr")

# clean the dataset and return a clean array with values
cleanDataSet = []
counter = 0
while counter < len(my_data):
    rowValue = my_data[counter].getText()
    rowValue = str(rowValue).split('\n')
    while("" in rowValue):
        rowValue.remove("")
        if '  ' in rowValue:
            rowValue.remove('  ')
    cleanDataSet.append(rowValue)
    counter = counter + 1

# grab distinct products and put in list
productList = []
for item in cleanDataSet:
    if item[3] != "Item":
        if item[3] not in productList:
            productList.append(item[3])

# grab product and units sold and put in dictionary
productCount = []
for productItem in cleanDataSet:
    if productItem[3] in productList:
        value = {"product": productItem[3], "quantity": productItem[4]}
        productCount.append(value)

# calculate the average products sold by product
averageProductCount = []
for productValue in productList:
    number = []
    for item in productCount:
        if productValue == item["product"]:
            number.append(item["quantity"])
    average = calculateAverage(number)
    averageProductCount.append([productValue, int(average)])

# TITLE
curr_sheet = my_workbook[0]
rows = curr_sheet.getRows()   
rows[0][0] = "Sales Data"


# Import the Clean Product Data
row_count = 1
for item in cleanDataSet:
    col_count = 0
    rows[row_count][col_count] = item[3]
    col_count = col_count + 1
    rows[row_count][col_count] = item[4]
    row_count = row_count + 1

# Import the Clean Product Data Averages
row_count = row_count
for item in averageProductCount:
    col_count = 0
    rows[row_count][col_count] = item[0] + " Average:"
    col_count = col_count + 1
    rows[row_count][col_count] = item[1]
    row_count = row_count + 1

curr_sheet = my_workbook[0]

# Save Google Sheet
curr_sheet.updateRows(rows)
