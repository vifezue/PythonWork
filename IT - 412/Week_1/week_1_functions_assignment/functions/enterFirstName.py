from checkForNull import checkfor_null
from checkForValue import check_for_value

def enter_FirstName():
    """Takes user entry for the First Name and validates the entry
    
    Returns:
        [string] -- method returns the First Name or an empty string
    """
    try:
        invalid_Namecharacters = ["!", "@","#","$","%","^","&","*","(",")","_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}"]
        checkFirstName = False
        while not checkFirstName:

        #Enter in EmployeeID
            employeeFirstName = input("Please enter the employee First Name: ")

        #Checks for Null Values
            if not checkfor_null(employeeFirstName)== True:
                checkFirstName = False
                break
                 
            count = len(employeeFirstName)

        #Check to see if its a string
            if str(employeeFirstName):
                if not check_for_value(employeeFirstName,invalid_Namecharacters):
                    checkFirstName = False
                    employeeFirstName = employeeFirstName.capitalize()
                else: checkFirstName = True                                            
            else:
                checkFirstName = False
                break             
            return employeeFirstName
    except:
            print("Invalid Entry")
            return ""