def enter_decision():
    """Takes user entry on whether to continue to add Student or Instructor entries
    
    Returns:
        string -- The response on whether to continue
    """
    enter_decision = True
    while True:
        response = input("Do you wish to add another individual (Y or N)?")
        if response.upper() == "N" or response.upper() == "Y":
            break
        else:
            print("That was not a valid entry. Please re-enter and try again.")
            continue
    return response.upper()