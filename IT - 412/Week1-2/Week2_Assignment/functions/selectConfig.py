import json
from functions.selectConfiguration import selection
from functions.saveSettings import saveSettings
from functions.saveOverride import saveOverrideFile

def changeSystemSettings():
    """Changes the value for the standard config  NOT USED
    """
    with open("text_files/basic_config.json") as json_obj:            
        settings = json.load(json_obj)
        isDone = False 
        while not isDone:   
            choice = selection()
            print("Current Setting " + settings[choice]+" ")
            userInput = input("Please enter the new setting :")
            settings[str(choice)] = userInput 
            print("Your Settings has been changed!")
            done = input("Would you like to change another setting? Press Y for Yes and N for No: ")
            if done.lower() == "y":
                continue
            else:
                saveSettingResponse = saveSettings()
                          
            if saveSettingResponse == "y":
                saveOverrideFile(settings)
                break
            else:
                break
                            
                            
                            
                            

