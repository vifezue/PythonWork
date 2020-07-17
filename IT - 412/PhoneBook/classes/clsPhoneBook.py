
class PhoneBook:
    def __init__(self,firstName,lastName,phoneNumber,phoneType):
        """Creates a PhoneBook class    
        Arguments:
            firstName string -- First name of the contact
            lastName string -- Last name of the contact
            phoneNumber int -- Formated Phone Number of the contact
            phoneType string -- The phone type of contact 
        """
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.phoneType = phoneType
        
    def createDictionary(self,firstName, lastName, phoneNumber, phoneType):
        """creates the dictionary for the Phone Book
    
    Arguments:
        firstName {string} 
        lastName {string} 
        phoneNumber {int} 
        phoneType {string} 
    """
        dictionary = {"firstName": firstName, "lastName": lastName, "phoneNumber": phoneNumber, "phoneType": phoneType}
        return dictionary        
        

    def createPhoneBookRecord(self):
        """Creates the Contact and stores it in a dictionary    
        Returns:
            dictionary -- returns dictionary
        """
        contact = self.createDictionary(self.firstName,self.lastName,self.phoneNumber,self.phoneType)
        return contact

    def showContact(self):
        """Prints the contact data to the screen
        """
        print("First Name: "+ self.firstName)
        print("Last Name: "+ self.lastName)
        print("Phone Type: "+ self.phoneType)
        print("Phone Number: "+ self.phoneNumber)

    def savePhoneBookContact(self,list):
        """Saves the Phone Book to the passed in list and print success message
        
        Arguments:
            list array -- the phone book as an array
        """
        list.append(self)
        #print("Contact Added Successfully!")
    