from checkForNull import checkfor_null
from checkForValue import check_for_value

def enter_email():
    """Takes user entry and saves the email address
    
    Returns:
        string -- returns the email address or an empty string
    """
    try:
        invalid_Emailcharacters = ["!","#","$","%","^","&","*","(",")","_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}"]
        checkEmail = False
        while not checkEmail:
            email = input("Please enter the employee email: ")
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