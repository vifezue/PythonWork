
import os.path
import logging
from distutils.dir_util import copy_tree
import shutil
import sys
from os import path
import platform
import send2trash
import re
import zipfile


def copyFile():
    try:
        my_path = getPath()

        file_to_copy = input("What is the file that you would like to copy?")
        folder_to_copy = input(
            "What is the folder that you would like to copy to?")

        shutil.copy2(file_to_copy, folder_to_copy)
    except Exception as error:
        print(error)


def createFolder():
    try:
        my_path = getPath()

        new_folder = input(
            "What is the name of the folder that you would like to make?")
        os.makedirs(os.path.join(my_path, new_folder))
    except Exception as error:
        print(error)


def deleteFile():
    try:
        my_path = getPath()
        my_root = getRoot()

        file_to_delete = input(
            "What is the file\\folder that you would like to delete?")

        send2trash.send2trash(os.path.join(my_path + file_to_delete))
    except Exception as error:
        print(error)


def getPath():
    try:
        my_system = platform.system()

        if my_system == "Windows":
            root_fs = "C:\\"
        else:
            root_fs = "/"

        final_filepath = os.path.join(root_fs, "logs")
        return final_filepath
    except Exception as error:
        print(error)


def getStartUpPath():
    try:
        my_system = platform.system()

        if my_system == "Windows":
            root_fs = "C:\\"
        else:
            root_fs = "/"
        destination = 'IT414-VictorIfezue'
        final_filepath = os.path.join(root_fs, "log_processing")
        return final_filepath
    except Exception as error:
        print(error)


def findAllForbiddenErrors(passed_string):
    """Finds all Forbidden 403 from logs

    Arguments:
        passed_string {string} -- [passed in logs]

    Returns:
        [list] -- [list of 403 logs found]
    """
    forbiddenErrors = re.compile(r'(.*(403).*)')
    forbiddenErrorsList = forbiddenErrors.findall(passed_string)
    return forbiddenErrorsList


def findAllInstalls(passed_string):
    """Finds all Forbidden 403 from logs

    Arguments:
        passed_string {string} -- [passed in logs]

    Returns:
        [list] -- [list of 403 logs found]
    """
    installs = re.compile(r'(.*install.*)')
    InstallsList = installs.findall(passed_string)
    return InstallsList


def findAllRegistrations(passed_string):
    """Finds all Forbidden 403 from logs

    Arguments:
        passed_string {string} -- [passed in logs]

    Returns:
        [list] -- [list of 403 logs found]
    """
    reistrations = re.compile(r'(.*\/wp-login\.php\?action=register.*)')
    registrationList = reistrations.findall(passed_string)
    return registrationList


def findAllSelects(passed_string):
    """Finds all Forbidden 403 from logs

    Arguments:
        passed_string {string} -- [passed in logs]

    Returns:
        [list] -- [list of 403 logs found]
    """
    select = re.compile(r'(.*select.*)')
    selectList = select.findall(passed_string)
    return selectList


def findAllStrings(passed_string):
    """Finds all Forbidden 403 from logs

    Arguments:
        passed_string {string} -- [passed in logs]

    Returns:
        [list] -- [list of 403 logs found]
    """
    val = re.compile(r'(.*\.\.\/.*)')
    valList = val.findall(passed_string)
    return valList


def generateErrorLogsService(passed_string, filePathLogs, matchesFile):
    """[summary]

    Arguments:
        passed_string {string} -- [passed in record of events]
        filePathLogs {string} -- [file path]
        matchesFile {object} -- [text file for logs to be written]
    """
    forbiddenErrorsList = findAllForbiddenErrors(passed_string)
    allInstallsList = findAllInstalls(passed_string)
    registrationList = findAllRegistrations(passed_string)
    selectList = findAllSelects(passed_string)
    valStringsList = findAllStrings(passed_string)

    listofLogs = [forbiddenErrorsList, allInstallsList,
                  registrationList, selectList, valStringsList]

    writeToLog(listofLogs, filePathLogs, matchesFile)


def findDataPoints(passed_string):
    """Regular Expression

    Arguments:
        passed_string {string} -- [string of the logs]

    Returns:
        [string] -- [formatted string of matched values]
    """

    IPAddressRegex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    IPAddress = IPAddressRegex.findall(passed_string)
    IPAddress = str(IPAddress).strip()

    dateRegex = re.compile(r'\[(.*?)\]')
    date = dateRegex.findall(passed_string)
    date = str(date).strip()

    methodTypeRegex = re.compile(r'\"(\D?\D\D\D.*?)\"(.*?)\"')
    methodType = methodTypeRegex.findall(passed_string)
    methodType = str(methodType).strip()

    bytesAndStatusCodeRegex = re.compile(r'\"\D?\D\D\D.*?\"(.*?)\"')
    bytesAndStatusCode = bytesAndStatusCodeRegex.findall(passed_string)
    bytesAndStatusCode = str(bytesAndStatusCode).replace("[", "")
    bytesAndStatusCode = str(bytesAndStatusCode).replace("]", "")
    bytesAndStatusCode = str(bytesAndStatusCode).replace("'", "")
    bytesAndStatusCode = str(bytesAndStatusCode).strip()
    bytesAndStatusCode = str(bytesAndStatusCode).split()
    statusCode = str(bytesAndStatusCode[0]).strip()
    strbytes = str(bytesAndStatusCode[1]).strip()

    parentURLRegex = re.compile(
        r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})')
    parentURL = parentURLRegex.findall(passed_string)
    parentURL = str(parentURL).strip()

    if len(parentURL) < 2:
        parentURLRegex = re.compile(r'(\"\s\D[^M](...)(.*?)\.com)')
        parentURL = parentURLRegex.findall(passed_string)

    userAgentRegex = re.compile(r'"-"\s\"(.*?)\"')
    userAgent = userAgentRegex.findall(passed_string)
    userAgent = str(userAgent).strip()

    logString = ("%s, %s, %s, %s, %s, %s, %s \n" % (IPAddress, date,
                                                    methodType, statusCode, strbytes, parentURL, userAgent))
    logString = logString.replace("[", "<")
    logString = logString.replace("]", ">")

    return logString


def writeToLog(logErrors, filePathLogs, matchesFile):
    """Writes to the matches text folder by loop

    Arguments:
        logErrors {string} -- [string of the log]
        filePathLogs {string} -- [string representation of the file location]
        matchesFile {object} -- [matches file for the specified folder]
    """
    matchestxtFileObj = open(matchesFile, "a")
    for arrayOflogs in logErrors:
        for log in arrayOflogs:
            # returns log error
            loggedError = findDataPoints(str(log))
            # writes the log error to file
            matchestxtFileObj = open(matchesFile, "a")
            matchestxtFileObj.write(str(loggedError)+"\n")
            matchestxtFileObj.close()

    # Remove Empty File if it contains no log errors
    fileSize = os.path.getsize(matchesFile)
    if fileSize == 0:
        send2trash(matchesFile)


def markFileAsProcessed(directory):
    """Marks the files in the folder as processed

    Arguments:
        directory {string} -- [string representation of the file location to write logs]
    """
    my_return = os.walk(directory)
    for item in my_return:
        for filename in item[2]:
            temp_filename = "processed_"+filename
            shutil.move(os.path.join(item[0], filename), os.path.join(
                item[0], temp_filename))


def moveFile():
    try:
        my_path = getPath()
        my_root = getRoot()

        file_to_move = input("What is the file that you would like to copy?")
        folder_to_move_to = input(
            "What is the folder that you would like to copy to?")

        shutil.move(os.path.join(my_path + file_to_move),
                    os.path.join(my_root + folder_to_move_to))
    except Exception as error:
        print(error)


def renameFile():
    try:
        my_path = getPath()

        file_to_copy = input("What is the file that you would like to change?")
        new_name = input("What is the new name for the file?")

        shutil.move(file_to_copy, new_name)
    except Exception as error:
        print(error)


def retrieve_file_paths(dirName):
    # setup file paths variable
    filePaths = []

    # Read all directory, subdirectories and file lists
    for root, directories, files in os.walk(dirName):
        for filename in files:
            # Create the full filepath by using os module.
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)

    # return all paths
    return filePaths


def showFiles():
    try:
        filePath = getPath()

        os.chdir(filePath)
        print("Printing the contents of " + os.getcwd())

        # gets the list of files
        listOfFiles = os.listdir(filePath)
        for fileItem in listOfFiles:
            print(fileItem)
    except Exception as error:
        print(error)


def sizeCheck(filePath, fileItem):
    try:
        # checks of the selection is a file/folder
        if os.path.isfile(os.path.join(filePath + fileItem)):
            tempFileSize = os.path.getsize(filePath+fileItem)
            # gets fileSize
            tempFileDivide = tempFileSize / 1073741824
            if tempFileDivide < 1:
                return True
            else:
                return False
    except Exception as error:
        print(error)


def zipLogFile(directoryName):
    # Call the function to retrieve all files and folders of the assigned directory
    filePaths = retrieve_file_paths(directoryName)

    # printing the list of all files to be zipped
    print('The following list of files will be zipped:')
    for fileName in filePaths:
        print(fileName)

    zipFileDestination = (os.path.join('text_files', 'results'))
    # writing files to a zipfile
    zip_file = zipfile.ZipFile(zipFileDestination+'.zip', 'w')
    with zip_file:
        # writing each file one by one
        for file in filePaths:
            zip_file.write(file)
    zip_file.close()
    print(zipFileDestination+'.zip file was created successfully!')
    print("Ending Script")
