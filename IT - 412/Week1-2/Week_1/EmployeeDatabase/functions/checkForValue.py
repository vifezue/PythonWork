def check_for_value(value,list):
    """Check for a value in the passed in list and returns a True or False
    
    Arguments:
        value {list of string} -- This is the list of values not accepted
        list {list} -- List of the passed in values
    
    Returns:
        Boolean -- Returns a False if the values is not accepted and exist in the not accepted list
    """
    if value in list:
        print("Invalid Entry. Please try again")
        return False
    else:
        return True