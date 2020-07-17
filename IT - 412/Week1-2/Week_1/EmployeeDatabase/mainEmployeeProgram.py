from functions.checkForNull import checkfor_null
from functions.enterEmployeeID import enter_employeeID
from functions.checkCondition import check_condition
from functions.enterFirstName import enter_FirstName
from functions.enterLastName import enter_LastName
from functions.enterEmail import enter_email
from functions.enterAddress import enter_address

employeeRecords = []
isValid = True

while isValid:
    employeeID = enter_employeeID()
    if employeeID:
        checkID = True
    else:
        checkID = False
    if not check_condition(checkID) == True:
        break
    employeeFirstName = enter_FirstName()
    if employeeFirstName:
        checkFirstName = True
    else:
        checkFirstName = False  
    if not check_condition(checkFirstName)== True:
        break
  
    employeeLastName = enter_LastName()
    if employeeLastName:
        checkLastName = True
    else:
        checkLastName = False
    if not check_condition(checkLastName) == True:
        break
    email = enter_email()
    if email:
        checkEmail = True
    else:
        checkEmail = False
   
    if not check_condition(checkEmail) == True:
        break

    address = enter_address()
    if address:
        checkAddress = True
    else:
        checkAddress = False
 
    if not check_condition(checkAddress) == True:
        break
    employee = dict(ID= employeeID, fName = employeeFirstName, lName = employeeLastName, email = email, Address = address)
    employeeRecords.append(employee.copy())

    response = input("Do you wish to add another Employee? Please enter a Y for YES or N for NO?")

    if response.upper() == "N":
        print(employeeRecords)
        break
    else:
        continue