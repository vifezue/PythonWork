from distutils.dir_util import copy_tree
from zipfile import ZipFile
from os import path
from functions.functionLibrary import *
import sys,  shutil, platform, os.path

scriptRunning = True
# Copy the contents of the folder

if scriptRunning == True:
    try:
        startUpPath = getStartUpPath()
        shutil.copytree(os.getcwd(), startUpPath)
        print("This project was copied to " + str(startUpPath))
    except Exception as error:
        print(error)
        scriptRunning = False

# Unzip the file contents
if scriptRunning == True:
    try:
        filePathLogs = getPath()
        sourceZipFile = 'text_files\\access_logs.zip'
        zipFile = (os.path.join(filePathLogs, sourceZipFile))

        with ZipFile(sourceZipFile, 'r') as zipObj:
            zipObj.extractall(filePathLogs)
    except Exception as error:
        print(error)
        scriptRunning = False

# Log the file records
if scriptRunning == True:
    try:
        my_logs = os.walk(filePathLogs, topdown=True)
        for directory in my_logs:
            for filename in directory[2]:
                logFilePath = (os.path.join(str(directory[0]), filename))

                createdMatchestxtFile = os.path.join(
                    str(directory[0]), "matches.txt")
                # Creates the matches text file in every folder
                matchestxtFileObj = open(createdMatchestxtFile, "w+")
                matchestxtFileObj.close()
                logFileData = open(logFilePath, "r")
                generateErrorLogsService(logFileData.read(), filePathLogs,
                                         createdMatchestxtFile)
                logFileData.close()
    except Exception as error:
        print(error)
        scriptRunning = False

# Zip File and mark files as processed
if scriptRunning == True:
    try:
        markFileAsProcessed(filePathLogs)
        zipLogFile(filePathLogs)
    except Exception as error:
        print(error)
