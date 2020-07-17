import platform
import os
import shutil
import logging
import os.path
from os import path
from shutil import copy, copy2
from classes.clsLogger import Log


def copyFile():
    filePath = getPath()
    fileToCopy = input("What is the name of the file you will like to copy?")
    if os.path.isfile(os.path.join(filePath, fileToCopy)):
        destinationFolder = input(
            "What is the name of the folder you would like to copy to?: ")
        if os.path.exists(destinationFolder) == True:
            shutil.copy2(destinationFolder, fileToCopy)
        else:
            print("The file path does not exist.")
    else:
        print("This is not a file.")


def copyFilesOnly(sourceFolder, destinationFolder):
    """Copies the files ONLY to the destination Folder

    Arguments:
        sourceFolder {[type]} -- [description]
        destinationFolder {[type]} -- [description]
    """
    Logger = Log()  # start the log

    folder = os.listdir(sourceFolder)
    mySystem = platform.system()  # get the OS System
    if len(folder) > 0:  # see if any files are in the folder
        for item in folder:  # loop through folder
            if mySystem == "Windows":
                source = "\\"+item
                destination = "\\"+item
            else:
                source = "/" + item
                destination = "/"+item
            if path.isfile(sourceFolder+source) == True:  # check to see if its a file
                # check to see if the file is less than 1GB
                if sizeCheck(sourceFolder, source) == True:
                    srcname = sourceFolder + source
                    dstname = destinationFolder + source
                    try:
                        copy(srcname, dstname)
                        Logger.logAction("file copied - ", item +
                                         " was copied to " + dstname)  # log the action
                    except SameFileError:  # throw exception if the source and destination is the same
                        print("You can't copy the same file.")
                else:
                    Logger.logAction("file to large - ", item +
                                     " was over 1GB ")  # log the action
            else:
                Logger.logAction("skipped folder - ", item +
                                 " folder was skipped")  # log the action
    else:
        print("The folder has no content. Please select a folder with files to perform a copy operation.")


def createFolder():
    filePath = getPath()

    newFolder = input(
        "What is the name of the folder that you would like to create?: ")
    os.makedirs(os.path.join(filePath, newFolder))
    return(newFolder)


def fileSizeCheck(filePath, fileItem):
    # checks of the selection is a file/folder
    if os.path.isfile(os.path.join(filePath, fileItem)):
        tempFileSize = os.path.getsize(filePath, fileItem)
        # gets fileSize
        tempFileDivide = tempFileSize / 1073741824  # conversion for megabytes
        if tempFileDivide < 1:
            print(fileItem + " | " + str(tempFileSize) + " bytes")
        else:
            print(fileItem + " | " + str(tempFileDivide) + " Gigabyes")

        # tempFileSize = os.path.getsize(filePath, fileItem)
    else:
        print(fileItem + " | " + str(tempFileSize) + " folder")


def getActionSelection(val):
    """Gets the type of Action the user wants to do

    Arguments:
        val {int} -- [user input]

    Returns:
        [string] -- [the action the user wants to do]
    """
    switch = {
        1: 'Copy Folder',
        2: 'Folder Creation',
        3: 'Exit'
    }
    if val in switch:
        return switch.get(val)
    else:
        return False


def getPath():
    mySystem = platform.system()

    if mySystem == "Windows":
        OSFileStructure = "C:\\"
    else:
        OSFileStructure = "/"

    finalDirectory = os.path.join(OSFileStructure, "example")
    # var is the name of the file in the C drive

    return finalDirectory


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


def showFiles():
    filePath = getPath()

    os.chdir(filePath)
    print("Printing the contents of " + os.getcwd())

    # gets the list of files
    listOfFiles = os.listdir(filePath)
    for fileItem in listOfFiles:
        print(fileItem)


def sizeCheck(filePath, fileItem):
    # checks of the selection is a file/folder
    if os.path.isfile(os.path.join(filePath + fileItem)):
        tempFileSize = os.path.getsize(filePath+fileItem)
        # gets fileSize
        tempFileDivide = tempFileSize / 1073741824
        if tempFileDivide < 1:
            return True
        else:
            return False


def showActionOptions():
    """Prints user statement for input
    """
    print("What would you like to do? \n"
          + "Please type in your selection by the number" +
          "\n 1 - Copy a Folder" +
          "\n 2 - Create Folder " +
            "\n 3 - Exit Program")
