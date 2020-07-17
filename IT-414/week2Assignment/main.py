
import os.path
import logging
from distutils.dir_util import copy_tree
from classes.clsLogger import Log
from functions.functionLibrary import *
import shutil
import sys
from os import path

"""[Main Executable]
Author: Victor Ifezue
Assignment - Week 2 - Reading And Writing Files Assignment

****
the join method was not working by the way so I had to
perform a workaround and combine the strings
****

"""

# I WOULD DEFINE THESE VARIABLES AS CONSTANT SO I MADE THEM ALL UPPERCASE PER CONVENTION
FILEPATH = getPath()  # CONST
SYSTEMLOG = Log()  # CONST
SYSTEM = platform.system()  # CONST

print("Week 2 - Reading And Writing Files Assignment")

SYSTEMLOG.logAction("Started Application", os.environ.get(
    'USERNAME'))  # Logs the username

actionType = getAction()  # Gets the action from the user

if str(actionType).upper() == 'COPY FOLDER':
    """Copy Folder Operation
    """
    selectedFolder = input(
        'Enter the name of the folder to copy the contents :')
    destinationFolder = input(
        'Enter the name of the folder you would like to move the items to:')

    if SYSTEM == "Windows":
        source = "\\"+selectedFolder
        destination = "\\"+destinationFolder
    else:
        source = "/" + selectedFolder
        destination = "/"+destinationFolder

    if path.isdir(FILEPATH+source) == False:
        print("The file that you would like to copy does not exist.")
        exit()

    if path.isdir(FILEPATH+destination) == True:
        copyFilesOnly(FILEPATH+source, FILEPATH+destination)
        pass
    else:
        print("The folder that you would like to copy does not exist.")
        answer = input(
            "Would you like to create the folder?\n Enter Y for Yes | N for No ONLY")
        if answer.lower() == "y":
            folder = createFolder()
            confirmation = input(
                "Would you like to copy to the folder you created? \n Enter Y for Yes | N for No ONLY")
            if confirmation.lower() == "y":
                copyFilesOnly(source, destination)
            else:
                pass
        else:
            pass

if str(actionType).upper() == 'FOLDER CREATION':
    """Creates a new folder
    """
    folder = createFolder()
    SYSTEMLOG.logAction("Created Folder", folder)
