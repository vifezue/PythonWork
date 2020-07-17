
def selection():
    """Logic to capture the user selection to see what setting the user would like to change
        
    Returns:
        Dictionary Value -- string
    """
    isGood = False
    while not isGood:
        settingChoice = input("Which setting would you like to change? \n"
        +"Please type in your selection by number :"
        +"\n 1 - Safe Mode \n 2 - Memory \n 3 - Error Log \n " +
        "4 - Allow File Uploads \n 5 - Use Caching \n 6 - Caching File \n 7 - Mail Host \n Enter Number: ")
        if not settingChoice.isnumeric():
            print("Please enter a valid number on the list.")
            continue
        else:
            settingChoice = int(settingChoice)
        switcher={
            1:'safeMode',
            2:'memory',
            3:'errorLog',
            4:'AllowFileUpload',
            5:'Use Caching',
            6:'Caching File',
            7:'Mail Host'
            }
        if settingChoice in switcher:
            return switcher.get(settingChoice)
            break
        else:
            print("Please enter a valid number on the list.")
            continue                        