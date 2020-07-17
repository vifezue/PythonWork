
def checkFirstName(firstName):
    """Check and validate first name   
    Returns:
        firstName -- string
    """
    firstName_ok = False
    while not firstName_ok:
        firstName_ok = validate_str(firstName)
        if not firstName_ok:            
            firstName = input("First name was not valid. Please try again: ")
            firstName_ok = validate_str(firstName)
    return firstName.title()

def checkLastName(lastName):
    """Check and validate the Last Name        
    Returns:
        lastName -- string of lastName
    """
    lastName_ok = False
    while not lastName_ok:
        lastName_ok = validate_str(lastName)
        if not lastName_ok:
            lastName = input("Last name was not valid. Please try again: ")
            lastName_ok = validate_str(lastName)
    return lastName.title()

def checkPhoneType(phoneType):
    """Check that the selected Phone Type is in the list"""
    try:    
        if phoneType == "":
            return False
        else:
            phoneTypes = ["Cell", "Home", "Office"]
            if phoneType in phoneTypes:
                return True
            else:
                return False
    except:
        return False
        
def checkPhoneNumber(phoneNumber):
    """Check and Validate the Phone Number"""
    phoneNumber_ok = False
    while not phoneNumber_ok:
        try:            
            phoneNumber_ok = validatePhoneNumber(phoneNumber)
            if not phoneNumber_ok:
                phoneNumber = input("Phone Number was not valid. Please try again: ")
                phoneNumber_ok = validatePhoneNumber(phoneNumber)
        except:
            continue
    return phone_format(phoneNumber) 

def createDictionary(firstName, lastName, phoneNumber, phoneType):
    """creates the dictionary for the Phone Book
    
    Arguments:
        firstName {string} 
        lastName {string} 
        phoneNumber {int} 
        phoneType {string} 
    """
    try:
        dictionary = {"firstName": firstName, "lastName": lastName, "phoneNumber": phoneNumber, "phoneType": phoneType}
        dictionary_ok = isinstance(dictionary,dict)
        if dictionary_ok == True and dictionary is not None:
            return dictionary
    except:
        pass
    
def getPhoneType():
    """Logic to capture the user selection to see what phone type.
        
    Returns:
        string Value -- string
    """
    phoneType_ok = False
    while not phoneType_ok:
        try:
            phoneType = input("What type of Phone Number is this? \n"
            +"Please type in your selection by the number :"
            +"\n 1 - Cell \n 2 - Home \n 3 - Office \n")
            if not phoneType.isnumeric():
                print("Please enter a valid number on the list.")
                continue
            else:
                phoneType = int(phoneType)
            switcher={
                1:'Cell',
                2:'Home',
                3:'Office'
                }
            if phoneType in switcher:
                return verifyPhoneType(switcher.get(phoneType))
                break
            else:
                print("Please enter a valid selection from the list.")
                continue
        except:
            print("Please enter a valid selection from the list.")
            continue
        
def phone_format(number):
    """Formats the Phone Number"""
    try:
        if number.isdigit():
            return format(int(number[:-1]), ",").replace(",", "-") + number[-1]  
    except:
        return number
    
def validatePhoneNumber(phoneNumber):
    """Validates the Phone Number from user entry
    
    Arguments:
        phoneNumber {string} -- user entry as string
    
    Returns:
        boolean -- True or false 
    """
    try:
        
        if phoneNumber == "" or hasLetters(phoneNumber) :
            return False
        else:
            phoneNumber_ok = isinstance(int(phoneNumber),int)
            if phoneNumber_ok == True:        
                try:
                    if len(phoneNumber) < 11 and len(phoneNumber) > 9:
                        return True
                    else:
                        return False
                except:
                    return False
    except:
        return False

def validate_str(passedStr):
    """Validates the string and make sure its only a string
        
    Arguments:
        passedStr {string} -- user entry entered string
    
    Returns:
        boolean -- True or False
    """
    try:        
        if isinstance(passedStr,int) == True:
            passedStr = str(passedStr)
        
        invalid_Namecharacters = ["!", "@","#","$","%","^","&","*","(",")","_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}"]
        for char in invalid_Namecharacters:
            if char in passedStr:
                return False
            else:
                continue
        
        if passedStr == "" or hasNumbers(passedStr):
            return False
        else:
            try:
                string_ok = isinstance(passedStr, str)
                if string_ok == True:
                    passedStr = passedStr.strip()
                    return True
                else:
                    return False
            except:
                return True 
    except:
        return False  
        
def verifyPhoneType(phoneType):
    """Validates the phoneType entry
    
    Arguments:
        phoneType string -- The phone type of the contact
    
    Returns:
        phoneType -- the phone type string
    """
    phoneType_ok = False
    while not phoneType_ok:
        phoneType_ok = checkPhoneType(phoneType)
        if not phoneType_ok:
            phoneType = input("Phone Type was not valid. Please enter Cell or Office or Phone: ")
            phoneType_ok = checkPhoneType(phoneType)
    return phoneType

def hasNumbers(inputString):
    """Checks if the string has numbers
    
    Arguments:
        inputString str -- passed in string
    
    Returns:
        boolean -- True if exist and False is str does not exist
    """
    return any(char.isdigit() for char in inputString)  

def hasLetters(inputString):
    """Checks if the string has numbers
    
    Arguments:
        inputString str -- passed in string
    
    Returns:
        boolean -- True if exist and False if number does not exist
    """
    return any(char.isalpha() for char in inputString)  

    