from functions.functionLibrary import *
from classes.clsPhoneBook import *

ContactList = []

print(":::::::::: CONTACT LIST :::::::::::")

isDone = False
while not isDone:
    firstName = checkFirstName(input("Please enter the First Name: "))
    lastName = checkLastName(input("Please enter the Last Name: "))
    phoneType = verifyPhoneType(getPhoneType())
    phoneNumber = checkPhoneNumber(input("Please enter the Phone Number:"))

    contact = PhoneBook(firstName,lastName,phoneNumber,phoneType)
    contact.showContact()
    contact.savePhoneBookContact(ContactList)

    response = input("Do you wish to add another employee? Please enter a Y for YES or N for NO?")
    if response.upper() == "N":
        print("Goodbye!")
        break
    else:
        continue

