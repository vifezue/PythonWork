from checkForNull import checkfor_null
from checkForValue import check_for_value

def enter_address():
    """Takes user entry and saves the address
    
    Returns:
        string -- Returns the Address or an empty string
    """
    try:
        invalid_addressCharacters = ["!", "\"","'", "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", ":", "[", "]", "{", "}", ")","."]
        checkAddress = False
        while not checkAddress:
            #Entered address
            address = input("Please enter the Employee Address: ")
            #checks to see if address was entered
            if not checkfor_null(address):
                address = "None Provided"
            #Checks to see if address is alphnum
            if not address.isalnum:
                checkAddress = False
                break
            if not check_for_value(address,invalid_addressCharacters):
                print("Invalid entry....")
                checkEmail = False
            return address
    except:
        print("Invalid Entry")
        return ""