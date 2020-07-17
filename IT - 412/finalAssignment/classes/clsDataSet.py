import pymysql
import json
import csv
from functions.functionLibrary import *


class validateData():
    def __init__(self, data):
        self.data = data

    def clean_data(self, file=None):
        """Cleans and reformats the data"""
        if file == None:
            with open(self.data, 'r') as file:
                file = file.readlines()
                #Remove Duplicates"""
                duplicateLines = file
                edittedText = []
                for line in duplicateLines:
                    if line not in edittedText and len(edittedText) > 0:
                        for item in edittedText:
                            if str(item) == str(line) and edittedText.__contains__(line) == True:
                                break
                            else:
                                if line not in edittedText:
                                    edittedText.append(line)
                    else:
                        edittedText.append(line)
                file = edittedText  
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
            with open(file, 'r') as file:
                file = file.readlines()
                #Remove Duplicates"""
                duplicateLines = file
                edittedText = []
                for line in duplicateLines:
                    if line not in edittedText and len(edittedText) > 0:
                        for item in edittedText:
                            if str(item) == str(line) and edittedText.__contains__(line) == True:
                                break
                            else:
                                if line not in edittedText:
                                    edittedText.append(line)
                    else:
                        edittedText.append(line)
                file = edittedText 
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
        
    def convert_csv(self):
        """Converts the data file to CSV """
        data = self.clean_data()
        convert_csv(data)

    def convert_json(self):
        """Converts the data file to jSon """
        data = self.clean_data()
        convert_json(data)