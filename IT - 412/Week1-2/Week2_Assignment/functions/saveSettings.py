

def saveSettings():
    """Checks the see if the user would like the save or discard changes.
    
    Returns:
        string -- the selection from the user
    """
    isValid = False
    while not isValid:
        selection = input("Would you like to save the configurations? Y for Yes and No the discard changes: ")
        if selection.lower() == "y" or selection.lower() == "n":
            return selection
            break
        else:
            print("Please enter a valid selection")
            continue
    