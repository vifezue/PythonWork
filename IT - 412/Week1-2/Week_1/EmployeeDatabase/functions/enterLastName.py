from functions.checkForNull import checkfor_null
from functions.checkForValue import check_for_value

def enter_LastName():
    """Takes users input and validates the lastname entered and stores the value
    
    Returns:
        [string] -- [stores the lastname value]
    """
    invalid_Namecharacters = ["!", "@","#","$","%","^","&","*","(",")","_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}"]
    try:
        checkLastName = False
        while not checkLastName:
            #Enter Lastname
            employeeLastName = input("Please enter the Employee Last Name: ")
            #Checks for Null Values
            if checkfor_null(employeeLastName):
                count = len(employeeLastName)
                    #Checks for string
            if str(employeeLastName):
                if not check_for_value(employeeLastName,invalid_Namecharacters):
                    checkLasName = False
                    employeeLastName = employeeLastName.capitalize()
                else: checkLastName = True
            return employeeLastName
    except:
         print("Invalid Entry")
         return ""
