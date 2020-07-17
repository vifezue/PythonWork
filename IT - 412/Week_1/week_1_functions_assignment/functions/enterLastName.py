from checkForNull import checkfor_null
from checkForValue import check_for_value

def enter_LastName():
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

def enter_email():
    try:
        invalid_Emailcharacters = ["!","#","$","%","^","&","*","(",")","_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}"]
        checkEmail = False
        while not checkEmail:
            email = input("Please enter the Employee Email: ")
            #Checks to see if input was entered
            if checkfor_null(email):
                if str(email):
                    if not check_for_value(email,invalid_Emailcharacters):
                        print("Invalid entry....")
                        checkEmail = False
                    else: checkEmail = True
                else:
                    checkEmail = False
                    break
            return email
    except:
        print("Invalid Entry")
        return ""