import json
import os.path
from functions.changeSettingsResponse import changeSettingsResponse
from functions.selectConfig import changeSystemSettings
from functions.selectConfigOverride import changeSystemSettingsOverride
from functions.saveOverride import saveOverrideFile

if os.path.exists("text_files/config_override.json"):
    
    with open("text_files/config_override.json") as json_obj:
        settings  = json.load(json_obj)
        if settings["AllowFileUpload"] == "" and settings["Use Caching"] == "" and settings["Caching File"] == "" and settings["Mail Host"]: 
            print("::::::::::::SYSTEM SETTINGS:::::::::::::\n")
            print("Safe Mode - " + settings["safeMode"]+ "\n")
            print("Memory - " + settings["memory"]+ "\n")
            print("Error Log - " + settings["errorLog"]+ "\n")            
            userResponse = changeSettingsResponse()
            if userResponse == "y":
                changeSystemSettingsOverride()
            else:
                pass
        else:
            with open("text_files/basic_config.json") as json_obj:
                settings  = json.load(json_obj)
                print("::::::::::::SYSTEM SETTINGS:::::::::::::\n")
                print("Safe Mode - " + settings["safeMode"]+ "\n")
                print("Memory - " + settings["memory"]+ "\n")
                print("Error Log - " + settings["errorLog"]+ "\n")  
                userResponse = changeSettingsResponse()
                if userResponse == "y":
                    changeSystemSettingsOverride()
                else:
                    pass            
else:
    with open("text_files/basic_config.json") as json_obj:
        settings  = json.load(json_obj)
        print("::::::::::::SYSTEM SETTINGS:::::::::::::\n")
        print("Safe Mode - " + settings["safeMode"]+ "\n")
        print("Memory - " + settings["memory"]+ "\n")
        print("Error Log - " + settings["errorLog"]+ "\n")  
        userResponse = changeSettingsResponse()
        if userResponse == "y":
            changeSystemSettingsOverride()
        else:
            pass            
        
            
            
        
        
        
            
                
                
                                
    
    