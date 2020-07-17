import os
import re
import platform
from selenium import webdriver

def renameFileAsPassed(file):
    """rename the files in the folder as passed

    Arguments:
        directory {file} -- [string representation of the file location to write logs]
    """
    my_system = platform.system()
    
    if my_system.lower() == "windows":
        strFile = file.split("\\")
    else:
        strFile = file.split("/")
        
    directory = getPath()        
    newFile = "passed_" + strFile[4]
    
    currentFilePath = (os.path.join(directory, strFile[4]))
    newFilePath = (os.path.join(directory, newFile))
    
    os.rename(currentFilePath,newFilePath)

def getPath():
    try:
        my_system = platform.system()

        if my_system == "Windows":
            root_fs = "C:\\IT414-VictorIfezue\week4Assignment"
        else:
            root_fs = "/IT414-VictorIfezue/week4Assignment"

        final_filepath = os.path.join(root_fs, "images")
        return final_filepath
    except Exception as error:
        print(error)
        
def startBrowser():
    """Start Chrome Browser
    """
    my_browser = webdriver.Chrome(
    executable_path="downloads\chromedriver.exe")
    my_browser.get(
    "https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week04/WI20-website-testing-sites/assignment/index.php")
    return my_browser

def isValidEmail(passedString):
    """ is valid email regex
    """
    emailRegex = re.compile(r'([\w\.-]+)@([\w\.-]+)')
    emailAddressStr = emailRegex.findall(passedString)
    if emailAddressStr:
        return True
    else: 
        return False
    
def startSubmitBrowser():
    """START FINAL BROWSER
    """
    my_browser = webdriver.Chrome(
    executable_path="downloads\chromedriver.exe")
    my_browser.get(
    "https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week04/WI20-website-testing-sites/assignment/thank_you.php")
    return my_browser
    
    
    
    