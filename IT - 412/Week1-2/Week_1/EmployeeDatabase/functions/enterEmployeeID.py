from functions.checkForNull import checkfor_null
from functions.checkForValue import check_for_value

def enter_employeeID():
    """Takes user entry to enter the Employee ID
    
    Returns:
        String -- Returns either an empty string or the employeeID
    """
    try:
        checkID = False
        while not checkID:
            employeeID = input("Please enter the employeeID: ")
            #Check for Null values
            if checkfor_null(employeeID) == True:
                count = len(employeeID)
            else:
                checkID = False
                break
            #Check count
            if int(employeeID):
                if count >=8:
                    print("Invalid entry....")
                    checkID = False 
                    break
                else: checkID = True
            return employeeID
    except:
        print("Invalid Entry!")
        return ""