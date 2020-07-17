import re


def findAllDates(passed_string):
    dateRegex = re.compile(r'(\d){1,2}(-|/)(\d)(\d){0,1}(-|/)(\d\d\d\d)')
    dateList = dateRegex.findall(passed_string)
    return dateList
    
def isValidDate(passed_date):
    
    dateRegex = re.compile(r'(\d){1,2}(-|/)(\d){1,2}(-|/)\d\d\d\d')
    dateTest = dateRegex.search(passed_date)

    #checks for null
    if dateTest is None:
        print("You did not enter a proper date")
        return False
    else:
        #checks the group for the string
        if passed_date == dateTest.group():
            #successful walk
            print("You did enter a proper date")
            return True
        else:
            print("You did not enter a proper date")
            return False
        
        
def isValidAmount(passed_amount):
    
    dateRegex = re.compile(r'(\d){1,2}(-|/)(\d){1,2}(-|/)\d\d\d\d')
    amountTest = dateRegex.search(passed_amount)

    #checks for null
    if amountTest is None:
        print("You did not enter a proper date")
        return False
    else:
        #checks the group for the string
        if passed_amount == amountTest.group():
            #successful walk
            print("You did enter a proper date")
            return True
        else:
            print("You did not enter a proper date")
            return False