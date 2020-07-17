def checkfor_null(val):
    """Checks for a null value
    
    Arguments:
        val {Any Type} -- The passed in value
    
    Returns:
        Boolean -- Returns True of False
    """
    if val == "":
        print("Invalid entry. Please enter a value.")
        checkID = False
        return False
    else:
        return True 