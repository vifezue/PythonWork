def changeSettingsResponse():
    """Gets user entry for the response to see if they would like to change the setting
    
    Returns:
        string -- the change setting response
    """
    responseAccepted = False
    while not responseAccepted:
        changeSettingResponse = input("Would you like to change a setting? \n"
                                      +"Please enter Y for Yes OR N for No: ")
        if changeSettingResponse.lower() == "y" or changeSettingResponse.lower() == "n":
            return changeSettingResponse
            break
        else:
            print("Invalid entry. Please try again!")
            continue